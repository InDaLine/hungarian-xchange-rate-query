from zeep import Client
import xml.etree.ElementTree as ET

def __main__():
    client = Client('http://www.mnb.hu/arfolyamok.asmx?wsdl')
    xr = client.service.GetExchangeRates(
        startDate = '2022-01-10', 
        endDate = '2022-01-10', 
        currencyNames='EUR'
    )
    etree = ET.fromstring(xr)
    # <MNBExchangeRates><Day date="2022-01-10"><Rate unit="1" curr="EUR">357,88</Rate></Day></MNBExchangeRates>
    rate_str = etree.find('Day').find('Rate').text
    rate = float(rate_str.replace(',', '.'))
    print(rate)

if __name__ == '__main__':
    __main__()


# {
#     "GetCurrencies": {},
#     "GetCurrencyUnits": {
#         "currencyNames": {
#             "optional": True,
#             "type": "String(value)"
#         }
#     },
#     "GetCurrentExchangeRates": {
#     },
#     "GetDateInterval": {
#     },
#     "GetExchangeRates": {
#         "startDate": {
#             "optional": True,
#             "type": "String(value)"
#         },
#         "endDate": {
#             "optional": True,
#             "type": "String(value)"
#         },
#         "currencyNames": {
#             "optional": True,
#             "type": "String(value)"
#         }
#     },
#     "GetInfo": {
#     }
# }
