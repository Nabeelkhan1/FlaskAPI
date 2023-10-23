#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Nabeelkhan1",
    author_email='nabeelkhan5849@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="y",
    entry_points={
        'console_scripts': [
            'project3=project3.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='project3',
    name='project3',
    packages=find_packages(include=['project3', 'project3.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Nabeelkhan1/project3',
    version='0.0.1',
    zip_safe=False,
)
