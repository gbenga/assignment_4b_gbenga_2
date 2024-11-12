# I think this would be more efficient for a long string
def validate_email(email):
  found_symbol = False
  for idx, char in enumerate(email):
    if char == "@":
      print(f"Valid email! Found @ at index {idx}")
      found_symbol = True
  if not found_symbol:
    print("Invalid email! Did not find @.")

validate_email("charlie.brown@peanuts.com")