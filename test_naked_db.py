import unittest
from unittest.mock import patch
from datetime import datetime 
import naked

class TestAsteroidProgram(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This method is called before any test cases are executed
        init_db()  # Initialize the database before running the tests

    @classmethod
    def tearDownClass(cls):
        # This method is called after all test cases are executed
        pass

    @patch('naked.requests.get')  # Replace the actual API call with a mock object
    def test_push_asteroids_arrays_to_db(self, mock_get):
        # Mock the API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{"element_count": 1, "near_earth_objects": {"2024-01-12": [{"name": "MockAsteroid", "nasa_jpl_url": "http://mockurl.com", "estimated_diameter": {"kilometers": {"estimated_diameter_min": 1.0, "estimated_diameter_max": 2.0}}, "is_potentially_hazardous_asteroid": false, "close_approach_data": [{"epoch_date_close_approach": 1642009200000, "relative_velocity": {"kilometers_per_hour": 1000}, "miss_distance": {"kilometers": 500000}}]}]}}'

        # Call your main function with the mock API response
        with patch('builtins.input', return_value=''):  # Mock user input to avoid any interruptions
            with patch('naked.datetime') as mock_datetime:
                mock_datetime.now.return_value = datetime(2024, 1, 12)  # Mock the current date

                ast_safe = []
                ast_hazardous = []

                # Run the main program logic
                naked.main()

                # Call your function that inserts data into the database
                push_asteroids_arrays_to_db('2024-01-12', ast_hazardous, 1)


if __name__ == '__main__':
    unittest.main()
