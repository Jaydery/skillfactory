import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)
max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'1) Номер заказа с самой большой стоимостью : {max_order}, стоимость заказа: {max_price}')

max_quantity = 0
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity
print(f'2) Номер заказа с самым большим количеством товаров : {max_order}')

max_date = {}
for order_num, orders_data in orders.items():
    date = orders_data['date']
    max_date [date] = max_date.get(date, 0) + 1
for date in max_date:
    max_date_order = max(max_date.values())
    if max_date[date] == max_date_order:
        dates = date
print(f'3) В {dates} было сделано больше всего заказов.')

user_order = 0
users_id = {}
for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    users_id[user_id] = users_id.get(user_id, 0) + 1
    orders_id = users_id.get(user_id)
    if orders_id > user_order:
        max_order = orders_id
print(f'4) Пользователь {user_id} сделал самое большое количество заказов за июль.')

user_price = 0
users_id = {}
for order_num, orders_data in orders.items():
    price = orders_data['price']
    user_id = orders_data['user_id']
    users_id[user_id] = users_id.get(user_id, 0) + 1
    users_id[user_id] += price
    if price > user_price:
        user_price = price
        user_id_price = user_id
print(f'5) У {user_id_price} самая большая суммарная стоимость заказов {user_price} за июль.')

total_price = 0
total_quantity = 0
total_order = 0
for order_num, orders_data in orders.items():
    price = orders_data['price']
    quantity = orders_data['quantity']
    total_quantity += quantity
    total_price += price
    total_order +=1
average_price = total_price / total_quantity
average_order = total_price / total_order
print(f'6) Средняя стоимость товаров в июле была {average_order}')
print(f'7) Средняя стоимость товаров в июле была {average_price}')