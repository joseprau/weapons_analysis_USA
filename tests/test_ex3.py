import unittest
from moduls.reding_processing import *
from moduls.data_exploration import *


class TestEx3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Preparing data for ex2")
        file_name = "../Data/nics-firearm-background-checks.csv"
        df = read_csv(file_name)
        df = clean_csv(df)
        df = rename_col(df)
        df = breakdown_date(df)
        df = erase_month(df)
        cls._df = groupby_state_and_year(df)
    def test_groupby_year_state(self):
        """
        test for testing groupby
        :return:
        """
        df = groupby_state_and_year(self._df)
        max_handgun = df.loc[df['handgun'].idxmax()]
        state_handgun, year_handgun = max_handgun['state'], max_handgun['year']
        max_longgun = df.loc[df['longgun'].idxmax()]
        state_longgun, year_longgun= max_longgun['state'], max_longgun['year']
        self.assertEqual(df['state'].nunique(), 55)
        self.assertEqual(state_handgun, "Florida")
        self.assertEqual(year_handgun, 2016)
        self.assertEqual(state_longgun, "Pennsylvania")
        self.assertEqual(year_longgun, 2012)


if __name__ == "__main__":
    suite_ex3 = unittest.TestLoader().loadTestsFromTestCase(TestEx3)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite_ex3)
