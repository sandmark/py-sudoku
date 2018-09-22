class Sudoku:
    """数独の問題を持ち、解決を行う。

    Sudoku#table -- 9x9の二次元配列。数独の問題を保持する。
    """

    def __init__(self):
        self._table = [[0 for i in range(9)] for j in range(9)]

    @property
    def table(self):
        return self._table
