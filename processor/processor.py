import os
import json
from utils.constants import *
from files.file import FileHandler

class Processor(): 
    def __init__(self):
        self.info={}
        self.pages = 0
        self.topics=[]
        self.min_pages=[]
        self.max_pages=[]
        self.readers=[]
        
        

    

    def add_topic(self,topic): 
        self.info.update(topic)
        print(json.dumps(self.info, indent=4))

        for key in self.info: 
            print(self.info[key][MAX_KEY])

    def process_info(self): 
        for key in self.info: 
            self.topics.append(key)
            self.min_pages.append(self.info[key][MIN_KEY])
            self.max_pages.append(self.info[key][MAX_KEY])
            self.readers.append(self.info[key][READERS_KEY])
        print('PROCESSED INFO: ')
        print(self.pages)
        print(self.topics)
        print(self.min_pages)
        print(self.max_pages)
        print(self.readers)

    def create_dzn(self): 
        
        self.process_info()
        self.file = FileHandler(self.topics, self.pages, self.min_pages, self.max_pages, self.readers)
        return self.file.create_dzn_file()

    def run_data(self):
       # print(command)
        return self.process_response()
    def create_response_dict(self, data):
        pass

    
    def process_response(self):
        command = str(os.popen(COMMAND).read())
        command = command.replace('=','').replace('-','').replace('\n','').replace('[','').replace(']','')
        print(command)
        tops, pags,includes, readers=command.split('_')[1:]
        tops=tops.replace('{','')
        tops=tops.replace('}', '')
        
        tops= tops.split(' : ')[1].split(', ')
        pags= pags.split(' : ')[1].split(', ')
        includes= includes.split(' : ')[1].split(', ')
        readers = readers.split(' : ')[1].split(', ')
        
        [value.capitalize() for value in includes]

        print(tops)
        print(pags)
        print(includes)
        print(readers)

        response = {TOPICS_RESPONSE : tops, 
                    PAGES_RESPONSE: pags, 
                    INCLUDE_RESPONSE: includes, 
                    READERS_RESPONSE: readers}
        return response