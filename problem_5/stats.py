from math import *
import sys

from ..problem_4.random_numbers import generate

def mean(data):
  return sum(data)/len(data)

# https://www.geeksforgeeks.org/find-median-of-list-in-python/
def median(data):
  data.sort() 

  mid = floor(len(data) / 2)
  if len(data) % 2 == 0:
    # if even number of datapoints
    return (data[mid] + data[mid -1]) / 2
  else:
    #if odd number of datapoints
    return data[mid]
  

def mode(data):
  occurrences = {}

  for d in data:
    if d in occurrences.keys():
      occurrences[d] +=1
    else:
      occurrences[d] = 1

  key_list = list(occurrences.keys())
  val_list = list(occurrences.values())
  highest_occurrence = max(val_list)
  # need to handle multiple modes
  mode = key_list[val_list.index(highest_occurrence)]

  return mode

# https://www.mathsisfun.com/data/standard-deviation.html
# https://www.geeksforgeeks.org/python-variance-of-list/
def variance(data):
  avg = mean(data)
  return sum((i - avg) ** 2 for i in data) / len(data) 
#could not get this to match statistics package

def standard_deviation(data):
  return sqrt(variance(data))

def stats(data):
  print(f"""
        mean: {mean(data)}
        median: {median(data)}
        mode: {mode(data)}
        variance: {variance(data)}
        standard deviation: {standard_deviation(data)}
        """)
  
def main():
  script, first = sys.argv
  try:
    num = int(first)
  except:
    print("please enter a whole number")
  else:
    # https://hkim-dev.github.io/programming/Understanding-Python's-'ImportError-Attempted-Relative-Import-With-No-Known-Parent-Package'-Error/
    #could only get it to work when run as a module from one directory above root (assignment_4b_gbenga)
    
    stats(generate(num, True))
    pass
    
if __name__ == "__main__":
  main()