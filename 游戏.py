#! /usr/bin/env python3
# -*- coding:UTF-8 -*-
from tkinter import *
from tkinter.messagebox import *
from winsound import *
import getpass
import os
import sys
import pickle
import _thread
import time
from win32api import *
from win32con import *

with open(r'd:\anaconda\data.pkl', 'rb') as f:
    data = pickle.load(f)
'''if GetSystemMetrics(0) != 1536 or GetSystemMetrics(1) != 864:
    showerror('Error',
              'The resolution is {}*{}, This game can only run in 1536*864!'.format(GetSystemMetrics(0),
                                                                                    GetSystemMetrics(1)))
    sys.exit()'''

timed = -1
win = Tk()
win.title('gme')
win.geometry('100x100')
win.state('zoomed')



def callback():
    MessageBeep(0)
    if askyesno('Sure?', 'Are you sure you want to quit the game?'):
        win.destroy()
    else:
        win.state("zoomed")


win.protocol("WM_DELETE_WINDOW", callback)
# justify option can help us change the place of the text
# Left, Right, Centre.  (W, E)
font = ("微软雅黑", 11)
Label(win, width=170, bg='gold', font=font, text=f"Welcome, {getpass.getuser()}!\nEnjoy this game!").\
    grid(row=0, columnspan=54)
moneybar = Label(win, width=85, height=2, bg='#bbbbbb', font=font, text='You purchase: $x')
moneybar.grid(row=1, column=0, columnspan=27)
timebar = Label(win, width=85, height=2, bg='#bbb0bb', font=font, text='You played 0 secs')
timebar.grid(row=1, column=27, columnspan=27)

# Message system
messages = Label(win, width=170, bg='yellow', font=font, text='No messages...')
messages.grid(row=2, columnspan=54)
# end
if data['lastday'] != int(time.strftime("%d", time.localtime())):
    data['money'] += 500
    data['lastday'] = int(time.strftime("%d", time.localtime()))
    messages['text'] = 'Coin +500'


def do_things():
    moneybar['text'] = f'Your Purchase: {"$%.2f" % data["money"]}'
    timebar['text'] = f'You Played {timed} secs'


def thread():
    _thread.start_new_thread(do_things, ())
    win.after(1, thread)


def t_time():
    global timed
    timed += 1
    if timed == 300 or timed == 600 or timed == 1800 or timed == 3600:
        if askyesno('Warning', 'You played {} minutes. Do you want to quit game now?'.format(int(timed/60)),
                    icon=WARNING):
            win.state("zoomed")
            sys.exit()
    if timed == 7200:
        showwarning('Warning', 'You played 2 hour. You must rest now.')
        sys.exit()
    win.after(1000, time)


thread()
t_time()
win.mainloop()
del data
with open(r'd:\anaconda\data.pkl', 'rb') as f:
    data = pickle.load(f)
with open(r'd:\anaconda\data.pkl', 'wb') as f:
    pickle.dump(data, f)