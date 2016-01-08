from fractions import Fraction


def print_quadratic(reduced_matrix):
    """
    Given an augmented matrix (3 by 4 containing a list of three lists of
    4 Fraction objects) in reduced row echelon form, return a string
    representing the quadratic function determined by the matrix in the form:
    f(x) = ax^2 + bx + c.  Terms will not be printed that have b or c
    values of 0.

      >>> m1 = [[Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(1, 1)]]
      >>> m1.append([Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(4, 1)])
      >>> m1.append([Fraction(0, 1), Fraction(0, 1), Fraction(1, 1), Fraction(10, 1)])
      >>> print_quadratic(m1)
      'f(x) = x^2 + 4x + 10'
      >>> m2 = [[Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(3, 14)]]
      >>> m2.append([Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(-51, 28)])
      >>> m2.append([Fraction(0, 1), Fraction(0, 1), Fraction(1, 1), Fraction(20, 7)])
      >>> print_quadratic(m2)
      'f(x) = 3/14x^2 - 51/28x + 20/7'
      >>> m3 = [[Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(1, 2)]]
      >>> m3.append([Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)])
      >>> m3.append([Fraction(0, 1), Fraction(0, 1), Fraction(1, 1), Fraction(2, 1)])
      >>> print_quadratic(m3)
      'f(x) = 1/2x^2 + 2'
      >>> m4 = [[Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(1, 35)]]
      >>> m4.append([Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(-69, 70)])
      >>> m4.append([Fraction(0, 1), Fraction(0, 1), Fraction(1, 1), Fraction(-41, 5)])
      >>> print_quadratic(m4)
      'f(x) = 1/35x^2 - 69/70x - 41/5'
      >>> m5 = [[Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(4, 1)]]
      >>> m5.append([Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)])
      >>> m5.append([Fraction(0, 1), Fraction(0, 1), Fraction(1, 1), Fraction(0, 1)])
      >>> print_quadratic(m5)
      'f(x) = 4x^2'
    """
    fstr = 'f(x) = {0}{1}{2}'
    a, b, c = reduced_matrix[0][3], reduced_matrix[1][3], reduced_matrix[2][3]
    if a == 1:
        astr = 'x^2'
    else:
        astr = str(a) + 'x^2'

    if b == 0:
        bstr = ''
    else:
        if b > 0:
            bop = ' + '
        else:
            bop = ' - '
        if abs(b) == 1:
            bcoeff = ''
        else:
            bcoeff = str(abs((b)))

        bstr = bop + bcoeff + 'x'

    if c == 0:
        cstr = ''
    else:
        if c > 0:
            cop = ' + '
        else:
            cop = ' - '

        cstr = cop + str(abs(c))

    return fstr.format(astr, bstr, cstr)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
