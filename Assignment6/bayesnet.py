import getopt, sys
class Node:
	def __init__(self,parents,value):
		self.parents = parents
		self.value = value

#def conditional(a,b,dict):
	
#def joint(a,b,c,dict):

def marginal(a,net):
	if net[a].parents == None:
		return net[a].value
	else:
		marg = 0
		p_t = []
		for parent in net[a].parents:
			p_t.append(marginal(parent,net))
		for key in net[a].value:
			if len(key) == 2:
				if key[0] == 't':
					p1 = p_t[0]
				else:
					p1 = 1 - p_t[0]
				
				if key[1] == 't':
					p2 = p_t[1]
				else:
					p2 = 1 - p_t[1]
				
				marg += net[a].value[key] * p1 * p2

			else:
				if key == 't':
					p = p_t[0]
				else:
					p = 1 - p_t[0]
				marg += net[a].value[key] * p
	return marg
def main():

	try:
		opts, args = getopt.getopt(sys.argv[1:], "g:j:m:p:")
	except getopt.GetoptError as err:
		print str(err)
		sys.exit(2)

	opts_dict = dict(opts)	
	bayesNet = dict()
	bayesNet["P"] = Node(None,.1)
	bayesNet["S"] = Node(None,.3)
	
	for item in opts:
		if item[0] == '-p' and item[1][0] == 'P':
			if '=' in item[1]:
				prob = float(item[1][2:])
				bayesNet["P"] = Node(None, prob)
			else:
				prob = float(item[1][1:])
				bayesNet["P"] = Node(None,prob)
		if item[0] == '-p' and item[1][0] == 'S':
			if '=' in item[1]:
				prob = float(item[1][2:])
				bayesNet["S"] = Node(None,prob)
			else:
				prob = float(item[1][1:])
				bayesNet["S"] = Node(None,prob)
	if "-p" in opts_dict:
		del opts_dict["-p"]
	
	bayesNet["C"] = Node(["P", "S"] ,{'tt': 0.05, 'tf':0.02, 'ft':0.03, 'ff':0.001})
	bayesNet["X"] = Node(["C"], {'t': 0.90, 'f': 0.20})
	bayesNet["D"] = Node(["C"], {'t' : 0.65, 'f' : 0.30})

	command, args = opts_dict.items()[0]
	
	calculation = 0.0
	if command == '-m' and len(args) == 1:
		calculation = marginal(args,bayesNet)
	else:
		calculation = 1 - marginal(args[1:],bayesNet)

	print (calculation)

if __name__ == "__main__":
	main()
