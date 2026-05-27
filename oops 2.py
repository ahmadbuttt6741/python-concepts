class Account:
    def __init__(self, acc_no, acc_pass):
        self.account_no = acc_no
        self.__account_pass = acc_pass  # name-mangled (private)

    def reset_pass(self):
        # demo: print private password
        print(self.__account_pass)


class FBAccount(Account):
    fb_account = "Muhammad Ahmad"


class InstaAccount(FBAccount):
    insta_account = FBAccount.fb_account


acc1 = Account("1231", "abcde")
print(acc1.account_no)
acc1.reset_pass()

acc2 = InstaAccount("9999", "pass123")
print(acc2.fb_account)
print(acc2.insta_account)



