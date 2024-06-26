per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Получение суммы от пользователя
money = int(input("Введите сумму, которую вы планируете положить под проценты: "))

# Вычисление суммы накопленных средств за год для каждого банка
deposit = [int(money * rate / 100) for rate in per_cent.values()]

# Вывод списка сумм накоплений для каждого банка
print("Суммы накоплений для каждого банка за год:", deposit)

# Нахождение максимальной суммы накоплений
max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать:", max_deposit)
