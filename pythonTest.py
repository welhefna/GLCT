"""Some examples for DP and memorization

I jsut do this to memorize what I learend within this week

"""

class Solution(object):
	def __init__(self):
		pass
		
	def tower_of_hanoi(self,S,D,E,nDisk):

		if nDisk>0:
			self.tower_of_hanoi(S,E,D,nDisk-1)
			print "Disk-{} from {} to {}".format(S,D,nDisk)
			self.tower_of_hanoi(E,D,S,nDisk-1)
			
	def minCostTicket(self,S,D,costs):
		if S==D:
			return 0
		if S==D-1:
			return costs[S][D]
			
		minCost=costs[S][D]
		for i in range(S+1,D):
			tCost=self.minCostTicket(S,i,costs)+self.minCostTicket(i,D,costs)
			
			if tCost<minCost:
				minCost=tCost
		return minCost
		
	def fibonacciDP(self,num):
	
		if num == 0 or num == 1:
			return num
			
		first = 1
		second = 1
		fib=0
		
		for i in range(3,num+1):
			fib=first+second
			first=second
			second=fib
			
		return fib
		
	def minCostTopDown(self,S,D,costs):
		
		n_stations = len(costs)
		
		memoMat=[list() for _ in xrange(n_stations)]
		for i in range(n_stations):
			memoMat[i]=[-1 for _ in range(n_stations)]
			
		return self.minCostHelper(S,D,costs,memoMat)
		
	def minCostHelper(self,S,D,costs,memo):
		if S==D or S==D-1:
			return costs[S][D]
			
		if memo[S][D] <0 :
			minCost=costs[S][D]
			for i in range(S+1,D):
				tCost=self.minCostHelper(S,i,costs,memo)+self.minCostHelper(i,D,costs,memo)
				if tCost<minCost:
					minCost=tCost
					
			memo[S][D]=minCost
			
		return memo[S][D]
			
			
def main():

	solution_object=Solution()
	solution_object.tower_of_hanoi('A','B','C',3)
	costs=[ 
		[0,1,4,1,4],
		[-1,0,0.5,13,2],
		[-1,-1,0,0.75,14],
		[-1,-1,-1,0,2],
		[-1,-1,-1,-1,0]
	      ]
	print solution_object.minCostTicket(0,4,costs)
	print solution_object.minCostTopDown(0,4,costs)
	print solution_object.fibonacciDP(5)
	
	
if __name__=="__main__":
	main()