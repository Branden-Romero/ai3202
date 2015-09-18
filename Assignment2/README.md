How to run:

$ python astar.py [textfile] [heuristic]

ex. $ python astar.py World1.txt 1

Heuristic:

heuristic = 1 - Use Manhattan Distance

heuristic = 2 - Use Modified Chebyshev Distance

Equation for Modified Chebyshev distance heuristic:

10 * |y2-y1|+|x2-x1| + (14 - 2 * 10) * min(|y2-y1|,|x2-x1|)

Motivation for selecting heuristic:

Manhattan distance only uses N,E,W,S movements, however the agent in this problem can move N,E,W,S,NE,NW,SE,SW. Therefore Modified Chebyshev distance may be more appropriate because it also take diagonal steps into consideration. Also, the Modified Chebyshev distance uses parameters, so that it can be better suited for a particular graph.

Performance:

(Manhattan Distance Heuristic, World1)

Cost of path-

130

Locations along the path-

[(0, 7), (1, 7), (2, 7), (3, 6), (3, 5), (4, 4), (5, 3), (6, 3), (7, 3), (8, 2), (9, 1), (9, 0)]

Number of locations evaluated (number of entries in closed)-

58

(Modified Chebyshev Distance Heuristic, World1)
Cost of path:
130
Locations along the path:
[(0, 7), (1, 7), (2, 7), (3, 6), (3, 5), (4, 4), (5, 3), (6, 3), (7, 2), (7, 1), (8, 0), (9, 0)]
Number of locations evaluated (number of entries in closed):
44


(Manhattan Distance Heuristic, World2)

Cost of path:

144

Locations along the path:

[(0, 7), (1, 7), (2, 7), (3, 6), (3, 5), (4, 4), (5, 3), (6, 3), (7, 2), (8, 1), (9, 0)]

Number of locations evaluated (number of entries in closed):

54


(Modified Chebyshev Distance Heuristic, World2)

Cost of path:

142

Locations along the path:

[(0, 7), (0, 6), (0, 5), (1, 4), (2, 4), (3, 4), (4, 3), (4, 2), (4, 1), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0)]

Number of locations evaluated (number of entries in closed):

38


The Modified Chebyshev Distance Heursitic performs better than the Manhattan distance.

