from datetime import date
from zeep import Client
import xml.etree.ElementTree as ET

class MnbService(object):
    def __init__(self) -> None:
        self.client = Client('http://www.mnb.hu/arfolyamok.asmx?wsdl')

    def get_current_exchange_rate(self, currency_code : str):
        last_publish_date = self.get_last_publish_date(self.client)
        rate = self.get_exchange_rate(currency_code, last_publish_date)
        return rate

    def get_exchange_rate(self, currency_code : str, query_date : str):
        xr = self.client.service.GetExchangeRates(
            startDate = query_date, 
            endDate = query_date, 
            currencyNames=currency_code
        )
        etree = ET.fromstring(xr)
        # <MNBExchangeRates><Day date="2022-01-10"><Rate unit="1" curr="EUR">357,88</Rate></Day></MNBExchangeRates>
        rate_str = etree.find('Day').find('Rate').text
        rate = float(rate_str.replace(',', '.'))
        return rate

    def get_last_publish_date(self, client : Client):
        date_interval_xml_str = client.service.GetDateInterval()
        # <MNBStoredInterval><DateInterval startdate="1949-01-03" enddate="2022-02-23" /></MNBStoredInterval>
        date_interval_etree = ET.fromstring(date_interval_xml_str)
        end_date = date_interval_etree.find('DateInterval').attrib['enddate']
        return end_date

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
