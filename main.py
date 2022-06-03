from page_getter import GetterOz, GetterWb
from parsers import PagesParser, ParserWb, ParserOz
from utilites import time_track, get_last_dir


@time_track
def get_html_pages():
    global oz_run, wb_run, sm_run
    par_oz = GetterOz()
    par_wb = GetterWb()
    if oz_run:
        par_oz.start()
    if wb_run:
        par_wb.start()
    if oz_run:
        par_oz.join()
    if wb_run:
        par_wb.join()


@time_track
def parse_pages():
    pl = {'oz': ParserOz, 'wb': ParserWb}
    parsers = [pl[platform](directory) for platform, directory in get_last_dir().items()]
    for par in parsers:
        par.run()


if __name__ == '__main__':
    oz_run = True
    wb_run = True
    sm_run = False
    # get_html_pages()
    parse_pages()
