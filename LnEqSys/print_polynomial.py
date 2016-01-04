from make_reduced_matrix import make_coeff_matrix as mm, reduce_matrix as rm


def print_quadratic(m):
    """
      >>> print_quadratic(rm(mm('test_data/3points1.dat')))
      'x^2 + 4x + 10'
      >>> print_quadratic(rm(mm('test_data/3points4.dat')))
      '3/14x^2 - 51/28x + 20/7'
      >>> print_quadratic(rm(mm('test_data/3points5.dat')))
      '1/2x^2 + 2'
      >>> print_quadratic(rm(mm('test_data/3points6.dat')))
      '1/35x^2 - 69/70x + 41/5'
    """
    fstr = '{0}{1}{2}'
    a, b, c = m[0][3], m[1][3], m[2][3]
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

        bstr = fstr.format(bop, bcoeff, 'x')

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
