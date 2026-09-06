

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Creating destination databases in Amazon Redshift
<a name="zero-etl-using.creating-db"></a>

To replicate data from your source into Amazon Redshift, you must create a database from your integration in Amazon Redshift.

Connect to your target Redshift Serverless workgroup or provisioned cluster and create a database with a reference to your integration identifier. This identifier is the value returned for `integration_id` when you query the [SVV\_INTEGRATION](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTEGRATION.html) view.

**Important**  
Before creating a database from your integration, your zero-ETL integration must be created and in the `Active` state on the Amazon Redshift console.

Before you can start replicating data from your source into Amazon Redshift, create a database from the integration in Amazon Redshift. You can either create the database using the Amazon Redshift console or the query editor v2. 

------
#### [ Amazon Redshift console ]

1. In the left navigation pane, choose **Zero-ETL integrations**.

1. From the integration list, choose an integration.

1. If you're using a provisioned cluster, you must first connect to the database. Choose **Connect to database**. You can connect using a recent connection, or by creating a new connection.

1. To create a database from the integration, choose **Create database from integration**. 

1. Enter a **Destination database name**. The **Integration ID** and **Data warehouse name** are pre-populated. 

   For Aurora PostgreSQL, RDS for PostgreSQL, RDS for Oracle, or Oracle Database@AWS sources, enter the **Source named database** that you specified when creating your zero-ETL integration. In these cases, you can map a maximum of 100 source databases to Amazon Redshift databases.

1. Choose **Create database**.

------
#### [ Amazon Redshift query editor v2 ]

1. Navigate to the Amazon Redshift console and choose **Query editor v2**.

1. In the left panel, choose your Amazon Redshift Serverless workgroup or Amazon Redshift provisioned cluster, and then connect to it.

1. To get the integration ID, navigate to the integration list on the Amazon Redshift console.

   Alternatively, run the following command to get the `integration_id` value:

   ```
   SELECT integration_id FROM SVV_INTEGRATION;
   ```

1. Then, run the following command to create the database. By specifying the integration ID, you create a connection between the database and your source.

   Substitute `integration_id` with the value returned by the previous command.

   ```
   CREATE DATABASE {{destination_db_name}} FROM INTEGRATION '{{integration_id}}';
   ```

   For Aurora PostgreSQL, RDS for PostgreSQL, RDS for Oracle, or Oracle Database@AWS sources, you must also include a reference to the named database within the source instance or cluster that you specified when you created the integration. For example:

   ```
   CREATE DATABASE {{"destination_db_name"}} FROM INTEGRATION '{{integration_id}}' DATABASE {{"named_db"}};
   ```

------

For more information about creating a database for a zero-ETL integration target, see [CREATE DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_DATABASE.html) in the *Amazon Redshift Database Developer Guide*. You can use ALTER DATBASE to change database parameters such as REFRESH INTERVAL. For more information about altering a database for a zero-ETL integration target, see [ALTER DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_DATABASE.html) in the *Amazon Redshift Database Developer Guide*.

**Note**  
Only your integration source can update data in the database you create from your integration. To change the schema of a table, run DDL or DML commands against tables in the source. You can run DDL and DML commands against tables in the source, but you can only run DDL commands and read-only queries on the destination database.

For information about viewing the status of a destination database, see [Viewing zero-ETL integrations](zero-etl-using.describing.md).

After creating a destination database, you can add data to your source. To add data to your source, see one of the following topics:
+ For Aurora sources, see [Add data to the source DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.querying.html#zero-etl.add-data-rds) in the *Amazon Aurora User Guide*.
+ For Amazon RDS sources, see [Add data to the source DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.querying.html#zero-etl.add-data-rds) in the *Amazon RDS User Guide*.
+ For DynamoDB sources, see [Getting started with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html) in the *Amazon DynamoDB Developer Guide*.
+ For zero-ETL integrations with applications sources, see [Zero-ETL integrations](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html) in the *AWS Glue Developer Guide*.