# setup.py file

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dspt7_utilities_jmiddour",  # the name that you will install via pip
    version="0.0.2",
    author="Joanne Middour",
    author_email="joanne-middour@outlook.com",
    description="Unit 3 Utilities Testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/jmmiddour/Lambdata-jmmiddour",
    # keywords="",
    packages=setuptools.find_packages(),  # ["my_lambdata"]
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7'
)
