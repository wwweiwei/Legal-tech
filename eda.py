import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datatable as dt
import sys
import csv
import time
from datetime import datetime

def EDA(filename):
    df = dt.fread(filename).to_pandas()
    print(df.head())
    ## check the missing values
    print(df.isnull().sum())
    
    ## calculate the percentage of each category
    print(df.court.value_counts(normalize=True))
    print(df.sys.value_counts(normalize=True))
    print(df.type.value_counts(normalize=True))
    
    print(df.date.describe())

    ## convert date into milliseconds
    def to_integer(dt_time):
        return 10000*dt_time.year + 100*dt_time.month + dt_time.day

    newdate_list = []
    for i in range(len(df)):
        _dt = datetime.fromisoformat(df.date[i])
        milliseconds = to_integer(_dt)
        newdate_list.append(milliseconds)
    df['newdate'] = newdate_list
    print(df.newdate.describe().apply(lambda x: format(x, 'f')))
    
    ## plot the pie chart
    df.type.value_counts(normalize=True).plot.pie()
    plt.show()

    ## plot the bar graph
    df.reason.value_counts(normalize=True).plot.barh()
    plt.show()

if __name__ == '__main__':
    EDA(sys.argv[1])
