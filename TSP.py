import heapq
intmax = 9999999999
fringList = []
def MinKey(V, key, mstset):
    min = intmax
    minindex = -1
    for v in range(V):
        if(key[v]<min and mstset[v]==False):
            min = key[v]
            minindex = v
    return minindex     

def PrimMst(M):
    V = len(M)
    if V == 0:
    	return 0
    mstset = [False]*V
    key = [intmax]*V
    #print("key" , key)
    parent = [-1] * V
    key[0] = 0
    parent[0] = -1
    cost = 0
    for cnt in range (V):
        u = MinKey(V, key, mstset)
        mstset[u] = True
        for v in range (V):
            if M[u][v] > 0 and mstset[v] == False and key[v] > M[u][v] :
                key[v] = M[u][v]
                parent[v] = u
    for i in range(1,V):
        cost = cost + M[i][parent[i]]

    return cost             


def MinSpanCost(C):
    Ver = list(range(len(A)))
    NC = [i for i in Ver+C if i not in Ver or i not in C]
    #print(NC)
    M = []
    for i in range(len(NC)):
        temp = []
        for j in range(len(NC)):
            temp.append(A[NC[i]][NC[j]])
        M.append(temp)
    #print(M)        
    mincost = PrimMst(M)
    return mincost


class Node():

	def __init__(self, curpath, f_value, curpathlen):
		self.path = list(curpath)
		self.f_val = f_value
		self.pathlen = curpathlen

	def __lt__(self, other):
		return self.f_val < other.f_val	

	def Successors(self, path):
		Ver = list(range(len(A)))
		#print(Ver, "Ver")
		#print(path, "path")
		M = [i for i in path+Ver if i not in Ver or i not in path]
		M.sort()
		return M
	
	def Find_G(self, vert):
		return self.pathlen + A[self.path[-1]][vert]

	def Finf_H(self, vert):
		newpath = list(self.path)
		newpath.append(vert)
		mincost = MinSpanCost(newpath)
		unvisited = list(self.Successors(newpath))
		if len(unvisited) == 0 :
			return mincost
		minstart = intmax
		for i in range(len(unvisited)):
			if minstart > A[newpath[0]][unvisited[i]] and A[newpath[0]][unvisited[i]] != 0:
				minstart = A[newpath[0]][unvisited[i]]
		return mincost + minstart		

	def Expand(self):
		child = self.Successors(self.path)
		#print("Successors", child)
		for i in range(len(child)):
			newpath = []
			newpath = list(self.path)
			#print("newpath" , newpath)
			g_value = self.Find_G(child[i])
			f_value = g_value + self.Finf_H(child[i])
			#print("g_values ", g_value)
			newpath.append(child[i])
			newnode = Node(newpath, f_value, g_value)
			heapq.heappush(fringList, newnode)

def Picknext():
	#if len(fringList) == 0:
		#print("Empty")
	return heapq.heappop(fringList)	

def A_star():

	mincost = MinSpanCost([0]) 
	startdist = intmax
	for i in range(1, len(A)):
		if startdist > A[0][i]:
			startdist = A[0][i]
	start_fvalue = mincost + startdist
	newnode = Node([0], start_fvalue ,0)
	fringList.append(newnode)
	#print("fringelist path ", fringList[0].path )
	while True:
		currnode = Picknext()
		print(currnode.path , " This is to be expanded ")
		if len(currnode.Successors(currnode.path)) == 0 :
			return currnode
		currnode.Expand()


with open("input.txt",'r') as f:
	lines = f.readlines()
N = int(lines[0])
A = [[int(x) for x in line.split()] for line in lines[1:]]


output = A_star()
print("path" , output.path)
answer = 0
for i in range(1, len(output.path)):
	answer = answer + A[output.path[i-1]][output.path[i]]
answer = answer + A[output.path[N-1]][output.path[0]]	
print("output" ,answer)

#N = 5
#A = [[0,10,8,9,7], [10,0,10,5,6], [8,10,0,8,9],[9,5,8,0,6], [7,6,9,6,0]]
#A = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]