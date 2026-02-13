"""CAGR calculator with Reality Coefficient calibration."""

def calc_cagr(
    oe_series: list[dict],
    reality_coefficients: dict[int, float] | None = None,
) -> dict:
    if len(oe_series) < 2:
        raise ValueError("Need at least 2 years of OE data")
    sorted_series = sorted(oe_series, key=lambda x: x["year"])
    rc = reality_coefficients or {}
    start = sorted_series[0]
    end = sorted_series[-1]
    start_calibrated = int(start["oe"] * rc.get(start["year"], 1.0))
    end_calibrated = int(end["oe"] * rc.get(end["year"], 1.0))
    periods = end["year"] - start["year"]
    if periods <= 0:
        raise ValueError("End year must be after start year")
    if start_calibrated <= 0:
        raise ValueError("Start OE must be positive")
    cagr = (end_calibrated / start_calibrated) ** (1 / periods) - 1
    return {
        "cagr": round(cagr, 4),
        "start_year": start["year"],
        "end_year": end["year"],
        "periods": periods,
        "start_oe_raw": start["oe"],
        "end_oe_raw": end["oe"],
        "start_oe_calibrated": start_calibrated,
        "end_oe_calibrated": end_calibrated,
    }
