import os
import re
import time
from datetime import datetime


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'\nФункция работала {elapsed} секунд(ы), или {elapsed // 60} минут.')
        return result

    return surrogate


def write_html(src, filename):
    with open(filename, 'w', encoding='utf8') as write_file:
        write_file.write(src)


def get_last_dir():
    pages_dir_from_os = os.listdir('htmls')
    dir_date_template = r'\d{2}-\d{2}-202\d'
    loaded_dirs = []
    for el in pages_dir_from_os:
        check_dir = re.findall(dir_date_template, el)
        if check_dir:
            loaded_dirs.append(datetime.strptime(el, '%d-%m-%Y'))
    final_dir = sorted(loaded_dirs)[-1].strftime('%d-%m-%Y')
    return final_dir
