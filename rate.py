import json


def get_stats_for_each_language(vacancy_list, target_languages):
    pass


def print_stats_for_each_language(language_stats):
    pass


def get_target_languages():
    pass


def get_argument_parser():
    pass


if __name__ = '__main__':
    args = get_argument_parser().parse_args()
    vacancies = json.load(args.infile)
    languages = get_target_languages()
    stats = get_language_statistics(vacancies, languages)
    print_language_statistics(stats)
