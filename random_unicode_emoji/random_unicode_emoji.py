#!/usr/bin/env python3
import os
import random


def random_emoji(count=1, version="latest", custom=[]):

    dirname = os.path.dirname(__file__)

    try:
        version = float(version)
    except ValueError:
        pass

    # Unicode Standard Emoji from https://www.unicode.org/Public/emoji/
    # wget -q -r -np -A "emoji-test.txt" -nH --cut-dirs=1 https://www.unicode.org/Public/emoji/ && find emoji/ -type d -empty -exec rmdir {} \; 2>/dev/null

    try:
        with open(os.path.join(dirname, f"./emoji/{version}/emoji-test.txt"), 'r', encoding='utf-8') as f:
            lines = [line.split(';', 1)[0].strip().split() for line in f.readlines() if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        versions = (os.listdir(os.path.join(dirname, './emoji')))
        print(f"Unicode version \"{version}\" is not supported. The following versions are supported:\n{', '.join(versions)}")
        exit()

    unicode = []

    for line in lines:
        emoji = ""
        for octet in line:
            emoji += chr(int("0x" + octet, 16))
        unicode.append(emoji)

    emojiSet = unicode + custom
    emojis = []

    for _ in range(0, count):
        emojis.append(random.choice(emojiSet))

    return emojis
