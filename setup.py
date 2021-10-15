from setuptools import setup
from pathlib import Path

code = Path(__file__).parent
readme = (code / "README.md").read_text()
requirements = (code / "requirements.txt").read_text().split("\n")

setup(
    name = "codebuddy",
    version = "v0.0.2",
    description = "stack overflow search on exception",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/0x44RU5H/codebuddy",
    author = "Aarush Gupta",
    author_email = "aarush@theaarushgupta.com",
    license = "AGPLv3+",
    classifiers = [
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    packages = ["codebuddy"],
    package_data = {},
    install_requires = requirements
)