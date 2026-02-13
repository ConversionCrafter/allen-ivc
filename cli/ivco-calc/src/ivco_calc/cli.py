"""IVCO CLI — composable valuation tools."""
import click
import json

@click.group()
@click.version_option(version="0.1.0")
def cli():
    """IVCO — Intrinsic Value Confidence Observatory CLI tools."""
    pass

def output_json(data: dict) -> None:
    """Print JSON to stdout for piping."""
    click.echo(json.dumps(data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    cli()
