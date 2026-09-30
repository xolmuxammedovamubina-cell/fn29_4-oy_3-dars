class User:
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.__birth_year = birth_year

    @property
    def birth_year(self):
        return self.__birth_year

class Employee(User):
    def __init__(self, first_name, last_name, birth_year, salary):
        super().__init__(first_name, last_name, birth_year)
        self.salary = salary

    def get_info(self):
        return f"{self.first_name} {self.last_name}. {self.birth_year}"

e1 = Employee("Sabrinaxon", "Hoshimjonova", 2010, 1000)
print(e1.get_info())
print(e1.__dict__)
print(e1.birth_year)