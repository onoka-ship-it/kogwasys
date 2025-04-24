# 🛡️ Kogwasys – Smart Contract Guardian | 智能合约卫士

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/github/license/onoka-ship-it/kogwasys)
![Issues](https://img.shields.io/github/issues/onoka-ship-it/kogwasys)
![Stars](https://img.shields.io/github/stars/onoka-ship-it/kogwasys?style=social)
![Last Commit](https://img.shields.io/github/last-commit/onoka-ship-it/kogwasys)

**Kogwasys** is a Python-powered command-line tool that protects Solidity smart contracts from critical security vulnerabilities. Built on [Slither](https://github.com/crytic/slither), it combines custom rule sets with trusted static analysis to detect classic and modern Web3 threats.

> “Audit your contracts before hackers do.”

---

## ✨ Features

- 🚨 Detects **Reentrancy**, **Oracle Manipulation**, **Unchecked Calls**, and more
- 🔍 Supports custom rule modules for modern vulnerabilities (2025 OWASP SC Top 10)
- 📂 Scans entire Solidity projects or individual `.sol` files
- 📊 Outputs detailed terminal reports in Chinese + optional **JSON** and **HTML** formats
- 🧩 VS Code compatible for integrated scanning workflows
- 💡 Fully extensible – add your own static analysis rules

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/onoka-ship-it/kogwasys.git
cd kogwasys

# 2. Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run a scan
kogwasys --target examples/VulnerableContract.sol

# 5. Output JSON + HTML to a custom folder
kogwasys --target examples/VulnerableContract.sol --json --html --out reports

# 🧠 Custom Rules Included
custom_check_reentrancy.py

custom_check_oracle.py

Add your own under kogwasys/rules/ and register in scanner.py