class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance
        self._valid = True

    def is_valid(self):
        return self._valid

    def set_valid(self, valid):
        self._valid = valid

    def get_owner(self):
        return self._owner

    def set_owner(self, owner):
        self._owner = owner

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance > 0:
            self._balance = balance

    def __str__(self):
        return f"{self._owner} has ${self._balance} on account."
