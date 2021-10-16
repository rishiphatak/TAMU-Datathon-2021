# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:07:12 2021

@author: Rishi2
"""

from gensim.parsing.preprocessing import preprocess_documents
from bs4 import BeautifulSoup

MIN_LEN = 300

def remove_short_sentences(paras):
    result = []
    for p in paras:
        if len(p.get_text()) > MIN_LEN:
            result.append(p.get_text())
    return result

def get_key_words(file_name):
    infile = open("docs/{}".format(file_name), encoding="utf8")
    contents = infile.read()
    soup = BeautifulSoup(contents, 'xml')
    ps = soup.find_all('P')
    kw_mat = preprocess_documents(remove_short_sentences(ps))
    res = []
    for kws in kw_mat:
        for word in kws:
            res.append(word)
    return res