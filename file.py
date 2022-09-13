import asyncio
from pprint import pprint

import pymongo

from src.parsers.lamoda_parser import LamodaParser

db_client = pymongo.MongoClient(
    "mongodb://mongodb:27017/?authSource=admin&readPreference=secondary&directConnection=true&ssl=false",
    username="mongoadmin", password="mongopassword"
)

current_db = db_client["pyloungedb"]

collection = current_db["youtubers"]

parsing = LamodaParser("https://www.lamoda.by/c/5971/shoes-muzhkrossovki/?sitelink=topmenuM&l=5")
collection.drop()


def pull_to_mongodb():
    for page in asyncio.run(parsing.get_all_data()):
        for item in page:
            collection.insert_one(item)
    print("Success")


pull_to_mongodb()

print(collection.count_documents({}))

# pylounge = {
#     'title': "PyLounge",
#     'url': 'https://www.youtube.com/watch?v=3bqcv8YmeQo&ab_channel=PyLounge-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BD%D0%B0Python%D0%B8%D0%B2%D1%81%D1%91%D0%BEIT',
#     'subscribers': 2100,
#     'views': 900000
# }
#
# ins_result = collection.insert_one(pylounge)
# print(ins_result.inserted_id)
#
# it_youtubers = [
#     {'title': 'АйтиБорода', 'url': 'https://www.youtube.com/c/ITBEARD', 'subscribers': 227000, 'views': 1200024},
#     {'title': 'Диджитализируй',
#      'url': 'https://www.youtube.com/c/%D0%94%D0%B8%D0%B4%D0%B6%D0%B8%D1%82%D0%B0%D0%BB%D0%B8%D0%B7%D0%B8%D1%80%D1%83%D0%B9',
#      'subscribers': 62700, 'views': 960245},
#     {'title': 'Senior Software Vlogger', 'url': 'https://www.youtube.com/c/SeniorSoftwareVlogger', 'subscribers': 90700,
#      'views': 2000000},
# ]
#
# ins_result = collection.insert_many(it_youtubers)
# print(ins_result.inserted_ids)
#
# subs = 2100
# print(collection.find_one({'subscribers': subs}))
# print(collection.count_documents({'subscribers': subs}))

# for channel in collection.find():
#     print(channel)
#
# print(collection.count_documents({'subscribers': {"$gt": 10000}}))
# print(collection.count_documents({'subscribers': {"$lt": 10000}}))
#
# for channel in collection.find({'subscribers': {"$gt": 10000}}).sort('title'):
#     print(channel)
#
# for channel in collection.find({"$and": [{'subscribers': {"$gt": 10000}}, {'views': {"$gt": 1000000}}]}):
#     print(channel["title"])
#
# for channel in collection.find({'title': {"$regex": "^Py(.*?)"}}):
#     print(channel["title"], '   ', channel["subscribers"])
#
# query = {'views': {'$in': list(range(0, 1000000))}}
#
# for channel in collection.find(query):
#     print(channel["title"])
#
# collection.update_one({'title': 'PyLounge'}, {"$set": {'subscribers': 50000}})
# print(collection.find_one({'title': 'PyLounge'}))
# print(collection.find_one_and_update({'title': 'PyLounge'}, {"$set": {"views": 1200000}}))
#
# collection.update_many({'subscribers': {"$gt": 100000}}, {"$set": {"views": 3000000}})
# for channel in collection.find({'subscribers': {'$gt': 100000}}):
#     print(channel['title'])
#
