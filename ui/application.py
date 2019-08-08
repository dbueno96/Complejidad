import os
import json
import tkinter as tk
from utils.constants import *
from processor.processor import Processor

class Application(tk.Frame): 
    def __init__(self, master=None): 
        super().__init__(master)
        self.master = master
        self.master.title(CONST_APP_TITLE)
        self.master.geometry('600x400+400+100')
        self.master.resizable(0,0)
        self.config(width=500, height=500)
        self.place(x=50, y=0)
        self.application_widgets()
        self.processor = Processor()
    
    def application_widgets(self): 
        self.create_frames()
        self.create_buttons()
        self.create_labels()
        self.create_entrys()

    
    def create_frames(self): 
        self.pages_frame = tk.Frame(self,width=500 , height=50)
        self.pages_frame.place(x=0, y=40)

        
        self.topics_frame= tk.Frame(self, width=500, height= 250)
        self.topics_frame.place(x=0, y=100)
        
    
    def create_labels(self): 
        tk.Label(self.pages_frame, text=CONST_TOTAL_PAGES).place(x=100, y=10)
        
        tk.Label(self.topics_frame,width=10,height= 2, justify='center', text=CONST_TOPIC_NAME).place(x=10, y=40)
        tk.Label(self.topics_frame, height= 2,justify='center',text=CONST_MIN_PAGES).place(x=113, y=40)
        tk.Label(self.topics_frame,height= 2,justify='center', text=CONST_MAX_PAGES).place(x=230, y=40)
        tk.Label(self.topics_frame,height= 2,justify='center',text=CONST_READERS).place(x=350, y=40)

    def create_entrys(self):
        self.max_pages = tk.Entry(self.pages_frame)
        self.max_pages.place(x= 300, y=10)

        self.topic_name_entry= tk.Entry(self.topics_frame)
        self.topic_name_entry.config(width=10, justify='center')
        self.topic_name_entry.place(x=10,y= 100)

        self.topic_min_entry=tk.Entry(self.topics_frame)
        self.topic_min_entry.config(width=10, justify='center')
        self.topic_min_entry.place(x=130, y=100 )

        self.topic_max_entry= tk.Entry(self.topics_frame)
        self.topic_max_entry.config(width=10, justify='center')
        self.topic_max_entry.place(x=245, y=100)

        self.topic_readers_entry= tk.Entry(self.topics_frame)
        self.topic_readers_entry.config (width=10, justify='center')
        self.topic_readers_entry.place(x=365, y=100)

    def create_buttons(self): 
        self.solve_button = tk.Button(self)
        self.solve_button.config(width=10, height=1)
        self.solve_button['text'] = CONST_SOLVE
        self.solve_button['command'] = self.create_data
        self.solve_button.place(x=200, y=325)  
        #Botón para agregar nuevo tema
        self.add_topic_button= tk.Button(self.topics_frame)
        self.add_topic_button.config(width=10, height=1)
        self.add_topic_button.place(x=270, y=180)
        self.add_topic_button['text'] = CONST_ADD_TOPIC
        self.add_topic_button['command']= self.add_topic

        ##Botón para consultar temas guardados
        self.check_topics_button = tk.Button(self.topics_frame)
        self.check_topics_button.config(width=10, height=1)
        self.check_topics_button.place(x=110, y=180)
        self.check_topics_button['text']= CONST_CHECK_TOPICS
        self.check_topics_button['command']= self.create_topics_window
        

    def create_topics_window(self):
        self.top = tk.Toplevel(self)
        self.top.geometry('550x400+400+100')
        self.top.title(TEMAS)
        scroll= tk.Scrollbar(self.top)
        c = tk.Canvas(self.top ,  yscrollcommand=scroll.set)
        
        scroll.config(command=c.yview)
        scroll.pack(side='right', fill ='y')
        
        top_frame= tk.Frame(c)
        top_frame.config(width=500)
        c.pack(side='left', fill='both', expand=True) 
        c.create_window(0,0, window=top_frame, anchor='nw')
        # texto =tk.Label(top_frame, wraplength=380)
        # texto.pack()
        self.top.update()
        c.config(scrollregion=c.bbox('all'))

        
        tk.Label(top_frame, text= CONST_TOPIC_NAME).grid(padx= (10,10), pady=(5,30),row=0, column=0)
        tk.Label(top_frame, text= CONST_MIN_PAGES).grid(padx= (10,10), pady=(5,30), row=0,column=1)
        tk.Label(top_frame, text= CONST_MAX_PAGES).grid(padx= (10,10), pady=(5,30),row=0,column=2)
        tk.Label(top_frame, text= CONST_READERS).grid(padx= (10,10), pady=(5,30),row=0,column=3)
        y=1
        for key in self.processor.info: 
            tk.Label(top_frame, text= key).grid(padx= (10,10), pady=(5,30),row=y, column=0)
            tk.Label(top_frame, text= self.processor.info[key][MIN_KEY]).grid(padx= (10,10), pady=(5,30), row=y,column=1)
            tk.Label(top_frame, text= self.processor.info[key][MAX_KEY]).grid(padx= (10,10), pady=(5,30),row=y,column=2)
            tk.Label(top_frame, text= self.processor.info[key][READERS_KEY]).grid(padx= (10,10), pady=(5,30),row=y,column=3)
            y=y+1

    def valid_entrys(self):
        # print (self.topic_name_entry.get())
        # print (self.topic_min_entry.get())
        # print( self.topic_max_entry.get())
        # print (self.topic_readers_entry.get())
        if  self.topic_name_entry.get() =='':
            True
        
        return False
        
    def add_topic(self): 
        dic = { READERS_KEY: int(self.topic_readers_entry.get()),            
                MAX_KEY : int(self.topic_max_entry.get()),
                MIN_KEY : int(self.topic_min_entry.get()),
        }
        self.processor.add_topic ( {self.topic_name_entry.get() : dic   } )
        self.topic_name_entry.delete(0, 100)
        self.topic_max_entry.delete(0, 100)
        self.topic_min_entry.delete(0, 100)
        self.topic_readers_entry.delete(0, 100)
        self.topic_name_entry.focus()
        self.max_pages.config(state='disabled')
        self.solve_button.config(state='normal')

    def show_solution(self):
        top = tk.Toplevel(self)
        top.geometry('500x400+400+100')
        top.title(RESULT_TITLE)
        scroll= tk.Scrollbar(top)
        c = tk.Canvas(top ,  yscrollcommand=scroll.set)
        
        scroll.config(command=c.yview)
        scroll.pack(side='right', fill ='y')
        
        top_frame= tk.Frame(c)
        top_frame.config(width=500)
        c.pack(side='left', fill='both', expand=True) 
        c.create_window(0,0, window=top_frame, anchor='nw')
        top.update()
        c.config(scrollregion=c.bbox('all'))
        
        response = self.run_data()
        self.processor= Processor()

        tk.Label(top_frame, text= CONST_TOPIC_NAME).grid(padx= (70,80), pady=(5,30),row=0, column=0)
        tk.Label(top_frame, text= CONST_RESULT_PAGES).grid(padx= (70,80), pady=(5,30), row=0,column=1)
        
        for i in range(len(response[TOPICS_RESPONSE])): 
            if response[INCLUDE_RESPONSE][i]=='true': 
                tk.Label(top_frame, text= response[TOPICS_RESPONSE][i]).grid(padx= (70,80), pady=(5,30), row=i+1,column=0)
                tk.Label(top_frame, text= response[PAGES_RESPONSE][i]).grid(padx= (70,80), pady=(5,30), row=i+1,column=1)

        tk.Label(top_frame, text= CONST_READERS).grid(padx= (70,80), pady=(5,30), row=len(response[TOPICS_RESPONSE])+1,column=0)
        tk.Label(top_frame, text= response[READERS_RESPONSE]).grid(padx= (70,80), pady=(5,30), row=len(response[TOPICS_RESPONSE])+1,column=1)

    def run_data(self):
        return self.processor.run_data()
        

    def create_data(self): 
        print('creating datazinc file..')
        self.topic_name_entry.delete(0, 100)
        self.topic_max_entry.delete(0, 100)
        self.topic_min_entry.delete(0, 100)
        self.topic_readers_entry.delete(0, 100)
        self.max_pages.config(state='normal')
        self.max_pages.focus()
        self.processor.pages=int(self.max_pages.get())
        self.max_pages.delete(0,100)
       
        self.processor.create_dzn()
        self.show_solution()
        print('Done!')
        

    