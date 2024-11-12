import statistics

def mean(data):
  return statistics.mean(data)

def median(data):
  return statistics.median(data)

def mode(data):
  return statistics.mode(data)


def variance(data):
  return statistics.variance(data)

def standard_deviation(data):
  return statistics.stdev(data)


def stats_from_package(data):
  print(f"""
        mean: {mean(data)}
        median: {median(data)}
        mode: {mode(data)}
        variance: {variance(data)}
        standard deviation: {standard_deviation(data)}
        """)
  
f_handle = open(f'./assignment_4b_gbenga/numbers.txt','r').read()
sample_data_from_file = f_handle.strip().split("\n")
# https://stackoverflow.com/questions/7422453/python-change-type-of-whole-list
sample_data = list(map(int, sample_data_from_file))
stats_from_package(sample_data)