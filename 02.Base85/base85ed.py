"""
Base85 encoder and decoder
"""

from __future__ import annotations
from beartype import beartype

ALPHABET = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
DECODE_MAP = {b: i for i, b in enumerate(ALPHABET)}


@beartype
def encode(b: bytes) -> bytes:
    """
    Base85 encoder
    """
    result = bytearray()

    for i in range(0, len(b), 4):
        chunk = b[i : i + 4]
        pad = 4 - len(chunk)
        chunk = chunk + b"\x00" * pad

        value = int.from_bytes(chunk, "big")

        digits = []
        for _ in range(5):
            digits.append(ALPHABET[value % 85])
            value //= 85
        digits.reverse()

        result.extend(digits[: 5 - pad])

    return bytes(result)


@beartype
def decode(b: bytes) -> bytes:
    """
    Base85 decoder
    """
    for byte in b:
        if byte not in DECODE_MAP:
            raise ValueError(f"Invalid character: {chr(byte)!r}")

    result = bytearray()

    for i in range(0, len(b), 5):
        chunk = b[i : i + 5]
        pad = 5 - len(chunk)
        chunk = chunk + bytes([ALPHABET[84]] * pad)

        value = 0
        for byte in chunk:
            value = value * 85 + DECODE_MAP[byte]

        result.extend(value.to_bytes(4, "big")[: 4 - pad])

    return bytes(result)
