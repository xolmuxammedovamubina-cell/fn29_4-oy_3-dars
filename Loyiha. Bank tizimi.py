class User:
    def __init__(self, name, phone, balance):
        self.name = name
        self._phone = phone
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Balans 0 dan kichik bo'lmasligi kerak")

    def __str__(self):
        return f"Ismi: {self.name}\nBalans: {self.__balance}"

    def __repr__(self):
        return f"User(Ismi: {self.name}, Telefon raqami: {self._phone}, Balans: {self.__balance})"


print("------------------------------------------------------")



class Client(User):
    def __init__(self, name, phone, balance, card_number):
        super().__init__(name, phone, balance)
        self.card_number = card_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Balansga pul qo'shildi")
        else:
            print("0 dan katta summa kiriting")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Balansdan pul yechildi")
            else:
                print("Balansda yetarli pul yo'q")
        else:
            print("0 dan katta summa kiriting")

    def info(self):
        return f"Ismi: {self.name}\nTelefon raqami: {self._phone}\nKarta raqami: {self.card_number}\nBalansi: {self.balance}"


print("------------------------------------------------------")



class Employee(User):
    def __init__(self, name, phone, balance, employee_id, salary):
        super().__init__(name, phone, balance)
        self.employee_id = employee_id
        self.salary = salary

    def work(self):
        return f"{self.name} - bank xodimi sifatida ishlayapti"

    def info(self):
        return f"Ismi: {self.name}\nTelefon raqami: {self._phone}\nXodimning identifikatsiya raqami: {self.employee_id}\nMaosh: {self.salary}"


print("------------------------------------------------------")


class Bank:
    def __init__(self):
        self.clients = []
        self.employees = []

    def add_client(self, client):
        self.clients.append(client)
        print(f"{client.name} bankka qo'shildi")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} bank xodimi sifatida qo'shildi")

    def show_clients(self):
        print("\n----- BARCHA MIJOZLAR -----")

        for client in self.clients:
            print(client.info())
            print("--------------------------")

    def show_employees(self):
        print("\n----- BARCHA XODIMLAR -----")

        for employee in self.employees:
            print(employee.info())
            print("--------------------------")

    def find_client(self, value):
        for client in self.clients:
            if client._phone == value or client.card_number == value:
                return client
        return None


print("------------------------------------------------------")

bank = Bank()


c1 = Client("Ali", "123456789", 1501000, "8600123456789010")
c2 = Client("Vali", "912345678", 1502000, "8600123456789011")
c3 = Client("Hasan", "923456789", 1503000, "8600123456789012")

e1 = Employee("Ali", "981234567", 1504000, "001", 5000000)
e2 = Employee("Vali", "987123456", 1505000, "002", 4500000)


bank.add_client(c1)
bank.add_client(c2)
bank.add_client(c3)
bank.add_employee(e1)
bank.add_employee(e2)

print("------------------------------------------------------")

c1.deposit(500000)
c2.withdraw(300000)

print("------------------------------------------------------")

print("Ali balans:", c1.balance)
print("Vali balans:", c2.balance)
print("Hasan balans:", c3.balance)

print("------------------------------------------------------")

bank.show_clients()
bank.show_employees()

print("------------------------------------------------------")

users = [c1, c2, c3, e1, e2]

for user in users:
    print(user.info())

print("------------------------------------------------------")

for user in users:
    if isinstance(user, Employee):
        print(user.work())

print("------------------------------------------------------")

for user in users:
    print(str(user))

print("------------------------------------------------------")

for user in users:
    print(repr(user))

print("------------------------------------------------------")

topilgan_mijoz = bank.find_client("123456789")

if topilgan_mijoz:
    print("Topilgan mijoz:")
    print(topilgan_mijoz.info())
else:
    print("Mijoz topilmadi")

print("------------------------------------------------------")

print("Public:", c1.name)
print("Protected:", c1._phone)

try:
    print(c1.__balance)
except AttributeError:
    print("Private __balance atributiga tashqaridan murojaat qilib bo'lmaydi")

print("Balance:", c1.balance)
