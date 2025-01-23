import random
from random import choice

#1
"""n = 45
new_list = []
#for i in range(n):
while n>=0:
    new_list.append(n)
    n=n-1
print (new_list)"""

#2
"""dinosaurs = ["Ти-рекс", "Трицератопс", "Велоцираптор", "Брахиозавр"]
new_world = 'пушистый'
new_list=[]
for dino in dinosaurs:
   # print(dino)
    dino=dino+' '+new_world
    #print(dino)
    new_list.append(dino)
print(new_list)"""

#3
"""ingredients = ["сыр", "яйца", "помидоры", "курица", "рыба", "грибы", "лук"]
resept=random.sample(ingredients , k =3)
print(resept)"""

'''ingredients = ["сыр", "яйца", "помидоры", "курица", "рыба", "грибы", "лук"]
new_resept =[]
for i in range(3):
    resept=random.choice(ingredients)
    if resept not in new_resept:
       new_resept.append(resept) 
    i=i+1
print(new_resept)'''

#4
'''names = [("Иванов", "Иван"), ("Петров", "Петр"), ("Сидоров", "Сидор")]
new_names = []
new_name = ()
for name in names:
    new_name = (name[1], name[0])
   # print(name[1], name[0])
    new_names.append(new_name)
print(new_names)
'''

#5
'''letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
new_pass=random.sample(letters , k =8)
#print(new_pass)
new_passord=''.join(new_pass)
print(new_passord)'''

#6
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_1 = []
numbers_2 = []
for num in numbers:
    if num % 2 == 0:
       # print(num)
        numbers_1.append(num)
    else:
        numbers_2.append(num)
print(numbers_1)
print(numbers_2)'''

#7
"""text = "Гарри Поттер и Тайная комната - Глава 2"
one_part = text.split(' - Глава')
book_title = one_part[0]
chapter_number = one_part[1]
print(f"Книга: {book_title}, Глава: {chapter_number}")"""

#8
'''greetings = ["С днём рождения!", "С Новым годом!", "Желаю успехов!", "Скучный текст"]
new_ = []
word_ = 'скучный'
for i in greetings:    
    if word_ not in i.lower():
        new_.append(i)
p = random.sample(new_ , k =1)
print(p)'''
     

#9
"""text = "Эта программа такая тупая! Вот блин!"
bad_words = ["тупая", "блин"]
for i in bad_words:
    text=text.replace(i, "*")
print(text)"""


#10
"""words = ["яблоко", "банан", "яблоко", "груша", "банан", "слива"]
new_words=[]
for i in words:
    if i not in new_words:
        new_words.append(i)
print(new_words)"""

#11
"""words = ["начало", "путь", "стоп", "дальше", "конец"]
stop_word = "стоп"
a=0
for i in words:
    if i!=stop_word:
        a=a+1
       # print(a)
    else:
        print(f'Было {a} слова до слова стоп')
        break"""