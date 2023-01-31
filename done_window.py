#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk

ws = Tk()
ws.title('Prikaway Pvt. Ltd.')
ws.geometry('200x100')
ws.config(bg='#345')
lbl=tk.Label(ws, text="Done",font=('calibre',10, 'bold'))
lbl.pack(padx=10,pady=10)
ws.mainloop()

