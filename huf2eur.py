from mnb import MnbService

def __main__():
    srv = MnbService()
    rate = srv.get_current_exchange_rate(currency_code='EUR')
    print(rate)

if __name__ == '__main__':
    __main__()

