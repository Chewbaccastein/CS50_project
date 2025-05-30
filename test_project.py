import pytest
from project import set_alarm, Clock

def test_am_pm():
    test_clock = Clock()
    test_clock.set_time(7,0,0)
    assert test_clock.am_pm() == "AM"
    test_clock.set_time(20,20,30)
    assert test_clock.am_pm() == "PM"
    test_clock.set_time(00,00,00)
    assert test_clock.am_pm() == "AM"
    test_clock.set_time(12,00,00)
    assert test_clock.am_pm() == "PM"

def test_set_time():
    test_clock = Clock()
    test_clock.set_time(5,45,24)
    assert test_clock.hour == 5
    assert test_clock.minute == 45
    assert test_clock.second == 24

def tick():
    test_clock = Clock()
    test_clock.set_time(11,59,59)
    test_clock.tick()
    assert (test_clock.hour, test_clock.minute, test_clock.second) == (12,0,0)
