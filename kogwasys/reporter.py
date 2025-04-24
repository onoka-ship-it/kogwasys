import json
from rich.console import Console
from rich.table import Table
from jinja2 import Environment, FileSystemLoader

console = Console()


def print_issues(issues):
    if not issues:
        console.print("[green bold]✅ No issues found.[/green bold]")
        return

    table = Table(title="Smart Contract Vulnerability Report")

    table.add_column("Severity", style="bold red")
    table.add_column("Contract", style="cyan")
    table.add_column("Function", style="magenta")
    table.add_column("Issue", style="yellow")

    for i in issues:
        severity = i.get("severity", "N/A")
        contract = i.get("contract", "N/A")
        function = i.get("function", "—")
        issue = i.get("issue", "Unknown issue")
        table.add_row(severity, contract, function, issue)

    console.print(table)


def write_json_report(issues, filename="BugReport.json"):
    try:
        with open(filename, "w") as f:
            json.dump(issues, f, indent=4)
        console.print(f"[bold cyan]📄 JSON report saved to {filename}[/bold cyan]")
    except Exception as e:
        console.print(f"[red]❌ Failed to write JSON report: {e}[/red]")


def write_html_report(issues, filename="BugReport.html"):
    try:
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("html_template.html")
        output = template.render(issues=issues)

        with open(filename, "w") as f:
            f.write(output)

        console.print(f"[bold green]🌐 HTML report saved to {filename}[/bold green]")
    except Exception as e:
        console.print(f"[red]❌ Failed to write HTML report: {e}[/red]")
