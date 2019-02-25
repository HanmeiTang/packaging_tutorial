# `setup.py` is the build script for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Hanmei_Tang-example-package-name-to-be-distributed",
    version="v2019.02.24",
    author="Hanmei Tang",
    author_email="hat003@eng.ucsd.edu",
    description="A packaging project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HanmeiTang/packaging_tutorial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
