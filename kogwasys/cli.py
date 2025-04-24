import click
from kogwasys.scanner import run_scan

@click.command()
@click.option("--target", "-t", required=True, help="Solidity file or directory to scan")
def main(target):
    run_scan(target)

if __name__ == "__main__":
    main()
