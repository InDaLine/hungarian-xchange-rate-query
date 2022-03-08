import argparse
from mnb import MnbService
import argparse

def __main__():
    srv = MnbService()
    args = CommandLineArgs()
    
    rate = srv.get_current_exchange_rate(currency_code='EUR')
    money_in_eur = args['money_in_eur']
    money_in_huf = money_in_eur * rate
    print(f"{money_in_huf:,} (rate: {rate})")

class CommandLineArgs(object):
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('money_in_eur', metavar='N', type=int, nargs='?', default=1)
        self._args = vars(parser.parse_args())

    def __getitem__(self, key):
        return self._args[key]


if __name__ == '__main__':
    __main__()

