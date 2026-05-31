import random

random_number =  random.randint(1,100)
# print(random_number)

while True:
  user_choice = input("Guess the number or Q to quit:")
  if(user_choice.lower() == 'q'):
    break
  user_choice = int(user_choice)
  if(user_choice == random_number):
    print("Success : Correct Guess!!")
    break
  elif(user_choice < random_number):
    print("Your number was too small , Take a bigger guess...")
  else:
    print("Your number was too big , Take a smaller  guess...")

print("-------Game over-------")
