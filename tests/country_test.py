import unittest
from city_functions import country_city

class NamesTestCase(unittest.TestCase):
    """tests for 'city_function.py'"""

    def test_city_country(self):
        """names like russia, kirov working good"""
        formatted_name = country_city('russia', 'kirov')
        self.assertEqual(formatted_name, 'Kirov, Russia')
    
    def test_city_country_population(self):
        """"names like russia, kirov, population 5000000 working good"""
        formatted_name = country_city('russia', 'kirov', 500000)
        self.assertEqual(formatted_name, 'Kirov, Russia - Population 500000')
if __name__ == "__main__":
    unittest.main()

