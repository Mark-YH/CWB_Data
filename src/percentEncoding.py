# coding: UTF-8
'''
Created on 2017-03-01

@author: Mark Hsu
'''
import urllib.parse

def uri_decoder(encoded_uri):
    return urllib.parse.unquote(encoded_uri)

def uri_encoder(decoded_uri):
    return urllib.parse.quote(decoded_uri)