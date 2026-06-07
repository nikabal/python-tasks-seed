"""
Unit tests for 02.Base85

TODO: Add more tests!
"""

import base85ed


def test_shorts_encode():
    """
    Test trivial short encodes
    """
    assert base85ed.encode(b"1") == b"F#"
    assert base85ed.encode(b"12") == b"F){"
    assert base85ed.encode(b"123") == b"F)}j"
    assert base85ed.encode(b"1234") == b"F)}kW"


def test_shorts_decode():
    """
    Test trivial short decodes
    """
    assert base85ed.decode(b"F#") == b"1"
    assert base85ed.decode(b"F){") == b"12"
    assert base85ed.decode(b"F)}j") == b"123"
    assert base85ed.decode(b"F)}kW") == b"1234"


def test_encode_decode_empty():
    """Пустая строка"""
    assert base85ed.encode(b"") == b""
    assert base85ed.decode(b"") == b""


def test_encode_decode_single_byte():
    """Один байт"""
    for i in range(256):
        original = bytes([i])
        encoded = base85ed.encode(original)
        decoded = base85ed.decode(encoded)
        assert decoded == original, f"Не работает для байта {i}"


def test_encode_decode_random_lengths():
    """Разная длина строк: от 0 до 100 байт"""
    for length in range(0, 101):
        original = bytes([65 + (i % 26) for i in range(length)])
        encoded = base85ed.encode(original)
        decoded = base85ed.decode(encoded)
        assert decoded == original, f"Не работает для длины {length}"


def test_encode_decode_random():
    """Случайные строки разной длины"""
    import random

    random.seed(42)

    lengths = [0, 1, 2, 3, 4, 5, 10, 17, 32, 33, 64, 100, 128, 255, 256, 511, 512, 1000]

    for length in lengths:
        original = bytes([random.randint(0, 255) for _ in range(length)])
        encoded = base85ed.encode(original)
        decoded = base85ed.decode(encoded)
        assert decoded == original, f"Не работает для длины {length}"
