from setuptools import setup

setup(
    name='siteisdown',
    version='0.1',
    py_modules=['siteisdown'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        siteisdown=main:cli
    ''',
)