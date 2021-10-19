from setuptools import setup

setup(
    name='my_deployer',
    version='0.1',
    packages=['pip', 'Click'],
    url='',
    license='',
    author='maxime.places',
    author_email='places_m@etna-alternance.net',
    description='Automated Docker deployment tool based on SSH',
    py_modules=['my_deployer'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'my_deployer=cli_commands:cli',
        ],
    },
)
