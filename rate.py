import json
import argparse
import sys
import matplotlib.pyplot as plt


def is_language_detected_in_text(language_synonym_list, text):
    for synonym in language_synonym_list:
        if synonym.lower() in text.lower():
            return True
    return False


def get_stats_for_each_language(vacancy_list, target_languages):
    stats = dict([(language, {'vacancy_count': 0, 'payment_sum': 0})
                  for language in target_languages])
    for vacancy in vacancy_list:
        for language, synonyms in target_languages.items():
            detected_in_title = is_language_detected_in_text(synonyms, 
                                                             vacancy['profession']) 
            detected = detected_in_title or \
                       is_language_detected_in_text(synonyms, vacancy['candidat']) 
            if not detected:
                continue
            stats[language]['vacancy_count'] += 1
            stats[language]['payment_sum'] += vacancy['payment']
            if detected_in_title:
                break

    for _, counters in stats.items():
        counters['average_payment'] = counters['payment_sum'] / counters['vacancy_count']\
                                   if counters['vacancy_count'] else 0
    return stats


def print_stats_for_each_language(language_stats, outfile):
    for language, stats in sorted(language_stats.items()):
        outfile.write('Name: %s\n' % language)        
        outfile.write('  Number of vacancies: %d\n' % stats['vacancy_count'])        
        outfile.write('  Average payment: %d\n' % stats['average_payment'])        


def load_vacancy_list(inputfile):
    return json.load(inputfile)


def get_target_languages():
    ''' Returns dictionary with target languages.

    An item in the dictionary  has the following structure:
    'name_to_display': ['name_to_search1', 'name_to_search2', ...]
    '''
    # programming languages mentioned in SuperJob research
    # https://tinyurl.com/hbnxv4t
    target_languages = { 'Java': ['Java'],
                         'Python': ['Python'],
                         'C/C++': ['C++'],
                         'Objective-C': ['Objective-C', 'Obj-C'],
                         'C#': ['C#'],
                         'PHP': ['PHP'],
                         'JavaScript': ['JavaScript', ' JS ', ' JS,'],
                         'Ruby': ['Ruby'],
                         'Delphi': ['Delphi'],
                         'Perl': ['Perl'], }
    return target_languages


def show_stats_histogram(stats):
    bar_coordinates = range(len(sorted(stats)))
    language_names = [name for name in sorted(stats)]
    average_payments = [stats[name]['average_payment'] for name in language_names]
    plt.figure(figsize=(12, 7))
    plt.bar(bar_coordinates, average_payments, tick_label=language_names, align='center')

    plt.figure(1).canvas.set_window_title('language salaries')
    plt.ylabel('Average salary')
    plt.xlabel('Language name')
    plt.title('Comparison of average salaries among different programming languages')
    plt.show()
    

def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', type=argparse.FileType('r'),
                        default=sys.stdin,
                        help='input JSON file, stdin by default')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('r'),
                        default=sys.stdout,
                        help='output file, stdout by default')
    parser.add_argument('-g', '--graph', action='store_true',
                        help='in addition to text output, provide '\
                             'graphical representation of the data')
    return parser


if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    vacancies = load_vacancy_list(args.infile)
    languages = get_target_languages()
    stats = get_stats_for_each_language(vacancies, languages)
    print_stats_for_each_language(stats, args.outfile)
    if args.graph:
        show_stats_histogram(stats)
