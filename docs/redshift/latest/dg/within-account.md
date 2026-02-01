Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Sharing read access to data within an

AWS account

With Amazon Redshift, you can share read access to data across different database
users or groups within the same AWS account. This feature allows you to control
data access privileges at a granular level, ensuring that only authorized users or
groups can read specific data sets.

## Share data for read purposes as a producer

administrator or database owner

1. Create datashares in your cluster. For more information, see [CREATE DATASHARE](r_CREATE_DATASHARE.md "r_CREATE_DATASHARE.md").

```
CREATE DATASHARE salesshare;
```

Cluster superuser and database owners can create datashares. Each
datashare is associated with a database during creation. Only objects from
that database can be shared in that datashare. Multiple datashares can be
created on the same database with the same or different granularity of
objects. There is no limit on the number of datashares a cluster can
create.

You can also use the Amazon Redshift console to create datashares. For more
information, see [Create a datashare](datashare-creation.md#create-datashare-console "datashare-creation.md#create-datashare-console"). 2. Delegate permissions to operate on the datashare. For more information,
see [GRANT](r_GRANT.md "r_GRANT.md") or [REVOKE](r_REVOKE.md "r_REVOKE.md").

The following example grants permissions to `dbuser` on
`salesshare`.

```
GRANT ALTER, SHARE ON DATASHARE salesshare TO dbuser;
```

Cluster superusers and the owners of the datashare can grant or revoke
modification permissions on the datashare to additional users. 3. Add objects to or remove objects from datashares. To add objects to a
datashare, add the schema before adding objects. When you add a schema,
Amazon Redshift doesn't add all the objects under it. Make sure to add these
explicitly. For more information, see [ALTER DATASHARE](r_ALTER_DATASHARE.md "r_ALTER_DATASHARE.md").

```
ALTER DATASHARE salesshare ADD SCHEMA PUBLIC;
ALTER DATASHARE salesshare ADD TABLE public.tickit_sales_redshift;
ALTER DATASHARE salesshare ADD ALL TABLES IN SCHEMA PUBLIC;
```

You can also add views to a datashare.

```
CREATE VIEW public.sales_data_summary_view AS SELECT * FROM public.tickit_sales_redshift;
ALTER DATASHARE salesshare ADD VIEW public.sales_data_summary_view;
```

Use ALTER DATASHARE to share schemas, and tables, views, and functions in
a given schema. Superusers, datashare owners, or users who have ALTER or ALL
permission on the datashare can alter the datashare to add objects to or
remove objects from it. Users should have the permissions to add or remove
objects from the datashare. Users should also be the owners of the objects
or have SELECT, USAGE, or ALL permissions on the objects.

You can also use GRANT to add objects to the datashare. This example
shows how:

```
GRANT SELECT ON TABLE public.tickit_sales_redshift TO DATASHARE salesshare;
```

This syntax is functionally equivalent to `ALTER DATASHARE
 salesshare ADD TABLE public.tickit_sales_redshift;`.

Use the INCLUDENEW clause to add any new tables, views, or SQL
user-defined functions (UDFs) created in a specified schema to the
datashare. Only superusers can change this property for each
datashare-schema pair.

```
ALTER DATASHARE salesshare ADD SCHEMA PUBLIC;
ALTER DATASHARE salesshare SET INCLUDENEW = TRUE FOR SCHEMA PUBLIC;
```

You can also use the Amazon Redshift console to add or remove objects from
datashares. For more information, see [Add datashare objects to
datashares](datashare-creation.md#add-datashare-object-console "datashare-creation.md#add-datashare-object-console"), [Removing datashare objects from
datashares](manage-datashare-existing-console.md#remove-datashare-object-console "manage-datashare-existing-console.md#remove-datashare-object-console"), and [Editing datashares created in your
account](manage-datashare-existing-console.md#edit-datashare-console "manage-datashare-existing-console.md#edit-datashare-console"). 4. Add consumers to or remove consumers from datashares. The following
example adds the consumer namespace to `salesshare`. The
namespace is the namespace globally unique identifier (GUID) of the consumer
cluster in the account. For more information, see [GRANT](r_GRANT.md "r_GRANT.md") or [REVOKE](r_REVOKE.md "r_REVOKE.md").

```
GRANT USAGE ON DATASHARE salesshare TO NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';
```

You can only grant permissions to one datashare consumer in a GRANT
statement.

Cluster superusers and the owners of datashare objects or users that have
SHARE permission on the datashare can add consumers to or remove consumers
from a datashare. To do so, they use GRANT USAGE or REVOKE USAGE.

To find the namespace of the cluster that you currently see, you can use
the SELECT CURRENT_NAMESPACE command. To find the namespace of a different
cluster within the same AWS account, go to the Amazon Redshift console cluster
details page. On that page, find the newly added namespace field.

You can also use the Amazon Redshift console to add or remove data consumers for
datashares. For more information, see [Add data consumers to
datashares](datashare-creation.md#add-data-consumer-console "datashare-creation.md#add-data-consumer-console") and [Removing data consumers from
datashares](manage-datashare-existing-console.md#remove-data-consumer-console "manage-datashare-existing-console.md#remove-data-consumer-console"). 5. (Optional) Add security restrictions to the datashare. The following
example shows that the consumer cluster with a public IP access is allowed
to read the datashare. For more information, see [ALTER DATASHARE](r_ALTER_DATASHARE.md "r_ALTER_DATASHARE.md").

```
ALTER DATASHARE salesshare SET PUBLICACCESSIBLE = TRUE;
```

You can modify properties about the type of consumers after datashare
creation. For example, you can define that clusters that want to consume
data from a given datashare can't be publicly accessible. Queries from
consumer clusters that don't meet security restrictions specified in
datashare are rejected at query runtime.

You can also use the Amazon Redshift console to edit datashares. For more
information, see [Editing datashares created in your
account](manage-datashare-existing-console.md#edit-datashare-console "manage-datashare-existing-console.md#edit-datashare-console"). 6. List datashares created in the cluster and look into the contents of the
datashare.

The following example displays the information of a datashare named
`salesshare`.

```
DESC DATASHARE salesshare;

 producer_account  |          producer_namespace          | share_type | share_name | object_type |           object_name          |   include_new
-------------------+--------------------------------------+------------+------------+-------------+--------------------------------+-------------------
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_users_redshift   |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_venue_redshift   |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_category_redshift|
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_date_redshift    |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_event_redshift   |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_listing_redshift |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | table       | public.tickit_sales_redshift   |
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | schema      | public                         |  t
 123456789012      | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | OUTBOUND   | salesshare | view        | public.sales_data_summary_view |
```

The following example displays the outbound datashares in a producer
cluster.

```
SHOW DATASHARES LIKE 'sales%';
```

The output looks similar to the following.

```
share_name | share_owner  | source_database | consumer_database | share_type |     createdate      | is_publicaccessible  | share_acl | producer_account |          producer_namespace
-----------+--------------+-----------------+-------------------+------------+---------------------+----------------------+-----------+------------------+---------------------------------------
salesshare |    100       | dev             |                   |  OUTBOUND  | 2020-12-09 02:27:08 |          True        |           |   123456789012   | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d
```

For more information, see [DESC DATASHARE](r_DESC_DATASHARE.md "r_DESC_DATASHARE.md") and [SHOW DATASHARES](r_SHOW_DATASHARES.md "r_SHOW_DATASHARES.md").

You can also use [SVV_DATASHARES](r_SVV_DATASHARES.md "r_SVV_DATASHARES.md"), [SVV_DATASHARE_CONSUMERS](r_SVV_DATASHARE_CONSUMERS.md "r_SVV_DATASHARE_CONSUMERS.md"), and [SVV_DATASHARE_OBJECTS](r_SVV_DATASHARE_OBJECTS.md "r_SVV_DATASHARE_OBJECTS.md") to view the datashares, the objects within the datashare, and the
datashare consumers. 7. Drop datashares. For more information, see [DROP DATASHARE](r_DROP_DATASHARE.md "r_DROP_DATASHARE.md").

You can delete the datashare objects at any point using [DROP DATASHARE](r_DROP_DATASHARE.md "r_DROP_DATASHARE.md"). Cluster
superusers and owners of datashare can drop datashares.

The following example drops a datashare named
`salesshare`.

```
DROP DATASHARE salesshare;
```

You can also use the Amazon Redshift console to delete datashares. For more
information, see [Deleting a datashare created in your
account](manage-datashare-existing-console.md#delete-datashare-console "manage-datashare-existing-console.md#delete-datashare-console"). 8. Use ALTER DATASHARE to remove objects from datashares at any point from
the datashare. Use REVOKE USAGE ON to revoke permissions on the datashare to
certain consumers. It revokes USAGE permissions on objects within a
datashare and instantly stops access to all consumer clusters. Listing
datashares and the metadata queries, such as listing databases and tables,
doesn't return the shared objects after access is revoked.

```
ALTER DATASHARE salesshare REMOVE TABLE public.tickit_sales_redshift;
```

You can also use the Amazon Redshift console to edit datashares. For more
information, see [Editing datashares created in your
account](manage-datashare-existing-console.md#edit-datashare-console "manage-datashare-existing-console.md#edit-datashare-console"). 9. Revoke access to the datashare from namespaces if you don't want to
share the data with the consumers anymore.

```
REVOKE USAGE ON DATASHARE salesshare FROM NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';
```

You can also use the Amazon Redshift console to edit datashares. For more
information, see [Editing datashares created in your
account](manage-datashare-existing-console.md#edit-datashare-console "manage-datashare-existing-console.md#edit-datashare-console").

## Share data for read purposes as a consumer

administrator

1. List the datashares that are made available to you and view the content
   of datashares. For more information, see [DESC DATASHARE](r_DESC_DATASHARE.md "r_DESC_DATASHARE.md") and [SHOW DATASHARES](r_SHOW_DATASHARES.md "r_SHOW_DATASHARES.md").

The following example displays the information of inbound datashares of a
specified producer namespace. When you run DESC DATASHARE as a consumer
administrator, you must specify the NAMESPACE option to view inbound
datashares.

```
DESC DATASHARE salesshare OF NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';


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

2. As a database superuser, you can create local databases that reference to
   the datashares. For more information, see [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md").

```
CREATE DATABASE sales_db FROM DATASHARE salesshare OF NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';
```

If you want more granular control over access to the objects in the local
database, use the WITH PERMISSIONS clause when creating the database. This
lets you grant object-level permissions for objects in the database in step 4.

```
CREATE DATABASE sales_db WITH PERMISSIONS FROM DATASHARE salesshare OF NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';
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
datashares](query-datashare-console.md#create-database-from-datashare-console "query-datashare-console.md#create-database-from-datashare-console"). 3. (Optional) Create external schemas to refer to and assign granular
permissions to specific schemas in the consumer database imported on the
consumer cluster. For more information, see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md").

```
CREATE EXTERNAL SCHEMA sales_schema FROM REDSHIFT DATABASE 'sales_db' SCHEMA 'public';
```

4. Grant permissions on databases and schema references created from the
   datashares to users and roles in the consumer cluster as needed. For more
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

If you created your database with WITH PERMISSIONS in step 2, you must
assign object-level permissions for objects in the shared database. A user
with only the USAGE permission can’t access any objects in a database
created with WITH PERMISSIONS until they’re granted additional object-level
permissions..

```
GRANT SELECT ON sales_db.public.tickit_sales_redshift to Bob;
```

5. Query data in the shared objects in the datashares.

Users and roles with permissions on consumer databases and schemas on
consumer clusters can explore and navigate the metadata of any shared
objects. They can also explore and navigate local objects in a consumer
cluster. To do this, they use JDBC or ODBC drivers or SVV_ALL and
SVV_REDSHIFT views.

Producer clusters might have many schemas in the database, tables, and
views within each schema. The users on the consumer side can see only the
subset of objects that are made available through the datashare. These users
can't see the entire metadata from the producer cluster. This approach
helps provide granular metadata security control with data sharing.

You continue to connect to local cluster databases. But now, you can also
read from the databases and schemas that are created from the datashare
using the three-part database.schema.table notation. You can perform queries
that span across any and all databases that are visible to you. These can be
local databases on the cluster or databases created from the datashares.
Consumer clusters can't connect to the databases created from the
datashares.

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
