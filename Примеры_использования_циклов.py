#1

#from math import *

#print("Arvuta peast! ...4*100-55")
#o_vastus=4*100-55
#vastus=int(input("Lahenda ülesanne ..."))
#k=1
#while True:
#    if vastus!=o_vastus:
#        print("Viga! Sisesta Õige vastus on ...", )
#        vastus=int(input("Sisesta vastus ..."))
#        k+=1      
#    else:
#        print("Õige vastus! Katsed oli ...",k )
#        break



#2

#x=0

#while x<30:
#    if x%2==1:
#        print(x, end=" ")
#    x+=1

#x=0

#while True:
#    if x%2==1:  
#        print(x, end=" ")
#    if x==30:
#        break
#    x+=1


#for x in range(0,30,1):
#    if x%2==1: print(x, end=" ")



print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => "))))  # добавил 2 скобки в конце строки
        break
    except ValueError:
        print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a
    paaris = 0
    paaritu = 0
    while b > 0:     # добавил двоеточее
            if b % 2 == 0:       # добавил ровно
                    paaris += 1    # поменял местами знаки + и =
            else:
                    paaritu += 1    # поменял местами знаки + и =
            b = b // 10
    print("Paarisarvud:", paaris)   # добавил запятую
    print("paarituid numbreid:", paaritu)   # добавил запятую
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake * sisestatud number")
    print()
    b=0
    while a > 0:       # добавил двоеточее
        number = a % 10
        a = a // 10
        b = b * 10
        b += number # поменял местами знаки + и =   
    print("*Tagurpidi* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine")    # удалил лишнюю скобку
    print()
    if c % 2 == 0:   # добавил ровно
        print(c," - paarisarv. Jagage poolt 2.")
    else:
        print(c," - paaritu number. Korrutage 3-ga, lisage 1 ja jagage 2.")
    while c != 1:
            if c % 2 == 0:   # добавил ровно
                    c = c / 2   # удалил ровно
            else:
                    c = (3*c + 1) / 2   # удалил ровно
            print(round(c), end=" ")   # добавил верный знак препинания
    print()
    print("Hüpotees on õige")   # добавил верный знак препинания