from bank_account import BankAccount


def main():
    account1 = BankAccount("Alex", 1000)
    account1.set_balance(-100)

    print(account1)


main()
