import openpyxl
import os


class ExcelTools:

    @staticmethod
    def save_parsed_data(data, filename):
        DIR_TO_SAVE = os.path.join(os.getcwd(), 'data')

        wb = openpyxl.Workbook()

        for curr_data in data:
            wb.create_sheet(title=curr_data['filename'])
            sheet = wb[curr_data['filename']]

            sheet.append(curr_data['headers'])

            for parsed_data in curr_data['parsed_data']:
                sheet.append(tuple(parsed_data.values()))

        full_path = os.path.join(DIR_TO_SAVE, filename)
        wb.remove(wb['Sheet'])
        wb.save(full_path)
        print('Файл сохранен по пути {}'.format(full_path))
