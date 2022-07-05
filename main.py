from config import today
from json_getter import OzJsonGetter, WbJsonGetter
from page_getter import GetterOz, GetterWb
from parsers import ParserWb, ParserOz
from utilites import time_track, get_last_dir, check_dir


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


def get_json_data():
    json_getters = {'oz': OzJsonGetter, 'wb': WbJsonGetter, 'sm': None}
    active_platforms = [getter() for name, getter in json_getters.items() if use_platforms[name]]
    for par in active_platforms:
        par.run()


if __name__ == '__main__':
    # oz_run = True
    # wb_run = True
    # sm_run = False
    # get_html_pages()
    # parse_pages()
    use_platforms = {'oz': True, 'wb': True, 'sm': False}
    get_json_data()
