import sqlite3
import os


class SQLTools:

    __init_script_path = os.path.join(os.getcwd(), 'scripts/init_db.sql')

    def __init__(self):
        self.__conn = None
        self.__customer_purchases_columns = {
            0: 'Имя клиента', 1: 'Сумма покупок'}
        self.__customer_bought_phone_сolumns = {0: 'Имя клиента'}
        self.__products_orders_columns = {
            0: 'Наименование товара', 1: 'Количество заказа'}

    def init_db(self):
        try:
            if not self.__conn:
                self.__conn = sqlite3.connect('pikta_tz.db')

                print('Подключение к базе данных произошло успешно')

                with open(self.__init_script_path, 'r') as f:
                    sql_script = f.read()

                self.__conn.executescript(sql_script)
                print("База данных успешно инициализирована")
                return

            print('Подключение к базе данных активно')

        except sqlite3.Error as error:
            print(
                'Произошла ошибка при подключении или инициализации базы данных по причине:{}'.format(error))

    def customer_purchases(self):
        if self.__check_init_db():
            return

        query = '''
                SELECT  
                    c.client_name,
                    SUM(p.price) as sum_price
                FROM
                    orders o
                LEFT JOIN clients c on o.client_id = c.client_id, 
                        products p on o.product_id = p.product_id 
                GROUP BY 
                    c.client_name 
                ORDER BY
                    c.client_name
                '''
        print('Список клиентов с общей суммой их покупок:')
        self.__execute_query(query, self.__customer_purchases_columns)

    def customer_bought_phone(self):
        if self.__check_init_db():
            return

        query = '''
                SELECT  
                    c.client_name
                FROM
                    orders o
                LEFT JOIN clients c on o.client_id = c.client_id, 
                        products p on o.product_id = p.product_id 
                WHERE p.product_name = 'Телефон'
                GROUP BY 
                    c.client_name 
                ORDER BY
                    c.client_name
                '''
        print('Список клиентов, которые купили телефон:')
        self.__execute_query(query, self.__customer_bought_phone_сolumns)

    def products_orders(self):
        if self.__check_init_db():
            return

        query = '''
                SELECT  
                    p.product_name,
                    count(*) as cnt
                FROM
                    products p
                INNER JOIN orders o on p.product_id = o.product_id 
                GROUP BY 
                    p.product_name
                ORDER BY
                    cnt DESC
                '''
        print('Список товаров с количество их заказа:')
        self.__execute_query(query, self.__products_orders_columns)

    def __execute_query(self, query, columns):
        try:
            with self.__conn:
                result = self.__conn.execute(query)
                for row in result:
                    for k, v in columns.items():
                        print('{:12}: {}'.format(v, row[k]))
                    print('-' * 40)
        except sqlite3.IntegrityError as e:
            print('Произошла ошибка при выполнении: ', e)

    def __check_init_db(self):
        if not self.__conn:
            print('Перед выполнением действия необходимо инициализировать базу данных, запустив команду 1 - Создание базы данных')
            return True

    def close_conn(self):
        if self.__conn:
            self.__conn.close()
