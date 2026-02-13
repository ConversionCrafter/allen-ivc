"""Blacklist and whitelist management."""

import sys
from .rules import load_rules, save_rules


def add_to_list(list_name: str, username: str, config_path: str | None = None) -> None:
    """Add a username to blacklist or whitelist."""
    rules = load_rules(config_path)
    username = username.lstrip("@").lower()

    if username in [u.lower() for u in rules.get(list_name, [])]:
        print(f"Already in {list_name}: @{username}", file=sys.stderr)
        return

    rules.setdefault(list_name, []).append(username)
    save_rules(rules, config_path)
    print(f"Added @{username} to {list_name}", file=sys.stderr)


def remove_from_list(list_name: str, username: str, config_path: str | None = None) -> None:
    """Remove a username from blacklist or whitelist."""
    rules = load_rules(config_path)
    username = username.lstrip("@").lower()

    current = rules.get(list_name, [])
    lower_list = [u.lower() for u in current]

    if username not in lower_list:
        print(f"Not found in {list_name}: @{username}", file=sys.stderr)
        return

    idx = lower_list.index(username)
    current.pop(idx)
    rules[list_name] = current
    save_rules(rules, config_path)
    print(f"Removed @{username} from {list_name}", file=sys.stderr)


def show_list(list_name: str, config_path: str | None = None) -> None:
    """Print all entries in a list."""
    rules = load_rules(config_path)
    entries = rules.get(list_name, [])

    if not entries:
        print(f"{list_name}: (empty)")
        return

    print(f"{list_name} ({len(entries)}):")
    for username in sorted(entries):
        print(f"  @{username}")
