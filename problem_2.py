import sys
# os.walk()
def file_walk(input):
  # folder_name = ""
  # for idx, i in enumerate(input):
  end_found = False
  try:
    # find index of first / print everything before it
    slash_index = input.index("/")
  except:
    end_found = True
    print(input)
    print("end of path")
  else:
    pass
  finally:
    if not end_found:
      # recurse
    pass
    # print(input[:slash_index])
    # remainder = input[slash_index:]
    # if len(remainder) <= 0:
    #   return 
    # else:
    #   file_walk(remainder)
    # chop that off and then put it back through the function
    # if what you want to put through the function the second time is nothing then stop


    # if i == "/":
    #   print(i)
    #   if idx == len(input):
    #     return
    #   else:
    #     file_walk(input[idx:])
  #   else:
  #     folder_name += i
  # print(folder_name + "/")

script, first = sys.argv
file_walk(first)