from tkinter import *


class CheckBar(Frame):
    def __init__(self, window, item=[]):
        Frame.__init__(self,)
        self.vars = []
        self.count = 1
        for i in item:
            var = IntVar()
            chk = Checkbutton(window, text=i, variable=var)
            chk.grid(column=0, row=self.count)
            self.vars.append(var)
            self.count += 1

    def state(self):
        return map((lambda var: var.get()), self.vars)
