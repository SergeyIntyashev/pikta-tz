import os
import json


class ParsingJsonTools:

    def __init__(self):
        self.__data_path = os.path.join(os.getcwd(), 'data')

    def get_data(self):
        result = []

        try:
            self.__fill_result_by_json(result, 'test1.json')
            self.__fill_result_by_json(result, 'test2.json')
            self.__fill_result_by_json(result, 'test3.json')
            return result
        except Exception as e:
            print('Произошла ошибки при парсинге файлов: ', e)

    def __fill_result_by_json(self, result, filename):

        file_path = os.path.join(self.__data_path, filename)

        if not os.path.exists(file_path):
            print('Файл с именем {} не найден в директории data'.format(filename))
            return

        with open(file_path) as f:
            json_data = json.load(f)

        json_data_keys = json_data.keys()
        if not ('headers' in json_data_keys and 'values' in json_data_keys):
            print('Файл с именем {} имеет неверную структуру. Наличие ключей headers и values обязательно'.format(
                filename))
            return

        current_data = []
        row_numbers = set()
        headers = set()
        for val in json_data['values']:
            row_numbers.add(val['properties']['Y'])

        for curr_number in row_numbers:
            current_row = {}
            for header in json_data['headers']:
                headers.add(header['properties']['QuickInfo'])
                current_x = header['properties']['X']
                for val in list(filter(
                        lambda item: item['properties']['X'] == current_x and item['properties']['Y'] == curr_number,
                        json_data['values'])):
                    current_row[header['properties']['QuickInfo']
                                ] = val['properties']['Text']
            current_data.append(current_row)

        result.append(
            {'filename': filename, 'headers': tuple(headers), 'parsed_data': current_data})
