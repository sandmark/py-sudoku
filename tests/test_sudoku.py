from nose.tools import *
from sudoku import Sudoku


class TestSudoku:
    """Sudokuオブジェクトのメソッドテスト"""

    PROBLEM = """001078000
005204000
000000906
050860407
026001030
104309020
512980743
768035090
430127060"""

    SOLVED = [[3, 9, 1, 6, 7, 8, 2, 5, 4],
              [6, 8, 5, 2, 9, 4, 3, 7, 1],
              [2, 4, 7, 5, 1, 3, 9, 8, 6],
              [9, 5, 3, 8, 6, 2, 4, 1, 7],
              [8, 2, 6, 7, 4, 1, 5, 3, 9],
              [1, 7, 4, 3, 5, 9, 6, 2, 8],
              [5, 1, 2, 9, 8, 6, 7, 4, 3],
              [7, 6, 8, 4, 3, 5, 1, 9, 2],
              [4, 3, 9, 1, 2, 7, 8, 6, 5]]

    def setup(self):
        self.sudoku = Sudoku()

    def test_solve(self):
        """数独問題を解決する"""
        self.sudoku.set_numbers(self.PROBLEM)
        self.sudoku.solve()
        eq_(self.SOLVED, self.sudoku.table)

    def test_table_length(self):
        """sudoku.tableは9x9の二次元配列を持つ"""
        eq_(9, len(self.sudoku.table))
        for line in self.sudoku.table:
            eq_(9, len(line))

    def test_set_numbers_with_valid_string(self):
        """sudoku.tableに9x9の数値をセットする"""
        string = '\n'.join(['1' * 9 for _ in range(9)])
        numbers = [[1 for _ in range(9)] for _ in range(9)]
        self.sudoku.set_numbers(string)
        eq_(numbers, self.sudoku.table)

    @raises(IndexError)
    def test_set_numbers_with_invalid_length(self):
        """不正な長さの入力は例外が発生する"""
        self.sudoku.set_numbers('129387')

    @raises(ValueError)
    def test_set_numbers_with_invalid_sequence(self):
        """数値以外の文字を含めると例外が発生する"""
        self.sudoku.set_numbers('asd')
