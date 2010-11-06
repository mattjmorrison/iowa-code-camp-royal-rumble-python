from setuptools import setup

setup(
    name="royal-rubmle-twitter",
    version="0.1",
    description="Python Twitter Clone for ICC Royal Rumble",
    author="Matthew J. Morrison",
    package_dir={'': 'src'},
    install_requires = (
        'wsgiref',
        'pesto',
        'Jinja2',
    ),
)