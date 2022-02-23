from datetime import date
from zeep import Client
import xml.etree.ElementTree as ET

def __main__():
    client = Client('http://www.mnb.hu/arfolyamok.asmx?wsdl')
    last_publish_date = get_last_publish_date(client)
    xr = client.service.GetExchangeRates(
        startDate = last_publish_date, 
        endDate = last_publish_date, 
        currencyNames='EUR'
    )
    etree = ET.fromstring(xr)
    # <MNBExchangeRates><Day date="2022-01-10"><Rate unit="1" curr="EUR">357,88</Rate></Day></MNBExchangeRates>
    rate_str = etree.find('Day').find('Rate').text
    rate = float(rate_str.replace(',', '.'))
    print(rate)

def get_last_publish_date(client : Client):
    date_interval_xml_str = client.service.GetDateInterval()
    # <MNBStoredInterval><DateInterval startdate="1949-01-03" enddate="2022-02-23" /></MNBStoredInterval>
    date_interval_etree = ET.fromstring(date_interval_xml_str)
    end_date = date_interval_etree.find('DateInterval').attrib['enddate']
    return end_date

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
