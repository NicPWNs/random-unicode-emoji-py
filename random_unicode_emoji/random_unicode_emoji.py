#!/usr/bin/env python3
import os
import random


def random_emoji(version="latest"):

    # Unicode Standard Emoji from
    # https://www.unicode.org/Public/emoji/

    try:
        with open(rf"./emoji/{version}/emoji-test.txt", 'r', encoding='utf-8') as f:
            lines = [line for line in f.readlines() if line.strip() and not line.startswith("#")]
    except:
        versions = (os.listdir("./emoji"))
        print(f"Unicode version \"{version}\" is not supported. The following versions are currently supported:\n{', '.join(versions)}")
        exit()

    emojiHex = random.choice(lines).split(';', 1)[0].strip().split()

    emoji = ""

    for octet in emojiHex:
        emoji += chr(int("0x" + octet, 16))

    return emoji
