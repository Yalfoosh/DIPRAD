from pathlib import Path
from setuptools import find_packages, setup


def readme(path=Path(__file__).resolve().parent / "README.md"):
    with open(path) as f:
        return f.read()


setup(
    name="diprad_dl",
    version="0.0.1",
    description="Graduate thesis: Deep learning",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Yalfoosh/DIPRAD/tree/main/dl",
    author="Miljenko Šuflaj",
    author_email="ms50144@fer.hr",
    license="Apache License 2.0",
    packages=find_packages(
        include=(
            "diprad_dl",
            "diprad_dl.*",
        )
    ),
    install_requires=[],
    python_requires=">=3.8, <3.9",
    include_package_data=True,
    zip_safe=False,
)
