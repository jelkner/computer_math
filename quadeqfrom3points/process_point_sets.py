import make_reduced_matrix as mrm
import print_polynomial as pp
from fractions import Fraction


def convert_to_point(point_string):
    """
      >>> convert_to_point('(3, 4)\\n')
      (Fraction(3, 1), Fraction(4, 1))
      >>> type(convert_to_point('(3, 4)')[0])
      <class 'fractions.Fraction'>
      >>> convert_to_point('(3/4, 1/3)\\n')
      (Fraction(3, 4), Fraction(1, 3))
      >>> convert_to_point(' (4/5, 7) ')
      (Fraction(4, 5), Fraction(7, 1))
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
       >>> points = load_points_sets_from_file('test_data/point_sets1.dat')
       >>> len(points)
       5
       >>> len(points[1])
       3
       >>> points[2][2][0]
       Fraction(-4, 5)
    """
    try:
        f = open(fname, 'r')
    except:
        print('{0} file not found.'.format(fname))
        return

    points = f.readlines()
    f.close()
    points = [three_points.split(';') for three_points in points]
    for point_set in points:
        for i, point in enumerate(point_set):
            point_set[i] = convert_to_point(point)
    return points


point_sets = load_points_sets_from_file('test_data.dat')
of = open('test_data_eqs.out', 'w')

for point_set in point_sets:
    raw_matrix = mrm.make_coeff_matrix(point_set)
    reduced_matrix = mrm.reduce_matrix(raw_matrix)
    of.write(pp.print_quadratic(reduced_matrix) + '\n')
