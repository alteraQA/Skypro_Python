class User:
    def __init__(self, first_name, last_name):
        self.username=first_name
        self.usersurname=last_name
    
    def sayName(self):
        print("Имя:", self.username)
    def saySurname(self):
        print("Фамилия: ", self.usersurname)
    def sayAll(self):
        print("Имя и фамилия:", self.username, self.usersurname)