"""Run setuptools."""
import pathlib

from setuptools import find_packages, setup

setup(
    name="tokotura",
    version="0.0.1",
    description="Snake guide.",
    url="https://github.com/noipeK/tokotura",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    package_data={"tokotura": ["py.typed"]},
    install_requires=[],
    extras_require={
      "all": [],
    },
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    license="MIT",
)
