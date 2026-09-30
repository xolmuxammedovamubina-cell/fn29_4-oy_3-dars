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

    
class Employee(User):
    def __init__(self, first_name, last_name, birth_day, salary):
        super().__init__(first_name, last_name, birth_day)
        self.salary = salary


class Manager(User):
    def __init__(self, first_name, last_name, birth_day, control):
        super().__init__(first_name, last_name, birth_day)
        self.control = control

# Poliforizm
    def get_info(self):
        return f"{self.first_name} {self.last_name}: Control: {self.control}"

    
class Director(Manager):
    def day_meeting(self):
        return f"Bugun 08:00 da majlis. By {self.get_info()}"


u1 = User("Toxir", "Toxirov", 2008)
e1 = Employee("Sabrina", "Xoshimjonova", 2010, 1000)
m1 = Manager("Shaxriyor", "Maxmudov", 2009, "Qattiqqo'l")
d1 = Director("Mubina", "Xolmuxammedova", 2008, "Pul bilan boshqarish")

print(e1.__dict__)
print(e1.get_info())
print(m1.get_info())
print(m1.__dict__)
print(d1.__dict__)
print(d1.get_info())