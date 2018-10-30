
#!/usr/bin/env python

import tkinter as tk
from view.home import Home
import config

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.frames = {}
        for F in (Home,Home):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
        self.display('Home')
    
    def display(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

app = MainApp()
app.title('Keybase')
app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(file=config.root+'/keybase.png'))
app.mainloop()