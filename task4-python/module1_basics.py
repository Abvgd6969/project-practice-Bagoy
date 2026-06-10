# Автор: Багой Тимур Вадимович
# Дата: 09.06
# Описание: Модуль 1. Переменные, типы данных, ввод и вывод.


def exercise_employee_card():
    """Выводит карточку сотрудника с переменными разных типов данных."""
    employee_name = "Иван Петров"
    employee_age = 28
    employee_salary = 75000.50
    is_employed = True

    print("Карточка сотрудника")
    print(f"Имя: {employee_name}")
    print(f"Возраст: {employee_age}")
    print(f"Заработная плата: {employee_salary} руб.")
    print(f"Работает сейчас: {is_employed}")


def exercise_greeting():
    """Запрашивает имя и город, затем выводит приветствие сотрудника."""
    employee_name = input("Введите имя сотрудника: ")
    city_name = input("Введите город офиса: ")
    print(f"Сотрудник {employee_name} работает в офисе {city_name}")


def exercise_total_cost():
    """Рассчитывает итоговую стоимость товара по цене и количеству."""
    item_price = float(input("Введите цену единицы товара: "))
    item_quantity = int(input("Введите количество единиц товара: "))
    total_cost = item_price * item_quantity
    print(f"Итоговая стоимость: {total_cost:.2f} руб.")


def exercise_deposit_income():
    """Рассчитывает доход по банковскому вкладу за один год."""
    deposit_amount = float(input("Введите сумму вклада: "))
    interest_rate = float(input("Введите процентную ставку годовых: "))
    income = deposit_amount * interest_rate / 100
    final_amount = deposit_amount + income
    print(f"Доход за год: {income:.2f} руб.")
    print(f"Итоговая сумма: {final_amount:.2f} руб.")


def exercise_profit_margin():
    """Рассчитывает прибыль и рентабельность продаж."""
    revenue = float(input("Введите выручку: "))
    costs = float(input("Введите общие затраты: "))
    profit = revenue - costs

    if revenue == 0:
        print("Рентабельность нельзя рассчитать, потому что выручка равна нулю.")
    else:
        margin = profit / revenue * 100
        print(f"Прибыль: {profit:.2f} руб.")
        print(f"Рентабельность продаж: {margin:.2f}%")


def main():
    """Запускает выбранное упражнение модуля 1."""
    actions = {
        "1": exercise_employee_card,
        "2": exercise_greeting,
        "3": exercise_total_cost,
        "4": exercise_deposit_income,
        "5": exercise_profit_margin,
    }

    print("Модуль 1. Выберите упражнение от 1 до 5")
    choice = input("Номер упражнения: ")
    action = actions.get(choice)

    if action:
        action()
    else:
        print("Такого упражнения нет.")


if __name__ == "__main__":
    main()
