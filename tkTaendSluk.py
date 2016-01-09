#!/usr/bin/python

'''
PHILIPS HUE SIMPLE ON AND OFF PANEL

idea: turn all lamps on or off
version: 1.0
by: Per Thykjaer Jensen
url: https://github.com/asathoor
license: GPLv3
licence text: http://www.gnu.org/licenses/gpl.txt
'''

from Tkinter import *
import requests
import json

''' the main class '''
class Lamper:

    ''' AUTORUN METHOD '''
    def __init__(self,master):

        frame = Frame(master)
        frame.pack()

        ''' label '''
        self.label = Label(frame,text="Hue: on / off panel")
        self.label.pack()
        
        ''' turn off light '''
        self.button = Button(frame,
            text="Off",
            fg="red",
            command=self.off)

        self.button.pack(side=RIGHT)

        ''' turn on light '''
        self.button = Button(frame,
            text="On",
            fg="blue",
            command=self.onn)

        self.button.pack(side=RIGHT)

    ''' THE ON AND OF METHODS '''

    ''' turn lamps off '''
    def off(self):
        print "Lamps = OFF"
        try:
            self.taend = json.dumps({"on":False})
            self.r = requests.put("http://192.168.0.xxx/api/xxxxxxxxxxxxxxxxxxxxxxxxxxxxx/groups/0/action", data=self.taend)

        except ValueError:
            print "some error happened"
            print self.r

    ''' turn lamps on '''
    def onn(self):
        print "Lamps = ON"
        try:
            self.taend = json.dumps({"on":True})
            self.r = requests.put("http://192.168.0.xxx/api/xxxxxxxxxxxxxxxxxxxxxxxxxxxxx/groups/0/action", data=self.taend)

        except ValueError:
            print "some error happened"
            print self.r

''' tk loop '''
root = Tk()
app = Lamper(root)
root.mainloop()
