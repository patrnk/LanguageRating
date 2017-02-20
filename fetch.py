import json
import os
import argparse
import requests


#TODO: add count and page params
def make_get_request_to_superjob(method, secret_key):
    headers = { 'X-Api-App-Id': secret_key }
    params = { 'keyword': 'программист' }   #FIXME: move to get_vacancy_list
    kwargs = { 'headers': headers, 'params': params }
    return requests.request(method='GET', 
                            url='https://api.superjob.ru/2.0/%s/' % method, 
                            **kwargs)


def get_vacancy_list(number_of_vacancies, secret_key):
    response = make_get_request_to_superjob('vacancies', key)
    if not response.ok:
        return None
    return response.json()['objects']


def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('number_of_vacancies', help='number of vacancies to retrieve')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'),
                        default='output.json', help='output JSON file')
    return parser


if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    key = os.environ['SUPERJOB_SECRET_KEY']
    vacancies = get_vacancy_list(args.number_of_vacancies, key)
    if vacancies is None:
        exit('Sorry, couldn\'t get the list')
    json.dump(vacancies, args.outfile)
