import requests
import json


class NalogRuTools:
    __HOST = "https://service.nalog.ru/addrno-proc.json"

    def definition_of_ifns_details(self, ifns, oktmmf=None):
        if oktmmf:
            self.__get_ifns_details(ifns, oktmmf)
        else:
            response = requests.post(
                self.__HOST, {'c': 'getOktmmf', 'ifns': ifns, 'okatom': ''})
            response_body = response.json()
            if self.__check_response_body_for_error(response_body):
                return
            print('Выберите код муниципального образования, если это необходимо, из предложенных ниже \n',
                  json.dumps(response_body['oktmmfList'], indent=4, ensure_ascii=False))
            self.__get_ifns_details(ifns, input())

    def __get_ifns_details(self, ifns, oktmmf):
        data = {'c': 'next',
                'step': '1',
                'npKind': 'fl',
                'objectAddr': '',
                'objectAddr_zip': '',
                'objectAddr_ifns': '',
                'objectAddr_okatom': '',
                'ifns': ifns,
                'oktmmf': oktmmf}

        response = requests.post(self.__HOST, data)
        response_body = response.json()
        if self.__check_response_body_for_error(response_body):
            return
        print('Результат вашего запроса \n', json.dumps(
            response_body, indent=4, ensure_ascii=False))

    def __check_response_body_for_error(self, response_body):
        result = None

        if 'ERRORS' in response_body.keys():
            print('Произошла ошибки при получении данных: ',
                  response_body['ERRORS'])
            result = True
        elif 'ERROR' in response_body.keys():
            print('Произошла ошибки при получении данных: ',
                  response_body['ERROR'])
            result = True

        return result
