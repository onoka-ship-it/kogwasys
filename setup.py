from setuptools import setup, find_packages

setup(
    name="kogwasys",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "slither-analyzer",
        "click"
    ],
    entry_points={
        "console_scripts": [
            "kogwasys=kogwasys.cli:main"
        ]
    },
)
