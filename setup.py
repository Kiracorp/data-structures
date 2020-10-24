import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data-structures-kiracorp",
    version="0.0.1",
    author="Kyler Green",
    author_email="kairaanomeiru@gmail.com",
    description="Implementation for common data structues",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kiracorp/data-structures",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)