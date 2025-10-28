Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Working with

Lake Formation-managed datashares as a consumer

With Amazon Redshift, you can access and analyze data shared with you through AWS Lake Formation
datashares. A datashare is a data product that contains a collection of data
objects, such as tables or databases, from different data sources.

After the AWS Lake Formation administrator discovers the datashare invitation and
creates a database in the AWS Glue Data Catalog that links to the datashare, the consumer
cluster or workgroup administrator can associate the cluster with the datashare
and the database in the AWS Glue Data Catalog, create a database local to the consumer
cluster or workgroup, and grant access to users and roles in the Amazon Redshift consumer
cluster or workgroup to start querying. Follow these steps to set up querying
permissions.

1. On the Amazon Redshift console, create an Redshift cluster to serve as the
   consumer cluster or workgroup, if needed. For information on how to create a
   cluster, see [Creating a cluster](../mgmt/managing-clusters-console.md#create-cluster "../mgmt/managing-clusters-console.md#create-cluster").
2. To list which databases in the AWS Glue Data Catalog consumer cluster or workgroup
   users have access to, run the [SHOW DATABASES](r_SHOW_DATABASES.md "r_SHOW_DATABASES.md")
   command.

```
`SHOW DATABASES FROM DATA CATALOG [ACCOUNT <account-id>,<account-id2>] [LIKE <expression>]`
```

Doing so lists the resources that are available from the Data Catalog, such as
the AWS Glue database’s ARN, database name, and information about the
datashare. 3. Using the AWS Glue database ARN from SHOW DATABASES, create a local database
in the consumer cluster or workgroup. For more information, see [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md").

```
`CREATE DATABASE lf_db FROM ARN <lake-formation-database-ARN> WITH [NO] DATA CATALOG SCHEMA [<schema>];`
```

4. Grant access on databases and schema references created from the
   datashares to users and roles in the consumer cluster or workgroup as
   needed. For more information, see [GRANT](r_GRANT.md "r_GRANT.md") or [REVOKE](r_REVOKE.md "r_REVOKE.md"). Note that users created from the [CREATE
   USER](r_CREATE_USER.md "r_CREATE_USER.md") command cannot access objects in datashare that have been
   shared to Lake Formation. Only users with access to both Redshift and Lake Formation can access
   datashares that have been shared with Lake Formation.

```
`GRANT USAGE ON DATABASE sales_db TO IAM:Bob;`
```

As a consumer cluster or workgroup administrator, you can only assign
permissions on the entire database created from the datashare to your users
and roles. In some cases, you need fine-grained controls on a subset of
database objects created from the datashare.

You can also create late-binding views on top of shared objects and use
these to assign granular permissions. You can also consider having producer
clusters or workgroups create additional datashares for you with the
granularity required. You can create as many schema references to the
database created from the datashare. 5. Database users can use the views SVV_EXTERNAL_TABLES and
SVV_EXTERNAL_COLUMNS to find all of the shared tables or columns within the
AWS Glue database

```
`SELECT * from svv_external_tables WHERE redshift_database_name = 'lf_db';

SELECT * from svv_external_columns WHERE redshift_database_name = 'lf_db';`

```

6. Query data in the shared objects in the datashares.

Users and roles with permissions on consumer databases and schemas on
consumer clusters or workgroups can explore and navigate the metadata of any
shared objects. They can also explore and navigate local objects in a
consumer cluster or workgroup. To do so, they can use the JDBC or ODBC
drivers or the SVV_ALL and SVV_EXTERNAL views.

```
`SELECT * FROM lf_db.schema.table;`
```

You can only use SELECT statements on shared objects. However, you can
create tables in the consumer cluster by querying the data from the shared
objects in a different local database.

```
// Connect to a local cluster database

// Create a view on shared objects and access it.
`CREATE VIEW sales_data
AS SELECT *
FROM sales_db.public.tickit_sales_redshift
WITH NO SCHEMA BINDING;

SELECT * FROM sales_data;`

```
