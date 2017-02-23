import json
import argparse
import sys


def is_language_detected_in_text(language_synonym_list, text):
    for synonym in language_synonym_list:
        if synonym in text:
            return True
    return False


def get_stats_for_each_language(vacancy_list, target_languages):
    stats = dict([(language, {'vacancy_count': 0, 'payment_sum': 0})
                  for language in target_languages]))
    for vacancy in vacancy_list:
        for language, synonyms in target_languages:
            detected_in_title = is_language_detected_in_text(synonyms, 
                                                             vacancy['profession']) 
            detected = detected_in_title or 
                       is_language_detected_in_text(synonyms, vacancy['candidat']) 
            if not detected:
                continue
            stats[language]['vacancy_count'] += 1
            stats[language]['payment_sum'] += vacancy['payment']
            if detected_in_title:
                break
    return stats


def print_stats_for_each_language(language_stats, outfile):
    for language, stats in language_stats:
        outfile.write('Name: %s\n' % language)        
        outfile.write('  Number of vacancies: %d\n' % stats['vacancy_count'])        
        average_payment = stats['payment_sum'] / stats['vacancy_count']
        outfile.write('  Average payment: %d\n' % average_payment)        



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
    print_stats_for_each_language(stats, args.outfile)
