def month_to_season(month):
    month=int(month)
    if month in [12, 1, 2]:
        print("Зима")
    elif month in [3, 4, 5]:
        print("Весна")
    elif month in [6, 7, 8]:
        print("Лето")
    elif month in [9, 10, 11]:
        print("Осень")
    else: print("В году 12 месяцев")


            
month_to_season(12)