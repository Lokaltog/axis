"""Setup for Axis."""

from setuptools import setup

setup(
    name="axis",
    packages=["axis"],
    version="26",
    description="A Python library for communicating with devices from Axis Communications",
    author="Robert Svensson",
    author_email="Kane610@users.noreply.github.com",
    license="MIT",
    url="https://github.com/Kane610/axis",
    download_url="https://github.com/Kane610/axis/archive/v26.tar.gz",
    install_requires=["requests"],
    keywords=["axis", "vapix", "onvif", "event stream", "homeassistant"],
    classifiers=["Natural Language :: English", "Programming Language :: Python :: 3"],
)
