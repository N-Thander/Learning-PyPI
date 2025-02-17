

from setuptools import setup, find_packages

setup(
    name="learning-pypi",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "learning-pypi=learning_pypi.cli:main"
        ]
    },
    author="N-Thander",
    author_email="nasiruddinthander2002@gmail.com",
    description="Learning PyPI: By developing a simple CLI tool for summing numbers.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/N-Thander/Learning-PyPI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
