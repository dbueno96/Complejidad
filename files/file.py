import os 
import json
from utils.constants import *


class FileHandler(): 
    def __init__(self,topics, pages, mins, maxs, readers): 
        self.topics=topics
        self.pages=pages
        self.mins=mins
        self.maxs=maxs
        self.readers=readers

        print('FILE DATA')
        print(self.topics)
        print(self.pages)
        print(self.mins)
        print(self.maxs)
        print(self.readers)


    def update_data(self):
        pass

    def print_data(self):
        print(json.dumps(self.data, indent=4))


    def create_dzn_file(self):
        with open(DATA_NAME, 'w') as topics: 
            topics.write('{}{}{}'.format(PAGES,EQUAL,str(self.pages)))
            topics.write(END_SENTENCE)
            topics.write(NEW_LINE)

            topics.write('{}{}{}'.format(TOPIC,EQUAL,KEY1))
            for val in self.topics: 
                topics.write('{}{}'.format(val,COMMA))
            topics.write(KEY2)
            topics.write(END_SENTENCE)
            topics.write(NEW_LINE)
    
            topics.write('{}{}{}'.format(MINS,EQUAL,BRACKET1))
            for val in self.mins: 
                topics.write('{}{}'.format(val,COMMA))
            topics.write(BRACKET2)
            topics.write(END_SENTENCE)
            topics.write(NEW_LINE)
            
            topics.write('{}{}{}'.format(MAXS,EQUAL,BRACKET1))
            for val in self.maxs:
                topics.write('{}{}'.format(val,COMMA))
            topics.write(BRACKET2)
            topics.write(END_SENTENCE)
            topics.write(NEW_LINE)

            
            topics.write('{}{}{}'.format(READERS,EQUAL,BRACKET1))
            for val in self.readers: 
                topics.write('{}{}'.format(val,COMMA))
            topics.write(BRACKET2)
            topics.write(END_SENTENCE)   
        