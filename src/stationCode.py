# coding: UTF-8
'''
Created on 2017-03-01

@author: Mark Hsu
'''
import csv

def getStation(county):
    '''
    @param {str} county name
    @return {list} if the file exists else return exception error.  
    '''
    filepath = 'model/station information/CWB Station Code utf8 county.csv'
    filepath = filepath.replace('county', county)
    try:
        with open(filepath, 'r', encoding='utf-8') as csvfile:
            result = []
            for i, row in enumerate(csv.reader(csvfile)):
                # if i=0, row = header = ['SiteId', 'County']
                # so pass it
                if i == 0:
                    continue
                result.append(row)
        return result
    except Exception as e:
        return e

def select(county):
    ''' 將需要的資料取出另存成一個csv file，目前需求為取出台中市的測站ID以及測站名稱
    @param {str} county name
    @return {boolean} if succeeded return True
    '''
    filepath = 'model/station information/CWB Station Code utf8 county.csv'
    try:
        with open('model/station information/CWB Station Code utf8.csv', encoding='utf-8') as csvfile:
            filepath = filepath.replace('county', county)
            result = []
            for row in csv.DictReader(csvfile):
                # SiteId start with letters C0 or 4 means that station belongs to CWB
                if row['County'] == '臺中市' and (row['SiteId'][0:2] == 'C0' or row['SiteId'][0] == '4'):
                    result.append([row['SiteId'], row['SiteName']])
#         print(result)
#         result = ['臺中', '467490'], ['梧棲', '467770'], ... ...]

        with open(filepath, 'w', encoding='utf-8') as csvfile:
            fieldnames = ['SiteId', 'County']
            # csv file is a binary format, with "\r\n" separating records.
            # we use lineterminator='\n', then it won't produce the unwanted newline.
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for i in range(len(result)):
                writer.writerow({'SiteId':result[i][0], 'County':result[i][1]})
                print('SiteId:{}\tCounty:{}'.format(result[i][0], result[i][1]))
        return True
    except Exception as e:
        print(e)
        return False
# select('臺中市') # for test this function
# print(getStation('臺中市')) # for test this function
