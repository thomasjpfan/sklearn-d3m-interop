#!/usr/bin/env python

from codecs import open
from setuptools import setup, find_packages

with open("requirements/base.txt") as f:
    install_requires = f.read().strip().split("\n")

with open("requirements/dev.txt") as f:
    dev_requires = f.read().strip().split("\n")

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name="sklearn-d3m-interop",
    version="0.0.1.0.22.2.post1",
    description="Interop between d3m's sklearn_wrap and sklearn",
    long_description=readme,
    author_email="thomasjpfan@gmail.com",
    url="https://github.com/thomasjpfan/sklearn-d3m-interop",
    packages=find_packages(include=["sklearn_d3m_interop"]),
    install_requires=install_requires,
    long_description_content_type="text/markdown",
    include_package_data=True,
    python_requires=">=3.6",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
    extras_require={
        "dev": dev_requires,
    },
)
