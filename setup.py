"""Setup for %module%."""

from distutils.core import setup

from setuptools import find_packages

setup(
    name="%module%",
    version="1.0",
    description="%module%",
    author="%author%",
    packages=find_packages(),
    package_data={"%module%": ["py.typed"]},
    install_requires=[],
    entry_points={"console_scripts": ["%module%=%module%.__main__:main"]},
)
