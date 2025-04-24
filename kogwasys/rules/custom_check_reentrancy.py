def check_reentrancy(contract):
    issues = []

    for func in contract.functions:
        source = func.source_mapping.get("content", "")
        if any(keyword in source for keyword in ["call.value", ".call(", ".transfer(", ".send("]):
            issues.append({
                "contract": contract.name,
                "function": func.name,
                "issue": "Possible reentrancy vulnerability from external call.",
                "severity": "High"
            })

    return issues
