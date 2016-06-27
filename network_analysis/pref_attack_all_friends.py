'''
Created on Apr 30, 2015

@author: pekzeki
'''

from pymongo import MongoClient
import networkx as nx
from network_analysis import graph_analysis as GA

degreeness_attack_list = ['rpOyqD_893cqmDAtJLbdog',
         'lC0KGXmIhyjzghBUlVnkhQ',
         'OXWWC30x-1Ee0B6hXLLZfw',
         'TWIg1Jx2jGiC8UqaKpNorw',
         'Q9SKKZgbTMf5fXTQerFdqw']

closeness_attack_list = ['rpOyqD_893cqmDAtJLbdog',
         'lC0KGXmIhyjzghBUlVnkhQ',
         '7zpDhrRZRTGCkAh3SHbEww',
         '_A_2A-bjADJTKBoWd_B5qg',
         'TWIg1Jx2jGiC8UqaKpNorw']

betweenness_attack_list = ['rpOyqD_893cqmDAtJLbdog',
         'lC0KGXmIhyjzghBUlVnkhQ',
         '7zpDhrRZRTGCkAh3SHbEww',
         'OXWWC30x-1Ee0B6hXLLZfw',
         'TWIg1Jx2jGiC8UqaKpNorw']

def attacked_graph(attack_list):

    G = nx.Graph()
    for user in user_collection.find():
        G.add_node(user.get("_id"))
        friend_list = user.get("friends")
        for friend in friend_list:
            G.add_edge(user.get("_id"), friend)
            
    for number in attack_list:
        G.remove_node(number)
            
    return G  

client = MongoClient()
db = client.yelp
user_collection = db.user_il_filtered
review_collection = db.review_il_filtered
business_collection = db.business_il_filtered

#D = attacked_graph(degreeness_attack_list)
#C = attacked_graph(closeness_attack_list)
B = attacked_graph(betweenness_attack_list)

#GA.analyze(D, "degreeness_attack")
#GA.analyze(C, "closeness_attack")
GA.analyze(B, "betweenness_attack")
