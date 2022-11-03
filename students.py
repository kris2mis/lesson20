# ТРЕНИРОВКА геттера, сеттера

class Student:
    """class description of student"""

    def __init__(self, name, age,
                 mark=4, alive=True):
        self._name = name
        self._age = age
        self.mark = mark
        self.alive = alive

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def del_name (self):
        del self._name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age

    def del_age(self):
        del self._age



    def __str__(self):
        msg = self.name
        msg += (" is still alive "
                if self.alive else " is dead ")
        msg += "(mark: " + str(self.mark) + ")"

        return msg


class Killer():
    """class description of
  student killer """

    # study or die
    def kill(self, student, mark):
        if isinstance(student, Student):
            if student.alive and student.mark < mark:
                student.alive = False
                return True

        return False
