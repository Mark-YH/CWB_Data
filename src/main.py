# coding: UTF-8
'''
Created on 2017-03-01

@author: Mark Hsu
'''
import requests
import tableToList
import stationCode
import percentEncoding
import csv
import time
def saveToCsv(result, date, stationId):
    try:
        filepath = 'model/'
        filepath += stationId + '_'
        filepath += date + '.csv'
        with open(filepath, 'w', encoding='utf-8') as csvfile:
            # csv file is a binary format, with "\r\n" separating records.
            # we use lineterminator='\n', then it won't produce the unwanted newline.
            writer = csv.writer(csvfile, lineterminator='\n')
            for item in result:
                writer.writerow(item)
        print('File {}_{}.csv saved'.format(stationId,date))
    except Exception as e:
        print(e)
    
def main():
    county = '臺中市'
    station = stationCode.getStation(county)
    # station = [['467490', '臺中'], ['467770', '梧棲'], ... ...]
    for item in station:
        stationId = item[0]
        stName = item[1]
        # 爬取資料的網址中，變數stname是經過兩次的percent encoding，可能是氣象局的bug?
        stName = percentEncoding.encode(percentEncoding.encode(stName))
        date = '2017-02-27'
        # 取資料的網址
        preUrl = 'http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain'
        url = preUrl + '&station=' + stationId + '&stname=' + stName + '&datepicker=' + date
    #     print(url)
        html = requests.get(url)
        tables = tableToList.getTables(html)
        result = tableToList.convert(tables[1])
        saveToCsv(result, date, stationId)
        time.sleep(2)
    
    print('All done.')
    
if __name__ == '__main__':
    main()

