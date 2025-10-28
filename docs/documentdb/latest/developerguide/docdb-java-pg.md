# Amazon DocumentDB Java programming guide

This comprehensive guide provides a detailed walk through for working with Amazon DocumentDB using MongoDB’s Java drivers, covering essential aspects of database operations and management.

###### Topics

- [Introduction](#java-pg-intro "#java-pg-intro")
- [Prerequisites](#java-pg-prereqs "#java-pg-prereqs")
- [Data models](#java-pg-data-models "#java-pg-data-models")
- [Connecting with a Java driver](java-pg-connect-mongo-driver.md "java-pg-connect-mongo-driver.md")
- [CRUD operations with Java](java-crud-operations.md "java-crud-operations.md")
- [Index management with Java](index-management-java.md "index-management-java.md")
- [Event-driven programming](event-driven-programming.md "event-driven-programming.md")

## Introduction

The guide begins with connectivity, explaining how to establish secure connections to DocumentDB clusters using the MongoDB Java driver.
It details the connection string components, SSL/TLS implementation, and various connection options including IAM authentication and connection pooling, along with robust error handling strategies.

In the CRUD (create, read, update, delete) operations section, the guide thoroughly covers document manipulation, demonstrating how to create, read, update, and delete documents using both single and bulk operations.
It explains the usage of filters, queries, and various operation options, while emphasizing best practices for error handling and implementing retry logic for improved reliability.
The guide also extensively covers index management, detailing the creation and maintenance of different index types including single-field, compound, sparse, and text indexes.
It explains how to optimize query performance through proper index selection and usage of the `explain()` function to analyze query execution plans.

The final section focuses on event-driven programming using Amazon DocumentDB's change streams, demonstrating how to implement real-time data change monitoring in Java applications.
It covers the implementation of change stream cursors, handling of resume tokens for continuous operation, and time-based operations for historical data processing.
Throughout the guide, practical code examples and best practices are provided, making it an invaluable resource for you when building robust Java applications with Amazon DocumentDB.

## Prerequisites

Before you begin, make sure you have the following:

- An AWS account with a configured DocumentDB cluster.
  See this [getting started blog post](https://aws.amazon.com/blogs/database/part-1-getting-started-with-amazon-documentdb-using-amazon-ec2/ "https://aws.amazon.com/blogs/database/part-1-getting-started-with-amazon-documentdb-using-amazon-ec2/") for DocumentDB cluster setup.
- Java Development Kit (JDK) installed (we will be using [Amazon Corretto 21](../../../corretto/latest/corretto-21-ug/downloads-list.md "../../../corretto/latest/corretto-21-ug/downloads-list.md") for this guide).
- Maven for dependency management.

## Data models for this guide

All the example code in this guide assumes a connection to a “ProgGuideData” test database that has a “Restaurants” collection.
All the sample codes in this guide work on a restaurant listing system and below is an example of what a document in this system looks like:

```
{
    "_id": "ab6ad8f119b5bca3efa2c7ae",
    "restaurantId": "REST-CRT9BL",
    "name": "Thai Curry Palace",
    "description": "Amazing Restaurant, must visit",
    "cuisine": "Thai",
    "address": {
        "street": "914 Park Street",
        "city": "Bryan",
        "state": "AL",
        "zipCode": "96865",
        "location": {
            "type": "Point",
            "coordinates": [-25.4619, 8.389]
        }
    },
    "contact": {
        "phone": "(669) 915-9056 x6657"
    },
    "rating": {
        "average": 3.4,
        "totalReviews": 275
    },
    "priceRange": "$",
    "menu": [{
        "category": "Appetizers",
        "items": [{
            "name": "Buffalo Chicken Wings",
            "price": 13.42
        }]
    }],
    "features": [
        "Private Dining"
    ],
    "isActive": false“ michelin”: {“
        star”: 3,
        “ranking_years”: 4
    }
}
```

All code samples showing CRUD, index management, and event-driven programming assumes that you have a
[`MongoClient`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoClient.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoClient.html") object `dbClient`,
a [`MongoDatabase`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoDatabase.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoDatabase.html") object `connectionDB`,
and a [`MongoCollection`](<https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoCollection.html#find()> "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoCollection.html#find()") object `collection`.

###### Note

All code examples in this guide have been tested with MongoDB Java driver version 5.3.0.
