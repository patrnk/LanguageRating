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
    ''' Returns dictionary with target languages.

    An item in the dictionary  has the following structure:
    'name_to_display': ['name_to_search1', 'name_to_search2', ...]
    '''
    # this is top-10 languages as ranked by IEEE in 2016
    # https://tinyurl.com/j7btjs2
    target_languages = { 'C': [' C ', ' C,', 'Си'],
                         'Java': ['Java'],
                         'Python': ['Python'],
                         'C/C++': ['C++'],
                         'R': [' R ', ' R,'],
                         'C#': ['C#'],
                         'PHP': ['PHP'],
                         'JavaScript': ['JavaScript', ' JS ', ' JS,'],
                         'Ruby': ['Ruby'],
                         'Go': ['Go'] }
    return target_languages


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
