import json
import os
import argparse
import requests


def make_get_request_to_superjob(method, secret_key, params):
    headers = { 'X-Api-App-Id': secret_key }
    kwargs = { 'headers': headers, 'params': params }
    return requests.request(method='GET', 
                            url='https://api.superjob.ru/2.0/%s/' % method, 
                            **kwargs)


def get_vacancy_list(number_of_vacancies, secret_key):
    #TODO: add additional keywords
    #TODO: download exactly number_of_vacancies
    params = { 'keyword': 'программист', 'count': 100 }
    response = make_get_request_to_superjob('vacancies', key, params)
    if not response.ok:
        return None
    return response.json()['objects']


def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--top', type=int, default=100,
                        help='number of vacancies to retrieve')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'),
                        default='output.json', help='output JSON file')
    return parser


if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    key = os.environ['SUPERJOB_SECRET_KEY']
    vacancies = get_vacancy_list(args.top, key)
    if vacancies is None:
        exit('Sorry, couldn\'t get the list')
    json.dump(vacancies, args.outfile)
