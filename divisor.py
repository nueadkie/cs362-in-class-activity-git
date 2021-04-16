def divisor(n):
  num_list = []
  for i in range(1, n + 1):
    if n % i == 0:
      num_list.append(i)
  
  return num_list

n = int(input("Please enter a number: "))
print("The divisors for this number are: ", divisor(n))