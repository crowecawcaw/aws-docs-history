# Creating a MongoDB target node

## Prerequisites needed

- A AWS Glue MongoDB connection, configured with an AWS Secrets Manager secret, as described in the previous section, [Creating a MongoDB connection](creating-mongodb-connection.md "creating-mongodb-connection.md").
- Appropriate permissions on your job to read the secret used by the connection.
- A MongoDB table you would like to write to, `tableName`.

## Adding a MongoDB data target

###### To add a **Data target – MongoDB** node:

1. Choose the connection for your MongoDB data source. Since you have created it, it should be
   available in the dropdown. If you need to create a
   connection, choose **Create MongoDB connection**. For more information see
   the previous section, [Creating a MongoDB connection](creating-mongodb-connection.md "creating-mongodb-connection.md").

Once you have chosen a connection, you can view the connection properties by clicking
**View properties**. 2. Choose a **Database**. Enter `mongodbName`. 3. Choose a **Collection**. Enter `mongodbCollection`. 4. Choose your **Partitioner**, **Partition size (MB)** and
**Partition key**. For more information about partition parameters, see ["connectionType": "mongodb" as
source](aws-glue-programming-etl-connect-mongodb-home.md#etl-connect-mongodb-as-source "aws-glue-programming-etl-connect-mongodb-home.md#etl-connect-mongodb-as-source"). 5. Choose **Retry Writes** if desired. 6. In **Custom MongoDB properties**, enter parameters and values as needed.
