# Find the Quadratic Function Through 3 Points

Find the quadratic function that contains three points with rational
coordinates, and print out the result in form:

    f(x) = ax^2 + bx + c.

**process_point_sets.py** loads the input from a text file in the following
format:

    (s1x1, s1y1); (s1x2, s1y2); (s1x3, s1y3)
    (s2x1, s2y1); (s2x2, s2y2); (s2x3, s2y3)
               ...
    (snx1, s2y1); (snx2, sny2); (snx3, sny3)

All three x values must be non-zero.

Parts:

0. make_aug_matrix.py
0. print_polynomial.py
0. process_point_sets.py
