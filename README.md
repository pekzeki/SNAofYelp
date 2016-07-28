# SNAofYelp
Social Network Analysis on famous Yelp Dataset 

# Desc
The dataset that was used in this project is available at http://www.yelp.com/dataset_challenge . Yelp provided a big dataset for public usage that includes information about local businesses, reviews and users in 10 cities across 4 countries. Other than business, user and review information it also contains some additional information such as, check-ins and tips. The basic entity relations and the samples from json files represented below. Unfortunately, lack of CPU and memory resources  the dataset was filtered. Instead of using all cities we just used the yelp data of Illinois.

# Tech

Data storage, MongoDB.
Programming, Python. (pymongo/networkx libraries)
Visualization, Gephi.

# Execution

Basic Setup

- Download the yelp dataset or use the dataset that we provided with the project.
- Extract the tar file to a directory.
- Download and install the MongoDB.
- Create a database called yelp in the MongoDB.
- Import the dataset to yelp database.
```sh
$ mongoimport --db yelp --collection business yelp_academic_dataset_business.json
$ mongoimport --db yelp --collection review yelp_academic_dataset_review.json
$ mongoimport --db yelp --collection user yelp_academic_dataset_user.json
```
- Install python packages.
```sh
$ pip install pymongo
$ pip install networkx
```
- Run python script that we have provided to filter the dataset.
```sh
$ python mongo_filter.py
$ pip install networkx
```

# Scripts

undirected_all_friends.py : Creates and analyzes a undirected user friendship graph by adding all users and their friends. G = (N, E) where N is the users exist in dataset and not exist in dataset but in their friendlist, E is the friend relationship between nodes.

undirected_db_friends.py : Creates and analyzes a undirected user friendship graph by adding all users and their friends if and only if they exist in our dataset. 
G = (N, E) where N is the users exist in dataset, E is the friend relationship between nodes.

bipartite_db_friends.py : Creates a undirected user – business relationship bipartite graph, converts the user – business relationship to a projected graph and analyzes both graph structures. 
(Bipartite) G = (U, V, E) where U consist of users and V consist of businesses, E is the review relationship between users and business.
(Projected) P = (N, E) where N is the users, E is the relationship between users after projection of the bipartite graph G.

compare_graphs.py : Intersects the undirected_db_friends and projected_db_friends, analyzes the intersection-graph.
I = (N, E) where N is the remaining nodes after intersection, E is the friend relationship 	between nodes.

pref_attack_all_friends.py : Removes the top-5 degree/closeness/betweenness central nodes and analyzes these three graphs respectively.
D = (N, E) where N is the remaining nodes after removal of top-5 degree central nodes, E is  the friendship relationship between nodes.
C = (N, E) where N is the remaining nodes after removal of top-5 closeness central nodes, E is the friendship relationship between nodes.
B = (N, E) where N is the remaining nodes after removal of top-5 betweenness central nodes, E is  the friendship relationship between nodes.

random_attack_all_friends.py : Removes the 5 nodes randomly and analyzes the resulting graphs.
R = (N, E) where N is the remaining nodes after removal of 5 randomly selected nodes, E is  	the friendship relationship between nodes.
