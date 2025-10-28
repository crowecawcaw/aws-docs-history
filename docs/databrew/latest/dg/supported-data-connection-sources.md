# Supported connections for data sources and outputs

You can connect to the following data sources for DataBrew recipe jobs. These include any
source of data that isn't a file you're uploading directly to DataBrew. The data
source that you're using might be called a database, a data warehouse, or something
else. We refer to all data providers as data sources or connections.

You can create a dataset using any of the following as data sources.

You can also use Amazon S3, AWS Glue Data Catalog, or JDBC databases supported through Amazon RDS for the
output of DataBrew recipe jobs. Amazon AppFlow and AWS Data Exchange aren't supported data stores for
the output of DataBrew recipe jobs.

- **Amazon S3**

You can use S3 to store and protect
any amount of data. To create a dataset, you specify an S3 URL where DataBrew can
access a data file, for example:
`s3://*your-bucket-name/*inventory-data.csv`

DataBrew can also read all of the files in an S3 folder, which means that you can
create a dataset that spans multiple files. To do this, specify an S3 URL in this form:
`s3://*your-bucket-name/your-folder-name/*`.

DataBrew supports only the following Amazon S3 storage classes: Standard, Reduced
Redundancy, Standard-IA, and S3 One Zone-IA. DataBrew ignores files with other
storage classes. DataBrew also ignores empty files (files containing 0 bytes). For
more information about Amazon S3 storage classes, see [Using Amazon S3
storage classes](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md") in the _Amazon S3 Console User
Guide_.

- **AWS Glue Data Catalog**

You can use the Data Catalog to define references to data that's stored in
the AWS Cloud. With the Data Catalog, you can build connections to individual
tables in the following services:

    + Data Catalog Amazon S3
    + Data Catalog Amazon Redshift
    + Data Catalog Amazon RDS
    + AWS Glue

DataBrew can also read all of the files in an Amazon S3 folder, which means that you can
create a dataset that spans multiple files. To do this, specify an Amazon S3 URL in
this form:
`s3://*your-bucket-name/your-folder-name/*`

To be used with DataBrew, Amazon S3 tables defined in the AWS Glue Data Catalog, must have a table
property added to them called a `classification`, which identifies the format
of the data as `csv`, `json`, or `parquet`, and the
`typeOfData` as `file`. If the
table property was not added when the table was created, you can add it using the AWS Glue console.

DataBrew supports only the Amazon S3 storage classes Standard, Reduced Redundancy,
Standard-IA, and S3 One Zone-IA. DataBrew ignores files with other storage classes.
DataBrew also ignores empty files (files containing 0 bytes). For more information
about Amazon S3 storage classes, see [Using Amazon S3 storage
classes](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md") in the _Amazon S3 Console User Guide_.

DataBrew can also access AWS Glue Data Catalog S3 tables from other accounts if an
appropriate resource policy is created. You can create a policy in the AWS Glue
console on the **Settings** tab under **Data
Catalog**. The following is an example policy specifically for a
single AWS Region.

###### Warning

This is a highly permissive resource policy that grants
`*$ACCOUNT_TO*` unrestricted access to the Data Catalog of
`*$ACCOUNT_FROM*`. In most cases, we recommend that you lock
your resource policy down to specific catalogs or tables. For more
information, see [AWS Glue resource policies
for access control](../../../glue/latest/dg/glue-resource-policies.md "../../../glue/latest/dg/glue-resource-policies.md") in the
_AWS Glue Developer Guide_.

In some cases, you might want to create a project or run a job in AWS Glue DataBrew in
`*$ACCOUNT_TO*` with an AWS Glue Data Catalog S3 table in
`*$ACCOUNT_FROM*` that points to an S3 location that is also in
`*$ACCOUNT_FROM*`. In such cases, the IAM role used when creating
the project and job in `*$ACCOUNT_TO*` must have permission to list
and get objects in that S3 location from `*$ACCOUNT_FROM*`. For more
information, see [Granting cross-account
access](../../../glue/latest/dg/cross-account-access.md "../../../glue/latest/dg/cross-account-access.md") in the _AWS Glue Developer Guide_.

- **Data connected using JDBC drivers**

You can create a dataset by connecting to data with a supported JDBC driver. For more information,
see [Using drivers with AWS Glue DataBrew](dbms-driver-connections.md "dbms-driver-connections.md").

DataBrew officially supports the following data sources using Java Database
Connectivity (JDBC):

    + Microsoft SQL Server
    + MySQL
    + Oracle
    + PostgreSQL
    + Amazon Redshift
    + Snowflake Connector for Spark

The data sources can be located anywhere that you can connect to them from DataBrew.
This list includes only JDBC connections that we've tested and can therefore
support.

Amazon Redshift and Snowflake Connector for Spark data sources can be connected in either of the following ways:

    + With a table name.
    + With a SQL query that spans multiple tables and operations.

SQL queries are executed when you start a project or a job run.

To connect to data that requires an unlisted JDBC driver, make sure that the
driver is compatible with JDK 8. To use the driver, store it in S3 in a
bucket where you can access it with your IAM role for DataBrew. Then point your
dataset at the driver file. For more information, see [Using drivers with AWS Glue DataBrew](dbms-driver-connections.md "dbms-driver-connections.md").

Example query for a SQL-based dataset:

```
SELECT
    *
FROM
    public.customer as c
JOIN
    public.customer_address as ca on c.current_address=ca.current_address
WHERE
    ca.address_id>0 AND ca.address_id<10001 ORDER BY ca.address_id

```

**Limitations of Custom SQL**

If you use a JDBC connection to access data for a DataBrew dataset, keep in mind the following:

    + AWS Glue DataBrew does not validate the custom SQL you provide as part of dataset
     creation. The SQL query will be executed when you start a project or job run.
     DataBrew takes the query you provide and passes it to the database engine using
     the default or provided JDBC drivers.
    + A dataset created with an invalid query will fail when it is used in a project or
     job. Validate your query before creating the dataset.
    + The **Validate SQL** feature is only available for Amazon Redshift-based data sources.
    + If you want to use a dataset in a project, limit SQL query runtime to under three
     minutes to avoid a timeout during project loading. Check the query runtime before
     creating a project.

- **Amazon AppFlow**

Using Amazon AppFlow, you can transfer
data into Amazon S3 from third-party Software-as-a-Service (SaaS) applications such as
Salesforce, Zendesk, Slack, and ServiceNow. You can then use the data to
create a DataBrew dataset.

In Amazon AppFlow, you create a connection and a flow to
transfer data between your third-party application and a destination application.
When using Amazon AppFlow with DataBrew, make sure that the Amazon AppFlow destination
application is Amazon S3. Amazon AppFlow destination applications other than Amazon S3 don't appear in the DataBrew console.
For more information on transferring data from your third-party application and creating Amazon AppFlow
connections and flows, see the
[Amazon AppFlow documentation](../../../appflow/index.md "../../../appflow/index.md").

When you choose **Connect new dataset** in the
**Datasets**
tab of DataBrew and click Amazon AppFlow, you see all flows in Amazon AppFlow that are configured
with Amazon S3 as the destination application. To use a flow's data for your
dataset, choose that flow.

Choosing **Create flow**, **Manage flows**, and
**View details** for Amazon AppFlow in the DataBrew console opens the
Amazon AppFlow console so that you can perform those tasks.

After you create a dataset from Amazon AppFlow, you can run the flow and view the lastest
flow run details when viewing dataset details or job details. When you run the
flow in DataBrew, the dataset is updated in S3 and is ready to be used in DataBrew.

The following situations can arise when you select an Amazon AppFlow flow in the DataBrew console
to create a dataset:

    + **Data hasn't been aggregated** -
     If the flow trigger is **Run on demand** or is
     **Run on schedule** with full data
     transfer, make sure to aggregate the data for the flow before
     using it to create a DataBrew dataset. Aggregating the flow combines all records in
     the flow into a single file. Flows with the trigger type
     **Run on schedule** with incremental
     data transfer, or **Run on event**
     don't require aggregation. To aggregate data in Amazon AppFlow, choose
     **Edit flow
     configuration** > **Destination details**
     > **Additional settings** >
     **Data transfer preference**.
    + **Flow hasn't been run** - If the
     run status for a flow is empty, it means one of the following:




    	- If the trigger for running the flow is  **Run on demand**, the flow has not yet been run.
    	- If the trigger for running the flow is  **Run
    	 on event**, the triggering event has not yet occurred.
    	- If the trigger for running the flow is
    	 **Run on schedule**, a scheduled run
    	 has not yet occurred.
    Before creating a dataset with a flow,
     choose **Run
     flow** for that flow.


    For more information, see
     [Amazon AppFlow flows](../../../appflow/latest/userguide/flows.md "../../../appflow/latest/userguide/flows.md") in the Amazon AppFlow User Guide.

- **AWS Data Exchange**

You can choose from
hundreds of third-party data sources that are available in AWS Data Exchange. By
subscribing to these data sources, you get the most up-to-date version of
the data.

To create a dataset, you specify the name of a AWS Data Exchange data product that
you're subscribed to and entitled to use.
