from finsymbols import symbols


class SymbolUtil:

    # generate Symbol
    @staticmethod
    def get_symbols():
        return symbols.get_sp500_symbols()

        # create symbol name from url
    @staticmethod
    def get_symbol_from_url(url):
        return url.split('/')[5]
