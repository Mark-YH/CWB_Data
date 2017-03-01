# coding: UTF-8
'''
Created on 2017-03-01

@author: Mark Hsu
'''
import requests
import tableToList
from percentEncoding import uri_encoder

def main():
    station = '467490'
    stName = '臺中'
    stName = uri_encoder(uri_encoder(stName))
    print(stName)
    
    
    date = '2017-02-27'
    origin_url = 'http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain'
    url = origin_url + '&station=' + station + '&stname=' + stName + '&datepicker=' + date
    print(url)
    html = requests.get(url)
    tables = tableToList.getTables(html)
    result = tableToList.convert(tables[1])
    for i,row in enumerate(result):
        print(row)
        for col in result[i]:
            print(col)

if __name__ == '__main__':
    main()

