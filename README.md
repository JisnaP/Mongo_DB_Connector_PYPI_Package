# Mongo_DB_Connector_PYPI_Package
A Python library to simplify MongoDB operations like creating databases, collections, inserting, updating, and deleting records, and performing bulk operations with CSV and Excel files.
Features
-Easily create and switch between databases and collections.
-Insert single or multiple records.
-Perform bulk inserts from CSV or Excel files.
-Update single or multiple records with ease.
-Delete single or multiple records.
-Support for custom queries using MongoDB's query syntax.

# Installation
Install the package via pip:
```bash 
pip install databaseautomation
```
# Usage
Here's a quick guide to get started with the package:
1. Import and Initialize
```bash 
from databaseautomation import mongo_operation
```
# Initialize the MongoDB operations
```bash
mongo_ops = mongo_operation(
    client_url="mongo_url",
    database_name="my_database",
    collection_name="my_collection"
)
```
2. Insert Records
Insert a Single Record
```bash 
mongo_ops.insert_record({"name": "Aliya", "age": 25}, "example_collection")
```
Insert Multiple Records
```bash 
records = [{"name": "Bob", "age": 25}, {"name": "Charlie", "age": 28}]
mongo_ops.insert_record(records, "my_collection")
```
3. Bulk Insert from File
# Insert records from a CSV or Excel file
```bash 
mongo_ops.bulk_insert("data.csv", "my_collection")
```
4. Update Records
Update a Single Record
```bash 
mongo_ops.update_record(
    query={"name": "Alice"},
    update_data={"age": 35},
    collection_name="my_collection"
)
```
Update Multiple Records
```bash 
mongo_ops.update_record(
    query={"age": {"$lt": 30}},
    update_data={"status": "young"},
    collection_name="my_collection",
    update_all=True
)
```
5. Delete Records
Delete a Single Record
```bash 
mongo_ops.delete_record(
    query={"name": "Charlie"},
    collection_name="my_collection"
)
```
Delete Multiple Records
```bash 
mongo_ops.delete_record(
    query={"age": {"$lt": 25}},
    collection_name="my_collection",
    delete_all=True
)
```
6. Advanced Features
Set a New Database

```bash 
mongo_ops.set_new_database("new_database")
```
7. Set a New Collection

```bash 
mongo_ops.set_new_collection("new_collection")
```
# Requirements
Python 3.8+
MongoDB Server
# Dependencies:
pymongo
pandas
ensure