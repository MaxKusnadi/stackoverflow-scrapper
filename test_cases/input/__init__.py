from app.input.UserInput import UserInput
from unittest.mock import patch

import unittest


class InputTestCase(unittest.TestCase):
	def setUp(self):
		self.userInput = UserInput()

	# Test language inputs
	@patch('builtins.input')
	def test_valid_language_input(self, mock_input):
		mock_input.return_value = "Ruby"
		language = self.userInput.ask_language()
		self.assertEqual(language, mock_input.return_value)

	def test_empty_language_input(self):
		self.assertRaises(ValueError, self.userInput.is_language_valid, "")

	def test_digit_language_input(self):
		self.assertRaises(ValueError, self.userInput.is_language_valid, "1234")

	# Test start year input
	@patch('builtins.input')
	def test_valid_start_year_input(self, mock_input):
		mock_input.return_value = "2016"
		language = self.userInput.ask_start_year()
		self.assertEqual(language, mock_input.return_value)

	# Test end year input
	@patch('builtins.input')
	def test_valid_end_year_input(self, mock_input):
		mock_input.return_value = "2016"
		language = self.userInput.ask_end_year("2010")
		self.assertEqual(language, mock_input.return_value)

	def test_year_not_number(self):
		self.assertRaises(ValueError, self.userInput.is_year_valid, "abcd")

	def test_year_not_positive(self):
		self.assertRaises(ValueError, self.userInput.is_year_positive, "-1")

	def test_end_year_not_valid(self):
		self.assertRaises(ValueError, self.userInput.is_end_year_valid, "2010", "2015")

	@patch('builtins.input')
	def test_valid_date_input(self, mock_input):
		mock_input.side_effect = ["2016", "2017"]
		start_year, end_year = self.userInput.ask_date()
		self.assertEqual(start_year, "2016")
		self.assertEqual(end_year, "2017")

	@patch('builtins.input')
	def test_valid_user_input(self, mock_input):
		mock_input.side_effect = ["Ruby", "2016", "2017"]
		language, start_year, end_year = self.userInput.get_user_input()
		self.assertEqual(language, "Ruby")
		self.assertEqual(start_year, "2016")
		self.assertEqual(end_year, "2017")