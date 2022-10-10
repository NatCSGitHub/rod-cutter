#Natasha Needham
#CS350
#Homework 6 Problem 8.1.6
#Winter 2021
#Python

import time
import random
import sys 
  
def max(a, b): 
	return a if (a > b) else b 
      
def cut(cost, i): 
	if(i <= 0): 
		return 0
	largest = -sys.maxsize-1
      
	for j in range(0, i): 
		largest = max(largest, cost[j] +  cut(cost, i - j - 1)) 
	return largest 

if __name__ == "__main__": 
	#each element is cost of rod of element number's size 
	arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75] 
	size = len(arr) 
	tic = time.perf_counter()
	print(f"Highest cost from size {size} array is", cut(arr, size))
	toc = time.perf_counter()
	print(f"The optimal cutting value was obtained in {1000*(toc-tic):0.4f} seconds") 

