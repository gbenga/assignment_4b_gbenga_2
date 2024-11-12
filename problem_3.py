def gcd(a,b):
  if a == 0:
    return b
  elif b == 0:
    return a
  elif a >= b:
    return gcd(a % b, b)
  else:
    return gcd(a,b % a)

def main():
  gcd(232,72)

if __name__ == "__main__":
  main()