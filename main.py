from page_getter import GetterOz, GetterWb
from utilites import time_track


@time_track
def get_html_pages():
    global oz_run, wb_run, sm_run
    parsers = [GetterOz() if oz_run else None, GetterWb() if wb_run else None]
    parsers = [x for x in parsers if x]
    for getter in parsers:
        getter.start()
    for getter in parsers:
        getter.join()


@time_track
def parse_pages():
    pass


if __name__ == '__main__':
    oz_run = True
    wb_run = False
    sm_run = False
    get_html_pages()
    # parse_pages()
