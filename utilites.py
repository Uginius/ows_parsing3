import os
import re
import time
from datetime import datetime
from config import date_pattern, dir_date_template


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'\nФункция работала {elapsed} секунд(ы), или {elapsed // 60} минут.')
        return result

    return surrogate


def write_utf8_file(src, filename):
    with open(filename, 'w', encoding='utf8') as write_file:
        write_file.write(src)


def append_utf8_file(src, filename):
    with open(filename, 'a', encoding='utf8') as append_file:
        append_file.write(src)


def get_last_dir():
    ld = [datetime.strptime(el, date_pattern) for el in os.listdir('htmls/') if re.findall(dir_date_template, el)]
    last_dir = f"htmls/{sorted(ld)[-1].strftime(date_pattern)}"
    result_dirs = re.findall(r'\w{2}_html_files', str(os.listdir(last_dir)))
    return {d[:2]: f'{last_dir}/{d}' for d in result_dirs}


def check_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
