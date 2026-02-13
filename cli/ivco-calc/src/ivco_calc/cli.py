"""IVCO CLI — composable valuation tools."""
import click
import json
from ivco_calc.owner_earnings import calc_owner_earnings
from ivco_calc.cagr import calc_cagr

@click.group()
@click.version_option(version="0.1.0")
def cli():
    """IVCO — Intrinsic Value Confidence Observatory CLI tools."""
    pass

def output_json(data: dict) -> None:
    """Print JSON to stdout for piping."""
    click.echo(json.dumps(data, indent=2, ensure_ascii=False))

@cli.command("calc-oe")
@click.option("--net-income", type=int, required=True)
@click.option("--depreciation", type=int, required=True)
@click.option("--amortization", type=int, required=True)
@click.option("--capex", type=int, required=True)
@click.option("--maintenance-ratio", type=float, required=True)
def calc_oe_cmd(net_income, depreciation, amortization, capex, maintenance_ratio):
    """Calculate Owner Earnings for a single year."""
    oe = calc_owner_earnings(
        net_income=net_income,
        depreciation=depreciation,
        amortization=amortization,
        capex=capex,
        maintenance_capex_ratio=maintenance_ratio
    )
    output_json({
        "owner_earnings": oe,
        "inputs": {
            "net_income": net_income,
            "depreciation": depreciation,
            "amortization": amortization,
            "capex": capex,
            "maintenance_capex_ratio": maintenance_ratio
        }
    })

@cli.command("calc-cagr")
@click.option("--start-oe", type=int, required=True)
@click.option("--end-oe", type=int, required=True)
@click.option("--start-year", type=int, required=True)
@click.option("--end-year", type=int, required=True)
@click.option("--rc-start", type=float, default=1.0)
@click.option("--rc-end", type=float, default=1.0)
def calc_cagr_cmd(start_oe, end_oe, start_year, end_year, rc_start, rc_end):
    """Calculate CAGR from Owner Earnings with Reality Coefficient."""
    oe_series = [{"year": start_year, "oe": start_oe}, {"year": end_year, "oe": end_oe}]
    rc = {start_year: rc_start, end_year: rc_end}
    result = calc_cagr(oe_series=oe_series, reality_coefficients=rc)
    output_json(result)

if __name__ == "__main__":
    cli()
