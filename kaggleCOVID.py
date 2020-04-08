import pandas as pd
import os
import time
from datetime import datetime

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

from urllib.request import Request, urlopen
import urllib.request
from bs4 import BeautifulSoup

import re

import math

style.use("dark_background")


train = pd.DataFrame.from_csv('/Users/ajaybati/Documents/COVID/train.csv')
regex = '15px">'+r'.*?'+'<'
countries = []
req = Request("https://www.worldometers.info/geography/alphabetical-list-of-countries/",
              headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    page = response.read()
    soup = BeautifulSoup(page, 'html.parser')
    large = soup.find('div'.encode("utf-8", "ignore"), 'table-responsive')
    for x in large.find_all("td"):
        if "15px" in str(x):
            countries.append(str(x).split('<td style="font-weight: bold; font-size:15px">')[1].split('</td>')[0])



# for country in countries:
#     try:
#         plot_df = train[(train["Country_Region"]==country)]
#         print(plot_df)
#         plot_df = plot_df.set_index(["Date"])
#         plot_df["Fatalities"].plot(label = country)
#         plt.legend()
#     except:
#         pass


count=0
for country in countries:
    count+=1
    if country == "United States of America":
        country="US"
    plot_df_master = train[(train["Country_Region"]==country)]
    try:

        if type(plot_df_master.iloc[0,0])==str:
            plt.figure(count)
            ids = list(plot_df_master.index)

            Province_States = []
            for id in ids:
                try:
                    a = plot_df_master.iloc[id-ids[0],0]
                except Exception as e:
                    pass
                if a not in Province_States:
                    Province_States.append(a)
            try:
                dateConverterList = list(plot_df_master["Date"])
                for x in range(len(dateConverterList)-1):
                     dateConverterList[x]=datetime.strptime(dateConverterList[x], "%Y-%m-%d")
                plot_df_master["Date"]=dateConverterList
            except Exception as e:
                pass

            highest = 0
            for province in Province_States:
                try:
                    plot_df=plot_df_master[(plot_df_master["Province_State"]==province)]
                    plot_df = plot_df.set_index(["Date"])
                    if plot_df["Fatalities"][-1]>highest:
                        highest = plot_df["Fatalities"][-1]
                        highestProvince = province
                    plot_df["Fatalities"].plot(label = province, color = 'b')
                    plt.legend()
                except Exception as e:
                    pass
            print(highestProvince,highest,"that's too much bro")
            plot_df=plot_df_master[(plot_df_master["Province_State"]==highestProvince)]
            plot_df = plot_df.set_index(["Date"])

            plot_df["Fatalities"].plot(label = highestProvince, color = 'r')
            plt.title(country)
            plt.legend()
    except Exception as e:
        pass
    # else:
    #
    #     plot_df_master=plot_df_master.set_index(["Date"])
    #     plot_df_master["Fatalities"].plot(color = 'b')

    plt.show()
