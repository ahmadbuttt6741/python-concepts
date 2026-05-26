class account:
  def __init__(self,acc_no,acc_pass):
    self.acount_no = acc_no
    self.__acount_pass = acc_pass

  def reset_pass(self):
    print(self.__acount_pass)
acc1 = account("1231","abcde")


print(acc1.acount_no)
# print(acc1.acount_pass)


acc1.reset_pass()


