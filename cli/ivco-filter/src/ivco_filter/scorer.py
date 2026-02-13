"""Scoring engine — applies G1-G5 garbage rules and U1-U5 useful rules."""

import re


def score_tweet(tweet: dict, rules: dict) -> dict:
    """Score a single tweet. Returns dict with score, reasons, and verdict.

    Args:
        tweet: Bird JSON tweet {"id", "text", "createdAt", "author": {"username", "name"}}
        rules: Loaded filter rules dict

    Returns:
        {"score": int, "garbage": [...], "useful": [...], "verdict": "keep"|"discard"|"review"}
    """
    text = tweet.get("text", "")
    text_lower = text.lower()
    username = tweet.get("author", {}).get("username", "").lower()

    score = 0
    garbage_hits = []
    useful_hits = []

    # --- Garbage Rules ---
    g_rules = rules.get("garbage_rules", {})

    # G1: Ticker spam
    g1 = g_rules.get("G1_ticker_spam", {})
    if g1.get("enabled"):
        pattern = g1.get("pattern", r"\$[A-Z]{1,5}")
        tickers = re.findall(pattern, text)
        if len(tickers) >= g1.get("min_tickers", 5):
            score += g1.get("penalty", -50)
            garbage_hits.append(f"G1: {len(tickers)} tickers found")

    # G2: Promo keywords
    g2 = g_rules.get("G2_promo_keywords", {})
    if g2.get("enabled"):
        for kw in g2.get("keywords", []):
            if kw.lower() in text_lower:
                score += g2.get("penalty", -40)
                garbage_hits.append(f"G2: promo '{kw}'")
                break  # One match is enough

    # G3: Payment mention
    g3 = g_rules.get("G3_payment_mention", {})
    if g3.get("enabled"):
        for kw in g3.get("keywords", []):
            if kw.lower() in text_lower:
                score += g3.get("penalty", -30)
                garbage_hits.append(f"G3: payment '{kw}'")
                break

    # G4: Short content
    g4 = g_rules.get("G4_short_content", {})
    if g4.get("enabled"):
        if len(text) < g4.get("min_chars", 80):
            has_analysis = any(
                kw.lower() in text_lower
                for kw in g4.get("analysis_keywords", [])
            )
            if not has_analysis:
                score += g4.get("penalty", -20)
                garbage_hits.append(f"G4: short ({len(text)} chars, no analysis keywords)")

    # G5: Background mention (disabled by default)
    g5 = g_rules.get("G5_background_mention", {})
    if g5.get("enabled"):
        # Placeholder for v2 NLP implementation
        pass

    # --- Useful Rules ---
    u_rules = rules.get("useful_rules", {})

    # U1: Analyst actions
    u1 = u_rules.get("U1_analyst_actions", {})
    if u1.get("enabled"):
        for kw in u1.get("keywords", []):
            if kw.lower() in text_lower:
                score += u1.get("bonus", 30)
                useful_hits.append(f"U1: analyst '{kw}'")
                break

    # U2: Earnings
    u2 = u_rules.get("U2_earnings", {})
    if u2.get("enabled"):
        for kw in u2.get("keywords", []):
            if kw.lower() in text_lower:
                score += u2.get("bonus", 25)
                useful_hits.append(f"U2: earnings '{kw}'")
                break

    # U3: Fundamental analysis
    u3 = u_rules.get("U3_fundamental_analysis", {})
    if u3.get("enabled"):
        for kw in u3.get("keywords", []):
            if kw.lower() in text_lower:
                score += u3.get("bonus", 20)
                useful_hits.append(f"U3: fundamental '{kw}'")
                break

    # U4: Major events
    u4 = u_rules.get("U4_major_events", {})
    if u4.get("enabled"):
        for kw in u4.get("keywords", []):
            if kw.lower() in text_lower:
                score += u4.get("bonus", 35)
                useful_hits.append(f"U4: event '{kw}'")
                break

    # U5: Whitelist bonus
    u5 = u_rules.get("U5_whitelist_bonus", {})
    if u5.get("enabled"):
        whitelist = [u.lower() for u in rules.get("whitelist", [])]
        if username in whitelist:
            score += u5.get("bonus", 15)
            useful_hits.append(f"U5: whitelisted @{username}")

    # --- Blacklist check (instant discard) ---
    blacklist = [u.lower() for u in rules.get("blacklist", [])]
    if username in blacklist:
        return {
            "score": -999,
            "garbage": [f"BLACKLISTED: @{username}"],
            "useful": [],
            "verdict": "discard",
        }

    # --- Verdict ---
    threshold = rules.get("score_threshold", 0)
    if score >= threshold + 20:
        verdict = "keep"
    elif score >= threshold:
        verdict = "review"
    else:
        verdict = "discard"

    return {
        "score": score,
        "garbage": garbage_hits,
        "useful": useful_hits,
        "verdict": verdict,
    }
