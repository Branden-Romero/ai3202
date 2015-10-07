import sys
import csv
directions = [(1,0), (0,1), (-1,0), (0,-1)]
class mdp:
	def __init__(self, graph):
		self.start = (0,len(graph)-1)
		self.end =  (len(graph[0])-1,0)
		self.actions_list = directions
		#graph.reverse()
		self.graph = graph
		self.gamma = .9
		self.states = set()
		self.reward = {}
		for i in range(0,len(self.graph[0])):
			for j in range(0,len(self.graph)):
				if self.graph[j][i] == 1:
					self.reward[i,j] = -1.0
					self.states.add((i,j))
				elif self.graph[j][i] == 3:
					self.reward[i,j] = -2.0
					self.states.add((i,j))
				elif self.graph[j][i] == 4:
					self.reward[i,j] = 1.0
					self.states.add((i,j))
				elif self.graph[j][i] == 0:
					self.reward[i,j] = 0
					self.states.add((i,j))
		self.reward[self.end[0],self.end[1]] = 50
				

	def reward(self, state):
		return self.reward[state]

	def model(self,state, action):
		if not action:
			return [(0.0, state)]
		else:
			f = tuple([sum(x) for x in zip(state,action)])
			if f in self.states:
				a1 = f
			else:
				a1 = state
			r = tuple([sum(x) for x in zip(state,directions[(directions.index(action)-1)])])
			if r in self.states:
				a2 = r
			else:
				a2 = state

			l = tuple([sum(x) for x in zip(state,directions[(directions.index(action)+1)%len(directions)])])
			if l in self.states:
				a3 = l
			else:
				a3 = state
			return [(.8, a1),(.1, a2),(.1, a3)]
	def actions(self,state):
		if state == self.end:
			return []
		else:
			return self.actions_list


def value_iteration(mdp, epsilon):
	U_p = dict([(state,0) for state in mdp.states])
	while True:
		U = U_p.copy()
		delta = 0
		for state in mdp.states:
			U_p[state] = mdp.reward[state] + mdp.gamma * max([sum([p*U[state_p] for (p,state_p) in mdp.model(state,action)]) for action in mdp.actions(state)])
			if abs(U_p[state] - U[state]) > delta:
				delta = abs(U_p[state]-U[state])
			if delta < epsilon*(1.0-mdp.gamma)/mdp.gamma:
				return U
def pi_mdp(mdp, U):
	pi_v = dict()
	for state in mdp.states:
		acts = mdp.actions(state)
		ind_max = acts[0]
		eu_max = sum([p*U[state_p] for (p,state_p) in mdp.model(state,ind_max)]) 
		for act in acts:
			eu = sum([p*U[state_p] for (p,state_p) in mdp.model(state,act)])
			if eu > eu_max:
				ind_max = act
				en_max = eu
		pi_v[state] = ind_max

	return pi_v

def main(argv):
	with open(argv[1], 'r') as f:
		r = csv.reader(f,delimiter=' ')
		d = list(r)
	f.closed
	d = d[:-1]
	for i in range(0,len(d)):
		d[i] = map(int, d[i])

	epsilon = float(argv[2])
	m = mdp(d)
	U = value_iteration(m,epsilon)
	pi_v = pi_mdp(m,U)
	us_opt = []
	path = []
	location = m.start
	print(pi_v)
	
	while location != m.end:
		path.append(location)
		us_opt.append(U[location])
		move = pi_v[location]
		location = (location[0]+move[0],location[1]+move[1])
	print('Optimal Path:')
	print(path)
	print('Utility scores along the optimal path:')
	print(us_opt)

if __name__ == "__main__":
	main(sys.argv)
