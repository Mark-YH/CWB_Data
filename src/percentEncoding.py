# coding: UTF-8
'''
Created on 2017-03-01

@author: Mark Hsu
'''
import urllib.parse

def decode(encoded_uri):
    return urllib.parse.unquote(encoded_uri)

def encode(decoded_uri):
    return urllib.parse.quote(decoded_uri)