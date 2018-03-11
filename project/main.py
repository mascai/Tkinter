# -*- coding: utf-8 -*-

from Tkinter import *
from multiprocessing import Process
import subprocess
import os

root = Tk()

def run_script(DT, RF, SVC, GB, KM, data, router, host, frac):
    print DT, RF, SVC, GB, KM, data, router, host, frac
    subprocess.Popen("./run.sh", shell=True)
    #subprocess.Popen("./run2.sh", shell=True)

def button_clicked():
    run_script(var_DT.get(), var_RF.get(), var_SVC.get(), var_GB.get(), var_KM.get(),
    	data.get(), router.get(), host.get(), frac.get())
def start():
	subprocess.Popen("./run2.sh", shell=True)

fields = ['Данные','Количество маршрутизаторов','Количество хостов','Распространение данных','']

for i in range(len(fields)):	
    Label(text=fields[i], relief=RIDGE, width=80).grid(row=i, column=0)

data   = Entry(root, relief=SUNKEN,width=30)
router = Entry(relief=SUNKEN,width=30)
host   = Entry(relief=SUNKEN,width=30)
frac   = Entry(relief=SUNKEN,width=30)

data.grid(row=0,column=1)
router.grid(row=1,column=1)
host.grid(row=2,column=1)	
frac.grid(row=3,column=1)

var_DT  = IntVar()
var_RF  = IntVar()
var_SVC = IntVar()
var_GB  = IntVar()	
var_KM  = IntVar()
c_DT  = Checkbutton(text="Decision Tree", relief=SUNKEN, variable=var_DT, onvalue=1, offvalue=0).grid(row=4, sticky=W)
c_RF  = Checkbutton(text="Random Forest", relief=SUNKEN, variable=var_RF, onvalue=1, offvalue=0).grid(row=4, sticky=W, padx = (140,0))
c_SVC = Checkbutton(text="SVC", relief=SUNKEN, variable=var_SVC, onvalue=1, offvalue=0).grid(row=4)
c_GB  = Checkbutton(text="Gradient Boosting", relief=SUNKEN, variable=var_GB, onvalue=1, offvalue=0).grid(row=4, sticky=W, padx= (400,0))
c_KM  = Checkbutton(text="K-means", relief=SUNKEN, variable=var_KM, onvalue=1, offvalue=0).grid(row=4, sticky=W, padx= (570,0))


button1 = Button(text='Start Mininet',fg='red',relief=SUNKEN, font='arial 14', command=button_clicked).grid(row=4, column=1)
button2 = Button(text='Start POX',fg='red',relief=SUNKEN, font='arial 14', command=start).grid(row=5, column=1)
mainloop()


#os.system("sudo mn --topo single,3 --mac --controller remote --switch ovsk")
#os.system("~/pox/pox.py forwarding.l2_learning")
#os.system("~/pox/pox.py forwarding.l2_pairs openflow.of_01 --port=6633");
#os.system("./run.sh")
