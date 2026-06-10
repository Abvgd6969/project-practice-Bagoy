# Автор: Багой Тимур Вадимович
# Дата: 09.06
# Описание: Модуль 2. Условные конструкции и циклы.


def exercise_financial_result():
    """Определяет финансовый результат месяца по величине прибыли."""
    profit = float(input("Введите итоговую прибыль за месяц: "))

    if profit > 0:
        print("Прибыль")
    elif profit < 0:
        print("Убыток")
    else:
        print("Безубыточность")


def exercise_business_category():
    """Классифицирует бизнес по годовой выручке."""
    revenue = float(input("Введите годовую выручку предприятия: "))

    if revenue < 1_000_000:
        category = "Микробизнес"
    elif revenue < 10_000_000:
        category = "Малый бизнес"
    elif revenue < 100_000_000:
        category = "Средний бизнес"
    else:
        category = "Крупный бизнес"

    print(f"Категория: {category}")


def exercise_ndfl():
    """Рассчитывает НДФЛ и зарплату на руки."""
    salary = float(input("Введите ежемесячную зарплату: "))
    tax_rate = 0.13 if salary <= 50_000 else 0.15
    tax_amount = salary * tax_rate
    net_salary = salary - tax_amount

    print(f"НДФЛ: {tax_amount:.2f} руб.")
    print(f"Зарплата на руки: {net_salary:.2f} руб.")


def exercise_interest_table():
    """Выводит таблицу доходности на 12 месяцев для капитала 100 000 руб."""
    rate = float(input("Введите годовую процентную ставку: "))
    capital = 100_000

    for month in range(1, 13):
        interest = capital * rate / 100 / 12 * month
        print(f"Месяц {month}: начисленные проценты = {interest:.2f} руб.")


def exercise_price_range():
    """Сравнивает цены товаров со средней ценой."""
    prices = [1290, 850, 2100, 1750, 990]
    average_price = sum(prices) / len(prices)

    print(f"Средняя цена: {average_price:.2f} руб.")
    for price in prices:
        mark = "ВЫШЕ СРЕДНЕГО" if price > average_price else "не выше среднего"
        print(f"Цена {price} руб. — {mark}")


def main():
    """Запускает выбранное упражнение модуля 2."""
    actions = {
        "1": exercise_financial_result,
        "2": exercise_business_category,
        "3": exercise_ndfl,
        "4": exercise_interest_table,
        "5": exercise_price_range,
    }

    print("Модуль 2. Выберите упражнение от 1 до 5")
    choice = input("Номер упражнения: ")
    action = actions.get(choice)

    if action:
        action()
    else:
        print("Такого упражнения нет.")


if __name__ == "__main__":
    main()
