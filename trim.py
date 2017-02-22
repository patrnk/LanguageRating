import json
import argparse


def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'),
                        help='the input JSON file with raw vacancies')
    parser.add_argument('outfile', type=argparse.FileType('w'),
                        help='the output JSON file')
    return parser


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


if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    raw_vacancies = json.load(args.infile)
    trimmed_vanacies = get_trimmed_vacancy_list(raw_vacancies)
    json.dump(trimmed_vanacies, args.outfile)
