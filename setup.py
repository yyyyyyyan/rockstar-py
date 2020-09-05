from setuptools import setup

with open("README.md") as file:
    long_description = file.read()

setup(
    name="rockstar-py",
    version="2.1.0",
    author="yyyyyyyan",
    author_email="contact@yyyyyyyan.tech",
    packages=["rockstarpy"],
    description="Python transpiler for the esoteric language Rockstar",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yyyyyyyan/rockstar-py",
    download_url="https://github.com/yyyyyyyan/rockstar-py/archive/2.1.0.zip",
    license="MIT",
    keywords="esoteric rockstar transpiler",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Interpreters",
    ],
    python_requires=">= 3.6",
    entry_points={
        "console_scripts": ["rockstar-py=rockstarpy.command_line:command_line"]
    },
)
