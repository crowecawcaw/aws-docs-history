# Query data in Amazon Athena or

Amazon Redshift in Amazon DataZone

In Amazon DataZone, once a subscriber has access to an asset in the catalog, they can
consume it (query and analyze) using Amazon Athena or Amazon Redshift query editor v2. You must be
a project owner or contributor to complete this task. Depending on the blueprints
enabled in the project, Amazon DataZone provides links to Amazon Athena and/or Amazon Redshift query
editor v2 on the right-hand side pane of the project page in the data portal.

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. In the Amazon DataZone data portal, choose **Browse Projects
   List** and then find and choose the project where you have the data
   that you want to analyze.
3. If the Data Lake blueprint is enabled on this project, a link to Amazon Athena is
   displayed in the right-hand side panel on the project's home page.

If the Data Warehouse blueprint is enabled on this project, a link to the
query editor is displayed in the right-hand side panel on the project's home
page.

###### Note

Blueprints are defined in the environment profile with which a project is
created.

###### Topics

- [Query data using Amazon Athena](#query-athena-with-deep-link "#query-athena-with-deep-link")
- [Query data using Amazon
  Redshift](#query-redshift-with-deep-link "#query-redshift-with-deep-link")

## Query data using Amazon Athena

Choose the Amazon Athena link to open the Amazon Athena query editor in a new tab in the
browser using the project’s credentials for authentication. The Amazon DataZone project
you're working with is automatically selected as the current workgroup in the query
editor.

In the Amazon Athena query editor, write and run your queries. Some common tasks
include:

- [Query and analyze your
  subscribed assets](#query-analyze-subscribed-data "#query-analyze-subscribed-data")
- [Create new tables](#create-new-tables "#create-new-tables")
- [Create a table from query
  results (CTAS) from an external S3 bucket](#create-tables-external-s3-bucket "#create-tables-external-s3-bucket")

### Query and analyze your

subscribed assets

If access to the assets that your project is subscribed to is not granted
automatically by Amazon DataZone, you must be authorized to access the underlying
data. For more information on how to grant access to these assets, see [Grant access for approved
subscriptions to unmanaged assets in Amazon DataZone](grant-access-to-unmanaged-asset.md "grant-access-to-unmanaged-asset.md").

If access to the assets that your project is subscribed to is [granted automatically by
Amazon DataZone](grant-access-to-glue-asset.md "grant-access-to-glue-asset.md"), you can run SQL queries on the tables and see the results
in Amazon Athena. For more information about using SQL in Amazon Athena, see [SQL reference for Athena](grant-access-to-glue-asset.md "grant-access-to-glue-asset.md").

When you navigate to the Amazon Athena query editor after choosing the Amazon Athena
link in the right-hand side panel on the project's home page, a
**Project** dropdown is displayed in the top-right corner
of the Amazon Athena query editor and your project context is automatically
selected.

You can see the following databases in the **Database**
dropdown:

- A publishing database
  (``{environmentname}`\_pub_db`).
  The purpose of this database is to provide you with an environment where
  you can produce new data within the context of your project and then be
  able to publish this data into the Amazon DataZone catalog. Project owners
  and contributors have read and write access to this database. Project
  viewers have only read access to this database.
- A subscription database
  (``{environmentname}`\_sub_db`).
  The purpose of this database is to share with you the data to which you
  have subscribed as a project member in the Amazon DataZone catalog, and to
  enable you to query that data.

### Create new tables

If you have connected to an external S3 bucket, you can use Amazon Athena to query
and analyze the assets from an external Amazon S3 bucket. In this scenario,
Amazon DataZone doesn't have permissions to grant access directly to the underlying
data in the external Amazon S3 bucket, and the external Amazon S3 data created outside the
project is not automatically managed in Lake Formation, and can't be managed by
Amazon DataZone. An alternative is to copy the data from the external Amazon S3 bucket to
a new table inside the project’s Amazon S3 bucket using a `CREATE TABLE`
statement in Amazon Athena. When you run a `CREATE TABLE` query in
Amazon Athena, you register your table with the AWS Glue Data Catalog.

To specify the path to your data in Amazon S3, use the `LOCATION`
property, as shown in the following example:

```

CREATE EXTERNAL TABLE 'test_table'(
...
)
ROW FORMAT ...
STORED AS INPUTFORMAT ...
OUTPUTFORMAT ...
LOCATION 's3://bucketname/folder/'

```

For more information, see [Table location in Amazon S3](../../../athena/latest/ug/tables-location-format.md "../../../athena/latest/ug/tables-location-format.md").

### Create a table from query

results (CTAS) from an external S3 bucket

When you subscribe to an asset, access to the underlying data is read-only.
You can use Amazon Athena to create a copy of the table. In Amazon Athena, `A
 CREATE TABLE AS SELECT (CTAS)` query creates a new table in Amazon Athena
from the results of a `SELECT` statement from another query. For
information about the CTAS syntax, see [CREATE TABLE AS](../../../athena/latest/ug/create-table-as.md "../../../athena/latest/ug/create-table-as.md").

The following example creates a table by copying all columns from a
table:

```

CREATE TABLE new_table AS
SELECT *
FROM old_table;

```

In the following variation of the same example, your `SELECT`
statement also includes a `WHERE` clause. In this case, the query
selects only those rows from the table that satisfy the `WHERE`
clause:

```

CREATE TABLE new_table AS
SELECT *
FROM old_table WHERE condition;

```

The following example creates a new query that runs on a set of columns from
another table:

```

CREATE TABLE new_table AS
SELECT column_1, column_2, ... column_n
FROM old_table;

```

This variation of the same example creates a new table from specific columns
from multiple tables:

```

CREATE TABLE new_table AS
SELECT column_1, column_2, ... column_n
FROM old_table_1, old_table_2, ... old_table_n;

```

These newly created tables are now a part of your projects’ AWS Glue database,
and can be made discoverable by others and shared with other Amazon DataZone projects
by publishing the data as an asset to the Amazon DataZone catalog.

## Query data using Amazon

Redshift

In the Amazon DataZone data portal, open an environment that uses the data warehouse
blueprint. Choose the **Amazon Redshift** link in the right-hand
panel on the environment page. This opens a confirmation dialog with necessary
details that help you establish a connection to your environmemnt’s Amazon Redshift
cluster or Amazon Redshift Serverless workgroup in the Amazon Redshift query editor
v2.0. Once you have identified the necessary details to establish the connection,
choose the **Open Amazon Redshift** button. This opens the Amazon
Redshift query editor v2.0 in a new tab in the browser using temporary credentials
of the Amazon DataZone environment.

In the query editor, follow the steps below depending on whether your environment
is using an Amazon Redshift Serverless workgroup or an Amazon Redshift cluster.

For an Amazon Redshift Serverless workgroup

1. In the query editor, identify you Amazon DataZone environment’s Amazon Redshift
   Serverless workgroup, right-click it and choose **Create a
   connection**.
2. Choose **Federated User** for authentication.
3. Provide the name of the Amazon DataZone environment's database.
4. Choose **Create connection**.

For an Amazon Redshift cluster:

1. In the query editor, identify you Amazon DataZone environment’s Amazon Redshift
   cluster, right-click it and choose **Create a connection**.
2. Select **Temporary credentials using your IAM identity**
   for authentication.
3. If the above authentication method is not available, open
   **Account settings** by choosing the gear button in the
   bottom left corner, choose **Authenticate with IAM
   credentials** and save. This is a one-time-only setting.
4. Provide the name of the Amazon DataZone environment’s database to create the
   connection.
5. Choose **Create connection**.

Now you can start querying against the tables and views within the Amazon Redshift
cluster or Amazon Redshift Serverless workgroup configured for your Amazon DataZone
environment.

Any Amazon Redshift tables or views that you have subscribed to are linked to the
Amazon Redshift cluster or Amazon Redshift Serverless workgroup that is configured
for the environment. You can subscribe to the tables and views as well as publish
any new tables and views that you create in your environment’s cluster or
database.

For example, let's take a scenario in which an environment is linked to an Amazon
Redshift cluster called `redshift-cluster-1` and a database called
`dev` in that cluster. Using the Amazon DataZone data portal, you can
query the tables and views that are added to your environment. Under the
`Analytics tools` section in the right-hand side pane of the data
portal, you can choose the Amazon Redshift link for this environment, which opens
the query editor. You can then right-click on `redshift-cluster-1`
cluster and create a connection using **Temporary credentials using your IAM
identity**. Once the connection is established, you can see all the
tables and views to which your environment has access under the
**dev** database.
