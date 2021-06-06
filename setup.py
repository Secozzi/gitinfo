from setuptools import setup, find_packages

setup(
    name="gitinfo",
    version="1.0.0.dev",
    description="Quickly get information about a Github repository",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "gitinfo = gitinfo.gitinfo:main",
        ]
    },
)
