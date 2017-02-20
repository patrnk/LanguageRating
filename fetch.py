from json import load
from json import dump
from os.path import exists
from argparse import ArgumentParser


def load_data_from_json_file(filepath):
    if not exists(filepath):
        return None
    with open(filepath, 'r') as f:
        return load(f)


def save_data_to_json_file(data, filepath):
    with open(filepath, 'w') as f:
        return dump(data, f)


def get_argument_parser():
    parser = ArgumentParser()
    parser.add_argument('number_of_vacancies', help='number of vacancies to retrieve')
    parser.add_argument('credentials_file', 
                        help='json file containing cliend_id and client_secret fields')
    return parser


if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    credentials = load_data_from_json_file(args.credentials_file)
    vacancies = get_vacancy_list(args.number_of_vacancies, credentials)
    save_data_to_json_file(vacancies)

