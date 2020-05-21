try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name="statispy",
    version="0.2.0",
    author="Shankhanil Ghosh",
    author_email="shankha.rik@gmail.com",
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)
