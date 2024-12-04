from setuptools import setup
import setuptools

setup(
    name="SFMLAudio",
    version="1.0",
    author="RiritoXXL",
    packages=setuptools.find_packages(),
    package_data={
        '': ['dll\\*.dll'],
    }
)