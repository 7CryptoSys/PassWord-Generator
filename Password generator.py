import random

#PASSWORD GENERATOR! 

upper_words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_words = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

password_chars = int(input("How many characters will your password have:"))

password = upper_words + lower_words + numbers

def generator(password):
  password = "".join(random.sample(password, password_chars))
  print(password)

print(generator(password))
