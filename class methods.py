class BankAccount:
    """A class representing a bank account with various methods"""

    # Class variable (shared across all instances)
    bank_name = "Python National Bank"
    interest_rate = 0.02

    def __init__(self, account_holder, account_number, initial_balance=0):
        self._account_holder = account_holder  # Protected attribute
        self._account_number = account_number  # Protected attribute
        self._balance = initial_balance        # Protected attribute
        self._transactions = []

        # Record initial transaction
        if initial_balance > 0:
            self._transactions.append(f"Initial deposit: ${initial_balance}")

    # PROPERTY (Getter and Setter) - For balance
    @property
    def balance(self):
        """Getter for balance"""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Setter for balance - prevents negative balance"""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

    # PROPERTY with only getter (read-only) - For account holder
    @property
    def account_holder(self):
        """Getter for account holder (read-only)"""
        return self._account_holder

    # PROPERTY with getter and setter with validation - For account number
    @property
    def account_number(self):
        """Getter for account number"""
        return self._account_number

    @account_number.setter
    def account_number(self, new_number):
        """Setter for account number with validation"""
        if not isinstance(new_number, str) or len(new_number) != 10:
            raise ValueError("Account number must be a 10-digit string")
        self._account_number = new_number

    # CLASS METHOD - Works with class variables
    @classmethod
    def update_interest_rate(cls, new_rate):
        """Update the interest rate for all accounts"""
        if not 0 <= new_rate <= 0.1:
            raise ValueError("Interest rate must be between 0 and 0.1")
        cls.interest_rate = new_rate
        print(f"Interest rate updated to {cls.interest_rate * 100}%")

    @classmethod
    def create_account_with_initial_bonus(cls, account_holder, account_number):
        """Factory method: creates account with $50 bonus"""
        bonus_amount = 50
        account = cls(account_holder, account_number, bonus_amount)
        account._transactions.append(f"Welcome bonus: ${bonus_amount}")
        print(f"Account created with ${bonus_amount} welcome bonus!")
        return account

    # STATIC METHOD - Doesn't access class or instance variables
    @staticmethod
    def validate_account_number(account_number):
        """Utility method to validate account number format"""
        return isinstance(account_number, str) and len(account_number) == 10 and account_number.isdigit()

    @staticmethod
    def calculate_compound_interest(principal, rate, years):
        """Calculate compound interest (pure utility function)"""
        return principal * (1 + rate) ** years

    # Instance methods
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount  # Using the setter
        self._transactions.append(f"Deposit: +${amount}")
        print(f"Deposited ${amount}. New balance: ${self.balance}")
        return True

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Available balance: ${self.balance}")

        self.balance -= amount
        self._transactions.append(f"Withdrawal: -${amount}")
        print(f"Withdrew ${amount}. New balance: ${self.balance}")
        return True

    def add_interest(self):
        """Add interest based on current interest rate"""
        interest = self.balance * self.__class__.interest_rate
        self.balance += interest
        self._transactions.append(f"Interest added: +${interest:.2f}")
        print(f"Added ${interest:.2f} interest. New balance: ${self.balance}")

    def get_transaction_history(self):
        """Return the transaction history"""
        return self._transactions.copy()  # Return a copy to protect original

    def __str__(self):
        return f"Account[{self.account_number}] - Holder: {self.account_holder} - Balance: ${self.balance:.2f}"


# DEMONSTRATION OF USAGE

if __name__ == "__main__":
    print("=" * 50)
    print("BANKING SYSTEM DEMONSTRATION")
    print("=" * 50)

    # 1. Using CLASS METHOD as factory
    print("\n1. Creating account with class method (factory):")
    account1 = BankAccount.create_account_with_initial_bonus("Alice Johnson", "1234567890")

    # 2. Creating regular account
    print("\n2. Creating regular account:")
    account2 = BankAccount("Bob Smith", "0987654321", 500)
    print(account2)

    # 3. Using INSTANCE METHODS
    print("\n3. Performing transactions:")
    account1.deposit(1000)
    account1.withdraw(200)
    account1.add_interest()

    # 4. Using STATIC METHODS
    print("\n4. Using static methods:")
    is_valid = BankAccount.validate_account_number("1234567890")
    print(f"Is '1234567890' valid account number? {is_valid}")

    interest = BankAccount.calculate_compound_interest(1000, 0.05, 3)
    print(f"Compound interest on $1000 at 5% for 3 years: ${interest:.2f}")

    # 5. Using PROPERTIES (Getters/Setters)
    print("\n5. Demonstrating getters and setters:")
    print(f"Current balance (via getter): ${account1.balance}")

    # Trying to set negative balance (will raise error)
    try:
        account1.balance = -100
    except ValueError as e:
        print(f"Error setting balance: {e}")

    # Valid setter usage
    account1.balance = 5000
    print(f"After direct balance set: ${account1.balance}")

    # Read-only property
    print(f"Account holder (read-only): {account1.account_holder}")
    # account1.account_holder = "New Name"  # This would raise AttributeError

    # Account number validation in setter
    try:
        account1.account_number = "123"  # Invalid length
    except ValueError as e:
        print(f"Error setting account number: {e}")

    account1.account_number = "9999999999"  # Valid
    print(f"Account number updated to: {account1.account_number}")

    # 6. Using CLASS METHOD to update class variable
    print("\n6. Updating class variable with class method:")
    print(f"Current interest rate: {BankAccount.interest_rate * 100}%")
    BankAccount.update_interest_rate(0.035)
    print(f"New interest rate: {BankAccount.interest_rate * 100}%")

    # 7. Display transaction history
    print("\n7. Transaction history for account1:")
    for i, transaction in enumerate(account1.get_transaction_history(), 1):
        print(f"  {i}. {transaction}")

    # 8. Show final account status
    print("\n8. Final account status:")
    print(account1)
    print(account2)

    # 9. Demonstrate class variable access
    print(f"\nBank name (class variable): {BankAccount.bank_name}")
    print(f"Access through instance: {account1.bank_name}")
