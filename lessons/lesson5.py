'''passwd = "123"
#a = (input("Введите пароль :"))
while input("Введите пароль :") == passwd:
    print ("пароль правильный")
    break
else:
    print ("пароль неверный") '''

'''a = 0
for i in range(0, 101, 1):
   # print(i)
    a += i
    print (a) '''


'''a= input("Введите слово :")
for i in a:
    print (i) '''

'''a= int(input("Введите число :"))
for i in range(1, 16, 1):
    print (i, a*i)'''
    
a= int(input("Введите число :"))+1
b=int(0)
for i in range(0, a, 2):
    #print(i)
    b+=i
print (b)