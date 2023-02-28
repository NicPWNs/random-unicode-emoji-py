#!/usr/bin/env python3
from bisect import bisect
from random import randrange
from itertools import accumulate

# Unicode Version 15.0
# https://www.unicode.org/charts/#symbols

EMOJI_RANGES_UNICODE = [
    # https://www.unicode.org/charts/PDF/U2600.pdf
    ('\U00002600', '\U000026FF'),
    # https://www.unicode.org/charts/PDF/U1F300.pdf
    ('\U0001F300', '\U0001F5FF'),
    # https://www.unicode.org/charts/PDF/U1F600.pdf
    ('\U0001F600', '\U0001F64F'),
    # https://www.unicode.org/charts/PDF/U1F680.pdf
    ('\U0001F680', '\U0001F6FF'),
    # https://www.unicode.org/charts/PDF/U1F900.pdf
    ('\U0001F900', '\U0001F9FF'),
    # https://www.unicode.org/charts/PDF/U1FA70.pdf
    ('\U0001FA70', '\U0001FAFF'),
]


def random_emoji():

    # Weighted distribution
    count = [ord(r[-1]) - ord(r[0]) + 1 for r in EMOJI_RANGES_UNICODE]
    weightDist = list(accumulate(count))

    # Get one index in the multiple ranges
    indexIndex = randrange(weightDist[-1])

    # Select the correct range
    emojiIndex = bisect(weightDist, indexIndex)
    emojiRange = EMOJI_RANGES_UNICODE[emojiIndex]

    # Calculate the index in the selected range
    indexRange = indexIndex
    if emojiIndex != 0:
        indexRange = indexIndex - weightDist[emojiIndex - 1]

    # Emoji
    emoji = chr(ord(emojiRange[0]) + indexRange)

    return (emoji)
