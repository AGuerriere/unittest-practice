import unittest
from city_state_file import city_state


class TestCities(unittest.TestCase):
    "Tests for city_state.py"
    def test_italy(self):
        test = city_state('rome', 'italy')
        self.assertEqual(test, 'Rome, Italy')
    def test_france(self):
        test = city_state('PariS', 'fRance')
        self.assertEqual(test, 'Paris, France')
    def test_population(self):
        test = city_state('Washington, D.C.', 'USA', '300m')
        self.assertEqual(test, 'Washington, D.C., Usa population: 300m')
    

unittest.main()