#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import datetime

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Scrivi il Lotto qui")

        button = Tkinter.Button(self,text=u"CALCOLA",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        giorno_dell_anno = datetime.date.today().strftime("%j")
        anno_part_A = datetime.date.today().strftime("%Y")
        anno_part_B = len(anno_part_A)
        anno_part_C = (anno_part_A[anno_part_B -2]+anno_part_A[anno_part_B -1])
        lotto = (giorno_dell_anno + anno_part_C)
        self.labelVariable.set(u"Lotto del giorno: " + lotto)

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        lotto = self.entryVariable.get()
        A = lotto[0]
        B = lotto[1]
        C = lotto[2]
        D = lotto[3]
        E = lotto[4]
        lota = (A + B + C)
        lotaint= int(lota)
        lotb = ("20" + D + E)
        lotbint= int(lotb)
        start_date = ("01/01/" + D + E)
        date_1 = datetime.datetime.strptime(start_date, "%d/%m/%y")
        end_date = date_1 + datetime.timedelta(days=lotaint -1)
        self.labelVariable.set("il lotto " + self.entryVariable.get() + " risale a: " + end_date.strftime('%Y-%m-%d'))
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        self.labelVariable.set( self.entryVariable.get()+" (Inserire il lotto da calcolare)" )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Lotto')
    app.mainloop()