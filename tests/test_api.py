import pytest

# import function that calculates the antipodes from api folder
from api import antipode_coords

# think about pytest fixtures
# think about how to group these test into a group of test, class?
def latitude_value(latitude):
    if latitude <= 90 or latitude > 0:
        anti_l = latitude * -1
    return anti_l


def test_latitude():
    assert func(33.749099) == -33.749099


def longitude_value(longitude):
    if longitude < 0:
        anti_long = longitude + 180
    elif longitude > 0:
        anti_long = longitude - 180
    else:
        print('Something is not right.')
    return anti_long


def test_longitude():
    assert another_func(95.609815) == -84.390185
