#!/usr/bin/env python3
"""ivco-filter — Score and filter tweets for IVCO relevance.

Usage:
  cat tweets.json | ivco-filter
  ivco-filter --input tweets.json
  ivco-filter --input tweets.json --output filtered.json
  ivco-filter --input tweets.json --verbose
  ivco-filter blacklist add @spammer
  ivco-filter blacklist remove @spammer
  ivco-filter blacklist list
  ivco-filter whitelist add @analyst
  ivco-filter whitelist list
  ivco-filter backtest --input historical.json --rules new-rules.json
"""

import argparse
import json
import sys

from .rules import load_rules
from .scorer import score_tweet
from .lists import add_to_list, remove_from_list, show_list


def filter_tweets(args) -> None:
    """Main filter pipeline: read → score → filter → output."""
    rules = load_rules(args.config)

    # Read input
    if args.input:
        try:
            with open(args.input, "r") as f:
                raw = f.read()
        except FileNotFoundError:
            print(f"ERROR: File not found: {args.input}", file=sys.stderr)
            sys.exit(1)
    elif not sys.stdin.isatty():
        raw = sys.stdin.read()
    else:
        print("ERROR: Provide --input FILE or pipe via stdin", file=sys.stderr)
        sys.exit(1)

    try:
        tweets = json.loads(raw)
    except json.JSONDecodeError:
        print("ERROR: Invalid JSON input", file=sys.stderr)
        sys.exit(1)

    if not isinstance(tweets, list):
        tweets = []

    results = []
    stats = {"keep": 0, "review": 0, "discard": 0, "total": len(tweets)}

    for tweet in tweets:
        result = score_tweet(tweet, rules)
        stats[result["verdict"]] += 1

        if args.verbose:
            username = tweet.get("author", {}).get("username", "?")
            text_preview = tweet.get("text", "")[:60].replace("\n", " ")
            print(
                f"  [{result['verdict'].upper():>7}] score={result['score']:+d} @{username}: {text_preview}",
                file=sys.stderr,
            )
            for g in result["garbage"]:
                print(f"           - {g}", file=sys.stderr)
            for u in result["useful"]:
                print(f"           + {u}", file=sys.stderr)

        # Keep tweet if not discarded (keep + review pass through)
        if result["verdict"] != "discard":
            # Annotate tweet with score metadata
            tweet["_filter"] = {
                "score": result["score"],
                "verdict": result["verdict"],
                "reasons": result["garbage"] + result["useful"],
            }
            results.append(tweet)

    # Output filtered tweets
    output = json.dumps(results, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
            f.write("\n")
        print(f"Written {len(results)} tweets to {args.output}", file=sys.stderr)
    else:
        print(output)

    # Summary to stderr
    print(
        f"Summary: {stats['total']} total → {stats['keep']} keep, "
        f"{stats['review']} review, {stats['discard']} discard",
        file=sys.stderr,
    )


def handle_list(args) -> None:
    """Handle blacklist/whitelist subcommands."""
    list_name = args.list_type  # "blacklist" or "whitelist"

    if args.list_action == "add":
        if not args.username:
            print("ERROR: Provide username to add", file=sys.stderr)
            sys.exit(1)
        add_to_list(list_name, args.username, args.config)
    elif args.list_action == "remove":
        if not args.username:
            print("ERROR: Provide username to remove", file=sys.stderr)
            sys.exit(1)
        remove_from_list(list_name, args.username, args.config)
    elif args.list_action == "list":
        show_list(list_name, args.config)


def handle_backtest(args) -> None:
    """Run backtest on historical data with specified rules."""
    rules = load_rules(args.rules or args.config)

    if not args.input:
        print("ERROR: --input required for backtest", file=sys.stderr)
        sys.exit(1)

    try:
        with open(args.input, "r") as f:
            tweets = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(tweets, list):
        tweets = []

    stats = {"keep": 0, "review": 0, "discard": 0}
    print(f"Backtesting {len(tweets)} tweets...\n")

    for tweet in tweets:
        result = score_tweet(tweet, rules)
        stats[result["verdict"]] += 1
        username = tweet.get("author", {}).get("username", "?")
        text_preview = tweet.get("text", "")[:60].replace("\n", " ")
        print(
            f"[{result['verdict'].upper():>7}] score={result['score']:+d} @{username}: {text_preview}"
        )
        for g in result["garbage"]:
            print(f"         - {g}")
        for u in result["useful"]:
            print(f"         + {u}")

    print(f"\nResults: {stats['keep']} keep, {stats['review']} review, {stats['discard']} discard")
    total = sum(stats.values())
    if total:
        print(f"Keep rate: {(stats['keep'] + stats['review']) / total * 100:.0f}%")


def main():
    parser = argparse.ArgumentParser(
        prog="ivco-filter",
        description="Score and filter tweets for IVCO relevance.",
    )
    parser.add_argument("--config", help="Path to filter-rules.json config")

    subparsers = parser.add_subparsers(dest="command")

    # Default (no subcommand) = filter mode
    parser.add_argument("--input", help="Path to JSON input file")
    parser.add_argument("--output", help="Path to write filtered JSON output")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show per-tweet scoring details")

    # blacklist subcommand
    bl_parser = subparsers.add_parser("blacklist", help="Manage blacklist")
    bl_parser.add_argument("list_action", choices=["add", "remove", "list"])
    bl_parser.add_argument("username", nargs="?", help="Username (with or without @)")
    bl_parser.set_defaults(list_type="blacklist")

    # whitelist subcommand
    wl_parser = subparsers.add_parser("whitelist", help="Manage whitelist")
    wl_parser.add_argument("list_action", choices=["add", "remove", "list"])
    wl_parser.add_argument("username", nargs="?", help="Username (with or without @)")
    wl_parser.set_defaults(list_type="whitelist")

    # backtest subcommand
    bt_parser = subparsers.add_parser("backtest", help="Backtest rules on historical data")
    bt_parser.add_argument("--input", required=True, help="Path to historical JSON data")
    bt_parser.add_argument("--rules", help="Path to alternative rules JSON (default: main config)")

    args = parser.parse_args()

    if args.command in ("blacklist", "whitelist"):
        handle_list(args)
    elif args.command == "backtest":
        handle_backtest(args)
    else:
        filter_tweets(args)


if __name__ == "__main__":
    main()
