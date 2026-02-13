"""Three-Stage DCF Engine — Allen Framework core.

Three-Tier Calibration Pipeline:
  Layer 1: Reality Coefficient -> calibrated OE (handled by cagr module)
  Layer 2: CAGR calculation (handled by cagr module)
  Layer 3: Confidence Coefficient -> adjusted CAGR

Three-Stage DCF:
  Stage 1 (years 1-5): CAGR x CC growth, discounted
  Stage 2 (years 6-10): Moderate CAGR, discounted
  Stage 3 (year 11+): Perpetuity with low growth, discounted to year 11

IV_per_share = round((DCF_Sum - Long_Term_Debt) * share_par_value / shares_outstanding_raw)
"""


def _calc_dcf_stages(
    latest_oe: int,
    stage1_cagr: float,
    stage2_cagr: float,
    stage3_cagr: float,
    discount_rate: float,
) -> dict:
    """Calculate DCF for all three stages."""
    yearly_values = []
    cumulative_oe = float(latest_oe)
    dcf_sum = 0.0

    # Stage 1: years 1-5
    for year in range(1, 6):
        cumulative_oe = cumulative_oe * (1 + stage1_cagr)
        discounted = cumulative_oe / ((1 + discount_rate) ** year)
        yearly_values.append({"year": year, "stage": 1, "value": round(discounted)})
        dcf_sum += discounted

    # Stage 2: years 6-10
    for year in range(6, 11):
        cumulative_oe = cumulative_oe * (1 + stage2_cagr)
        discounted = cumulative_oe / ((1 + discount_rate) ** year)
        yearly_values.append({"year": year, "stage": 2, "value": round(discounted)})
        dcf_sum += discounted

    # Stage 3: perpetuity (year 11+)
    # Gordon Growth Model: TV = CF_11 / (r - g), discounted to year 0 by (1+r)^11
    perpetuity_oe = cumulative_oe * (1 + stage3_cagr)
    perpetuity_value = perpetuity_oe / (discount_rate - stage3_cagr)
    discounted_perpetuity = perpetuity_value / ((1 + discount_rate) ** 11)
    yearly_values.append({"year": 11, "stage": 3, "value": round(discounted_perpetuity)})
    dcf_sum += discounted_perpetuity

    return {"yearly_values": yearly_values, "dcf_sum": round(dcf_sum)}


def calc_three_stage_dcf(
    latest_oe: int,
    cagr: float,
    cc_low: float,
    cc_high: float,
    stage2_cagr: float,
    stage3_cagr: float,
    discount_rate: float,
    long_term_debt: int,
    shares_outstanding_raw: int,
    share_par_value: int = 10,
) -> dict:
    """Full three-stage DCF calculation.

    Args:
        latest_oe: Most recent year Owner Earnings (same unit as debt).
        cagr: Historical OE CAGR (full precision, e.g. 0.17660669...).
        cc_low: Confidence Coefficient lower bound (e.g. 1.2).
        cc_high: Confidence Coefficient upper bound (e.g. 1.5).
        stage2_cagr: Stage 2 moderate growth rate (e.g. 0.15).
        stage3_cagr: Stage 3 perpetuity growth rate (e.g. 0.05).
        discount_rate: Discount rate (e.g. 0.08).
        long_term_debt: Long-term debt (bonds + long-term loans).
        shares_outstanding_raw: Raw share capital from financial statements.
        share_par_value: Par value per share (10 for Taiwan stocks).

    Returns:
        Dict with full DCF breakdown and IV Range.
    """
    if discount_rate <= stage3_cagr:
        raise ValueError(
            f"discount_rate ({discount_rate}) must exceed stage3_cagr ({stage3_cagr}) "
            "for Gordon Growth Model perpetuity"
        )
    if shares_outstanding_raw <= 0:
        raise ValueError(f"shares_outstanding_raw must be positive, got {shares_outstanding_raw}")

    stage1_cagr_low = cagr * cc_low
    stage1_cagr_high = cagr * cc_high

    low = _calc_dcf_stages(latest_oe, stage1_cagr_low, stage2_cagr, stage3_cagr, discount_rate)
    high = _calc_dcf_stages(latest_oe, stage1_cagr_high, stage2_cagr, stage3_cagr, discount_rate)

    iv_total_low = low["dcf_sum"] - long_term_debt
    iv_total_high = high["dcf_sum"] - long_term_debt

    iv_per_share_low = round(iv_total_low * share_par_value / shares_outstanding_raw)
    iv_per_share_high = round(iv_total_high * share_par_value / shares_outstanding_raw)

    return {
        "stage1_cagr_low": round(stage1_cagr_low, 4),
        "stage1_cagr_high": round(stage1_cagr_high, 4),
        "stage2_cagr": stage2_cagr,
        "stage3_cagr": stage3_cagr,
        "discount_rate": discount_rate,
        "dcf_sum_low": low["dcf_sum"],
        "dcf_sum_high": high["dcf_sum"],
        "long_term_debt": long_term_debt,
        "iv_total_low": iv_total_low,
        "iv_total_high": iv_total_high,
        "shares_outstanding": shares_outstanding_raw,
        "share_par_value": share_par_value,
        "iv_per_share_low": iv_per_share_low,
        "iv_per_share_high": iv_per_share_high,
        "dcf_low_detail": low["yearly_values"],
        "dcf_high_detail": high["yearly_values"],
    }
