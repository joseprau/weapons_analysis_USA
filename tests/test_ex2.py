import unittest

import pandas as pd
from moduls.reding_processing import read_csv, clean_csv, rename_col, breakdown_date, erase_month


class TestEx2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Preparing data for ex2")
        file_name = "../Data/nics-firearm-background-checks.csv"
        df = read_csv(file_name)
        df = clean_csv(df)
        cls._df = rename_col(df)

    def test_break_down(self):
        """
        Test for breakdown_date
        :return:
        """
        self._df = breakdown_date(self._df)
        self.assertIn("year", self._df.columns)

    def test_erase_month(self):
        """
        test for erase_month
        :return:
        """
        df = erase_month(self._df)
        self.assertNotIn("month", df.columns)


if __name__ == "__main__":
    suite_ex2 = unittest.TestLoader().loadTestsFromTestCase(TestEx2)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite_ex2)


