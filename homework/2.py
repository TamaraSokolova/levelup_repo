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