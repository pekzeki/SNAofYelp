'''
Created on May 2, 2015

@author: pekzeki
'''

from pymongo import MongoClient
import networkx as nx
from networkx.algorithms import bipartite
from network_analysis import graph_analysis as GA

def biparted_graph():
    
    B = nx.Graph()
    for user in user_collection.find():
        B.add_node(user.get("_id"), user=True, bipartite=0)
    for business in business_collection.find():
        B.add_node(business.get("_id"), business=True, bipartite=1)
    for review in review_collection.find():
        if B.has_edge(review.get("user_id"), review.get("business_id")):
            # we added this one before, just increase the weight by one
            B[review.get("user_id")][review.get("business_id")]['weight'] += 1
        else:
            # new edge. add with weight=1
            B.add_edge(review.get("user_id"), review.get("business_id"), weight=1)
    
    return B
    
def folded_graph(B):
    
    bottom_nodes, top_nodes = bipartite.sets(B)
    F = bipartite.projected_graph(B, top_nodes)
    
    return F

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

B = biparted_graph()
F = folded_graph(B)
G = db_friends_graph()

I = G.copy()
I.remove_nodes_from(n for n in G if n not in F)

GA.analyze(I, "intersection")