from setuptools import setup, find_packages

setup(
    name="hello_world",
    version="0.0.1",
    author="Alisson Martineli",
    author_email="martineli.alisson@gmail.com",
    description="My first python package",
    long_description="Hello World! (a simple python package example)",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.8',
)
