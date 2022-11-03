class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner  # поле
        self._balance = balance

    # геттер, сеттер , делитер - 3 метода
    # (для чтения, для записи, для удаления (по желанию))

    def get_owner(self):
        return self._owner

    def set_owner(self, owner):
        self._owner = owner

    def del_owner(self):
        del self._owner

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance > 0:  # это защита
            self._balance = balance

    def del_balance(self):
        del self._balance

    def __str__(self):
        return f"{self._owner} has ${self._balance} on account."

    # класс проперти берет на себя 3 метода (а методы обратятся к протектед полям) -
    # чтобы не обращаться к 3 методам, он сам автоматически вызовет нужную вещь
    owner = property(get_owner, set_owner, del_owner, "owner property")
    balance = property(fget=get_balance, fset=set_balance, fdel=del_balance, doc="balance property")
