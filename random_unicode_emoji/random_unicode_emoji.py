#!/usr/bin/env python3
from typing import List, Union
import os
import random

EMOJI_DIR = os.path.join(os.path.dirname(__file__), 'emoji')

class EmojiVersionError(Exception):
    """Raised when an unsupported emoji version is requested."""
    pass

def random_emoji(count: int = 1,
                version: Union[str, float] = "latest",
                custom: List[str] = None) -> List[str]:
    """
    Generate random emoji(s) from Unicode Standard or custom list.

    Args:
        count: Number of emojis to return
        version: Unicode emoji version
        custom: List of custom emojis to include

    Returns:
        List of random emojis

    Raises:
        EmojiVersionError: If the requested version is not supported
        ValueError: If count is less than 1
    """
    if count < 1:
        raise ValueError("Count must be greater than 0")

    custom = custom or []

    try:
        version = float(version) if version != "latest" else version
    except ValueError:
        pass

    try:
        with open(os.path.join(EMOJI_DIR, f"{version}/emoji-test.txt"), 'r', encoding='utf-8') as f:
            lines = [line.split(';', 1)[0].strip().split()
                    for line in f.readlines()
                    if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        versions = os.listdir(EMOJI_DIR)
        raise EmojiVersionError(
            f"Unicode version '{version}' is not supported. "
            f"Supported versions: {', '.join(versions)}"
        )

    unicode = [''.join(chr(int(f"0x{octet}", 16)) for octet in line)
               for line in lines]

    emoji_set = unicode + custom
    return random.choices(emoji_set, k=count)
