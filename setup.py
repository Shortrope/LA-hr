from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='Human Resources: Manage users',
    long_description=readme,
    author='Mario',
    author_email='mario@mario.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
