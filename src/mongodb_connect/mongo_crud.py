from typing import Any
import pandas as pd
from pymongo.mongo_client import MongoClient
import json


class mongo_operation:
    __collection = None  # private/protected variable
    __database = None

    def __init__(self, client_url: str, database_name: str, collection_name: str = None):
        self.client_url = client_url
        self.database_name = database_name
        self.collection_name = collection_name

    def create_mongo_client(self, collection=None):
        client = MongoClient(self.client_url)
        return client

    def create_database(self, collection=None):
        if mongo_operation.__database is None:
            client = self.create_mongo_client(collection)
            self.database = client[self.database_name]
        return self.database

    def set_new_database(self, database: str):
        self.database = self.create_mongo_client()[database]
        mongo_operation.__database = database
        self.database_name = database

    def set_new_collection(self, collection_name: str):
        self.collection = self.__connect_database()[collection_name]
        mongo_operation.__collection = collection_name
        self.collection_name = collection_name

    def __connect_database(self):
        if mongo_operation.__database is None:
            self.database = self.create_mongo_client()[self.database_name]
        return self.database

    def create_collection(self, collection=None):
        if mongo_operation.__collection is None:
            database = self.create_database(collection)
            self.collection = database[self.collection_name]
            mongo_operation.__collection = collection

        if mongo_operation.__collection != collection:
            database = self.create_database(collection)
            self.collection = database[self.collection_name]
            mongo_operation.__collection = collection

        return self.collection

    def insert_record(self, record: dict, collection_name: str) -> Any:
        if type(record) == list:
            for data in record:
                if type(data) != dict:
                    raise TypeError("record must be in the dict")
            collection = self.create_collection(collection_name)
            collection.insert_many(record)
        elif type(record) == dict:
            collection = self.create_collection(collection_name)
            collection.insert_one(record)

    def bulk_insert(self, datafile, collection_name: str = None):
        self.path = datafile

        if self.path.endswith('.csv'):
            dataframe = pd.read_csv(self.path, encoding='utf-8')

        elif self.path.endswith(".xlsx"):
            dataframe = pd.read_excel(self.path, encoding='utf-8')

        datajson = json.loads(dataframe.to_json(orient='records'))
        collection = self.create_collection()
        collection.insert_many(datajson)

    def update_record(self, query: dict, update_data: dict, collection_name: str = None, update_all: bool = False):
        collection = self.create_collection(collection_name)

        if update_all:
            result = collection.update_many(query, {"$set": update_data})
        else:
            result = collection.update_one(query, {"$set": update_data})

        return result.modified_count

    def delete_record(self, query: dict, collection_name: str = None, delete_all: bool = False):
        collection = self.create_collection(collection_name)

        if delete_all:
            result = collection.delete_many(query)
        else:
            result = collection.delete_one(query)

        return result.deleted_count
