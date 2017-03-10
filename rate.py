import json
import argparse
import sys
import matplotlib.pyplot as plt


def is_language_detected_in_text(language_synonym_list, text):
    for synonym in language_synonym_list:
        if synonym.lower() in text.lower():
            return True
    return False


def initialize_language_statistics_dictionary(languages):
    statistics = {}
    for language in languages:
        statistics[language] = {'vacancy_count': 0, 'payment_sum': 0}
    return statistics

def get_language_statistics(vacancy_list):
    # programming languages mentioned in SuperJob research
    # https://www.superjob.ru/research/articles/111800/samye-vysokie-zarplaty-v-sfere-it/
    language_search_keywords = { 'Java': ['Java'],
                                 'Python': ['Python'],
                                 'C/C++': ['C++'],
                                 'Objective-C': ['Objective-C', 'Obj-C'],
                                 'C#': ['C#'],
                                 'PHP': ['PHP'],
                                 'JavaScript': ['JavaScript', 'JS'],
                                 'Ruby': ['Ruby'],
                                 'Delphi': ['Delphi'],
                                 'Perl': ['Perl'], 
                                 }
    stats = initialize_language_statistics_dictionary(language_search_keywords.keys())
    for vacancy in vacancy_list:
        for language, synonyms in language_search_keywords.items():
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

    for counters in stats.values():
        if counters['vacancy_count'] == 0:
            counters['average_payment'] = 0
            continue
        counters['average_payment'] = counters['payment_sum'] / counters['vacancy_count']

    return stats


def print_statistics_for_each_language(language_statistics, outfile):
    for language, stats in sorted(language_statistics.items()):
        outfile.write('Name: %s\n' % language)        
        outfile.write('  Number of vacancies: %d\n' % stats['vacancy_count'])        
        outfile.write('  Average payment: %d\n' % stats['average_payment'])        


def show_statistics_histogram(statistics):
    bar_coordinates = range(len(sorted(statistics)))
    language_names = [name for name in sorted(statistics)]
    average_payments = [statistics[name]['average_payment'] for name in language_names]
    plt.figure(figsize=(12, 7))
    plt.bar(bar_coordinates, average_payments, tick_label=language_names, align='center')

    plt.figure(1).canvas.set_window_title('language salaries')
    plt.ylabel('Average salary')
    plt.xlabel('Language name')
    plt.title('Comparison of average salaries among different programming languages')
    plt.show()
    

def get_cli_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', type=argparse.FileType('r'),
                        default=sys.stdin,
                        help='input JSON file, stdin by default')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='output file, stdout by default')
    parser.add_argument('-g', '--graph', action='store_true',
                        help='in addition to text output, provide '\
                             'graphical representation of the data')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_cli_arguments()
    vacancies = json.load(args.infile)
    stats = get_language_statistics(vacancies)
    print_statistics_for_each_language(stats, args.outfile)
    if args.graph:
        show_statistics_histogram(stats)
