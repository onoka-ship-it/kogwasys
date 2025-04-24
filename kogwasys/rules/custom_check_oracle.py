def check_price_oracle_issues(contract):
    issues = []
    for var in contract.state_variables_declared:
        # Example pattern: public price feed or centralized price dependency
        if "price" in var.name.lower() and var.visibility == "public":
            issues.append({
                "contract": contract.name,
                "issue": f"Public price variable '{var.name}' may be manipulated externally.",
                "severity": "High"
            })

    for func in contract.functions:
        if "getPrice" in func.name or "oracle" in func.name.lower():
            issues.append({
                "contract": contract.name,
                "function": func.name,
                "issue": "Potential centralized oracle call in function.",
                "severity": "Medium"
            })

    return issues
