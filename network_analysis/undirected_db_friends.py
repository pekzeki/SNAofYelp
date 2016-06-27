'''
Created on May 2, 2015

@author: pekzeki
'''

from pymongo import MongoClient
import networkx as nx
from network_analysis import graph_analysis as GA

def db_friends_graph():
    
    G = nx.Graph()
    for user in user_collection.find():
        G.add_node(user.get("_id"))
        friend_list = user.get("friends")
        for friend in friend_list:
            if user_collection.find_one({ '_id' : friend}) is not None:
                G.add_edge(user.get("_id"), friend)
                
    return G    

client = MongoClient()
db = client.yelp
user_collection = db.user_il_filtered
review_collection = db.review_il_filtered
business_collection = db.business_il_filtered

G = db_friends_graph()

GA.analyze(G, "undirected_db_friends")