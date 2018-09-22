class Sudoku:
    """数独の問題を持ち、解決を行う。

    Sudoku#table -- 9x9の二次元配列。数独の問題を保持する。
    """

    def __init__(self):
        self._table = [[0 for _ in range(9)] for _ in range(9)]

    def set_numbers(self, string):
        """tableに数値をセットする"""
        serialized = [[int(i) for i in l] for l in string.split('\n')]
        for y in range(9):
            for x in range(9):
                self._table[x][y] = serialized[x][y]

    @property
    def table(self):
        return self._table
