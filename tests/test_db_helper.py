from unittest import TestCase
from unittest.mock import patch
# from src.db_helper import DbHelper

class TestDbHelper(TestCase):

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self,MockDBHelper):
        
        db_helper = MockDBHelper() # Mock Object

        db_helper.get_maximum_salary.return_value = 158220
        db_helper.get_minimum_salary.return_value = 38623

        Min = db_helper.get_minimum_salary()
        Max = db_helper.get_maximum_salary()

        self.assertTrue(Max > Min)

        db_helper.get_maximum_salary.return_value = 10
        db_helper.get_minimum_salary.return_value = 1

        Min = db_helper.get_minimum_salary()
        Max = db_helper.get_maximum_salary()

        self.assertTrue(Max > Min)