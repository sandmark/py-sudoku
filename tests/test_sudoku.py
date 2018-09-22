from nose.tools import *
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
