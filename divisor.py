def divisor(n):
  num_list = []
  for i in range(1, n + 1):
    if n % i == 0:
      num_list.append(i)
  
  return num_list

while True:
  n = input("Please enter a number: ")
  if n.isdigit():
    n = int(n)
    break
  else:
    print("Invalid input.")

print("The divisors for", n, "are:", divisor(n))