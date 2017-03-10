import json
import argparse
import sys


def trim(raw_vacancy):
    payment = raw_vacancy['payment'] or raw_vacancy['payment_from']
    payment = payment or raw_vacancy['payment_to']
    trimmed_vacancy = { 'profession': raw_vacancy['profession'],
                        'candidat': raw_vacancy['candidat'],
                        'payment': payment }
    return trimmed_vacancy


def get_trimmed_vacancy_list(raw_vacancy_list):
    trimmed_vacancy_list = []
    for raw_vacancy in raw_vacancy_list:
        trimmed_vacancy_list.append(trim(raw_vacancy))
    return trimmed_vacancy_list


def get_cli_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', type=argparse.FileType('r'),
                        default=sys.stdin,
                        help='JSON file with vacancies from SuperJob, stdin by default')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='JSON file for trimmed vacancies, stdout by default')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_cli_arguments()
    raw_vacancies = json.load(args.infile)
    trimmed_vanacies = get_trimmed_vacancy_list(raw_vacancies)
    json.dump(trimmed_vanacies, args.outfile)
