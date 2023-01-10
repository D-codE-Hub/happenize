from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in happenize/__init__.py
from happenize import __version__ as version

setup(
	name="happenize",
	version=version,
	description="App for happenize",
	author="D-codE",
	author_email="mailtodecode@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
