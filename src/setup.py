import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flexio-templating-tool",
    version="1.0.0",
    author="Thibaud Jeannin",
    author_email="team@flexio.fr",
    description="Flexio Templating Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flexiooss/flexio-templating-tool",
    python_requires='>=3',
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License:: OSI Approved:: Apache Software License"
    ]
)

