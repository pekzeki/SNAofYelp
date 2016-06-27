'''
Created on Apr 26, 2015

@author: Salih Zeki Irkdas
'''

from operator import itemgetter

import networkx as nx
import pylab as plt
import os
import shutil

'''
Prints the number of nodes and edges in the given graph.
'''
def number_of_nodes_and_edges(G, file_name):
    file_name.write("Number of Nodes: " + str(G.number_of_nodes()) + "\n")
    file_name.write("Number of Edges: " + str(G.number_of_edges()) + "\n")
    
'''
Prints the degree distribution and log-log plot of the given graph.
'''
def degree_distribution(G, folder_name):
    values = sorted(G.degree().values())
    hist = [values.count(x) for x in values]
    
    plt.figure()
    plt.grid()
    plt.plot(values, hist, "bo-")
    plt.legend(["degree"])
    plt.xlabel("Degree")
    plt.ylabel("Nodes")
    plt.title("Degree Distribution")
    #plt.xlim([0, 2*10**2])
    plt.savefig(folder_name + "/degree_dist.pdf")
    plt.close()
    
    plt.figure()
    plt.grid()
    plt.loglog(values, hist, "bo-")
    plt.legend(["degree"])
    plt.xlabel("Degree")
    plt.ylabel("Nodes")
    plt.title("LogLog Degree Distribution")
    #plt.xlim([0, 2*10**2])
    plt.savefig(folder_name + "/loglog_degree_dist.pdf")
    plt.close()
    
'''
Prints the average clustering coefficient of the given graph.
'''
def average_clustering_coefficient(G, file_name):
    clustering_coefficient = nx.clustering(G)
    file_name.write("Average Clustering Coefficient: " + str(sum(clustering_coefficient.values())/len(clustering_coefficient)) + "\n")
    
'''
Prints the number of triangles in the given graph.
'''
def number_of_triangles(G, file_name):
    triangles = nx.triangles(G)
    file_name.write("Number of Triangles: " + str(sum(triangles.values())/3) + "\n")
    
'''
Prints the diameter of the given graph.
'''
def diameter(connected_component_graphs, file_name):       
    max_diameter = 0
    for connected_component in connected_component_graphs:
        diameter  = nx.diameter(connected_component)
        if max_diameter < diameter:
            max_diameter = diameter
    file_name.write("Diameter: " + str(max_diameter) + "\n")
        
'''
Prints the number of connected components in the given graph.
'''
def number_of_connected_components(connected_component_graphs, file_name):        
    file_name.write("Number of Connected Components: " + str(len(connected_component_graphs)) + "\n")
    
'''
Prints the number of nodes/edges/average_path_length of the largest connected components in the given graph.
'''
def largest_connected_component(connected_component_graphs, file_name):        
    
    largest_connected_component = sorted(connected_component_graphs, key=len, reverse=True)[0]
    file_name.write("Number of Nodes (Largest Connected Component): " + str(largest_connected_component.number_of_nodes()) + "\n")
    file_name.write("Number of Edges (Largest Connected Component): " + str(largest_connected_component.number_of_edges()) + "\n")
    file_name.write("Average Path Length (Largest Connected Component): " + str(nx.average_shortest_path_length(largest_connected_component)) + "\n")

'''
Prints the ratio of nodes/edges/average_path_length of the 2nd largest connected components 
with respect to 1st largest connected components in the given graph.
'''
def second_largest_connected_component(connected_component_graphs, file_name):        
    
    _1st_largest_connected_component = sorted(connected_component_graphs, key=len, reverse=True)[0]
    _2nd_largest_connected_component = sorted(connected_component_graphs, key=len, reverse=True)[1]
    
    _1st_nodes = float(_1st_largest_connected_component.number_of_nodes())
    _1st_edges = float(_1st_largest_connected_component.number_of_edges())
    _2nd_nodes = float(_2nd_largest_connected_component.number_of_nodes())
    _2nd_edges = float(_2nd_largest_connected_component.number_of_edges())
    
    file_name.write("Node Ratio (2nd Largest Connected Component): " + str(_2nd_nodes/_1st_nodes) + "\n")
    file_name.write("Edge Ratio (2nd Largest Connected Component): " + str(_2nd_edges/_1st_edges) + "\n")
    
'''
Prints the degree, closeness, betweenness centrality measures features of the
top-10 scored nodes in the given graph.
'''
def special_features(G, file_name):        
    
    degree = nx.degree_centrality(G)
    degree_sorted = sorted(degree.items(), key = itemgetter(1), reverse=True)
    file_name.write("Degree Centrality: " + str(degree_sorted[:10]) + "\n")
    
    closeness = nx.closeness_centrality(G)
    closeness_sorted = sorted(closeness.items(), key = itemgetter(1), reverse=True)
    file_name.write("Closeness Centrality: " + str(closeness_sorted[:10]) + "\n")
    
    betweenness = nx.betweenness_centrality(G)
    betweenness_sorted = sorted(betweenness.items(), key = itemgetter(1), reverse=True)
    file_name.write("Betweenness Centrality: " + str(betweenness_sorted[:10]) + "\n")

'''
Prints the nodes has no adjacent(neighbor) in the given graph.
'''
def no_adjacents(G, file_name):
    alone_node_count = 0
    for node in G.nodes():
        if nx.degree(G, node) == 0:
            alone_node_count += 1
    file_name.write("Number of Alone Nodes: " + str(alone_node_count) + "\n")
    
def analyze(G, folder_name):
    
    if os.path.exists(folder_name): 
        shutil.rmtree(folder_name) 
    
    os.makedirs(folder_name)
    file_name = open(folder_name+'/results.txt','w')
    
    number_of_nodes_and_edges(G, file_name)
    degree_distribution(G, folder_name)
    average_clustering_coefficient(G, file_name)
    number_of_triangles(G, file_name)
    no_adjacents(G, file_name)
    
    connected_component_graphs = list(nx.connected_component_subgraphs(G))
    number_of_connected_components(connected_component_graphs, file_name)
    largest_connected_component(connected_component_graphs, file_name)
    second_largest_connected_component(connected_component_graphs, file_name)
    diameter(connected_component_graphs, file_name)
    special_features(G, file_name)
    
    file_name.close()
    
    nx.write_gexf(G, folder_name + "/" + folder_name + "_graph.gexf")
