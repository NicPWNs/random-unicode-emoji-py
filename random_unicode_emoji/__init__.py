from random_unicode_emoji.random_unicode_emoji import random_emoji

__author__ = 'Nic Jones'
__email__ = 'nic@nicpjones.com'
__version__ = '2.9'
__doc__ = """
Random Unicode Emoji
====================
A simple Python package that returns random Unicode emojis.

Install
-------
Install the package:
>>> pip install random-unicode-emoji

Usage
-----
Use the package:
>>> # Import the Library
>>> from random_unicode_emoji import random_emoji
>>> # Use the Function
>>> print(random_emoji())
>>> # Return Specific Count
>>> print(random_emoji(count=3))
>>> # Use Specific Version
>>> print(random_emoji(version="15.0"))
>>> # Append Custom Emoji
>>> print(random_emoji(custom=['X.X',':D']))
>>> # All Together Now
>>> print(random_emoji(3, 15, ['X.X',':D']))

Upgrade
-------
Upgrade the package to the latest version:
>>> pip install random-unicode-emoji -U
"""
