import setuptools
import re

VERSIONFILE="random_unicode_emoji/__init__.py"
getversion = re.search( r"^__version__ = ['\"]([^'\"]*)['\"]", open(VERSIONFILE, "rt").read(), re.M)
if getversion:
    new_version = getversion.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

with open("README.md", "r", encoding="utf-8") as r:
    long_description = r.read()
    long_description = re.sub("\u2B50", "star", long_description)
    long_description = re.sub("\u2764", "", long_description)

    setuptools.setup(
        name='random_unicode_emoji',
        python_requires='>=3',
        version=new_version,
        license='MIT',
        author="Nic Jones",
        author_email='nic@nicpjones.com',
        description='A Python package and function to retrieve a random Unicode emoji. \u2764',
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=setuptools.find_packages(),
        url='https://github.com/NicPWNs/random-unicode-emoji',
        download_url ='https://github.com/NicPWNs/random-unicode-emoji/releases',
        keywords='random unicode emoji function',
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )
