import json
import os
import argparse
import requests


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
    print(vacancies.text)
    json.dump(vacancies, args.outfile)
    #save_data_to_json_file(vacancies, 'test.json')
