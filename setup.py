from setuptools import setup, find_namespace_packages

setup(
    name='GithubPackages',

    url='https://github.com/Mike396/virtual_environment_exercise.git',
    author='mks',
    author_email='',

    packages=find_namespace_packages(include=['GithubPackages']),
)
