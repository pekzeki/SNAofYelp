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
