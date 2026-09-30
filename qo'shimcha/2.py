class User:
    def __init__(self, first_name, last_name, birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_day = birth_day

    def get_info(self):
        return f"{self.first_name} {self.last_name}"
    
class Employee(User):
    def __init__(self, first_name, last_name, birth_day, salary):
        super().__init__(first_name, last_name, birth_day)
        self.salary = salary

u1 = User("Toxir", "Toxirov", 2008)
e1 = Employee("Sabrina", "Xoshimjonova", 2010, 1000)

# print(e1.__dict__)
print(e1.get_info())