import random
import sys

def generate(n, should_write_to_file):
  data_set = []
  for x in range(0,n):
    data_set.append(random.randint(0, 100))
  sorted_data_set = sorted(data_set)

  if should_write_to_file:
    fhandle = open('./assignment_4b_gbenga/numbers.txt', 'w')
    for s in sorted_data_set:
      fhandle.write(f"{s}\n")
    fhandle.close()
  return sorted_data_set

script, first = sys.argv
generate(int(first),True)