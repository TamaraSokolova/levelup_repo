import math
import random
#1
'''a=0
for i in range(100):
    a=a+i    
print('Сумма=', a)'''

#2
'''a=str(input('Введите слово: '))
for i in a: #range(a,len(a)):
    print(i) #, end='') '''

#3
'''x=int(input('Введите число: '))
for i in range(1,11):
    print(x*i)'''

#4
'''a=0
n=int(input('Введите число: '))
for i in range(0,n+1, 2):   
    a=a+i    
print('Сумма четных чисел от 1 до ', n,' равна ', a)'''

#5
'''a=0
n=int(input('Введите число: '))
for i in range(n+1):   
    while i%3==0:
        a=a+i        
        break
print('Сумма чисел, кратных 3, от 1 до', n, 'равна', a) '''

#6
'''n=int(input('Введите простое число: '))
if (n<=0):
    print("Введите число больше нуля")
else:
    for i in range(2,n):
        if (n%i)==0:
            print(i, ' ',n,' не является простым числом')
            break
    else:
        print(n,' простое число')'''

#7
'''n=int(input('Введите число: '))
i=1
m=1
while (i<=n):
   # print(i)
    i+=1
    m=m*(i-1)
   # print(m)
print(m)'''

#8
'''n=str(input('Введите слово: '))
y=len(n)
#a=[]
b=str()
for i in range(y):  
    y=y-1 
   #print(n[y])
    #a.append(n[y])
    b=b+n[y]
#print(a)
print(b)'''
           
#9
'''rand_n=random.randint(0,100)
print (rand_n)
n=int(input('Введите число: '))
if n==rand_n:
    print ('Вы угадали число')
elif rand_n-10<=n<=rand_n+10:
    print('Горячо')
else:
    print('Холодно')'''

#10
'''n=str(input('Введите строку: '))
n1=n.lower()
n2=n1.replace(' ','')
#print(n2)
y=len(n2)
c=[]
for b in range(y):
    c.append(n2[b])
#print(c)
m=[]
for a in range(y):  
    y=y-1 
    m.append(n2[y])
#print(m)
for i in range(0,len(n2),1):
    for j in range(0,len(n2),1):
        if c[i]==m[j]:
            print('Это палиндром!')
        break
    break
'''



'''for s in range(0,len(n2),1):
    for d in range (len(n2),0,-1):
        if c[s]==c[d]:
            print('2')'''
   
