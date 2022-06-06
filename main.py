from page_getter import GetterOz, GetterWb
from parsers import ParserWb, ParserOz
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
    last_dir = get_last_dir()
    pl = []
    if oz_run:
        pl.append(ParserOz(last_dir['oz']))
    if wb_run:
        pl.append(ParserWb(last_dir['wb']))
    for par in pl:
        par.run()


if __name__ == '__main__':
    oz_run = False
    wb_run = True
    sm_run = False
    # get_html_pages()
    parse_pages()
