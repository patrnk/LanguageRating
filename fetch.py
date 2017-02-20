if __name__ == '__main__':
    args = get_argument_parser()
    credentials = load_data_from_json_file(args.credentials_file)
    vacancies = get_vacancy_list(args.number_of_vacancies, credentials)
    save_data_to_json_file(vacancies)

