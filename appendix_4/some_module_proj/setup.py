from setuptools import setup, find_packages


setup(
    name='some_package',
    description='Demonstrate packaging and distribution',
    version='1.0',
    author='lanoir42',
    author_email='lanoir42@example.org',
    url='https://github.com/lanoir42',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
