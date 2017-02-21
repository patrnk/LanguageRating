import json


def get_argument_parser():
    pass


def get_trimmed_vacancies(raw_vacancies):
    pass


if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    raw_vacancies = json.load(args.infile)
    trimmed_vanacies = get_trimmed_vacancies(raw_vacancies)
    json.dump(trimmed_vanacies, args.outfile)
