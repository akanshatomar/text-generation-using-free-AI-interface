# import json

# check ="a"
# with open('sample.json', 'r') as file:
#     data = json.load(file)
# if check in data:
#     print(True)
# else:
#     print(False)
import json
from xml.dom.minidom import Document

def check_value(data, val):
    #return any(player['steam64']==val for player in data['players'])

 with open('sample.json', 'r') as f_in:
    data = json.load(f_in)

print(check_value(Document, 76561198046619692))
