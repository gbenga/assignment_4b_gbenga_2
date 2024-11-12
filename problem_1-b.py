def validate_email(email, i):
  if i > len(email) - 1:
    print("Invalid email! Did not find @.")
  else:
    if email[i] == "@":
      print(f"Valid email! Found @ at index {i}")
    else:
      validate_email(email, i+1)  

validate_email("charlie.brown@peanuts.com", 0)