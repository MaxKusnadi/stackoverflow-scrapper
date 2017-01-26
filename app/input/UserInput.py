import logging

class UserInput(object):

	def get_user_input(self):
		language = self.ask_language()
		start_date, end_date = self.ask_date()
		return (language, start_date, end_date)

	def ask_date(self):
		start_year = self.ask_start_year()
		end_year = self.ask_end_year(start_year)
		return (start_year, end_year)

	def ask_start_year(self):
		is_start_year_valid = False

		while not is_start_year_valid:
			start_year = input("What is the starting year?")
			try:
				logging.debug("Start year: %s" % (start_year,))
				is_start_year_validValid = self.is_year_valid(start_year)
			except ValueError as e:
				logging.error(e)
				continue
			except Exception as e:
				logging.error(e)
				continue
			else:
				break

		return start_year

	def ask_end_year(self, start_year):
		is_end_year_valid = False

		while not is_end_year_valid:
			end_year = input("What is the ending year?")
			try:
				logging.debug("End year: %s" % (end_year,))
				is_end_year_validValid = self.is_end_year_valid(end_year, start_year)
			except ValueError as e:
				logging.error(e)
				continue
			except Exception as e:
				logging.error(e)
				continue
			else:
				break
		return end_year

	def is_end_year_valid(self, end_year, start_year):
		is_year_valid = self.is_year_valid(end_year)
		is_end_year_after_start = self.is_end_year_after_start(end_year, start_year)
		return is_year_valid and is_end_year_after_start

	def is_end_year_after_start(self, end_year, start_year):
		if int(end_year) < int(start_year):
			raise ValueError("End year can't be earlier than start_year")
		return True

	def is_year_valid(self, year):
		is_year_number = self.is_year_number(year)
		is_year_positive = self.is_year_positive(year)
		return is_year_positive and is_year_number


	def is_year_number(self, year):
		if not year.isdigit():
			raise ValueError("Year must be a number")
		return True

	def is_year_positive(self, year):
		if int(year) <= 0:
			raise ValueError("Year must be positive")
		return True

	def ask_language(self):
		is_input_valid = False

		while not is_input_valid:
			language = input("What language are you interested in: ")
			try:
				logging.debug("Input: %s" % (language,))
				is_input_valid = self.is_language_valid(language)
			except ValueError as e:
				logging.error(e)
				continue
			except Exception as e:
				logging.error(e)
				continue
			else:
				break
		return language

	def is_language_valid(self, language):
		is_language_empty = self.is_language_empty(language)
		is_language_digit = self.is_language_digit(language)
		return not is_language_empty and not is_language_digit

	def is_language_empty(self, language):
		if len(language) == 0:
			raise ValueError("Input can't be empty")
		return False

	def is_language_digit(self, language):
		if language.isdigit():
			raise ValueError("Language can't be all numbers")
		return False
