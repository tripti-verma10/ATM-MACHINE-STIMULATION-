# ATM Machine Simulation

class ATM:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def change_pin(self):
        old_pin = input("Enter your old PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            self.pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Invalid old PIN. Try again!")

    def transaction_enquiry(self):
        print(f"Your account balance is: ${self.balance:.2f}")

    def cash_withdrawal(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance. Try again!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! Your new balance is: ${self.balance:.2f}")

    def cash_deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        print(f"Deposit successful! Your new balance is: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Your account balance is: ${self.balance:.2f}")

def main():
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    atm = ATM(account_number, pin, balance=1000)  # initial balance is $1000

    while True:
        print("\nATM Menu:")
        print("1. Change PIN")
        print("2. Transaction Enquiry")
        print("3. Cash Withdrawal")
        print("4. Cash Deposit")
        print("5. Check Balance")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.change_pin()
        elif choice == "2":
            atm.transaction_enquiry()
        elif choice == "3":
            atm.cash_withdrawal()
        elif choice == "4":
            atm.cash_deposit()
        elif choice == "5":
            atm.check_balance()
        elif choice == "6":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()