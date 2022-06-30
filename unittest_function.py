from dev_functions import get_formatted_name
import unittest


class NameTestCase(unittest.TestCase):
    """ Test for dev_functions.py."""
    def test_first_last_name(self):
        """ Do names like 'joseph Vinod' work ?"""
        formatted_name = get_formatted_name('joseph', 'vinod')
        self.assertEqual(formatted_name,'joseph vinod')

    def test_first_middle_last_name(self):
        """ Do names like 'Niel Nitin Mukesh'"""
        formatted_name = get_formatted_name('Neil','Mukesh',middle='Nitin')
        self.assertEqual(formatted_name,'Neil Nitin Mukesh')

if __name__ == "__main__":
    unittest.main()