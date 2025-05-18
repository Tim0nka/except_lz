from proverka import Provero4ka

def main():
    file = "var2.csv"
    columns = ['Участники гражданского оборота', 'Тип операции', 'Сумма операции', 'Вид расчета', 'Место оплаты', 'Терминал оплаты', 'Дата оплаты', 'Время оплаты', 'Результат операции', 'Cash-back', 'Сумма cash-back']
    types = {"Тип операции": "object", "Сумма операции": "float64", "Дата оплаты": "object", "Время оплаты": "object"}

    checker = Provero4ka(file, columns, types)

    try:
        checker.process()
    except (FileNotFoundError, ValueError, TypeError, RuntimeError) as e:
        print(str(e))

if __name__ == "__main__":
    main()
