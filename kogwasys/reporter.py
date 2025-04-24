def print_issues(issues):
    if not issues:
        print("✅ No issues found.")
        return
    for i in issues:
        print(f"[{i['severity']}] {i['contract']}::{i['function']} - {i['issue']}")
