import json
import argparse
import sys


def get_stats_for_each_language(vacancy_list, target_languages):
    pass


def print_stats_for_each_language(language_stats):
    pass


def load_vacancy_list(inputfile):
    return json.load(inputfile)


def get_target_languages():
    pass


def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', type=argparse.FileType('r'),
                        default='trimmed_vacancies.json',
                        help='input JSON file')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('r'),
                        default=sys.stdout,
                        help='output file, stdout by default')
    return parser


if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    vacancies = load_vacancy_list(args.infile)
    languages = get_target_languages()
    stats = get_stats_for_each_language(vacancies, languages)
    print_stats_for_each_language(stats)
