def is_year_leap(year):
    if year%4==0:
        print(year, "True")
    else:
        print(year, "False")

y_str=input("Введите год: ")
y_num=int(y_str)
is_year_leap(y_num)