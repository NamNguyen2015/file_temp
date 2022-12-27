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

#st.markdown(get_binary_file_downloader_html(fp, 'My Data'), unsafe_allow_html=True)
