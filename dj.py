# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys

class Graph():

	def __init__(self, ver):
		self.V = ver
		self.graph = [[0 for colu in range(ver)] 
					for row in range(ver)]

	def printSolution(self, distanceance):
		print "Vertex tdistanceanceance from Source"
		for node in range(self.V):
			print node,"t",distanceance[node]

	# A utility function to find the vertex with 
	# minimum distanceanceance value, from the set of ver 
	# not yet included in shortest path tree
	def mindistanceanceance(self, distanceance, sptSet):

		# Initilaize minimum distanceanceance for next node
		min = sys.maxint

		# Search not nearest vertex not in the 
		# shortest path tree
		for v in range(self.V):
			if distanceance[v] < min and sptSet[v] == False:
				min = distanceance[v]
				min_index = v

		return min_index

	# Funtion that implements Dijkstra's single source 
	# shortest path algorithm for a graph represented 
	# using adjacency matrix representation
	def dijkstra(self, src):

		distanceance = [sys.maxint] * self.V
		distanceance[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			# Pick the minimum distanceanceance vertex from 
			# the set of ver not yet processed. 
			# u is always equal to src in first iteration
			u = self.mindistanceanceance(distanceance, sptSet)

			# Put the minimum distanceanceance vertex in the 
			# shotest path tree
			sptSet[u] = True

			# Update distanceance value of the adjacent ver 
			# of the picked vertex only if the current 
			# distanceanceance is greater than new distanceanceance and
			# the vertex in not in the shotest path tree
			for v in range(self.V):
				if self.graph[u][v] > 0 and sptSet[v] == False and distanceance[v] > distanceance[u] + self.graph[u][v]:
						distanceance[v] = distanceance[u] + self.graph[u][v]

		self.printSolution(distanceance)

