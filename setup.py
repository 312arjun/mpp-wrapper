from setuptools import setup, find_packages

setup(
    name="mpp_cli_wrapper",
    version="1.0",
    packages=find_packages(),
    package_data={"mpp_cli_wrapper": ["bin/*"]},  # Ensure binary files are included
    include_package_data=True,
    install_requires=[],
)
