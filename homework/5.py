#1 Программа отслеживает общее количество клиентов. Напишите функцию, которая увеличивает глобальный счётчик клиентов.

'''clients = 0

def add_client():
    # Увеличьте значение глобальной переменной clients на 1
    pass
    global clients
    clients +=1
    return clients

add_client()
add_client()
print(clients)  # Ожидаемый результат: 2'''

#2
#Есть глобальная переменная с базовой ценой товара. Напишите функцию, которая временно изменяет цену локально.

'''base_price = 100

def apply_discount(discount):
    # Локально измените базовую цену, применив скидку
    new_price = base_price - base_price*discount/100  # Локально посчитайте цену со скидкой
    print(f"Цена со скидкой: {new_price}")

apply_discount(20)  # Цена со скидкой: 80
print(base_price)   # Ожидаемый результат: 100'''

#3 
# Напишите функцию, которая добавляет к каждому товару налог 20%, и примените её с помощью map.

"""prices = [100, 200, 300, 400]

def apply_tax(price):
    final_p=price+price*0.2
    return final_p

final_prices = map(apply_tax, prices)  # Используйте map для применения функции apply_tax
print(list(final_prices))  # Ожидаемый результат: [120.0, 240.0, 360.0, 480.0]"""

#4. Фильтр товаров по цене
#Есть список цен. Используйте filter, чтобы оставить только товары дороже 150.
"""
prices = [50, 120, 180, 300, 75]

def filter_price(price):
    if price>150:
        my_price=price
        return my_price

# Используйте filter, чтобы отобрать только товары дороже 150
expensive_items = filter(filter_price, prices)
print(list(expensive_items))  # Ожидаемый результат: [180, 300]"""

#5. Применение скидки к категории товаров
#У вас есть список цен и категория, к которой нужно применить скидку. Напишите функцию, которая с помощью map применяет скидку 10% к заданным категориям.
"""
products = [
    {"name": "Laptop", "price": 1000, "category": "electronics"},
    {"name": "Shirt", "price": 50, "category": "clothing"},
    {"name": "Phone", "price": 600, "category": "electronics"},
]

def apply_discount(product):
    # Если категория electronics, примените скидку 10%
   # for product in products:     
        if product['category']=='electronics':
            product['price']=product['price']-product['price']*0.1             
        #print(product)
        return product   
  
discounted_products =map(apply_discount, products)  # Используйте map
print(list(discounted_products))
# Ожидаемый результат:
# [{"name": "Laptop", "price": 900.0, "category": "electronics"},
#  {"name": "Shirt", "price": 50, "category": "clothing"},
#  {"name": "Phone", "price": 540.0, "category": "electronics"}]
"""

#6. Удаление товаров с низким рейтингом через filter
#Фильтруйте товары с рейтингом меньше 4.
"""
products = [
    {"name": "Laptop", "rating": 4.5},
    {"name": "Shirt", "rating": 3.8},
    {"name": "Phone", "rating": 4.2},
]

def filter_rating(product):
    #for product in products:
    if product['rating']==3.8:
        return False
    else:
        return True
    #return products


# Используйте filter для удаления товаров с рейтингом < 4
high_rating_products = filter(filter_rating, products)
print(list(high_rating_products))
# Ожидаемый результат: [{"name": "Laptop", "rating": 4.5}, {"name": "Phone", "rating": 4.2}]
"""

#7. Перевод в рубли через map
#Есть список цен в долларах. Напишите функцию, которая переводит их в рубли (курс 1 USD = 75 RUB), и примените через map.
"""
prices_usd = [10, 20, 30, 40]

def to_rub(price):
    # Переведите цену в рубли
    return price*75
prices_rub = map(to_rub, prices_usd)  # Используйте map для преобразования
print(list(prices_rub))  # Ожидаемый результат: [750, 1500, 2250, 3000
"""

#8. Отбор участников старше 18 лет
#У вас есть список участников с возрастом. Используйте filter, чтобы оставить только тех, кто старше 18 лет.
'''
participants = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 16},
    {"name": "Diana", "age": 22},
]

def filter_age(a):
    if a['age']>18:
        return True
    else:
        return False
# Используйте filter для отбора участников старше 18 лет
adults = filter(filter_age,participants)
print(list(adults))
# Ожидаемый результат: [{"name": "Bob", "age": 20}, {"name": "Diana", "age": 22}]
'''
#9. Генерация строк описания товаров через map
#Создайте список строк описания для каждого товара вида: "Товар: , Цена: ".
"""
import itertools

products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Shirt", "price": 50},
    {"name": "Phone", "price": 600},
]

new_list=[]

def format_product(product):
    # Верните строку вида: "Товар: <name>, Цена: <price>"
    if product in products:             
        new_list=(f"Товар: {product['name']}, Цена : {product['price']}")  
    return new_list
    
descriptions = map(format_product, products)  # Используйте map
print(list(descriptions))
# Ожидаемый результат: ["Товар: Laptop, Цена: 1000", "Товар: Shirt, Цена: 50", "Товар: Phone, Цена: 600"]
"""

#10. Фильтр по ключевому слову в названии
#Дан список товаров. Оставьте только те, у которых в названии есть ключевое слово "Phone".
'''
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone Case", "price": 30},
    {"name": "Phone", "price": 600},
]
filter_worf='Phone'

def filter_Phone(product):
    if product in products:
        if filter_worf in product['name']:
            return product

# Используйте filter, чтобы оставить только товары с "Phone" в названии
phones = filter(filter_Phone, products)
print(list(phones))
'''

#11. Сумма произвольного количества чисел (*args)
#Напишите функцию, которая принимает произвольное количество чисел и возвращает их сумму.
'''
def sum_numbers(*args):
    # Верните сумму всех переданных чисел
    return sum(args)

result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Ожидаемый результат: 15
'''

#12. Наибольшее число из *args
#Напишите функцию, которая принимает произвольное количество чисел и возвращает наибольшее из них.
'''
def max_number(*args):
    # Верните наибольшее число
    return max(args)

result = max_number(10, 25, 50, 5, 30)
print(result)  # Ожидаемый результат: 50
'''

#13. Приветствие произвольного количества людей (*args)
#Напишите функцию, которая принимает список имен и приветствует каждого из них.

'''m=[]
def greet_people(*args):
    # Для каждого имени выведите "Привет, <имя>!"
    for i in args:
        m.append(f'Привет, {i}!')
    return m
        
print('\n'.join(greet_people("Alice", "Bob", "Charlie")))
# Ожидаемый результат:
# Привет, Alice!
# Привет, Bob!
# Привет, Charlie!'''

#14. Создание словаря из ключей и значений (**kwargs)
#Напишите функцию, которая принимает произвольное количество именованных аргументов и возвращает их в виде словаря.
'''
def create_dict(**kwargs):
    # Верните kwargs как словарь    
    return(kwargs)   
                
        
result = create_dict(name="Alice", age=25, city="New York")
print(result)  # Ожидаемый результат: {'name': 'Alice', 'age': 25, 'city': 'New York'}
'''

#15. Форматирование текста с помощью **kwargs
#Напишите функцию, которая принимает текстовый шаблон и подставляет значения из **kwargs.
'''
def format_text(template, **kwargs):
    # Используйте .format() для подстановки значений из kwargs
    tr=template.format(**kwargs)
    return tr

result = format_text("Привет, {name}! Ты живешь в {city}.", name="Alice", city="New York")
print(result)  # Ожидаемый результат: "Привет, Alice! Ты живешь в New York."
'''

#16. Объединение списков через *args
#Напишите функцию, которая принимает произвольное количество списков и возвращает их объединение в один список.
'''
def merge_lists(*args):
    # Объедините все переданные списки
    rez=sum(args, [])
    return rez

result = merge_lists([1, 2], [3, 4], [5, 6])
print(result)  # Ожидаемый результат: [1, 2, 3, 4, 5, 6]
'''

#17. Фильтрация параметров через **kwargs
#Напишите функцию, которая принимает параметры через **kwargs и возвращает только те, где значение больше 10.
'''new_dict = {}

def filter_kwargs(**kwargs):
    # Верните словарь с ключами, где значение больше 10
    for k, v in kwargs.items():
        if v>10: 
            new_dict[k]=v
    return new_dict 
                     
        
result = filter_kwargs(a=5, b=15, c=25, d=8)
print(result)  # Ожидаемый результат: {'b': 15, 'c': 25}
'''

#18. Комбинация *args и **kwargs
#Напишите функцию, которая принимает список имен через *args и сообщения через **kwargs, чтобы отправить каждому сообщение.
'''
def send_messages(*args, **kwargs):
    # Для каждого имени выведите сообщение вида:
    # "Привет, <имя>! <сообщение>"
    # Используйте значение kwargs['message']
    for a in args:
        m=str(f'Привет {a}, {kwargs['message']}')
        print (m)
        
send_messages("Alice", "Bob", message="У вас новое уведомление!")
# Ожидаемый результат:
# Привет, Alice! У вас новое уведомление!
# Привет, Bob! У вас новое уведомление!
#print(send_messages)
'''
import math
#19. Сложение чисел и ключевых параметров
#Напишите функцию, которая принимает числовые аргументы через *args и добавляет к их сумме значения из **kwargs, если они являются числами.
'''
def sum_args_kwargs(*args, **kwargs):
    # Сложите числа из args и числовые значения из kwargs
    for a in args:
       a +=a
    #return a
    for k in kwargs:
        m=kwargs[k]
        #print(m)
        if isinstance(m, int):
            #print(m)
            a+=m
    return a
  

result = sum_args_kwargs(1, 2, 3, x=4, y=5, z="не число")
print(result)  # Ожидаемый результат: 15
'''

#20. Проверка ключевых аргументов (**kwargs)
#Напишите функцию, которая проверяет наличие ключа required в **kwargs и возвращает его значение. Если ключа нет, возвращает "Ключ не найден".
'''w="required"
def check_required(**kwargs):
    # Проверьте наличие ключа required
    for k in kwargs:
        if k==w:
            return "Это важно"
        else:
            return "Ключ не найден"
result1 = check_required(required="Это важно", optional="Это не важно")
result2 = check_required(optional="Это не важно")
print(result1)  # Ожидаемый результат: "Это важно"
print(result2)  # Ожидаемый результат: "Ключ не найден"'''
