"""Minimal setup file for tasks project."""

from setuptools import find_packages, setup


setup(
    name='tasks',
    version='0.1.0',
    license='proprietary',
    description='Minimal Project Task Management',
    author='lanoir42',
    author_email='lanoir42jin@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
