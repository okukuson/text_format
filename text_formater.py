#!/usr/bin/env python

import pyperclip as pycl

#type set sentences
def text_formater():
    text = pycl.paste()
    data2 = text.strip()
    data = data2.lower()
    pycl.copy(data)
    return data

if __name__ == "__main__":
    text_formater()