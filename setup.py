import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="progmod", 
    version="0.0.1",
    author="Martin Clementz",
    author_email="martincclementz@gmail.com",
    description="En pakke for programering og modelering X",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NadderudVGS/ProgMod-Pakka",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)