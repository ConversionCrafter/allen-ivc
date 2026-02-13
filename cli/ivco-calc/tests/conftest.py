"""TSMC test fixtures — ground truth from Allen's hand calculation."""
import pytest

@pytest.fixture
def tsmc_annual_data():
    """TSMC 2013-2022 financial data (all values in NT$K)."""
    return [
        {"year": 2013, "net_income": 188_018_937, "depreciation": 153_979_847, "amortization": 2_202_022, "capex": 287_594_773},
        {"year": 2014, "net_income": 263_780_869, "depreciation": 197_645_186, "amortization": 2_606_349, "capex": 288_540_028},
        {"year": 2015, "net_income": 306_556_167, "depreciation": 219_303_369, "amortization": 3_202_200, "capex": 257_516_835},
        {"year": 2016, "net_income": 334_338_236, "depreciation": 220_084_998, "amortization": 3_743_406, "capex": 326_508_158},
        {"year": 2017, "net_income": 343_146_848, "depreciation": 255_795_962, "amortization": 4_346_736, "capex": 327_956_630},
        {"year": 2018, "net_income": 351_184_406, "depreciation": 288_124_897, "amortization": 4_421_405, "capex": 315_405_143},
        {"year": 2019, "net_income": 345_343_809, "depreciation": 281_411_832, "amortization": 5_472_409, "capex": 454_712_784},
        {"year": 2020, "net_income": 518_158_082, "depreciation": 324_538_443, "amortization": 7_186_248, "capex": 506_138_977},
        {"year": 2021, "net_income": 597_073_134, "depreciation": 414_187_700, "amortization": 8_207_169, "capex": 838_367_791},
        {"year": 2022, "net_income": 1_016_900_515, "depreciation": 428_498_179, "amortization": 8_756_094, "capex": 1_075_620_698},
    ]

@pytest.fixture
def tsmc_expected_oe():
    """Expected Owner Earnings per year (maintenance_capex_ratio = 0.20)."""
    return {
        2013: 286_681_851,
        2014: 406_324_398,
        2015: 477_558_369,
        2016: 492_865_008,
        2017: 537_698_220,
        2018: 580_649_679,
        2019: 541_285_493,
        2020: 748_654_978,
        2021: 851_794_445,
        2022: 1_239_030_648,
    }

@pytest.fixture
def tsmc_parameters():
    """TSMC 7 company-specific parameters."""
    return {
        "maintenance_capex_ratio": 0.20,
        "reality_coefficient": {year: 1.0 for year in range(2013, 2023)},
        "cc_low": 1.2,
        "cc_high": 1.5,
        "stage2_cagr": 0.15,
        "stage3_cagr": 0.05,
        "discount_rate": 0.08,
        "long_term_debt": 1_673_432_925,
        "shares_outstanding_raw": 259_303_805,
        "share_par_value": 10,
    }

@pytest.fixture
def tsmc_expected_iv():
    """Expected IV Range from Allen's hand calculation."""
    return {
        "cagr": 0.1766,
        "stage1_cagr_low": 0.2119,
        "stage1_cagr_high": 0.2649,
        "dcf_sum_low": 120_037_432_375,
        "dcf_sum_high": 147_889_066_294,
        "iv_total_low": 118_363_999_450,
        "iv_total_high": 146_215_633_369,
        "iv_per_share_low": 4565,
        "iv_per_share_high": 5639,
    }
