#https://www.python-course.eu/tkinter_layout_management.php
#http://effbot.org/tkinterbook/grid.htm

# -*- coding: utf-8 -*-

from Tkinter import *

fields = ['Данные','Количество маршрутизаторов','Количество хостов','Распространение данных','']

for i in range(len(fields)):
	
    Label(text=fields[i], relief=RIDGE, width=80).grid(row=i, column=0)

Entry(relief=SUNKEN,width=30).grid(row=0,column=1)
Entry(relief=SUNKEN,width=30).grid(row=1,column=1)
Entry(relief=SUNKEN,width=30).grid(row=2,column=1)	
Entry(relief=SUNKEN,width=30).grid(row=3,column=1)
var_DT  = IntVar()
var_RF  = IntVar()
var_SVC = IntVar()
var_GB  = IntVar()	
var_KM  = IntVar()
c_DT  = Checkbutton(text="Decision Tree", relief=SUNKEN, variable=var_DT).grid(row=4, sticky=W)
c_RF  = Checkbutton(text="Random Forest", relief=SUNKEN, variable=var_RF).grid(row=4, sticky=W, padx = (140,0))
c_SVC = Checkbutton(text="SVC", relief=SUNKEN, variable=var_SVC).grid(row=4)
c_GB =  Checkbutton(text="Gradient Boosting", relief=SUNKEN, variable=var_GB).grid(row=4, sticky=W, padx= (400,0))
c_KM =  Checkbutton(text="K-means", relief=SUNKEN, variable=var_KM).grid(row=4, sticky=W, padx= (570,0))

button=Button(text='Start',fg='red',relief=SUNKEN, font='arial 14').grid(row=4, column=1)


mainloop()
