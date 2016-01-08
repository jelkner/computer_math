#!/usr/bin/env python3
from fractions import Fraction


class AugMatrix:
    """
    Defines a 3 by 4 matrix representing a system of three linear equations
    in three variables with Fraction values.
    """
    def __init__(self, elements):
        """
          >>> elements = [[3, 1, 2, 31], [1, 1, 2, 19], [1, 3, 2, 25]]
          >>> lnsys = AugMatrix(elements)
          >>> lnsys.elements[1][2]
          Fraction(2, 1)
        """
        self.elements = []
        for row in elements:
            self.elements.append([Fraction(val) for val in row])

    def __str__(self):
        """
          >>> elements = [[3, 1, 2, 31], [1, 1, 2, 19], [1, 3, 2, 25]]
          >>> lnsys = AugMatrix(elements)
          >>> print(lnsys)
          [3    1    2  |  31]
          [1    1    2  |  19]
          [1    3    2  |  25]
        """
        form = """[{0}    {1}    {2}  |  {3}]
[{4}    {5}    {6}  |  {7}]
[{8}    {9}    {10}  |  {11}]"""
        return form.format(self.elements[0][0], self.elements[0][1],
                           self.elements[0][2], self.elements[0][3],
                           self.elements[1][0], self.elements[1][1],
                           self.elements[1][2], self.elements[1][3],
                           self.elements[2][0], self.elements[2][1],
                           self.elements[2][2], self.elements[2][3])

    def reduced_row_echelon(self):
        """
          >>> elements = [[3, 1, 2, 31], [1, 1, 2, 19], [1, 3, 2, 25]]
          >>> lnsys = AugMatrix(elements)
        """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
