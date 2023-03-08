from random import randint
n=0
while n<3:
    a=int(randint(0,10))
    b=int(randint(0,10))
    print(a , "+",  b , "=")
    c=int(input("Запишите ответ"))
    if a+b!=c:
        n=n+1
if n==3:
    print("Конец игры")