#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date
import json
import gspread_dataframe as gd
import pandas as pd

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

def shee_upd(d,sl_n,a,sl_p):
    temp=[]
    next_row=int(next_available_row(sl_n))
    s=0.00
    for x in d:
        for y in a.iterrows():
            if x==y[1][1]:
                if x=='':
                    continue
                else:
                    now=date.today()
                    json_str = json.dumps({now}, default=str)
                    price=float(1+y[1][4]/100)*float(y[1][3])*float(d[x][0])
                    temp.append([y[1][0],x,d[x][0],price,json_str])
                    s=s+price
    df=pd.DataFrame(temp,columns={'Tender S.No.','item name','quantity','net price','date of entry'})
    gd.set_with_dataframe(worksheet=sl_n,dataframe=df,include_index=False,include_column_header=False,row=int(next_row))
    gd.set_with_dataframe(worksheet=sl_p,dataframe=df,include_index=False,include_column_header=False,row=3)
    return s
    
    

