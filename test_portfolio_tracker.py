import unittest
from portfolio_tracker import *

class TestPortfolioTracker(unittest.TestCase):


    def test_symbol_passed_to_generate_symbol_from_url_method(self):

        self.assertEqual(generate_url_from_symbol('MSFT'), 'http://in.finance.yahoo.com/q?s=MSFT', "these are NOT the same")


    def test_when_spaces_around_tuple_elements_in_the_input_file_exist(self):

        p = {}
        p[0] = [('GOOG', 400), ('AMZN', 60), ('MS', 50)]
        p[1] = [('SGI', 80), ('GOOG', 40), ('MS', 30)]
        p[2] = [('GOOG', 10), ('MS', 50)]
        p[3] = [('BHARTIART.NS', 5), ('TER', 10), ('XCRA', 20), ('A', 30)]
        
        self.assertDictEqual(extract_symbols_and_count_from_file("space_around_tup_elements.txt"), p, "not equal")
        """Cool. So the spaces around tuple elements are ignored. """


    def test_when_spaces_around_symbol_letters_in_the_input_file_exist(self):

        p = {}
        p[0] = [('GOOG', 400), ('AMZN', 60), ('MS', 50)]
        p[1] = [('SGI', 80), ('GOOG', 40), ('MS', 30)]
        p[2] = [('GOOG', 10), ('MS', 50)]
        p[3] = [('BHARTIART.NS', 5), ('TER', 10), ('XCRA', 20), ('A', 30)]
    
        self.assertDictEqual(extract_symbols_and_count_from_file("space_around_symbol_letters.txt"), p, "not equal")
        # Make the source code work by removing spaces around symbol letters 


    def test_when_both_single_and_double_quotes_are_used_around_symbol_in_the_input_file(self):

        p = {}
        p[0] = [('GOOG', 400), ('AMZN', 60), ('MS', 50)]
        p[1] = [('SGI', 80), ('GOOG', 40), ('MS', 30)]
        p[2] = [('GOOG', 10), ('MS', 50)]
        p[3] = [('BHARTIART.NS', 5), ('TER', 10), ('XCRA', 20), ('A', 30)]

        self.assertDictEqual(extract_symbols_and_count_from_file("quotes_missing_around_symbol.txt"), p, "not equal")
        """Make the source code work by removing spaces around symbol letters """


    def test_when_both_lower_and_upper_case_letters_in_the_input_file_exist(self):

        p = {}
        p[0] = [('GOOG', 400), ('AMZN', 60), ('MS', 50)]
        p[1] = [('SGI', 80), ('GOOG', 40), ('MS', 30)]
        p[2] = [('GOOG', 10), ('MS', 50)]
        p[3] = [('BHARTIART.NS', 5), ('TER', 10), ('XCRA', 20), ('A', 30)]
        
        self.assertDictEqual(extract_symbols_and_count_from_file("mix_of_upper_and_lower_case_letters_in_symbol.txt"), p, "not equal")


if __name__ == '__main__':
	unittest.main()
