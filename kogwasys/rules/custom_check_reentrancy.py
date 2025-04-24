def check_reentrancy(contract):
    issues = []

    for func in contract.functions:
        if hasattr(func, "source_mapping") and hasattr(func.source_mapping, "content"):
            source = func.source_mapping.content.lower()

            # Broaden the match to cover more variations
            if "call.value" in source or ".call{" in source or ".call.value(" in source or ".call(" in source:
                issues.append({
                    "contract": contract.name,
                    "function": func.name,
                    "issue": "Possible reentrancy vulnerability from external call.",
                    "severity": "High"
                })

    return issues
