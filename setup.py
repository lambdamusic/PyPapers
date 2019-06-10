from setuptools import setup, find_packages

setup(
    name = 'cliapp',
    version = '0.1.0',
    packages = find_packages(),
    include_package_data=True,
    install_requires=[
        'Click==6.6',
    ],
    entry_points='''
        [console_scripts]
        cliapp = cliapp.cli:main_cli
        quicktest_cliapp = cliapp.tests.quicktest:quicktest_cli
    ''',
)
