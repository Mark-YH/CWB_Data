# coding: UTF-8
'''
Created on 2017-03-01

@author: Mark Hsu
'''
from bs4 import BeautifulSoup
import re
def getTables(html):
    ''' get tables from HTML by BeautifulSoup4 library
    '''
    soup = BeautifulSoup(html.text, "html.parser")
    return soup.findAll('table')

def convert(table):
    '''
    total: 26 rows, 15 columns, 2 kinds of headers
    row 0 and row 1 are headers. only need the header of row 1 
    row 2 ~ row 25 are columns
    row[0~25]
    columns[0~14]
    header[0~14]
    '''
    result=[]
    for i, row in enumerate(table.find_all('tr')):
        if i == 0:
            continue

#         print('---This is row{}: ---'.format(i))
        temp=[]
#         for j, col in enumerate(row.find_all('th')):
        for col in row.find_all('th'):
            temp.append(tagFilter(str(col), header=True))
#             print('---This is header{}: \t{}'.format(j, tagFilter(str(col))))
        if temp!=[]:
            result.append(temp)
#             print(temp)
        temp=[]
#         for j, col in enumerate(row.find_all('td')):
        for col in row.find_all('td'):
            temp.append(tagFilter(str(col)))
#             print('---This is column{}: \t{}'.format(j, tagFilter(str(col))))
        if temp!=[]:
            result.append(temp)
#             print(temp)

    return result

def tagFilter(s,header=False):
    if header:
        s=s.replace('<br>',' ')
    s=s.replace('\xa0', '')
    s = re.sub(r'</?\w+[^>]*>','',s)
    return s
