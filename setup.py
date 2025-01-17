from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()


def local_scheme(version):
    """Skip the local version (eg. +xyz of 0.6.1.dev4+gdf99fe2)
    to be able to upload to Test PyPI"""
    return ""


setup(
    name="prettytable",
    description="A simple Python library for easily displaying tabular data in a "
    "visually appealing ASCII table format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Luke Maurits",
    author_email="luke@maurits.id.au",
    maintainer="Jazzband",
    url="https://github.com/jazzband/prettytable",
    project_urls={"Source": "https://github.com/jazzband/prettytable"},
    license="BSD (3 clause)",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    use_scm_version={"local_scheme": local_scheme},
    setup_requires=["setuptools_scm"],
    install_requires=[
        "importlib-metadata; python_version < '3.8'",
        "wcwidth",
    ],
    extras_require={"tests": ["pytest", "pytest-cov"]},
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: BSD License",
        "Topic :: Text Processing",
    ],
)
