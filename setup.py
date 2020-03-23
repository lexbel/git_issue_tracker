import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fh:
    version = fh.read().strip()

setuptools.setup(
    name="issue-fix-version-tracker",
    version=version,
    author="Aleksandr Belyaev",
    author_email="lexbel89@gmail.com",
    description="Issue fix version tracker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lexbel/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
