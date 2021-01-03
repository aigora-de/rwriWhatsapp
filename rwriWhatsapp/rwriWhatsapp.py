import re
import networkx as nx
import pandas as pd


class WhatsAppParser:

    @staticmethod
    def run():
        print("Hello World...")


regex = re.compile(r'(\[\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2}\]) (.*:) (.*$)')
regex2 = re.compile(r'')
g = nx.Graph()
nodes = []
links = []
df = pd.DataFrame()

with open('../data/_chat.txt') as f:
    for line in f:
        #match = re.search(regex, line)
        #if match:
        result = re.search(regex, line)
        if result:
            dateTime = result.group(1)
            oP = result.group(2)
            msg = result.group(3)
            df.append([dateTime, oP, msg])
            #print('{}, {}, {}'.format(result.group(1), result.group(2), result.group(3)))
            #print('----------------------------------------------')
        elif len(line.strip()) == 0:
            print('zero!!!!!!!!!!!!!')
        else:
            df.append([dateTime, oP, line])
            #print('false {}'.format(line))
    print('Finished')