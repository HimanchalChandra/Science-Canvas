#Parsing & Manipulation of CSV & JSON
#STRUCTURE 1
import pandas as pd
from collections import OrderedDict
import json    

#loading and defining the datatypes for some columns
df = pd.read_csv('players_10k.csv', dtype={"player_fifa_api_id" : str})


results = []#This list will be used to in json.dump function to convert to proper json 

#Iterating through the dataframe in groups made on basis of player_fifa_api_id
for (player_fifa_api_id), bag in df.groupby(["player_fifa_api_id"],sort = False):   
    contents_df = bag.drop(['player_fifa_api_id','id','player_api_id'], axis=1)
    contents_df1 = bag.drop(['player_fifa_api_id','id','player_api_id','date'], axis=1)
    player_record = []#This list wil contain attributes of players date wise
    
    #Iterating through the rows in each group to get data for various dates
    for index,row in contents_df.iterrows():
        attributes = [OrderedDict(row.drop('date'))]
        player_record.append(OrderedDict([("date",row['date'] ),("attributes",attributes)])) 
        
    results.append(OrderedDict([("player",player_fifa_api_id ),("player_record", player_record)]))#appending key value pairs in the list

print (json.dumps(results, indent=4))#printing the json data
with open('JSON_structure1.json', 'w') as outfile:#writing the file to system
    outfile.write(json.dumps(results, indent=4))
