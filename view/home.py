import tkinter as tk 
import controller as  ctrl
from tkinter import ttk

class Home(tk.Frame):

    def __init__(self, parent, controller):
        # Main Frame
        tk.Frame.__init__(self, parent, )
        self.controller = controller
        self.controller.geometry("600x540")
        self.controller.grid_columnconfigure(0, weight=1)
        self.controller.grid_rowconfigure(0, weight=1)
        self.controller.resizable(False, False) 
        
        # ===========================  Search container  =======================
        search_container = tk.Frame(self.controller)
        search_container.grid(row=0, sticky='nwe', padx=10, pady=10)

        self.squery = tk.StringVar()
        ent01 = tk.Entry(search_container, width=60, textvariable=self.squery)
        ent01.grid(row=0)
        btn01 = tk.Button(search_container, text="Search", width=6, command=lambda:ctrl.listSearch(t02, self.squery.get()))
        btn01.grid(row=0, column=9, padx=(15, 0))

        # =========================== Result Container =======================
        result = tk.LabelFrame(self.controller, relief='groove', text="Result")
        result.place(x=310, y=60, width=280, height=300)

        # Inner frame
        cInnerFrame = tk.Frame(result,padx=10)
        cInnerFrame.place(x=0, y=22, width=270, height=250)
        sb02 = tk.Scrollbar(cInnerFrame, orient='vertical')
        sb02.pack(side='right', fill='y', expand=1)

        t01 = tk.Text(cInnerFrame, padx=10, pady=5) 
        t01.pack(side='left', fill='both', expand=1)

        t01.config(yscrollcommand=sb02.set)
        sb02.config(command=t01.yview)               
       
        # ============================ Avalable connections Container ==============================
        related = tk.LabelFrame(self.controller, relief='groove', text="Available connections")
        related.place(x=10, y=60, width=280, height=300)

        innerFrame =  tk.Frame(related, padx=10)
        innerFrame.place(x=0, y=22, width=270, height=250)

        t02 = tk.Listbox(innerFrame)
        t02.pack(side='left', fill='both', expand=1)
        t02.bind('<<ListboxSelect>>', lambda event, output=t01:ctrl.onSelect(event,output))

        sb01 =  tk.Scrollbar(innerFrame, orient='vertical')
        t02.config(yscrollcommand=sb01.set) 
        sb01.config(command=t02.yview)
        sb01.pack(side='right', fill='y')

        # ================================= Tab Container ==========================================
        tabcontainer = ttk.Notebook(self.controller)
        tabcontainer.place(x=10, y=380, width=580, height=140)



        # ************* New form Container *************** 
        add = tk.Frame(tabcontainer, padx=10, pady=10)
        add.place(x=10, y=370, width=580, height=130)

        tabcontainer.add(add, text='Add')   


        # Create Two column layout
        col_l_01 = tk.Frame(add,padx=25 )
        col_l_01.pack(side='left', anchor='n') 

        col_r_01 = tk.Frame(add, padx=25)
        col_r_01.pack(side='left',anchor='n')
        

        alb01 = tk.Label(col_l_01, text='Name : ')
        alb01.grid(row=0, column=0)
        self.conn = tk.StringVar()
        aety01 = tk.Entry(col_l_01, textvariable=self.conn)
        aety01.grid(row=0, column=1)

        alb02 = tk.Label(col_r_01, text='Username : ')
        alb02.grid(row=0, column=2)
        self.user = tk.StringVar()
        aety02 = tk.Entry(col_r_01, textvariable=self.user)
        aety02.grid(row=0, column=3)

        alb03 = tk.Label(col_l_01, text='Type : ')
        alb03.grid(row=1, sticky='w')
        self.type = tk.StringVar()
        aety03 = tk.Entry(col_l_01, textvariable=self.type)
        aety03.grid(row=1, column=1)

        alb04 = tk.Label(col_r_01, text='Password : ')
        alb04.grid(row=1, column=2)
        self.password = tk.StringVar()
        aety04 = tk.Entry(col_r_01, textvariable=self.password)
        aety04.grid(row=1, column=3)

        alb05 = tk.Label(col_l_01, text='URL : ')
        alb05.grid(row=2, column=0, sticky='w')
        self.url = tk.StringVar()
        aety05 = tk.Entry(col_l_01, textvariable=self.url)
        aety05.grid(row=2, column=1)
        add_elems = {
                   'name' : self.conn,
                    'type' : self.type,
                    'user' : self.user,
                    'password' : self.password,
                    'url' : self.url
               }
        btn02 = tk.Button(add, text='Add', command=lambda:ctrl.add_data(
               add_elems, 
                t02              
                ))
        btn02.place(x=480, y=70)
        btn03 = tk.Button(add, text='Cancel', command=lambda:ctrl.clearField(add_elems))
        btn03.place(x=400, y=70)

        # **************** Update form Container ****************

        update = tk.Frame(tabcontainer, padx=10, pady=10)
        update.place(x=10, y=370, width=580, height=130)

        tabcontainer.add(update, text='Update')   


        # Create Two column layout
        col_l_02 = tk.Frame(update,padx=25 )
        col_l_02.pack(side='left', anchor='n') 

        col_r_02 = tk.Frame(update, padx=25)
        col_r_02.pack(side='left',anchor='n')
        
        alb11 = tk.Label(col_l_02, text='Id : ')
        alb11.grid(row=0, column=0)
        self.id = tk.StringVar()
        aety11 = tk.Entry(col_l_02, textvariable=self.id)
        aety11.grid(row=0, column=1)

        alb06 = tk.Label(col_l_02, text='Name : ')
        alb06.grid(row=1, column=0)
        self.conn01 = tk.StringVar()
        aety06 = tk.Entry(col_l_02, textvariable=self.conn01)
        aety06.grid(row=1, column=1)

        alb08 = tk.Label(col_l_02, text='Type : ')
        alb08.grid(row=2, column=0, sticky='w')
        self.type01 = tk.StringVar()
        aety08 = tk.Entry(col_l_02, textvariable=self.type01)
        aety08.grid(row=2, column=1)

        alb07 = tk.Label(col_r_02, text='Username : ')
        alb07.grid(row=0, column=0)
        self.user01 = tk.StringVar()
        aety07 = tk.Entry(col_r_02, textvariable=self.user01)
        aety07.grid(row=0, column=1)


        alb09 = tk.Label(col_r_02, text='Password : ')
        alb09.grid(row=1, column=0)
        self.password01 = tk.StringVar()
        aety09 = tk.Entry(col_r_02, textvariable=self.password01)
        aety09.grid(row=1, column=1)

        alb10 = tk.Label(col_r_02, text='URL : ')
        alb10.grid(row=2, column=0, sticky='w')
        self.url01 = tk.StringVar()
        aety10 = tk.Entry(col_r_02, textvariable=self.url01)
        aety10.grid(row=2, column=1)
        update_elems = {
                    'name' : self.conn01,
                    'type' : self.type01,
                    'user' : self.user01,
                    'password' : self.password01,
                    'url' : self.url01,
                    'id' : self.id
               }
        btn04 = tk.Button(update, text='Update', command=lambda:ctrl.update_data(
               update_elems,                              
                ))
        btn04.place(x=480, y=70)
        btn05 = tk.Button(update, text='Cancel', command=lambda:ctrl.clearField(update_elems))
        btn05.place(x=400, y=70)
        

    
        # Adding connection to listbox window onload
        ctrl.listInsert(t02)
        # Fill data to fields automatically
        fieldList = {'name':aety06, 'type':aety08, 'username':aety07, 'password':aety09, 'url':aety10 }
        aety11.bind('<FocusOut>', lambda event, fields=fieldList :ctrl.entryInsert(event, fields))
        


        
