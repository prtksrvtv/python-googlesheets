#!/usr/bin/env python
# coding: utf-8

# In[27]:


from tkinter import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter.ttk import *
import gspread
from sheet_update import *
from numtoword import *

def choice(ch):
    def rty(d):

        for x in d:
            if d[x][0].get()=='':
                d[x][0]=0

            else:
                d[x][0]=d[x][0].get()

        sl_n=gc.get_worksheet(1)
        sl_p=gc.get_worksheet(2)
        r=shee_upd(d,sl_n,a,sl_p)
        z=str(r).split('.')
        if int(z[1])==0:
            totsum=number_to_word(int(r))
        else:
            totsum=number_to_word(round(r,2))
        sl_p.update_acell('A1',value=totsum)
        os.system('python done_window.py')



    gs=gspread.service_account(r'C:\Users\ayush\Downloads\Prikaway\Invoice Generating Program\python-access-357214-446b081bdda7.json')
    gc=gs.open('SSGJ-Raashan Shop')
    sl = gc.get_worksheet(0)
    a=pd.DataFrame(sl.get_all_records())
    d={}
    a=a[a['Tender Number'].isin([ch])]
        
    for y in a.iterrows():
        d[y[1][1]] = 0


    root=Tk()
    root.title("Prikaway Pvt. Ltd.")
    # setting the windows size
    root.geometry("400x500")
    main_frame=Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=scrollbar.set)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame, anchor='nw')
    count=2
    na_label = tk.Label(second_frame, text = 'Enter the Quantity of each Item', font=('calibre',10, 'bold'),anchor='center')
    na_label.grid(row=1,column=0)
    for x in d:

        name_label = tk.Label(second_frame, text = x, font=('calibre',10, 'bold'))
        name_entry = tk.Entry(second_frame, font=('calibre',10,'normal'))
        name_label.grid(row=count,column=0)
        name_entry.grid(row=count,column=1)
        d[x]=[name_entry]
        count+=1

    submit = Button(
        second_frame,
        text='SUBMIT', command= lambda: rty(d)
        )
    submit.grid(row=count,column=0)

    root.mainloop()


# In[ ]:




