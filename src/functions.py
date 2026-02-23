import pandas as pd
import requests
from io import StringIO
def read(path, div=","):
    return pd.read_csv(path, sep=div)
def groupby(x, columns):
    return x.groupby(columns).size()
def listing (x,columns):
    list = []
    for i in x[columns].unique():
        list.append(i)
    return list
def web_read(url_text,user_text,match_text):
    url = url_text
    headers = {'User-Agent' : user_text}
    html = requests.get(url, headers=headers, timeout=30).text
    return pd.read_html(StringIO(html), match=match_text)[0]
