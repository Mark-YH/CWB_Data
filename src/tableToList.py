# coding: UTF-8
'''
Created on 2017-03-01

@author: Mark Hsu
'''
from bs4 import BeautifulSoup

def getTables(html):
    soup = BeautifulSoup(html.text, "html.parser")
    return soup.findAll('table')

def convert(table):
    result = []
    for i,row in enumerate(table.find_all('tr')):
        result.append([])   
        print('---This is row{}: ---'.format(i))
        for j,col in enumerate(row.find_all('th')):
            print('---This is header{}: \t{}'.format(j,col))
            result[i]=col
            #print('-*-End of header -*-')
        for j,col in enumerate(row.find_all('td')):
            print('---This is column{}: \t{}'.format(j,col))
            result[i]=col
            #print('---End of column ---')
        print('---End of row ---')
    print('****\n{}\n****'.format(result))
    return result
