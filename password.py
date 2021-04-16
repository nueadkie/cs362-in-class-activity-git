import random

def password_gen(n):
  symbols = "!@#$%^&*()QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm"
  password = ""
  for i in range(n):
    password += random.choice(symbols)
  return password

while True:
  n = input("Please enter a password length: ")
  if n.isdigit():
    n = int(n)
    break
  else:
    print("Invalid input.")

password = password_gen(n)
print("Your password is:", password)