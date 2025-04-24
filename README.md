# 🛡️ Kogwasys – Smart Contract Guardian | 智能合约卫士

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/github/license/your-org/kogwasys)
![Status](https://img.shields.io/badge/status-active-success)
[![CodeQL](https://github.com/onoka-ship-it/kogwasys/actions/workflows/codeql.yml/badge.svg)](https://github.com/onoka-ship-it/kogwasys/actions/workflows/codeql.yml)
![License](https://img.shields.io/github/license/onoka-ship-it/kogwasys)


**Kogwasys** is a Python-powered command-line tool that protects Solidity smart contracts from critical security vulnerabilities. Built on [Slither](https://github.com/crytic/slither), it combines custom rule sets with trusted static analysis to detect classic and modern Web3 threats.

> “Audit your contracts before hackers do.”

---

## ✨ Features

- 🚨 Detects **Reentrancy**, **Oracle Manipulation**, **Unchecked Calls**, and more
- 🔍 Supports custom rule modules for modern vulnerabilities (2025 OWASP SC Top 10)
- 📂 Scans entire Solidity projects or individual `.sol` files
- 📊 Outputs detailed terminal reports in Chinese + optional JSON format
- 🧩 VS Code compatible for integrated scanning workflows
- 💡 Fully extensible – add your own static analysis rules

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-org/kogwasys.git
cd kogwasys

# 2. Set up virtualenv
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run a scan
kogwasys --target path/to/Contract.sol
