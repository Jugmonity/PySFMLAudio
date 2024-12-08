from setuptools import setup
import setuptools

setup(
    name="PySFMLAudio",
    version="1.0",
    author="Jugmonity",
    packages=setuptools.find_packages(),
    package_data={
        '': ['x64sfml\\*.dll'],
    }
)
