from src.cipher import encrypt, decrypt, crack
import pytest



def test_encrypt_shift_1():
    actual = encrypt('abc',1)
    expected = 'bcd'
    assert actual == expected

def test_encrypt_all_uppercase():
    actual = encrypt('ALL UPPERCASE', 20)
    expected = 'UFF OJJYLWUMY'
    assert actual == expected

def test_decrypt_shift_5():
    encrypted = encrypt('Welcome HOME', 5)
    actual = decrypt(encrypted, 5)
    expected = 'Welcome HOME'
    assert actual == expected

def test_shift_wraps_around():
    actual = encrypt('abc',27)
    expected = 'bcd'
    assert actual == expected

def test_letter_wraps_around():
    actual = encrypt('zzz',1)
    expected = 'aaa'
    assert actual == expected