#1
"""a=0
print(sum([a+i for i in range(1, 101)]))"""

#2
#inp=str(input('Enter word: '))
"""pr_word = [print(word) for word in str(input('Enter word: '))]"""

#3
"""a=int(input('Enter number: '))
tabl = [print(a*i) for i in range(1,11)]"""

#4
'''a=0
n=int(input("Enter number: "))
print(f'Сумма четных чисел от 1 до {n} равна', sum([a+i for i in range(1,n+1) if (i%2==0)]))'''

#5
'''a=0
n=int(input('Enter number: '))
print(f'Сумма чисел, кратных 3 от 1 до {n} равна', sum([a+i for i in range(1,n+1) if i%3==0]))'''

#6
'''n=int(input('Enter number: '))
number_s = [n  for i in range(2, n) if n%i!=0]
number_d = [n  for i in range(2, n) if n%i==0]
if n in number_d:
    print(f'{n} - difficuld number')
else:
    print(f'{n} - simple number')'''

#7
'''from math import prod
a=1
n=int(input('Введите число: '))
print(f"{n}! = ", prod([a*i for i in range(1,n+1)]))
'''

'''#8
n=str(input('Введите слово: '))
#print(n[::-1] )
b=[i for i in n[::-1]]
result=str('').join(b)
print(result)
'''
#9
'''import random
rand_n=random.randint(0,100)
n=int(input('Введите число: '))
new_r=[n for n in range(rand_n-10, rand_n+11)]
if n==rand_n: a=(f'You are right! It is {rand_n}')
elif (n!=rand_n)&(n in new_r): print(f'{n} Горячо! Задумано было число {rand_n}')
else: print(f'{n} Холодно! Задумано было число {rand_n}')'''

#10
'''n=str(input('Введите строку: '))
n1=n.lower()
n2=n1.replace(' ','')
y=len(n2)
if n2[::1]==n2[::-1]:
    print(f'{n[::-1]} - это палиндром!')
else: 
    print(f'{n} - не палиндром')'''
