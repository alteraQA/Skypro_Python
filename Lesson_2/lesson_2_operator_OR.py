crit1="red"
crit2="lock"

color=input("Введите цвет: ")
feature=input("Введите параметр: ")
if crit1==color or crit2==feature:
    print("Ура! Нашли!")
else:
    print("Что-то не то.. Ищем дальше!")   