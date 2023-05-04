import requests
import bs4
import numpy as np

a = input("Введите нужное количество билетов - ")
s = input("Введите возраст участников - ")
total_sum = 0
number_of_tickets = int(a)
age_list = list(map(int, s.split()))
if number_of_tickets == len(age_list):
    for i, value in enumerate(age_list):
        if value >= 18 and value <= 24:
            total_sum += 990
        elif value > 24:
            total_sum += 1390
        elif value < 18:
            print("Лица, моложе 18 лет, проходят бесплатно")
else:
    print("Подождите, Товарищ! Вы заявили другое количество билетов!")
if number_of_tickets > 3:
    total_sum -= (total_sum/100*10)
    print("Общая сумма к оплате с учетом скидки составляет - ", total_sum)
elif number_of_tickets == len(age_list):
    print("Общая сумма к оплате составляет - ", total_sum)
else:
    print("Заявите нужное количество билетов!")






