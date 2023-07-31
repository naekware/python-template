"""Setup for %module%."""

from distutils.core import setup

setup(
    name="%module%",
    version="1.0",
    description="%module%",
    author="%author%",
    packages=["%module%"],
    entry_points={"console_scripts": ["%module%=%module%.__main__:main"]},
)
