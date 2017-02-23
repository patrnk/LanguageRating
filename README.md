# LanguageSalary
Collection of scripts that help to get an average salary for some programming languages based on vacancy descriptions from SuperJob.ru

For a quickstart, just run
```#!bash
$ python3 fetch.py | python3 trim.py | python3 rate.py | less
```
which will output the number of job openings and average salary for each programming language.

Each script can be used on its own. For a complete description of how to use a particular script, use ```-h``` option.
### fetch.py
Allows the user to download an arbitrary number of job openings from "Programming and development" catalogue and save it into a file in JSON format. As an example, the following will download 500 vacancies and save them to ```output.json```:
```#!bash
$ python3 fetch.py --top 500 -o vacancies.json
```
### trim.py
The script takes a JSON file, expecting it to be similar to the one produced by ```fetch.py```. Then it strips all irrelevant job description, leaving only requirements, salary and the title, and writes it back to a JSON file. Example usage:
```#!bash
$ python3 trim.py -i vacancies.json -o trimmed_vacancies.json
```
### rate.py
Finally, this script takes a JSON file produced by ```trim.py``` and outputs the number of job openings and average salary for each programming language in its list. The list of programming languages is stored directly in the source code for the sake of simplicity. Example usage:
```#!bash
$ python3 rate.py -i trimmed_vacancies.json -o rated_languages.txt -g
```
The ```-g``` option tells the script to draw a histogram representing the data written into ```rated_languages.txt```:
![](https://i.imgur.com/wKUUlfB.png "")
# Project Goals
This is a homework assignment for the [styleru_py course](https://github.com/patrnk/styleru_py-notes).
