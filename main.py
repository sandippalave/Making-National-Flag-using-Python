class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print('Personal Information')
        print(' ')
        print('Name is- ', self.name)
        print('Age is- ',self.age)
        print('Gender is- ',self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposits(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(self.name,'your updated Balance is ',self.balance)

    def withdraw(self, withdraw):
        self.withdraw = withdraw
        if self.balance<self.withdraw:
            print("Sorry,Insufficient Balance")
        else:
            self.balance = self.balance - self.withdraw
            print('You withdrawan Rs.',self.withdraw)

    def view_balance(self):
            print('You have Rs.',self.balance, 'in your account')



if __name__ == '__main__':
    x = Bank('Sandip', 22, 'Male')
    x.view_balance()


