'''
Created on Apr 30, 2015

@author: pekzeki
'''

from pymongo import MongoClient

def filter_dataset():
    business_filtered = db.create_collection("business_pa_filtered")
    user_filtered = db.create_collection("user_pa_filtered")
    review_filtered = db.create_collection("review_pa_filtered")
    
    businesses = business_collection.find({ 'state' : 'PA' })
    for business in businesses:
        business["_id"]= business.get("business_id")
        business_filtered.insert(business)
        
        reviews = review_collection.find({ 'business_id' :  business.get("business_id")})
        for review in reviews:
            review["_id"]= review.get("review_id")
            review_filtered.insert(review)
            
            user = user_collection.find_one({'user_id' : review.get("user_id")})
            if user is not None:
                exist = user_filtered.find_one({'user_id' : user.get("user_id")})
                if exist is None:
                    user["_id"]= user.get("user_id")
                    user_filtered.insert(user) 


client = MongoClient()
db = client.yelp
user_collection = db.user
review_collection = db.review
business_collection = db.business

filter_dataset()