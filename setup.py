import sys
from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

name = "pyrule34"  # R34API
version = "1.0.0"
description = "Asynchronous wrapper for rule34.xxx."
keywords = ["async rule34", "rule34 api", "wrapper"]

classifiers = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: Implementation :: PyPy',
]

author = "Hypick"
author_email = "twerka420@gmail.com"
url = "https://github.com/Hypick122/pyrule34"
project_urls = {
    # "Documentation": "",
    "Source": url,
}

install_requires = [
    "aiohttp >= 3.8.6",
    "beautifulsoup4 >= 4.12.2",  # 4.9.3
]

if __name__ == "__main__":
    if sys.version_info < (3, 5):
        raise RuntimeError('%s %s requires Python 3.5 or greater' % (name, version))

    setup(
        name=name,
        version=version,
        description=description,
        long_description=long_description,
        long_description_content_type="text/markdown",
        author=author,
        author_email=author_email,
        classifiers=classifiers,
        url=url,
        project_urls=project_urls,
        keywords=keywords,
        packages=['pyrule34'],
        install_requires=install_requires,
        python_requires='>=3.5',
    )
