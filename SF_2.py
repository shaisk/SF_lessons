def calculate_ticket_price(age):
    if age < 18:
        return 0
    elif 18 <= age < 25:
        return 990
    else:
        return 1390

def main():
    num_tickets = int(input("Введите количество билетов, которые вы хотите приобрести: "))
    total_cost = 0
    for _ in range(num_tickets):
        age = int(input("Введите возраст посетителя: "))
        ticket_price = calculate_ticket_price(age)
        total_cost += ticket_price

    if num_tickets > 3:
        total_cost *= 0.9  # Применяем 10% скидку, если билетов больше 3

    print("Сумма к оплате:", total_cost, "руб.")

main()
