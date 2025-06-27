from setuptools import setup, find_packages # type: ignore

setup(
    name='golden_spice_venture',
    version='0.1.0',  # Hardcoded!
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    description='Django project for Golden Spice Venture',
    author='golden_spice_venture',
)
