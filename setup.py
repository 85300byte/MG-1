from setuptools import setup, find_packages # type: ignore

setup(
    name='golden_spices',
    version='0.1.0',  # 🔒 Hardcoded to avoid dynamic errors
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    description='Django project for Golden Spices',
    author='Golden Spices',
)
