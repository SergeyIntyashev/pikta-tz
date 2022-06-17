from modules.nalogru_tools import NalogRuTools
from modules.sql_tools import SQLTools
from modules.parsing_json_tools import ParsingJsonTools
from modules.excel_tools import ExcelTools


def execute_task1():
    parsing_json_tools = ParsingJsonTools()
    parsed_data = parsing_json_tools.get_data()

    ExcelTools.save_parsed_data(parsed_data, 'parsed_test.xlsx')


def execute_task2():
    nalogru_tools = NalogRuTools()

    print('Введите код ИФНС')
    ifns_code = input()

    print('Введите код муниципального образования')
    oktmmf = input()

    nalogru_tools.definition_of_ifns_details(ifns_code, oktmmf)


def execute_task3():
    sql_tools = SQLTools()
    while True:
        print('''Введите номер метода для получения результатов:
                    1 - Создание базы данных
                    2 - Список клиентов с общей суммой их покупок
                    3 - Список клиентов, которые купили телефон
                    4 - Список товаров, с количеством их заказа
                    exit - для выхода
                ''')
        match input():
            case '1':
                sql_tools.init_db()
            case '2':
                sql_tools.customer_purchases()
            case '3':
                sql_tools.customer_bought_phone()
            case '4':
                sql_tools.products_orders()
            case 'exit':
                sql_tools.close_conn()
                break
            case _:
                print('Такой команды не существует')


if __name__ == '__main__':

    while True:
        print('''Введите номер задания для выполнения:
                    1 - Парсинг JSON
                    2 - HTTP-запросы
                    3 - SQL
                    exit - для выхода
                ''')

        command = input()

        match command:
            case '1':
                execute_task1()
            case '2':
                execute_task2()
            case '3':
                execute_task3()
            case 'exit':
                break
            case _:
                print('Такой команды не существует')
