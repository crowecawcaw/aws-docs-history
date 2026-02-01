Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Sharing licensed Amazon Redshift data on AWS Data Exchange

When creating AWS Data Exchange datashares and adding them to an AWS Data Exchange product, providers can
license data in Amazon Redshift that consumers can discover, subscribe to, and query
up-to-date data in Amazon Redshift when they have active AWS Data Exchange subscriptions.

With AWS Data Exchange datashares added to an AWS Data Exchange product, consumers automatically have
access to a product's datashares when their subscription starts and retain their
access as long as their subscription is active.

###### Topics

- [Working with AWS Data Exchange datashares as a
  producer](adx-getting-started-producer.md "adx-getting-started-producer.md")
- [Working with AWS Data Exchange datashares as a
  consumer](#adx-getting-started-consumer "#adx-getting-started-consumer")

## Working with AWS Data Exchange datashares as a

consumer

With Amazon Redshift, you can access and analyze datasets from AWS Data Exchange without having to
store or manage copies of the data.

**If you are a consumer, follow these steps to discover
data products that contain AWS Data Exchange datashares and query Amazon Redshift
data:**

1. On the AWS Data Exchange console, discover and subscribe to data products that
   contains AWS Data Exchange datashares.

Once your subscription starts, you can access licensed Amazon Redshift data that is
imported as assets to datasets that contain AWS Data Exchange datashares.

For more information on how to get started with using data products that
contain AWS Data Exchange datashares, see [Subscribing to data products on AWS Data Exchange](../../../data-exchange/latest/userguide/subscribe-to-data-sets.md "../../../data-exchange/latest/userguide/subscribe-to-data-sets.md"). 2. On the Amazon Redshift console, create an Amazon Redshift cluster, if needed.

For information on how to create a cluster, see [Creating a cluster](../mgmt/managing-clusters-console.md#create-cluster "../mgmt/managing-clusters-console.md#create-cluster"). 3. List the datashares that are made available to you and view the content
of datashares. For more information, see [DESC DATASHARE](r_DESC_DATASHARE.md "r_DESC_DATASHARE.md") and [SHOW DATASHARES](r_SHOW_DATASHARES.md "r_SHOW_DATASHARES.md").

The following example displays the information of inbound datashares of a
specified producer namespace. When you run DESC DATASHARE as a consumer
administrator, you must specify the ACCOUNT and NAMESPACE option to view
inbound datashares.

```
DESC DATASHARE salesshare of ACCOUNT '123456789012' NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';

 producer_account  |          producer_namespace          | share_type | share_name | object_type |           object_name           |   include_new
-------------------+--------------------------------------+------------+------------+-------------+---------------------------------+------------------
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | table       | public.tickit_users_redshift    |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | table       | public.tickit_venue_redshift    |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | table       | public.tickit_category_redshift |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | table       | public.tickit_date_redshift     |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | table       | public.tickit_event_redshift    |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | table       | public.tickit_listing_redshift  |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | table       | public.tickit_sales_redshift    |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | schema      | public                          |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | INBOUND    | salesshare | view        | public.sales_data_summary_view  |
```

Only cluster superusers can do this. You can also use SVV_DATASHARES to
view the datashares and SVV_DATASHARE_OBJECTS to view the objects within the
datashare.

The following example displays the inbound datashares in a consumer
cluster.

```
SHOW DATASHARES LIKE 'sales%';


 share_name | share_owner | source_database | consumer_database | share_type | createdate | is_publicaccessible | share_acl | producer_account |          producer_namespace
------------+-------------+-----------------+-------------------+------------+------------+---------------------+-----------+------------------+--------------------------------------
 salesshare |             |                 |                   | INBOUND    |            |         t           |           |   123456789012   | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d
```

4. Create local databases that reference to the datashares. You must specify
   the ACCOUNT and NAMESPACE option to create local databases for AWS Data Exchange
   datashares. For more information, see [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md").

```
CREATE DATABASE sales_db FROM DATASHARE salesshare OF ACCOUNT '123456789012' NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';
```

If you want more granular control over access to the objects in the local
database, use the WITH PERMISSIONS clause when creating the database. This
lets you grant object-level permissions for objects in the database in step 6.

```
CREATE DATABASE sales_db WITH PERMISSIONS FROM DATASHARE salesshare OF ACCOUNT '123456789012' NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';
```

You can see databases that you created from the datashare by querying the
[SVV_REDSHIFT_DATABASES](r_SVV_REDSHIFT_DATABASES.md "r_SVV_REDSHIFT_DATABASES.md") view. You can connect to these
databases directly, or you can connect to a local database on your consumer
cluster and perform a cross-database query to query the data from the
datashare databases. You can't create a datashare on top of database
objects created from an existing datashare. However, you can copy the data
into a separate table on the consumer cluster, perform any processing
needed, and then share the new objects that were created.

You can also use the Amazon Redshift console to create databases from datashares.
For more information, see [Creating databases from
datashares](query-datashare-console.md#create-database-from-datashare-console "query-datashare-console.md#create-database-from-datashare-console"). 5. (Optional) Create external schemas to refer to and assign granular
permissions to specific schemas in the consumer database imported on the
consumer cluster. For more information, see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md").

```
CREATE EXTERNAL SCHEMA sales_schema FROM REDSHIFT DATABASE 'sales_db' SCHEMA 'public';
```

6. Grant permissions on databases and schema references created from the
   datashares to user or roles in the consumer cluster as needed. For more
   information, see [GRANT](r_GRANT.md "r_GRANT.md") or [REVOKE](r_REVOKE.md "r_REVOKE.md").

```
GRANT USAGE ON DATABASE sales_db TO Bob;
```

```
GRANT USAGE ON SCHEMA sales_schema TO ROLE Analyst_role;
```

If you created your database without WITH PERMISSIONS, you can only
assign permissions on the entire database created from the datashare to your
users and roles. In some cases, you need fine-grained controls on a subset
of database objects created from the datashare. If so, you can create an
external schema reference that points to specific schemas in the datashare
(as described in the previous step) and provide granular permissions at
schema level.

You can also create late-binding views on top of shared objects and use
these to assign granular permissions. You can also consider having producer
clusters create additional datashares for you with the granularity required.
You can create as many schema references to the database created from the
datashare as you need.

If you created your database with WITH PERMISSIONS in step 4, you must
assign object-level permissions for objects in the shared database. A user
with only the USAGE permission can’t access any objects in a database
created with WITH PERMISSIONS until they’re granted additional object-level
permissions..

```
GRANT SELECT ON sales_db.public.tickit_sales_redshift to Bob;
```

7. Query data in the shared objects in the datashares.

Users and roles with permissions on consumer databases and schemas on
consumer clusters can explore and navigate the metadata of any shared
objects. They can also explore and navigate local objects in a consumer
cluster. To do this, they use JDBC or ODBC drivers, the SHOW commands, or
SVV_ALL and SVV_REDSHIFT views.

Producer clusters might have many schemas in the database, tables, and
views within each schema. The users on the consumer side can see only the
subset of objects that are made available through the datashare. These users
can't see the entire metadata from the producer cluster. This approach helps
provide granular metadata security control with data sharing.

You continue to connect to local cluster databases. But now, you can also
read from the databases and schemas that are created from the datashare
using the three-part database.schema.table notation. You can perform queries
that span across any and all databases that are visible to you. These can be
local databases on the cluster or databases created from the datashares. Or,
you can directly connect to these consumer databases and run queries against
the shared objects with partial notation.

You can access the data using full qualification. For more information,
see [Cross-database query examples](cross-database_example.md "cross-database_example.md").

```
SELECT * FROM sales_db.public.tickit_sales_redshift ORDER BY 1,2 LIMIT 5;

 salesid | listid | sellerid | buyerid | eventid | dateid | qtysold | pricepaid | commission |      saletime
---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------
       1 |      1 |    36861 |   21191 |    7872 |   1875 |       4 |    728.00 |     109.20 | 2008-02-18 02:36:48
       2 |      4 |     8117 |   11498 |    4337 |   1983 |       2 |     76.00 |      11.40 | 2008-06-06 05:00:16
       3 |      5 |     1616 |   17433 |    8647 |   1983 |       2 |    350.00 |      52.50 | 2008-06-06 08:26:17
       4 |      5 |     1616 |   19715 |    8647 |   1986 |       1 |    175.00 |      26.25 | 2008-06-09 08:38:52
       5 |      6 |    47402 |   14115 |    8240 |   2069 |       2 |    154.00 |      23.10 | 2008-08-31 09:17:02
```

You can only use SELECT statements on shared objects. However, you can
create tables in the consumer cluster by querying the data from the shared
objects in a different local database.

In addition to queries, consumers can create views on shared objects.
Only late-binding views or materialized views are supported. Amazon Redshift
doesn't support regular views on shared data. Views that consumers
create can span across multiple local databases or databases created from
datashares. For more information, see [CREATE VIEW](r_CREATE_VIEW.md "r_CREATE_VIEW.md").

```
// Connect to a local cluster database

// Create a view on shared objects and access it.
CREATE VIEW sales_data
AS SELECT *
FROM sales_db.public.tickit_sales_redshift
WITH NO SCHEMA BINDING;

SELECT * FROM sales_data;
```
