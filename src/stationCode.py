# coding: UTF-8
'''
Created on 2017-03-01

@author: Mark Hsu
'''
import csv
import os.path

def getStation():
    with open('model/CWB Station Code utf8.csv', 'r', encoding='utf-8') as f:
        count = 0
        result = []
        for row in csv.DictReader(f):
            if row['County'] == '臺中市' and (row['SiteId'][0:2] == 'C0' or row['SiteId'][0] == '4'):
    #             print(count,'\t',row['SiteId'],row['SiteName'])
                count += 1
                result.append({row['SiteId']:row['SiteName']})
        return result

def select(county):
    filename = 'model/CWB Station Code utf8 county.csv'
    try:
        with open('model/CWB Station Code utf8.csv', encoding='utf-8') as f:
            filename = filename.replace('county', county)
            result = {}
            for row in csv.DictReader(f):
                if row['County'] == '臺中市' and (row['SiteId'][0:2] == 'C0' or row['SiteId'][0] == '4'):
                    result[row['SiteId']] = row['SiteName']
        print(result['SiteId'])
#         with open(filename, 'w', encoding='utf-8') as csvfile:
#             fieldnames = ['SiteId', 'County']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows({'SiteId':result['SiteId'], 'County':result['County']})
#檢查result格式 重新寫入######
    except Exception as e:
        print(e)

select('臺中市')


# li = getStation()
# for i,item in enumerate(li):
#     print(i,item)
