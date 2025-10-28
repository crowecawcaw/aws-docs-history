Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using cross-database queries with the query

editor

This topic explains how to use cross-database queries with the query editor. Cross-database
queries are queries that operate on multiple databases within a single Amazon Redshift cluster.

You can use cross-database queries to access data from any of the databases on your Amazon Redshift
cluster without having to connect to that specific database. When you run cross-database
queries on any other unconnected databases, you have read and write access only to those
database objects.

You can query and write to other database objects using fully qualified object names
expressed with three-part notation. The full path to any database object consists of three
components: database name, schema, and name of the object. An example is
`database_name.schema_name.object_name`.

###### To use cross-database queries with the query editor v2

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Create a cluster to use cross-database queries in Amazon Redshift query editor v2. For more
   information, see [Creating a cluster](../mgmt/managing-clusters-console.md#create-cluster.html "../mgmt/managing-clusters-console.md#create-cluster.html") in the _Amazon Redshift Management Guide_.
3. Enable access to the query editor with the appropriate permissions. For more
   information, see [Querying a database using the query editor v2](../mgmt/query-editor-v2.md "../mgmt/query-editor-v2.md") in the _Amazon Redshift Management Guide_.
4. On the navigation menu, choose **Query editor v2**, then connect to a database in your cluster.

When you connect to the query editor v2 for the first time, Amazon Redshift shows the
resources for the connected database by default. 5. Choose the other databases that you have access to view database objects for these
other databases. To view objects, make sure that you have the appropriate
permissions. After you choose a database, Amazon Redshift shows the list of schemas from the
database.

Select a schema to see the list of database objects within that schema.

###### Note

Amazon Redshift doesn't directly support query catalog objects that are part of
AWS Glue or federated databases. To query these, first create external schemas
that refer to those external data sources in each database.

Amazon Redshift cross-database queries with three-part notation don't support
metadata tables under the schemas `information_schema` and
`pg_catalog` because these metadata views are specific to a
database. 6. (Optional) Filter the list of tables or views for the schema that you selected.
