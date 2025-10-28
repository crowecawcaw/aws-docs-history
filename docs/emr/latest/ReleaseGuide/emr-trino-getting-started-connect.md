# Connect to the primary node for the Amazon EMR cluster and run queries

## Provision test data and configure permissions

You can test Amazon EMR with Trino by using AWS Glue Data Catalog and its Hive metastore. These prerequisite steps describe how to set up test data, if you
haven't done so:

1. Create an SSH key to use for communication encryption, if you haven't already.
2. You can choose from several file systems to store data and log files. To start, create an Amazon S3 bucket. Give the
   bucket a unique name. When you create it, specify the encryption key that you created.

###### Note

Choose the same region to create both your storage bucket and the Amazon EMR cluster. 3. Choose the bucket you created. Choose **Create folder** and give the folder a memorable name. When you create the folder, choose a security configuration. You can choose
the security settings for the parent, or make the security settings more specialized. 4. Add test data to your folder. For the purposes of this tutorial, using a .csv of comma-separated records works well for completing this use case. 5. After you add data to an Amazon S3 bucket, configure a table in AWS Glue to provide an abstraction layer for querying the data.

## Connect and run queries

The following describes how you connect to and run queries on a cluster running Trino. Before you do this, make sure you set up the
Hive metastore connector, which is described in the previous procedure, so that metastore tables are visible.

1. We recommend using EC2 Instance Connect to connect to your cluster, because it provides a secure connection. Choose **Connect to the Primary node using
   SSH** from the cluster summary. The connection
   requires that the security group has an inbound rule to allow connections through port 22 to clients in the subnet. You also must use the user **hadoop** when connecting.
2. Start the Trino CLI by running `trino-cli`. This provides for you to run commands and query data with Trino.
3. Run `show catalogs;`. Check that the **hive** catalog is listed. This provides a list of catalogs available, which contain data stores
   or system settings.
4. To see the schemas available, run `show schemas in hive;`. From here, you can run `use `schema-name`;` and include the name
   of your schema. Then you can run `show tables;` to list
   tables.
5. Query a table by running a command like `SELECT * FROM `table-name``, using the name of a table in your schema. If you already ran the `USE`statement to 
connect to a specific schema, you 
don't have to use two-part notation such as`schema`.`table`.
