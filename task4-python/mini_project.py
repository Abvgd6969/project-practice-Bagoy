# Автор: Багой Тимур Вадимович
# Дата: 09.06
# Описание: Мини-проект. Вариант 6 — анализ динамики продаж за полугодие.


def get_sales_data():
    """Запрашивает выручку за шесть месяцев и возвращает список данных."""
    sales_data = []

    for month_number in range(1, 7):
        month_name = input(f"Введите название {month_number}-го месяца: ")
        revenue = float(input(f"Введите выручку за месяц {month_name}: "))
        sales_data.append({"month": month_name, "revenue": revenue})

    return sales_data


def analyze_sales(sales_data):
    """Возвращает основные показатели продаж за полугодие."""
    revenues = [item["revenue"] for item in sales_data]
    total_revenue = sum(revenues)
    average_revenue = total_revenue / len(revenues)
    best_month = max(sales_data, key=lambda item: item["revenue"])
    worst_month = min(sales_data, key=lambda item: item["revenue"])

    return total_revenue, average_revenue, best_month, worst_month


def print_dynamics(sales_data):
    """Печатает динамику выручки каждого месяца относительно предыдущего."""
    print("\nДинамика по месяцам:")

    for index, item in enumerate(sales_data):
        if index == 0:
            print(f"{item['month']}: базовый месяц, выручка {item['revenue']:.2f} руб.")
            continue

        previous_revenue = sales_data[index - 1]["revenue"]
        current_revenue = item["revenue"]

        if current_revenue > previous_revenue:
            status = "рост"
        elif current_revenue < previous_revenue:
            status = "снижение"
        else:
            status = "без изменений"

        difference = current_revenue - previous_revenue
        print(f"{item['month']}: {status}, изменение {difference:.2f} руб.")


def print_report(sales_data):
    """Формирует итоговый отчёт по продажам за полугодие."""
    total_revenue, average_revenue, best_month, worst_month = analyze_sales(sales_data)

    print("\nОтчёт по продажам за полугодие")
    print(f"Общая выручка: {total_revenue:.2f} руб.")
    print(f"Среднемесячная выручка: {average_revenue:.2f} руб.")
    print(f"Лучший месяц: {best_month['month']} — {best_month['revenue']:.2f} руб.")
    print(f"Худший месяц: {worst_month['month']} — {worst_month['revenue']:.2f} руб.")
    print_dynamics(sales_data)


def main():
    """Запускает мини-проект анализа динамики продаж."""
    print("Мини-проект: анализ динамики продаж за полугодие")
    sales_data = get_sales_data()
    print_report(sales_data)


if __name__ == "__main__":
    main()
