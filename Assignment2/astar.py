import sys
import csv

class Node:
	def __init__(self,key,parent):
		self.location = key
		self.g = 0
		self.h = 0
		self.f = 0
		self.parent = parent

def min_node(node_list):
	minimum = float('inf')
	for node in node_list:
		if node.f < minimum:
			minimum = node.f
			q = node
	return q

def movable(location):
	x,y = location
	if x < 0 or y < 0 or x >= len(graph[0]) or y >= len(graph):
		return False
	return not graph[y][x] == 2
		

def find_neighbors(node):
	x,y = node.location
	neighbors = [(x+1,y),(x,y+1),(x-1,y),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y+1)]
	neighbors_valid = filter(movable, neighbors)
	return neighbors_valid

def distance(start,end):
	x1,y1 = start
	x2,y2 = end
	dist = 0
	if abs(y2-y1) + abs(x2-x1) > 1:
		dist = 14
	else:
		dist = 10

	if graph[y2][x2] == 1:
		dist = dist + 10

	return dist

def heuristic1(p1, p2):
	x1,y1 = p1
	x2,y2 = p2
	return abs(y2-y1) + abs(x2-x1)

def heuristic2(p1, p2):
	x1,y1 = p1
	x2,y2 = p2
	return abs(y2-y1)+abs(x2-x1) - 2 * min(abs(y2-y1),abs(x2-x1))

def inList(list1,list2,node):
	for item in list1:
		if item.location == node.location:
			return True
	
	for item in list2:
		if item.location == node.location:
			return True
	return False

def astar(start,end,heuristic):
	open_list = [start]
	closed_list = []
	while open_list:
		q = min_node(open_list)
		open_list.pop(open_list.index(q))
		neighbors = find_neighbors(q)
		for neighbor in neighbors:
			node = Node(neighbor,q)
			node.g = q.g + distance(q.location,node.location)
			if heuristic == 1:
				node.h = heuristic1(node.location,end)
			elif heuristic == 2:
				node.h = heuristic2(node.location,end)	
			node.f = node.g + node.h
			
			if node.location == end:
				return (node,len(closed_list))

			if not inList(open_list,closed_list,node):
				open_list.append(node)

		closed_list.append(q)
			

def main(argv):
	with open(argv[1], 'r') as f:
		r = csv.reader(f,delimiter=' ')
		d = list(r)
	f.closed
	
	d = d[:-1]
	for i in range(0,len(d)):
		d[i] = map(int, d[i])
	global graph 
	graph = d
	start = Node((0,len(d)-1),None)
	heuristic = int(argv[2])
	node,num_eval = astar(start,(len(d[0])-1,0),heuristic)
	cost = node.g
	path = []
	
	while node.parent:
		path = [node.location] + path
		node = node.parent
	path = [node.location] + path
	
	print("Cost of path:")
	print(cost)
	print("Locations along the path:")
	print(path)
	print("Number of locations evaluated (number of entries in closed):")
	print(num_eval)

if __name__ == "__main__":
	main(sys.argv)
