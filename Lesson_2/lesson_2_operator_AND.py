user_login="test"
user_password="test123"

login=input("Введите логин: ")
password=input("Введите праоль: ")
if login==user_login and password==user_password:
    print("Авторизация пройдена успешно!")
else:
    print ("Неверно введен логин или пароль")
