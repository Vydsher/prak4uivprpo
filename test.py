import re
import unittest
from main import clean_text  # Замените your_script_file на имя вашего файла скрипта

class TestCleanText(unittest.TestCase):
    def test_names_censored(self):
        text = "John Doe and Jane Smith"
        expected_output = "[censored] and [censored]"
        self.assertEqual(clean_text(text), expected_output)

    def test_phone_numbers_censored(self):
        text = "Call me at +12345678901"
        expected_output = "Call me at [censored]"
        self.assertEqual(clean_text(text), expected_output)

    def test_geo_data_censored(self):
        text = "My IP address is 192.168.0.1"
        expected_output = "My IP address is [censored]"
        self.assertEqual(clean_text(text), expected_output)

if __name__ == '__main__':
    unittest.main()