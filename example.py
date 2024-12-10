# run.py
from product import Product
from order import Order
from customer import Customer
from discount import Discount

# Создаём продукты
laptop = Product("Laptop", 1000)
phone = Product("Smartphone", 500)
tablet = Product("Tablet", 300)

# Создаём клиентов
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Создаём заказы и добавляем к клиентам
order1 = Order([laptop, phone])
customer1.add_order(order1)

order2 = Order([tablet])
customer2.add_order(order2)

order3 = Order([phone, tablet])
customer1.add_order(order3)

# Применяем скидку
summer_discount = Discount("Summer sale", 10)
discounted_price = summer_discount.apply_discount(laptop.price, summer_discount.discount_percent)

print(f"Скидочная цена на {laptop.name}: {discounted_price}")

# Общая информация
print(f"Всего заказов: {Order.total_orders()}")
print(f"Общая выручка: {Order.total_revenue()}")

# Вывод информации
print(customer1)
print(customer2)
print(order1)
print(order2)
print(order3)
print(laptop == phone)
print(tablet < phone)