import shutil


def copy_files(names):
    for file in names:
        # src_old = f'htmls/03-06-2022/wb_html_files/03-06-2022_{file}'
        src_file = f'htmls/04-06-2022/wb_html_files/{file}'
        result_file = f'htmls/05-06-2022/wb_html_files/{file}'
        shutil.copy2(src_file, result_file)
        print(f' copy {src_file}  to  {result_file}')


def get_error_files():
    with open('log.txt', 'r', encoding='utf8') as read_file:
        names = [line.split()[0] for line in read_file]
        return names


if __name__ == '__main__':
    error_names = get_error_files()
    copy_files(error_names)
