"""Test CAGR calculation against TSMC ground truth."""
from ivco_calc.cagr import calc_cagr

def test_tsmc_cagr_simple(tsmc_expected_oe, tsmc_parameters):
    oe_series = [{"year": y, "oe": tsmc_expected_oe[y]} for y in sorted(tsmc_expected_oe.keys())]
    result = calc_cagr(oe_series=oe_series, reality_coefficients=tsmc_parameters["reality_coefficient"])
    assert abs(result["cagr"] - 0.1766) < 0.0001, f"Got {result['cagr']}"
    assert result["start_year"] == 2013
    assert result["end_year"] == 2022
    assert result["periods"] == 9

def test_tsmc_cagr_with_reality_adjustment():
    oe_series = [{"year": 2013, "oe": 286_681_851}, {"year": 2022, "oe": 1_239_030_648}]
    rc = {2013: 1.25, 2022: 1.0}
    result = calc_cagr(oe_series=oe_series, reality_coefficients=rc)
    assert abs(result["cagr"] - 0.1477) < 0.001
