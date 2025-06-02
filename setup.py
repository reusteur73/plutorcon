from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='plutorcon',
    author='ReuS',
    version='1.0.3',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='Python RCON client for Plutonium',
    url="https://github.com/reusteur73/plutorcon",
    project_urls={
        "Documentation": "https://github.com/reusteur73/plutorcon#readme",
        "Source Code": "https://github.com/reusteur73/plutorcon",
        "Bug Tracker": "https://github.com/reusteur73/plutorcon/issues",
    },
)