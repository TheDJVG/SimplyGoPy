import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = ['simplygo']

requires = [
    'requests'
]

setuptools.setup(
    name='simplygopy',
    version='2021.5.1',
    install_requires=requires,
    author="D. van Gorkum",
    author_email="djvg@djvg.net",
    description="Python 3 module to talk to SimplyGo from Transit Link in Singapore",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheDJVG/SimplyGoPy",
    python_requires='>=3.6',
    packages=packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
