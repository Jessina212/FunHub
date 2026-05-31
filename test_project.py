from datetime import datetime, timedelta
from unittest.mock import patch
from project import check, match, ran_generator, alert, greet, play_again

def test_check():
    assert check(22, 33) == True
    assert check(2200, 2200) == False
    assert check (56, 78) == True

def test_match():
    assert match (2290, 2339) == 1
    assert match (3340, 3305) == 2
    assert match(2222, 3333) == 0
    assert match (7865, 8756) == 0

def test_ran_generator():
    n = ran_generator()
    assert n is not None
    assert 1000<n<9999

def test_alert():
    n = alert(75, datetime.now()-timedelta(minutes=1))
    assert n is not None

    a = alert(75, datetime.now())
    assert a is None

def test_greet():
    n = greet()
    print(n)
    assert n is not None
    assert "Start Guessing!" in n

def test_play_again():
    with patch("builtins.input", return_value=1):
        result = play_again()
        assert result == "again"
