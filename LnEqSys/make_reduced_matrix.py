from fractions import Fraction


def make_coeff_matrix(points):
    """
    Take a list of three tuples containing pairs of Fraction objects
    representing the (x, y) coordinates of non-colinear points, and return a
    3 by 4 augmented matrix (a list of length 3 containing lists of length
    4 of Fraction objects) with the coefficients for a, b, and c and the
    y value for ax^2 + bx + c with the given x.

      >>> point_list1 = [(Fraction(1, 1), Fraction(15, 1))]
      >>> point_list1.append((Fraction(3, 1), Fraction(31, 1)))
      >>> point_list1.append((Fraction(-2, 1), Fraction(6, 1)))
      >>> make_coeff_matrix(point_list1)[0]
      [Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(15, 1)]
      >>> make_coeff_matrix(point_list1)[1]
      [Fraction(9, 1), Fraction(3, 1), Fraction(1, 1), Fraction(31, 1)]
      >>> make_coeff_matrix(point_list1)[2]
      [Fraction(4, 1), Fraction(-2, 1), Fraction(1, 1), Fraction(6, 1)]
      >>> point_list2 = [(Fraction(1, 2), Fraction(5, 6))]
      >>> point_list2.append((Fraction(3, 1), Fraction(17, 1)))
      >>> point_list2.append((Fraction(-4, 5), Fraction(11, 1)))
      >>> make_coeff_matrix(point_list2)[0]
      [Fraction(1, 4), Fraction(1, 2), Fraction(1, 1), Fraction(5, 6)]
      >>> make_coeff_matrix(point_list2)[1]
      [Fraction(9, 1), Fraction(3, 1), Fraction(1, 1), Fraction(17, 1)]
      >>> make_coeff_matrix(point_list2)[2]
      [Fraction(16, 25), Fraction(-4, 5), Fraction(1, 1), Fraction(11, 1)]
    """
    augmatrix = []
    for point in points:
        augmatrix.append([point[0]**2, point[0], Fraction(1, 1), point[1]])
    return augmatrix


def reduce_matrix(m):
    """
    Take a 3 by 4 augmented matrix (a list of length 3 containing lists of
    length 4 of Fraction objects) with the coefficients for a, b, and c and the
    y value for ax^2 + bx + c with the given x, and return the augmented matrix
    in reduced row echelon form.

      >>> point_list1 = [(Fraction(1, 1), Fraction(15, 1))]
      >>> point_list1.append((Fraction(3, 1), Fraction(31, 1)))
      >>> point_list1.append((Fraction(-2, 1), Fraction(6, 1)))
      >>> augmatrix1 = make_coeff_matrix(point_list1)   
      >>> reduced_matrix1 = reduce_matrix(augmatrix1)
      >>> reduced_matrix1[0]
      [Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(1, 1)]
      >>> reduced_matrix1[1]
      [Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(4, 1)]
      >>> reduced_matrix1[2]
      [Fraction(0, 1), Fraction(0, 1), Fraction(1, 1), Fraction(10, 1)]
      >>> point_list2 = [(Fraction(1, 2), Fraction(5, 6))]
      >>> point_list2.append((Fraction(3, 1), Fraction(17, 1)))
      >>> point_list2.append((Fraction(-4, 5), Fraction(11, 1)))
      >>> augmatrix2 = make_coeff_matrix(point_list2)   
      >>> reduced_matrix2 = reduce_matrix(augmatrix2)
      >>> reduced_matrix2[0]
      [Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(2786, 741)]
    """
    # Make all leading coefficients 1
    for num, vals in enumerate(m):
        m[num] = [val / vals[0] for val in vals]

    # Subtract -1 times row 1 from rows 2 and 3
    for row in 1, 2:
        for col in range(4):
            m[row][col] -= m[0][col]

    # Make leading coefficients of rows 2 and 3 (b value) 1
    for row in 1, 2:
        m[row] = [val / m[row][1] for val in m[row]]

    # Solve for c by subtracting row 2 from row 3 and diving row 3 by c
    for col in range(4):
        m[2][col] -= m[1][col]
    m[2] = [val / m[2][2] for val in m[2]]

    # Solve for b by subtracting negative row 2 c times row 3 from row 2
    # and dividing row 2 by b value
    negmultrow3 = [-m[1][2] * val for val in m[2]]
    m[1] = [m[1][i] + negmultrow3[i] for i in range(4)]

    # Solve for a by subtracting negative rows 2 and 3 from row 1
    negmultrow2 = [-m[0][1] * val for val in m[1]]
    m[0] = [m[0][i] + negmultrow2[i] for i in range(4)]
    negmultrow3 = [-m[0][2] * val for val in m[2]]
    m[0] = [m[0][i] + negmultrow3[i] for i in range(4)]

    return m

if __name__ == '__main__':
    import doctest
    doctest.testmod()
