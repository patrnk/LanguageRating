from json import load
from json import dump
from os.path import exists


def load_data_from_json_file(filepath):
    if not exists(filepath):
        return None
    with open(filepath, 'r') as f:
        return load(f)


def save_data_to_json_file(data, filepath):
    with open(filepath, 'w') as f:
        return dump(data, f)


if __name__ == '__main__':
    args = get_argument_parser()
    credentials = load_data_from_json_file(args.credentials_file)
    vacancies = get_vacancy_list(args.number_of_vacancies, credentials)
    save_data_to_json_file(vacancies)

