# Working with MongoDB connections in ETL jobs

You can create a connection for MongoDB and then use that connection in your AWS Glue job. For more
information, see [MongoDB connections](aws-glue-programming-etl-connect-mongodb-home.md "aws-glue-programming-etl-connect-mongodb-home.md") in the AWS Glue programming guide. The
connection `url`, `username` and `password` are stored in the MongoDB connection.
Other options can be specified in your ETL job script using the `additionalOptions` parameter of
`glueContext.getCatalogSource`. The other options can include:

- `database`: (Required) The MongoDB database to read from.
- `collection`: (Required) The MongoDB collection to read from.
  By placing the `database` and `collection` information inside the ETL
  job script, you can use the same connection for in multiple jobs.

1. Create an AWS Glue Data Catalog connection for the MongoDB data source. See ["connectionType": "mongodb"](aws-glue-programming-etl-connect.md#aws-glue-programming-etl-connect-mongodb "aws-glue-programming-etl-connect.md#aws-glue-programming-etl-connect-mongodb") for a description of the
   connection parameters. You can create the connection using the console, APIs or CLI.
2. Create a database in the AWS Glue Data Catalog to store the table definitions for your MongoDB
   data. See [Creating databases](define-database.md "define-database.md") for more
   information.
3. Create a crawler that crawls the data in the MongoDB using the information in the
   connection to connect to the MongoDB. The crawler creates the tables in the AWS Glue Data Catalog that
   describe the tables in the MongoDB database that you use in your job. See [Using crawlers to populate the Data Catalog](add-crawler.md "add-crawler.md") for more information.
4. Create a job with a custom script. You can create the job using the console, APIs or
   CLI. For more information, see [Adding Jobs in AWS Glue](add-job.md "add-job.md").
5. Choose the data targets for your job. The tables that represent the data target can be
   defined in your Data Catalog, or your job can create the target tables when it runs. You choose a
   target location when you author the job. If the target requires a connection, the connection
   is also referenced in your job. If your job requires multiple data targets, you can add them
   later by editing the script.
6. Customize the job-processing environment by providing arguments for your job and
   generated script.

Here is an example of creating a `DynamicFrame` from the MongoDB database
based on the table structure defined in the Data Catalog. The code uses
`additionalOptions` to provide the additional data source information:

Scala

```
val resultFrame: DynamicFrame = glueContext.getCatalogSource(
        database = `catalogDB`,
        tableName = `catalogTable`,
        additionalOptions = JsonOptions(Map("database" -> `DATABASE_NAME`,
                "collection" -> `COLLECTION_NAME`))
      ).getDynamicFrame()
```

Python

```
glue_context.create_dynamic_frame_from_catalog(
        database = `catalogDB`,
        table_name = `catalogTable`,
        additional_options = {"database":"`database_name`",
            "collection":"`collection_name`"})
```

7. Run the job, either on-demand or through a trigger.
