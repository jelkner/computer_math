import make_reduced_matrix as mrm
import print_polynomial as pp
from fractions import Fraction


def convert_string_to_points(point_string):
    """
      >>> convert_string_to_point('(3, 4)\\n')
      (Fraction(3, 1), Fraction(4, 1))
      >>> type(convert_string_to_point('(3, 4)')[0])
      <class 'fractions.Fraction'>
      >>> convert_string_to_point('(3/4, 1/3)\\n')
      (Fraction(3, 4), Fraction(1, 3))
    """
    coords = list(point_string.strip().split(', '))
    coords[0] = coords[0].lstrip('(')
    coords[1] = coords[1].rstrip(')')
    for i, val in enumerate(coords):
        val = Fraction(val)
        coords[i] = val
    return tuple(coords)


def load_points_sets_from_file(fname):
    """
       >>> len(load_points_from_file('test_data/point_sets1.dat'))
       5
    """
    """
       >>> load_points_from_file('test_data/point_sets1.dat')[0]
       (Fraction(1, 1), Fraction(15, 1))
       >>> load_points_from_file('test_data/point_sets1.dat')[1]
       (Fraction(3, 1), Fraction(31, 1))
    """
    try:
        f = open(fname, 'r')
    except:
        print('{0} file not found.'.format(fname))
        return

    points = f.readlines()
    f.close()
    pvals = [convert_string_to_point(pval) for pval in pvals]
    return pvals


if __name__ == '__main__':
    import doctest
    doctest.testmod()
