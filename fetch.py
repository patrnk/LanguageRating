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


def fetch_page_of_programming_vacancies(page_number, secret_key):
    max_items_per_page = 100  # API won't allow more
    programming_catalogue = 48
    moscow_id = 4
    params = { 'page': page_number, 'count': max_items_per_page, 
               'show_new': time.time(), 'catalogues': 48, 
               'no_agreement': 1, 'town': moscow_id }
    response = make_get_request_to_superjob('vacancies', key, params)
    response.raise_for_status()
    return response.json()['objects']


def fetch_vacancies(number_of_vacancies, secret_key):
    vacancy_list = []
    vacancies_left = number_of_vacancies
    page_number = 0
    while vacancies_left > 0:
        new_vacancies = fetch_page_of_programming_vacancies(page_number, secret_key)
        vacancy_list += new_vacancies[:vacancies_left]
        vacancies_left -= len(new_vacancies)
        page_number += 1
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
    vacancies = fetch_vacancies(args.top, key)
    json.dump(vacancies, args.outfile)
