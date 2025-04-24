from slither.slither import Slither
from kogwasys.rules.custom_check_oracle import check_price_oracle_issues
from kogwasys.rules.custom_check_reentrancy import check_reentrancy
from kogwasys.reporter import print_issues, write_json_report, write_html_report
import os


def run_scan(target_path, json_output=False, html_output=False, output_dir="."):
    try:
        slither = Slither(target_path)
    except Exception as e:
        print(f"❌ Failed to analyze target: {e}")
        return

    all_issues = []

    for contract in slither.contracts:
        for func in contract.functions:
            # Built-in check for unsafe delegatecall
            if hasattr(func, "source_mapping") and hasattr(func.source_mapping, "content"):
                content = func.source_mapping.content
                if "delegatecall" in content:
                    all_issues.append({
                        "contract": contract.name,
                        "function": func.name,
                        "issue": "Potential unsafe delegatecall",
                        "severity": "High"
                    })

        # Apply custom rules
        all_issues.extend(check_price_oracle_issues(contract))
        all_issues.extend(check_reentrancy(contract))

    # Print summary in terminal
    print_issues(all_issues)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Output JSON if enabled
    if json_output:
        write_json_report(all_issues, filename=os.path.join(output_dir, "BugReport.json"))

    # Output HTML if enabled
    if html_output:
        write_html_report(all_issues, filename=os.path.join(output_dir, "BugReport.html"))
