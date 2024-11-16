from working import convert
import pytest


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
        convert("9 AM - 5 PM")
        convert("09:00 AM - 17:00 PM")
        convert("9 AM 5:30 PM")
        convert("8:60 AM to 4:60 PM")


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")


def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")
