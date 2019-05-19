# -*- coding: utf-8 -*-
import setuptools

with open('README.md', 'r') as fp:
    long_description = fp.read()


setuptools.setup(
    name="DrfRequestJsonValidator",
    version='0.0.1',
    author='Li Xujia',
    author_email='lixujia.cn@gmail.com',
    description="A package use for validate json payload with jsonschema",
    url="https://github.com/lixujia/DrfRequestJsonValidator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=['setup.py', 'requirements.txt']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
