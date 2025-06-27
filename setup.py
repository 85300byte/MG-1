from setuptools import setup, find_packages

setup(
    name='golden_spices',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'manage = manage:main',
        ]
    },
    description='Django project for Golden Spices',
    author='Golden Spices',
)
