from nose.tools import eq_
from sudoku import Sudoku


class TestSudoku:
    """Sudokuオブジェクトのメソッドテスト"""

    def setup(self):
        self.sudoku = Sudoku()

    def test_table_length(self):
        """sudoku.tableは9x9の二次元配列を持つ"""
        eq_(9, len(self.sudoku.table))
        for line in self.sudoku.table:
            eq_(9, len(line))
