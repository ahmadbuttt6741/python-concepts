import random
import string

x =  (string.ascii_letters)
y = (string.digits)
z =  (string.punctuation)

single_string = x+y+z
# print(single_string)
# val = random.choice (single_string)


pas_len = int(input("Enter the length of Password: "))
password = ''

for i in range(pas_len):
  password += random.choice(single_string)

print("Your password is : ",password)
