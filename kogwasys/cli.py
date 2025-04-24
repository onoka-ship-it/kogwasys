import click
from kogwasys.scanner import run_scan

@click.command()
@click.option("--target", "-t", required=True, help="Solidity file or directory to scan")
@click.option("--json", "json_output", is_flag=True, help="Output results as JSON")
@click.option("--html", "html_output", is_flag=True, help="Output results as HTML")
@click.option("--out", "output_dir", default=".", help="Directory to save output reports")
def main(target, json_output, html_output, output_dir):
    run_scan(target, json_output=json_output, html_output=html_output, output_dir=output_dir)

if __name__ == "__main__":
    main()
