import pandas as pd
import os
import time
from datetime import datetime

from time import mktime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

import sys

style.use("dark_background")

import re

path = "/Users/ajaybati/Documents/intraQuarter"

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

percent= []

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    count = 0
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)] #gets each file for stocks
    stock_list.sort()
    df = pd.DataFrame(columns = ['Date',
                                 'Unix',
                                 'Ticker',
                                 'DE Ratio',
                                 'Price',
                                 'stock_p_change',
                                 'SP 500',
                                 'sp_change',
                                 'Difference',
                                 'Status'])

    sp500_df = pd.DataFrame.from_csv("^GSPC.csv")

    ticker_list =[]
    for each_dir in stock_list[1:25]: #each
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

                    try:
                        value = (source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                        if value != "N/A":
                            value=float(value)
                    except Exception as e:
                        try:
                            value = (source.split(gather+':</td>\n<td class="yfnc_tabledata1">')[1].split('</td>')[0])
                            if value !="N/A":
                                value=float(value)
                        except Exception as e:
                            value = "N/A"


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

                    df = df.append({'Date':date_stamp,
                                    'Unix':unix_time,
                                    'Ticker':ticker,
                                    'DE Ratio':value,
                                    'Price':stock_price,
                                    'stock_p_change':stock_p_change,
                                    'SP 500':sp500_value,
                                    'sp_change':sp500_p_change,
                                    'Difference':difference,
                                    'Status':status},ignore_index = True)
                except Exception as e:
                    pass







    for each_ticker in ticker_list:
        try:
            plot_df = df[(df['Ticker']==each_ticker)]
            plot_df = plot_df.set_index(['Date'])

            if plot_df['Status'][-1] == "underperform":
                color = 'r'
            else:
                color = 'b'

            plot_df['Difference'].plot(label=each_ticker, color=color)
            plt.legend()
        except:
            pass

    plt.show()

    save = gather.replace(' ', '').replace(')','').replace('(','').replace('/','')+('.csv')
    df.to_csv(save)
    print(save)





Key_Stats()
