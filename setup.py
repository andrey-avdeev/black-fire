# -*- coding: utf-8 -*-
import io

from setuptools import setup, find_packages

with io.open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

version = "0.0.1"

setup(
    name="black-fire",
    version=version,
    description="Usefull wrappers for https://github.com/google/python-fire",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Artur Kuzin",
    license="Apache 2.0",
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
    ],
    keywords="python-fire black-fire fire",
    url="https://github.com/andrey-avdeev/black-fire",
)
