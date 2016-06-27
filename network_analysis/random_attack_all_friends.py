'''
Created on Apr 30, 2015

@author: pekzeki
'''

from pymongo import MongoClient
import networkx as nx
from network_analysis import graph_analysis as GA
from random import randint 

def random_attacked_graph(random_attack_list):

    G = nx.Graph()
    for user in user_collection.find():
        G.add_node(user.get("_id"))
        friend_list = user.get("friends")
        for friend in friend_list:
            G.add_edge(user.get("_id"), friend)
        
    for number in random_attack_list:
        user = user_collection.find().limit(-1).skip(number).next()
        G.remove_node(user.get("_id"))
        print user.get("_id")
            
    return G  

client = MongoClient()
db = client.yelp
user_collection = db.user_il_filtered
review_collection = db.review_il_filtered
business_collection = db.business_il_filtered

collection_length = user_collection.find().count()
random_attack_list = ([randint(0, collection_length),
         randint(0, collection_length),
         randint(0, collection_length),
         randint(0, collection_length),
         randint(0, collection_length)])

R = random_attacked_graph(random_attack_list)

GA.analyze(R, "random_attack-3")
