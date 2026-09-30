class User:
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def get_info(self):
        return f"{self.first_name} {self.last_name}"


class Employee:
    def __init__(self, phone, salary):
        self.phone = phone
        self.salary = salary

    def get_info(self):
        return f"{self.phone} {self.salary}"


class Manager(User, Employee):
    def __init__(self, first_name, last_name, birth_year, phone, salary, email):
        User.__init__(self, first_name, last_name, birth_year)
        Employee.__init__(self, phone, salary)
        self.email = email

m1 = Manager("Toxir", "Toxiriov", 2000, "+998", 10000, "t@gmail.com")
# print(m1.__dict__)
print(m1.get_info())

print(User.get_info(m1))
print(Employee.get_info(m1))
