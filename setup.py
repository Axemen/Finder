import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'ez-glob',
    version = '0.0.1',
    author = 'Jonathan Randolph',
    author_email='Jrandolph011@gmail.com',
    description='A small package for finding files and directories',
    long_description_content_type="text/markdown",
    url = 'https://github.com/Axemen/ez-glob',
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires = '>=3.7'
)