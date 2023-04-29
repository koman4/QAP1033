import requests
import bs4
import numpy as np

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = 100000

A = per_cent.get('ТКБ')
bank1 = money + (money/100*A)
B = per_cent.get('СКБ')
bank2 = money + (money/100*B)
C = per_cent.get('ВТБ')
bank3 = money + (money/100*C)
D = per_cent.get('СБЕР')
bank4 = money + (money/100*D)
deposit = [bank1, bank2, bank3, bank4]
max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать — " + str(int(max_deposit)) + ". " )
