#!/usr/bin/env python
import setuptools

description = """
Library that provides access to available data.
"""

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [req for req in f.read().splitlines() if not req.startswith('-r')]

setuptools.setup(
    name="trunky-template-repository",
    version="0.0.1",
    description=description,
    url="https://github.com/trunkduyn/template_repository",
    author="Trunky",
    packages=setuptools.find_namespace_packages(exclude=["*.test"]),
    install_requires=requirements,
    include_package_data=True
)
