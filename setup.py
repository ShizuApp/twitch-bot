from setuptools import find_packages
from setuptools import setup

requirements = []
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='Eigoku',
    version='1.0.0',
    description='Custom bot for Twitch.tv',
    license='MIT',
    author='Eduardo Jimenez',
    author_email='eduardojimfan@gmail.com',
    url='https://github.com/Shizuhime/Twitch-Bot',
    packages=find_packages(exclude=('tests*')),
    install_requieres=[requirements],
    classifiers=[
        'Development Status :: Alpha/On development',
        'License :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9'
    ],
    entry_point= { 'console_script': [ 'close-client = close:main' ] },
)