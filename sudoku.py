import math
import pprint


class SolvedException(Exception):
    pass


class Sudoku:
    """数独の問題を持ち、解決を行う。

    Sudoku#table -- 9x9の二次元配列。数独の問題を保持する。
    """

    def __init__(self):
        self._table = [[0 for _ in range(9)] for _ in range(9)]

    def __str__(self):
        return pprint.pformat(self.table)

    def set_numbers(self, string):
        """tableに数値をセットする"""
        serialized = [[int(i) for i in l] for l in string.split('\n')]
        for y in range(9):
            for x in range(9):
                self._table[x][y] = serialized[x][y]

    def solve(self):
        """tableの問題を解決する"""
        def solver(n, table):
            if n == 9 * 9:
                raise SolvedException(table)
            else:
                x = math.floor(n / 9)
                y = n % 9
                if table[x][y] != 0:
                    return solver(n + 1, table)
                else:
                    for i in range(1, 10):
                        if self.__is_valid(i, (x, y)):
                            table[x][y] = i
                            solver(n + 1, table)
                            table[x][y] = 0

        try:
            solver(0, self.table[:])
        except SolvedException as e:
            self._table = e.args[0]

    def __is_valid(self, n, pos):
        """table[x,y]にnが矛盾なく配置できる場合は真を返す"""
        row = self.__is_valid_row(n, pos[0])
        col = self.__is_valid_col(n, pos[1])
        box = self.__is_valid_box(n, pos)
        return row and col and box

    def __is_valid_row(self, n, x):
        """行にnが配置できる場合は真を返す"""
        for i in range(9):
            if self.table[x][i] == n:
                return False
        return True

    def __is_valid_col(self, n, y):
        """列にnが配置できる場合は真を返す"""
        for i in range(9):
            if self.table[i][y] == n:
                return False
        return True

    def __is_valid_box(self, n, pos):
        """枠内にnが配置できる場合は真を返す"""
        x = (math.floor(pos[0] / 3) * 3)
        y = (math.floor(pos[1] / 3) * 3)
        for i in range(2):
            for j in range(2):
                if self.table[x + i][y + j] == n:
                    return False
        return True

    @property
    def table(self):
        return self._table
