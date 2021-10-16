# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:07:12 2021

@author: Rishi2
"""

from gensim.parsing.preprocessing import *
from bs4 import BeautifulSoup

MIN_LEN = 300

def remove_short_sentences(paras):
    result = []
    for p in paras:
        if len(p.get_text()) > MIN_LEN:
            result.append(p.get_text())
    return result

# file_name : fully qualified path
def get_key_words(file_name):
    infile = open(file_name, encoding="utf8")
    contents = infile.read()
    soup = BeautifulSoup(contents, 'xml')
    ps = soup.find_all('P')
    full_doc = " ".join(remove_short_sentences(ps))
    CUSTOM_FILTERS = [lambda x: x.lower(), strip_tags, strip_punctuation, strip_multiple_whitespaces,
                   strip_numeric, remove_stopwords, strip_short, strip_non_alphanum]
    return preprocess_string(full_doc, CUSTOM_FILTERS)

# print(get_key_words("C:\Junior Year\TAMUDatathon2021\docs/01-10222.xml"))