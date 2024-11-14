# os.walk()
import sys
indentation = ''
def file_walk(input):
  global indentation
  input = indentation + input
  try:
    slash_index = input.index("/")
  except:
    print(input)
  else:
    print(input[:slash_index + 1])
    if "/" not in input:
      print("base")
      return
    else:
      indentation += ' '
      file_walk(input[slash_index + 1:])
      return

script, first = sys.argv
file_walk(first)