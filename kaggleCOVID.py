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

import numpy as np
from sklearn.svm import SVR
import numpy as np

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


def graphGeneral():
    for country in countries:
        try:
            plot_df = train[(train["Country_Region"]==country)]
            print(country)
            plot_df = plot_df.set_index(["Date"])
            plot_df["Fatalities"].plot(label = country)
            plt.legend()
        except:
            pass
    plt.show()

def graphProvinces():
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

def graphTotal(show = False):
    data_dict = {}
    plot_df= train[(train["Country_Region"]=="Afghanistan")]
    plot_df=plot_df["Date"]
    for date in plot_df:
        real_date = datetime.strptime(date, "%Y-%m-%d")
        plot_date_gather = train[(train["Date"]==date)]
        total = 0
        largest = 0
        for fatality in plot_date_gather["Fatalities"]:
            if fatality> largest:
                largest = fatality
            total+=fatality
        print(date, total, "Highest contributor:", largest)
        data_dict[real_date]=total




    xData=[]
    for x in range(len(list(data_dict.keys()))):
        xData.append([x+1])
    X = xData

    y = list(data_dict.values())
    # plt.plot(xData, list(data_dict.values()))


    # #############################################################################
    # Fit regression model
    svr_rbf = SVR(kernel='rbf', C=100, gamma=0.001, epsilon=.1)
    svr_lin = SVR(kernel='linear', C=100, gamma='auto')
    svr_poly = SVR(kernel='poly', C=100, gamma='auto',degree=3, epsilon=.1,
                   coef0=1)
    print()

    lw = 2

    svrs = [svr_lin]
    kernel_label = ['Linear']
    model_color = ['g']
    print("starting to fit now")
    if show:
        fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 10), sharey=True)
        # for 0, svr in enumerate(svrs):
    theX = []
    for x in range(20):
        theX.append([x+76])
    prediction = svr_poly.fit(X,y).predict(theX)
    print(prediction, len(prediction))
    plt.plot(theX, list(prediction))
    plt.show()
    # plt.plot(X, svr_rbf.fit(X, y).predict(theX), color=model_color[0], lw=lw,
    #               label='{} model'.format(kernel_label[0]))
    # if show:
    #     plt.scatter(X[svr_poly.support_], y[svr_poly.support_], facecolor="none",
    #                      edgecolor=model_color[0], s=50,
    #                      label='{} support vectors'.format(kernel_label[0]))
    #     plt.scatter(X[np.setdiff1d(np.arange(len(X)), svr_poly.support_)],
    #                      y[np.setdiff1d(np.arange(len(X)), svr_poly.support_)],
    #                      facecolor="none", edgecolor="k", s=50,
    #                      label='other training data')
    # plt.show()
    # if show:
    #     fig.text(0.5, 0.04, 'data', ha='center', va='center')
    #     fig.text(0.06, 0.5, 'target', ha='center', va='center', rotation='vertical')
    #     fig.suptitle("Support Vector Regression", fontsize=14)


graphTotal()
