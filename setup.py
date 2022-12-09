#!/usr/bin/env python
import setuptools

description = """
Library that provides access to available data.
"""

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [req for req in f.read().splitlines() if not req.startswith('-r')]

setuptools.setup(
    name="trunky-general-utils",
    version="0.0.2",
    description=description,
    url="https://github.com/trunkduyn/general_utils",
    author="Trunky",
    packages=setuptools.find_namespace_packages(exclude=["*.test"]),
    install_requires=requirements,
    include_package_data=True
)
