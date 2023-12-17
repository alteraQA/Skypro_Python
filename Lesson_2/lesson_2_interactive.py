rate_str=input("Оцените, пожалуйста, работу оператора от 1 до 5:  ")
rate=int(rate_str)
if (rate<1):
    rate=1
if (rate>5):
    rate=5
feedback=''    
if rate==1:
    feedback=input("Уточните, пожалуйста, что мы можем улучшить в нашем сервисе? ")
elif rate == 2:
    feedback=input("Нам очень, жаль, что так случилось, утончите, пожалуйста, причину оченки 2: ") 
elif rate==3:
    feedback=input("Напишите, пожалуйста, что мы могли бы улучшить:  ")       
elif rate==4:
    feedback=input("А почему не 5? )) ")
elif rate==5:
    feedback=input("Спасибо за высокую оценку! За что нам похвалить оператора? ")