import json
import os
import time
import argparse
import requests
import sys


def make_get_request_to_superjob(method, secret_key, params):
    headers = { 'X-Api-App-Id': secret_key }
    kwargs = { 'headers': headers, 'params': params }
    url = 'https://api.superjob.ru/2.0/%s/' % method
    return requests.get(url, **kwargs)


def get_vacancy_list(number_of_vacancies, secret_key):
    max_items_per_page = 100  # API won't allow more
    programming_catalogue = 48
    moscow_id = 4
    params = { 'page': 0, 'count': max_items_per_page, 
               'show_new': time.time(), 'catalogues': 48, 
               'no_agreement': 1, 'town': moscow_id }
    response = make_get_request_to_superjob('vacancies', key, params)
    if not response.ok:
        return
    vacancy_list = []
    for vacancy_num in range(0, number_of_vacancies, params['count']):
        new_vacancies = response.json()['objects']
        vacancies_left = number_of_vacancies - vacancy_num
        vacancy_list += new_vacancies[:vacancies_left]
        params['page'] += 1
    return vacancy_list


def get_cli_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--top', type=int, default=100,
                        help='number of vacancies to retrieve')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'),
                        default=sys.stdout, help='output JSON file, stdout by default')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_cli_arguments()
    key = os.environ['SUPERJOB_SECRET_KEY']
    vacancies = get_vacancy_list(args.top, key)
    if vacancies is None:
        sys.exit('Sorry, couldn\'t get the list')
    json.dump(vacancies, args.outfile)
