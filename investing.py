import pandas as pd
import os
import time
from datetime import datetime

from time import mktime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

import sys

style.use("ggplot")

import re

import numpy as np
from sklearn import svm

path = "/Users/ajaybati/Documents/intraQuarter"

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

percent= []

def Key_Stats(gather=["Total Debt/Equity",
                      'Trailing P/E',
                      'Price/Sales',
                      'Price/Book',
                      'Profit Margin',
                      'Operating Margin',
                      'Return on Assets',
                      'Return on Equity',
                      'Revenue Per Share',
                      'Market Cap',
                    'Enterprise Value',
                    'Forward P/E',
                    'PEG Ratio',
                    'Enterprise Value/Revenue',
                    'Enterprise Value/EBITDA',
                    'Revenue',
                    'Gross Profit',
                    'EBITDA',
                    'Net Income Avl to Common ',
                    'Diluted EPS',
                    'Earnings Growth',
                    'Revenue Growth',
                    'Total Cash',
                    'Total Cash Per Share',
                    'Total Debt',
                    'Current Ratio',
                    'Book Value Per Share',
                    'Cash Flow',
                    'Beta',
                    'Held by Insiders',
                    'Held by Institutions',
                    'Shares Short (as of',
                    'Short Ratio',
                    'Short % of Float',
                    'Shares Short (prior ']):
    count = 0
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)] #gets each file for stocks
    stock_list.sort()
    df = pd.DataFrame(columns = ['Date',
                                 'Unix',
                                 'Ticker',
                                 'Price',
                                 'stock_p_change',
                                 'SP500',
                                 'sp500_p_change',
                                 'Difference',
                                 'DE Ratio',
                                 'Trailing P/E',
                                 'Price/Sales',
                                 'Price/Book',
                                 'Profit Margin',
                                 'Operating Margin',
                                 'Return on Assets',
                                 'Return on Equity',
                                 'Revenue Per Share',
                                 'Market Cap',
                                 'Enterprise Value',
                                 'Forward P/E',
                                 'PEG Ratio',
                                 'Enterprise Value/Revenue',
                                 'Enterprise Value/EBITDA',
                                 'Revenue',
                                 'Gross Profit',
                                 'EBITDA',
                                 'Net Income Avl to Common ',
                                 'Diluted EPS',
                                 'Earnings Growth',
                                 'Revenue Growth',
                                 'Total Cash',
                                 'Total Cash Per Share',
                                 'Total Debt',
                                 'Current Ratio',
                                 'Book Value Per Share',
                                 'Cash Flow',
                                 'Beta',
                                 'Held by Insiders',
                                 'Held by Institutions',
                                 'Shares Short (as of',
                                 'Short Ratio',
                                 'Short % of Float',
                                 'Shares Short (prior ',
                                 'Status'])


    sp500_df = pd.DataFrame.from_csv("^GSPC.csv")
    count=0
    ticker_list =[]
    for each_dir in stock_list[1:]: #each
        count+=1
        print(round(count/len(stock_list)*100),"%")
        each_file = os.listdir(each_dir)
        each_file.sort()
        ticker = each_dir.split("_KeyStats")[1].split("/")[1]
        ticker_list.append(ticker)

        starting_stock_value = False
        starting_sp500_value = False

        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')

                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = each_dir+'/'+file
                source = open(full_file_path,'r').read()

                try:
                    value_list = []
                    for each_data in gather:
                        try:
                            regex = re.escape(each_data) + r'.*?(\d{1,8}\.\d{1,8}M?B?|N/A)%?</td>'

                            value = re.search(regex, source)

                            value = value.group(1)

                            if "B" in value:
                                value = float(value.replace("B",''))*1000000000
                            elif "M" in value:
                                value = float(value.replace("M",''))*1000000

                            value_list.append(value)
                        except Exception as e:
                            value = "N/A"
                            value_list.append(value)


                    try:
                        sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_date)]
                        sp500_value = float(row["Adj Close"])
                    except:
                        try:
                            sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                            row = sp500_df[(sp500_df.index == sp500_date)]
                            sp500_value = float(row["Adj Close"])
                        except Exception as e:
                            pass



                    try:
                        stock_price = float(source.split('</small><big><b>')[1].split('</b></big>')[0])
                    except Exception as e:
                        try:
                            stock_price = (source.split('</small><big><b>')[1].split('</b></big>')[0])
                            stock_price = re.search(r'(\d{0,8}\.\d{0,8})', stock_price)
                            stock_price = float(stock_price.group(1))

                        except Exception as e:
                            try:
                                stock_price = source.split('</span></span> <span class="')
                                index=0

                                stock_price = stock_price[0]
                                for x in range(8):
                                    if is_int(stock_price[-x-1]):
                                        index=-x-1
                                    elif stock_price[-x-1] ==".":
                                        index=-x-1
                                stock_price = float(stock_price[index:])


                            except Exception as e:
                                stock_price = source.split('</span></span><span class="')
                                index=0

                                stock_price = stock_price[0]
                                for x in range(8):
                                    if is_int(stock_price[-x-1]):
                                        index=-x-1
                                    elif stock_price[-x-1] ==".":
                                        index=-x-1
                                stock_price = float(stock_price[index:])

                    if not starting_stock_value:
                        starting_stock_value=stock_price
                    if not starting_sp500_value:
                        starting_sp500_value=sp500_value

                    stock_p_change=((stock_price - starting_stock_value)/starting_stock_value)*100

                    sp500_p_change=((sp500_value - starting_sp500_value)/starting_sp500_value)*100

                    difference = stock_p_change-sp500_p_change

                    if difference > 0:
                        status = "outperform"
                    else:
                        status = "underperform"

                    if value_list.count("N/A") >0:
                        pass
                    else:
                        df = df.append({'Date':date_stamp,
                                        'Unix':unix_time,
                                        'Ticker':ticker,
                                        'Price':stock_price,
                                        'stock_p_change':stock_p_change,
                                        'SP500':sp500_value,
                                        'sp500_p_change':sp500_p_change,
                                        'Difference':difference,
                                        'DE Ratio':value_list[0],
                                        #'Market Cap':value_list[1],
                                        'Trailing P/E':value_list[1],
                                        'Price/Sales':value_list[2],
                                        'Price/Book':value_list[3],
                                        'Profit Margin':value_list[4],
                                        'Operating Margin':value_list[5],
                                        'Return on Assets':value_list[6],
                                        'Return on Equity':value_list[7],
                                        'Revenue Per Share':value_list[8],
                                        'Market Cap':value_list[9],
                                         'Enterprise Value':value_list[10],
                                         'Forward P/E':value_list[11],
                                         'PEG Ratio':value_list[12],
                                         'Enterprise Value/Revenue':value_list[13],
                                         'Enterprise Value/EBITDA':value_list[14],
                                         'Revenue':value_list[15],
                                         'Gross Profit':value_list[16],
                                         'EBITDA':value_list[17],
                                         'Net Income Avl to Common ':value_list[18],
                                         'Diluted EPS':value_list[19],
                                         'Earnings Growth':value_list[20],
                                         'Revenue Growth':value_list[21],
                                         'Total Cash':value_list[22],
                                         'Total Cash Per Share':value_list[23],
                                         'Total Debt':value_list[24],
                                         'Current Ratio':value_list[25],
                                         'Book Value Per Share':value_list[26],
                                         'Cash Flow':value_list[27],
                                         'Beta':value_list[28],
                                         'Held by Insiders':value_list[29],
                                         'Held by Institutions':value_list[30],
                                         'Shares Short (as of':value_list[31],
                                         'Short Ratio':value_list[32],
                                         'Short % of Float':value_list[33],
                                         'Shares Short (prior ':value_list[34],
                                        'Status':status},
                                       ignore_index=True)
                except Exception as e:
                    pass







    # for each_ticker in ticker_list:
    #     try:
    #
    #         plot_df = df[(df['Ticker']==each_ticker)]
    #         plot_df = plot_df.set_index(['Date'])
    #
    #         # if plot_df['Status'][-1] == "underperform":
    #         #     color = 'r'
    #         # else:
    #         #     color = 'b'
    #
    #         plot_df['Difference'].plot(label=each_ticker)
    #         plt.legend()
    #     except Exception as e:
    #         pass
    #
    # plt.show()

    df.to_csv("investing_analysis.csv")


def data_set(features = ['Date',
                             'Unix',
                             'Ticker',
                             'Price',
                             'stock_p_change',
                             'SP500',
                             'sp500_p_change',
                             'Difference',
                             'DE Ratio',
                             'Trailing P/E',
                             'Price/Sales',
                             'Price/Book',
                             'Profit Margin',
                             'Operating Margin',
                             'Return on Assets',
                             'Return on Equity',
                             'Revenue Per Share',
                             'Market Cap',
                             'Enterprise Value',
                             'Forward P/E',
                             'PEG Ratio',
                             'Enterprise Value/Revenue',
                             'Enterprise Value/EBITDA',
                             'Revenue',
                             'Gross Profit',
                             'EBITDA',
                             'Net Income Avl to Common ',
                             'Diluted EPS',
                             'Earnings Growth',
                             'Revenue Growth',
                             'Total Cash',
                             'Total Cash Per Share',
                             'Total Debt',
                             'Current Ratio',
                             'Book Value Per Share',
                             'Cash Flow',
                             'Beta',
                             'Held by Insiders',
                             'Held by Institutions',
                             'Shares Short (as of',
                             'Short Ratio',
                             'Short % of Float',
                             'Shares Short (prior ',
                             'Status']):
    dataDF = pd.DataFrame.from_csv("investing_analysis.csv")
    dataDF = dataDF[:100]
    X = np.array((dataDF[features].values))

    y = list(dataDF["Status"].replace("underperform",0).replace('outperform',1).values)

    return X,y

def sk_analysis():
    X, y = data_set()
    clf = svm.SVC(kernel='linear', C= 1.0)

    clf.fit(X,y)

    w = clf.coef_[0]

    a = -w[0] / w[1]

    xx = np.linspace(min(X[:,0]), max(X[:,0]))
    yy = a * xx-clf.intercept_[0]/w[1]

    h0= plt.plot(xx, yy, "k-", label = "n weighted")

    plt.scatter(X[:,0],X[:,1],c=y)

    plt.ylabel("Trailing P/e")

    plt.xlabel("DE Ratio")

    plt.show()




print(data_set())
