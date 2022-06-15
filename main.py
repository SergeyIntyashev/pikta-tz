from modules.nalogru_tools import NalogRuTools

if __name__ == '__main__':
    nalogru_tools = NalogRuTools()

    try:
        print('Пожалуйста, введите код ИФНС')
        ifns_code = input()

        print('Пожалуйста, введите код муниципального образования')
        oktmmf = input()

        nalogru_tools.definition_of_ifns_details(ifns_code, oktmmf)
    except Exception as e:
        print('Произошла ошибка при выполнении запроса:', e)
