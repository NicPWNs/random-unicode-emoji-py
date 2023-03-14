#!/usr/bin/env python3
import os
import random


def random_emoji(version="latest"):

    try:
        version = float(version)
    except ValueError:
        pass

    # Unicode Standard Emoji from https://www.unicode.org/Public/emoji/
    # wget -q -r -np -A "emoji-test.txt" -nH --cut-dirs=1 https://www.unicode.org/Public/emoji/ && find emoji/ -type d -empty -exec rmdir {} \; 2>/dev/null

    try:
        with open(os.path.join(os.path.dirname(__file__), f"./emoji/{version}/emoji-test.txt"), 'r', encoding='utf-8') as f:
            lines = [line for line in f.readlines() if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        versions = (os.listdir(os.path.join(os.path.dirname(__file__), './emoji')))
        raise Exception(f"Unicode version \"{version}\" is not supported. The following versions are currently supported:\n{', '.join(versions)}")

    emoji = ""

    for octet in random.choice(lines).split(';', 1)[0].strip().split():
        emoji += chr(int("0x" + octet, 16))

    return emoji
