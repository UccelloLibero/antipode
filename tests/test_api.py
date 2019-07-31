import unittest

# import function that calculates the antipodes from api folder
from api import antipode_coords

# define a new test case called TestCoords which inherits from unittest.TestCase
class TestCoords(unittest.TestCase): #pass both longitude and latitude as arguments?

    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()
    # define a test method
    # test the input values passed in querystring are correct
    # test that the result is as expected coords eg. 33.749099

    # create the inputs
    # execute the code while capturing the output
    # compare the output to the expected result
    def test_latitude(self):
        anti_latitude = self.app.get('/antipode/')
        # test the latitude value entered and test output
        # make assertions?
        pass

    def test_longitude(self):
        # test the longitude value received and responde
        # make assertions?
        pass

    # test for expected errors like wrong type of data passed a string
    def test_wrong_value(self):
        data = ''
        with self.assertRaises(TypeError):
            result = calc(data)

if __name__ == '__main__':
    unittest.main()
