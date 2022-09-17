import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "oneNeuron_pypi"
USER_NAME = "GopalakrishnanSubramani"

setuptools.setup(
    name="src",
    version="0.0.2",
    author=USER_NAME,
    author_email="gopalinlatvia@gmail.com",
    description="A small package for ANN implement",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "pandas",
        "numpy",
        "seaborn",
        "PyYAML",
    ]
)
