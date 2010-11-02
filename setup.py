from setuptools import setup

setup(
    name="royal-rubmle-twitter",
    version="0.1",
    description="Django Twitter Clone for ICC Royal Rumble",
    author="Matthew J. Morrison",
    package_dir={'': 'src'},
    install_requires = (
        'mock',
    ),
)