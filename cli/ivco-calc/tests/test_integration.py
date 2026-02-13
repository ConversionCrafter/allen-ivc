"""End-to-end integration: raw TSMC financials → IV Range."""

from ivco_calc.owner_earnings import calc_owner_earnings
from ivco_calc.cagr import calc_cagr
from ivco_calc.dcf import calc_three_stage_dcf
from ivco_calc.verify import verify_iv_range


def test_tsmc_end_to_end(tsmc_annual_data, tsmc_parameters, tsmc_expected_iv):
    """Full pipeline: financials → OE → CAGR → DCF → IV → verify."""
    params = tsmc_parameters

    # Step 1: Calculate OE for all years
    oe_series = []
    for row in tsmc_annual_data:
        oe = calc_owner_earnings(
            net_income=row["net_income"],
            depreciation=row["depreciation"],
            amortization=row["amortization"],
            capex=row["capex"],
            maintenance_capex_ratio=params["maintenance_capex_ratio"],
        )
        oe_series.append({"year": row["year"], "oe": oe})

    # Step 2: Calculate CAGR
    cagr_result = calc_cagr(
        oe_series=oe_series,
        reality_coefficients=params["reality_coefficient"],
    )

    # Step 3: Three-stage DCF
    latest_oe = oe_series[-1]["oe"]
    dcf_result = calc_three_stage_dcf(
        latest_oe=latest_oe,
        cagr=cagr_result["cagr"],
        cc_low=params["cc_low"],
        cc_high=params["cc_high"],
        stage2_cagr=params["stage2_cagr"],
        stage3_cagr=params["stage3_cagr"],
        discount_rate=params["discount_rate"],
        long_term_debt=params["long_term_debt"],
        shares_outstanding_raw=params["shares_outstanding_raw"],
        share_par_value=params["share_par_value"],
    )

    # Step 4: Verify against Allen's hand calculation
    verification = verify_iv_range(
        computed_low=dcf_result["iv_per_share_low"],
        computed_high=dcf_result["iv_per_share_high"],
        expected_low=tsmc_expected_iv["iv_per_share_low"],
        expected_high=tsmc_expected_iv["iv_per_share_high"],
    )

    assert verification["status"] == "PASS", (
        f"IV mismatch: got NT${dcf_result['iv_per_share_low']}~{dcf_result['iv_per_share_high']}, "
        f"expected NT${tsmc_expected_iv['iv_per_share_low']}~{tsmc_expected_iv['iv_per_share_high']}"
    )
