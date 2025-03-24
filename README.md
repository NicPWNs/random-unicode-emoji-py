# random-unicode-emoji

[![python](https://img.shields.io/pypi/pyversions/random-unicode-emoji)](https://pypi.org/project/random-unicode-emoji/)
[![pypi](https://img.shields.io/pypi/v/random-unicode-emoji)](https://pypi.org/project/random-unicode-emoji/)
[![Unicode](https://img.shields.io/badge/Unicode-15.0-success)](https://www.unicode.org/Public/emoji/15.0/)
[![downloads](https://pepy.tech/badge/random-unicode-emoji)](https://pepy.tech/project/random-unicode-emoji)
[![stars](https://img.shields.io/github/stars/NicPWNs/random-unicode-emoji-py)](https://github.com/NicPWNs/random-unicode-emoji-py/stargazers)
[![forks](https://img.shields.io/github/forks/NicPWNs/random-unicode-emoji-py.svg)](https://github.com/NicPWNs/random-unicode-emoji-py/forks)
[![repo size](https://img.shields.io/github/repo-size/NicPWNs/random-unicode-emoji-py)](https://github.com/NicPWNs/random-unicode-emoji-py)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/NicPWNs/random-unicode-emoji-py/blob/main/LICENSE.rst)
[![issues](https://img.shields.io/github/issues/NicPWNs/random-unicode-emoji-py.svg)](https://github.com/NicPWNs/random-unicode-emoji-py/issues)

A simple Python package that returns random Unicode emojis. 🐍

> Like this repo? Give it a [⭐ on GitHub!](https://github.com/NicPWNs/random-unicode-emoji-py)

## Install

Install the package:

```bash
pip install random-unicode-emoji
```

> No dependencies!

## Usage

Use the package:

```py
# Import the Library
from random_unicode_emoji import random_emoji
# Use the Function
print(random_emoji())
# Return Specific Count
print(random_emoji(count=3))
# Use Specific Version
print(random_emoji(version="15.0"))
# Append Custom Emoji
print(random_emoji(custom=['(° ͜ʖ ͡°)','(╯°□°)╯︵ ┻━┻']))
# All Together Now
print(random_emoji(3, 15, ['(° ͜ʖ ͡°)','(╯°□°)╯︵ ┻━┻']))
```

## Upgrade

Upgrade the package to the latest version:

```bash
pip install random-unicode-emoji -U
```

## Unicode

Uses Unicode Standard Emoji from [Unicode.org](https://www.unicode.org/Public/emoji/)

### Supported Unicode Versions

4.0, 5.0, 11.0, 12.0, 12.1, 13.0, 13.1, 14.0, 15.0, 15.1, 16.0 (latest)

> _Uses latest version by default._

## Language

This is the Python 🐍 version. There is also a [JavaScript 📜](https://github.com/NicPWNs/random-unicode-emoji) and [Rust ⚙️](https://github.com/NicPWNs/random-unicode-emoji-rs) version.

## Maintainer

[Nic Jones, (@NicPWNs)](https://github.com/NicPWNs)

## Credit

Originally Inspired by [randomEmoji.py](https://gist.github.com/shello/efa2655e8a7bce52f273)
