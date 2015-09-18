How to run:
$ python astar.py [textfile] [heuristic]
ex. $ python astar.py World1.txt 1

Heuristic:
heuristic = 1 - Use Manhattan Distance
heuristic = 2 - Use Chebyshev Distance

Equation for Chebyshev distance heuristic:
|y2-y1|+|x2-x1| - 2 * min(|y2-y1|,|x2-x1|)

Motivation for selecting heuristic:
Manhattan distance only uses N,E,W,S movements, however the agent in this problem can move N,E,W,S,NE,NW,SE,SW. Therefore Chebyshev distance may be more appropriate because it also take diagonal steps into consideration.
Performance:
(Manhattan Distance Heuristic, World1)
Cost of path-
130
Locations along the path-
[(0, 7), (1, 7), (2, 7), (3, 6), (3, 5), (4, 4), (5, 3), (6, 3), (7, 3), (8, 2), (9, 1), (9, 0)]
Number of locations evaluated (number of entries in closed)-
58

(Chebyshev Distance Heuristic, World1)
Cost of path-
130
Locations along the path-
[(0, 7), (1, 7), (2, 7), (3, 6), (3, 5), (4, 4), (5, 3), (6, 3), (7, 3), (8, 2), (9, 1), (9, 0)]
Number of locations evaluated (number of entries in closed)-
58

(Manhattan Distance Heuristic, World2)
Cost of path:
144
Locations along the path:
[(0, 7), (1, 7), (2, 7), (3, 6), (3, 5), (4, 4), (5, 3), (6, 3), (7, 2), (8, 1), (9, 0)]
Number of locations evaluated (number of entries in closed):
54

(Chebyshev Distance Heuristic, World2)
Cost of path:
144
Locations along the path:
[(0, 7), (1, 7), (2, 7), (3, 6), (3, 5), (4, 4), (5, 3), (6, 3), (7, 2), (8, 1), (9, 0)]
Number of locations evaluated (number of entries in closed):
54

They both had the same performance and path and evaluations

