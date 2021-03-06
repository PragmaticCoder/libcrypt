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


def test_transform_returns_encrypted_string():
    codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    content = 'another message here!'

    assert LibCrypt(codes=codes).transform(content) == '1n4th2r m2ss1g2 h2r2!'


def test_transform_returns_decrypted_string():
    codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    content = 'th3s 3s 1 m2ss1g2.'

    assert LibCrypt(codes=codes).transform(content) == 'this is a message.'


def test_transform_cycle():
    codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    content = 'th3s 3s 1 m2ss1g2.'

    result = LibCrypt(codes=codes).transform(content)
    assert LibCrypt(codes=codes).transform(result) == content


def test_transform_when_empty_string():
    codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    content = ''

    assert len(LibCrypt(codes=codes).transform(content)) == 0


def test_transform_when_empty_codes():
    codes = {}
    content = 'th3s 3s 1 m2ss1g2.'

    assert LibCrypt(codes=codes).transform(content) == 'th3s 3s 1 m2ss1g2.'
