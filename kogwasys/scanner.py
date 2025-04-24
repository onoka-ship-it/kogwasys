from slither.slither import Slither
from kogwasys.rules.custom_check_oracle import check_price_oracle_issues
from kogwasys.rules.custom_check_reentrancy import check_reentrancy
from kogwasys.reporter import print_issues

def run_scan(target_path):
    slither = Slither(target_path)
    all_issues = []

    for contract in slither.contracts:
        # Built-in example check
        for func in contract.functions:
            if "delegatecall" in func.source_mapping.get("content", ""):
                all_issues.append({
                    "contract": contract.name,
                    "function": func.name,
                    "issue": "Potential unsafe delegatecall",
                    "severity": "High"
                })

        # Custom rules
        all_issues.extend(check_price_oracle_issues(contract))
        all_issues.extend(check_reentrancy(contract))

    print_issues(all_issues)
