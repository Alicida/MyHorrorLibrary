from setuptools import setup, find_packages

setup(
    name="api-horror-library",
    version="0.1.0",
    description="Paquete que incluye una aplicación API REST para mi biblioteca de Horror.",
    packages=find_packages(),
    package_data={'readme':['README.md']}
)