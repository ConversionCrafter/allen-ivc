"""Test three-stage DCF against TSMC ground truth."""
import pytest
from ivco_calc.dcf import calc_three_stage_dcf

def test_tsmc_dcf_full(tsmc_expected_oe, tsmc_parameters, tsmc_expected_iv):
    params = tsmc_parameters
    latest_oe = tsmc_expected_oe[2022]
    result = calc_three_stage_dcf(
        latest_oe=latest_oe, cagr=tsmc_expected_iv["cagr"],
        cc_low=params["cc_low"], cc_high=params["cc_high"],
        stage2_cagr=params["stage2_cagr"], stage3_cagr=params["stage3_cagr"],
        discount_rate=params["discount_rate"], long_term_debt=params["long_term_debt"],
        shares_outstanding_raw=params["shares_outstanding_raw"],
        share_par_value=params["share_par_value"],
    )
    assert result["iv_per_share_low"] == tsmc_expected_iv["iv_per_share_low"], \
        f"Low: got {result['iv_per_share_low']}, expected {tsmc_expected_iv['iv_per_share_low']}"
    assert result["iv_per_share_high"] == tsmc_expected_iv["iv_per_share_high"], \
        f"High: got {result['iv_per_share_high']}, expected {tsmc_expected_iv['iv_per_share_high']}"

def test_tsmc_stage1_year1(tsmc_expected_oe, tsmc_expected_iv):
    """Verify Year 1 discounted value matches Allen's spreadsheet."""
    latest_oe = tsmc_expected_oe[2022]
    cagr_low = tsmc_expected_iv["stage1_cagr_low"]
    year1 = round(latest_oe * (1 + cagr_low) / (1 + 0.08))
    assert year1 == 1_390_385_169, f"Year 1: got {year1}, expected 1,390,385,169"


def test_dcf_invalid_discount_rate():
    """discount_rate <= stage3_cagr must raise ValueError."""
    with pytest.raises(ValueError, match="discount_rate"):
        calc_three_stage_dcf(
            latest_oe=1_000_000, cagr=0.10, cc_low=1.0, cc_high=1.5,
            stage2_cagr=0.10, stage3_cagr=0.08, discount_rate=0.05,
            long_term_debt=0, shares_outstanding_raw=1_000_000,
        )


def test_dcf_zero_shares():
    """shares_outstanding_raw <= 0 must raise ValueError."""
    with pytest.raises(ValueError, match="shares_outstanding_raw"):
        calc_three_stage_dcf(
            latest_oe=1_000_000, cagr=0.10, cc_low=1.0, cc_high=1.5,
            stage2_cagr=0.10, stage3_cagr=0.03, discount_rate=0.08,
            long_term_debt=0, shares_outstanding_raw=0,
        )
