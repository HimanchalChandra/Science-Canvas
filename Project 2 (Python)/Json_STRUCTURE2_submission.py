#Parsing & Manipulation of CSV & JSON
#STRUCTURE 2
import pandas as pd 
from collections import OrderedDict
import json    

#Loading the data and defining the datatype of few columns
df = pd.read_csv('players_10k.csv', dtype={"player_fifa_api_id" : str})

results = []#This list will be used to in json.dump function to convert to proper json

df1 = df.drop(['player_fifa_api_id','id','player_api_id','date'], axis=1)

g = list(df1.columns.values)#Listing all the attributes

#Iterating through the dataframe in groups made on basis of player_fifa_api_id
for (player_fifa_api_id), bag in df.groupby(["player_fifa_api_id"],sort = False):
    contents_df = bag.drop(['player_fifa_api_id','id','player_api_id'], axis=1)
    contents_df1 = bag.drop(['player_fifa_api_id','id','player_api_id','date'], axis=1)
    player_record = []#This list will contain attributes of players for all dates 
    attributes = []#This list will contain attributes of players 
    max1 = max(bag['date'])#calculating latest date
    min1 = min(bag['date'])#calculating oldest date
    attr = []#this list will have lists of different attributes like dribbling, crossing
    for j in range (0,38):#appending 38 empty lists to attr......these empty lists will contain values of attributes of different dates
        attr.append([])

    #filling the above added empty lists with attributes collected on different dates
    for index,row in contents_df.iterrows():
       for j in range (0,38):
        l=row[g[j]]
        attr[j].append(l)
   
    #appending key value pairs to attributes list eg. key = heading_accuracy, value=[44,45,46] 
    for u in range (0,38):
        attributes.append(OrderedDict([(g[u],attr[u])]))  
         
    player_record.append(OrderedDict([("date_recorded_min",min1 ),("date_recorded_max",max1 ),("attributes",attributes)]))#appending key value pairs to player_record list 
    results.append(OrderedDict([("player",player_fifa_api_id ),("player_record", player_record)]))#appending key value pairs in the list

print (json.dumps(results, indent=4))#printing the json data
with open('JSON_structure2.json', 'w') as outfile:#writing the file to system
    outfile.write(json.dumps(results, indent=3))