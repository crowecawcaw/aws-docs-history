# Creating a MongoDB source node

## Prerequisites needed

- A AWS Glue MongoDB connection, as described in the previous section, [Creating a MongoDB connection](creating-mongodb-connection.md "creating-mongodb-connection.md").
- If you chose to create an Secrets Manager secret, appropriate permissions on your job to read the secret used by the connection.
- A MongoDB collection you would like to read from. You will need identification information for the collection.

A MongoDB collection is identified by a database name and a collection name,
`mongodbName`, `mongodbCollection`.

## Adding a MongoDB data source

###### To add a **Data source – MongoDB** node:

1. Choose the connection for your MongoDB data source. Since you have created it, it should be
   available in the dropdown. If you need to create a
   connection, choose **Create MongoDB connection**. For more information see
   the previous section, [Creating a MongoDB connection](creating-mongodb-connection.md "creating-mongodb-connection.md").

Once you have chosen a connection, you can view the connection properties by clicking
**View properties**. 2. Choose a **Database**. Enter `mongodbName`. 3. Choose a **Collection**. Enter `mongodbCollection`. 4. Choose your **Partitioner**, **Partition size (MB)** and
**Partition key**. For more information about partition parameters, see ["connectionType": "mongodb" as
source](aws-glue-programming-etl-connect-mongodb-home.md#etl-connect-mongodb-as-source "aws-glue-programming-etl-connect-mongodb-home.md#etl-connect-mongodb-as-source"). 5. In **Custom MongoDB properties**, enter parameters and values as needed.
