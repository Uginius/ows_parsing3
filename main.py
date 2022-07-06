@time_track
def get_html_pages():
    global is_run
    platforms_dict = {'oz': GetterOz, 'wb': GetterWb, 'sm': GetterSm}
    getters = [getter() for shop, getter in platforms_dict.items() if is_run[shop]]
    for getter in getters:
        getter.start()
    for getter in getters:
        getter.join()


@time_track
def parse_pages():
    last_dir = get_last_dir()
    parsers_dict = {'oz': ParserOz, 'wb': ParserWb, 'sm': ParserSm}
    parsers = [par(last_dir[shop]) for shop, par in parsers_dict.items() if is_run[shop]]
    for par in parsers:
        par.run()


@time_track
def get_json_data():
    json_getters = {'oz': OzJsonGetter, 'wb': WbJsonGetter, 'sm': None}
    active_platforms = [getter() for name, getter in json_getters.items() if use_platforms[name]]
    for par in active_platforms:
        par.run()


if __name__ == '__main__':
    is_run = {'oz': True, 'wb': False, 'sm': False}
    get_html_pages()
    # parse_pages()
    # get_json_data()
