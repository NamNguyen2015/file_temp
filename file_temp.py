#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:37:21 2022

@author: namnguyen
"""

import streamlit as st
import json
import pandas as pd
import os
import tempfile
import base64

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href




# create a temporary file and write some data to it
fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')
fp.write(b'My name is Nam')
# read data from file
fp.seek(0)
fp.read()
#b'Hello world!'
# close the file, it will be removed
fp.close()

st.markdown(get_binary_file_downloader_html(fp, 'My Data'), unsafe_allow_html=True)