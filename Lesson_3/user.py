class User:
    def __init__(self, first_name, last_name):
        self.username=first_name
        self.usersurname=last_name
    
    def SayName(self):
        print("Имя: ", self.username)
    def SaySurname(self):
        print("Фамилия: ", self.usersurname)
    def SayAll(self):
        print("Имя и фамилия: ", self.username, self.username)