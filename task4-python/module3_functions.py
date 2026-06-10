# Автор: Багой Тимур Вадимович
# Дата: 09.06
# Описание: Модуль 3. Функции в Python.


def calculate_profit(revenue, costs):
    """Возвращает прибыль как разницу между выручкой и затратами."""
    return revenue - costs


def calculate_vat(price, vat_rate=20):
    """Возвращает сумму НДС для указанной цены и ставки."""
    return price * vat_rate / 100


def get_business_category(revenue):
    """Возвращает категорию бизнеса по размеру годовой выручки."""
    if revenue < 1_000_000:
        return "микробизнес"
    if revenue < 10_000_000:
        return "малый бизнес"
    if revenue < 100_000_000:
        return "средний бизнес"
    return "крупный бизнес"


def compound_interest(capital, rate, years):
    """Рассчитывает итоговую сумму по формуле сложного процента."""
    return capital * (1 + rate / 100) ** years


def apply_discount(price, discount_percent):
    """Возвращает цену товара после применения скидки."""
    return price * (1 - discount_percent / 100)


def main():
    """Демонстрирует работу пяти функций модуля."""
    print("1. Расчёт прибыли")
    for revenue, costs in [(150000, 90000), (210000, 160000), (95000, 120000)]:
        profit = calculate_profit(revenue, costs)
        print(f"Выручка {revenue}, затраты {costs}, прибыль {profit} руб.")

    print("\n2. Расчёт НДС")
    print(f"НДС по ставке 20%: {calculate_vat(1000):.2f} руб.")
    print(f"НДС по ставке 10%: {calculate_vat(1000, 10):.2f} руб.")

    print("\n3. Категории бизнеса")
    for revenue in [800000, 5_000_000, 50_000_000, 200_000_000]:
        print(f"Выручка {revenue}: {get_business_category(revenue)}")

    print("\n4. Сложный процент")
    for years in [3, 5, 10]:
        amount = compound_interest(100000, 8, years)
        print(f"Срок {years} лет: {amount:.2f} руб.")

    print("\n5. Применение скидки")
    prices = [1200, 2500, 990, 5600, 4300]
    for price in prices:
        new_price = apply_discount(price, 15)
        print(f"Было {price} руб., стало {new_price:.2f} руб.")


if __name__ == "__main__":
    main()
