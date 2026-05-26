# class car:
#   Company = 'Vehicles'
#   def  __init__(self,fullname):
#     self.name = fullname
#     print('Creating new object')
#   name = "BMW"
#   colour = "blue"

#   def welcome(self):
#     print('Welcome')



# c1 = car('BMW')
# # c2 = car()
# print(c1)
# print(c1.Company)
# print(c1.name)
# print(c1.colour)
# c1.welcome()
# # print(c1.colour)
# # print(c2.name)



class student:
  def __init__(self, name , marks):
    self.name = name
    self.marks = marks

  def avg(self):
    sum = 0
    for val in self.marks:
      sum += val
    print('Name',self.name)
    print('Average marks:',int(sum/len(self.marks)))

  @staticmethod
  def hello():
    print('hello')


s1 = student("Ahmad ",[67,87,97])

# s1.avg()
# s1.hello()




class Acount:
  def __init__(self,bal,acc):
    self.balance = bal
    self.account = acc

  def get_balance(self):
    return self.balance

  def debit(self,amount):
    self.balance -= amount
    print("Rs", amount ,'was debited')
    print("Remaining Balance is ",self.get_balance())

  def credit(self,amount):
    self.balance += amount
    print("Rs", amount ,'was credited')
    print("Total Balance is ",self.get_balance())



acc1 = Acount(10000, 1234)
print("Total balance",acc1.balance)
print('Acount no',acc1.account)


acc1.debit(1200)
acc1.credit(900)
acc1.credit(200)
acc1.credit(100)
acc1.debit(200)

