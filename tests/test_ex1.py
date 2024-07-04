
import unittest
import pandas as pd
from moduls.reding_processing import *
from moduls.data_exploration import *


class TestsEx1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Loading dataset for TestEx1")
        cls._df = pd.read_csv("../Data/nics-firearm-background-checks.csv")

    def test_read_csv(self):
        file_to_read = "../Data/nics-firearm-background-checks.csv"
        self.assertFalse(read_csv(file_to_read).empty)

    def test_clean_csv(self):
        df_clean = clean_csv(self._df)
        self.assertEqual(len(df_clean.columns), 5)
        self.assertIn("permit", df_clean.columns)
        self._df = df_clean

    def test_rename_col(self):
        df = rename_col(self._df)
        self.assertIn("longgun", df.columns)
        self.assertNotIn("long gun", df.columns)
        self._df = df


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestsEx1)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)




