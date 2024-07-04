import unittest
from moduls.reding_processing import *
from moduls.data_exploration import *


class TestEx5(unittest.TestCase):
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

    def test_groupby_state(self):
        df = groupby_state(self._df)
        self.assertNotIn('year', df.columns)
        self.assertEqual(len(df.columns), 4)
        self.assertEqual(df['state'].nunique(), 55)
        self._df = df

    def test_clean_states(self):
        df = clean_state(self._df)
        self.assertEqual(df['state'].nunique(), 51)
        self._df = df

    def test_merge_dfs(self):
        df2 = read_csv("../Data/us-state-populations.csv")
        df = merge_datasets(self._df, df2)
        self.assertGreater(len(df.columns), len(self._df.columns))
        self._df = df

    def calculate_relative_values(self):
        df = calculate_relative_value(self._df)
        mean_permits = df[df['permit']].mean()
        self.assertEqual(mean_permits, 34.88)


if __name__ == "__main__":
    suite_ex5 = unittest.TestLoader().loadTestsFromTestCase(TestEx5)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite_ex5)