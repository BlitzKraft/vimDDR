from setuptools import setup, find_packages
from os import path
import platform

if (platform.system() == 'Windows'):
    getch = 'msvcrt'
else:
    getch = 'getch'

setup(
    name='vimddr',
    version='0.1.0',
    description='Improve your vim reflexes!',
    url='https://github.com/BlitzKraft/vimDDR',
    author='BK Bolisetty',
    author_email='bk@blitzkraft.me',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment',
        'Environment :: Console',
        'Topic :: Terminals',
        'Topic :: Text Editors',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords=['vim', 'commandline', 'games'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[getch],
    extras_require={
    },
    entry_points={
        'console_scripts': [
            'vimddr=game:main',
        ],
    },
)
