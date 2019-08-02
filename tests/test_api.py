import pytest

# import function that calculates the antipodes from api folder
from api import antipode_coords

# adding scope='module' creating this specific fixture instance to save on time, since new_antipode_coords will be invoked once per test module
def func(latitude):
    if latitude <= 90 or latitude > 0:
        anti_l = latitude * -1
    return anti_l


def test_latitude():
    assert func(33.749099) == -33.749099


def another_func(longitude):
    if longitude < 0:
        anti_long = longitude + 180
    elif longitude > 0:
        anti_long = longitude - 180
    else:
        print('Something is not right.')
    return anti_long


def test_longitude():
    assert another_func(95.609815) == -84.390185
