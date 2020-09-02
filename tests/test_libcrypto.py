#!/usr/bin/env python

"""Tests for `src` package."""

from src.libcrypt import LibCrypt


def test_encode_success():
    codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    content = 'another message here!'

    assert LibCrypt(codes=codes)._encode(content) == '1n4th2r m2ss1g2 h2r2!'


def test_decode_success():
    codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    content = 'th3s 3s 1 m2ss1g2.'

    assert LibCrypt(codes=codes)._decode(content) == 'this is a message.'
