import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "steve-ede-ipyxact",
    version = "0.3.2",
    author = "Olof Kindgren",
    author_email = "olof.kindgren@gmail.com",
    description = "Python IP-Xact handling library",
    license = "MIT",
    keywords = "ipxact IP-Xact HDL ASIC FPGA",
    url = "https://github.com/olofk/ipyxact",
    packages = ['ipyxact'],
    long_description = read('README.md'),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    ],
    entry_points={"console_scripts": ["ipxact2v = ipyxact.ipxact2v:main"]},
    install_requires=[
        'pyyaml',
    ],
)
