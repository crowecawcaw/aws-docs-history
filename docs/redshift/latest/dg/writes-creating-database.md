Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a database from a datashare in

Amazon Redshift

With Amazon Redshift, you can use a datashare to create a database, and then query data
across datashares from producer clusters to securely access live data without
copying or transferring it. The following steps cover the details of setting up a
database in your Amazon Redshift environment.

Console
Before you can query data in the datashare, you must create a database
from a datashare. You can create only one database from a specified
datashare.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**,
   then choose your cluster. The cluster details page appears.
3. Choose **Datashares**. The datashare list
   appears.
4. In the **Datashares from other clusters**
   section, choose **Connect to database**. For more
   information, see [Connecting to a database](connect-database-console.md "connect-database-console.md").
5. Choose a datashare that you want to create databases from, then
   choose **Create database from datashare**. The
   Create database from datashare page appears.
6. In the **Database name**, specify a database
   name. The database name must be 1–64 alphanumeric characters
   (lowercase only) and it can't be a reserved word.
7. Choose **Create**.

After the database is created, you can query data in the database or
perform write operations, if they have been granted, authorized, and
associated by the consumer administrator.

API
To share data for read purposes as a consumer administrator, perform
the following steps.

1. List the datashares that are made available to you and view the
   content of datashares. For more information, see [DESC DATASHARE](r_DESC_DATASHARE.md "r_DESC_DATASHARE.md")
   and [SHOW DATASHARES](r_SHOW_DATASHARES.md "r_SHOW_DATASHARES.md").

The following example displays the information of inbound
datashares of a specified producer namespace. When you run DESC
DATASHARE as a consumer administrator, you must specify the
NAMESPACE option to view inbound datashares.

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

Only cluster superusers can do this. You can also use
SVV_DATASHARES to view the datashares and SVV_DATASHARE_OBJECTS to
view the objects within the datashare.

The following example displays the inbound datashares in a
consumer cluster.

```
SHOW DATASHARES LIKE 'sales%';


 share_name | share_owner | source_database | consumer_database | share_type | createdate | is_publicaccessible | share_acl | producer_account |          producer_namespace
------------+-------------+-----------------+-------------------+------------+------------+---------------------+-----------+------------------+--------------------------------------
 salesshare |             |                 |                   | INBOUND    |            |         t           |           |   123456789012   | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d
```

2. As a database superuser, you can create local databases that
   reference to the datashares. For more information, see [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md").

```
CREATE DATABASE sales_db FROM DATASHARE salesshare OF NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';
```

If you want more granular control over access to the objects in
the local database, use the WITH PERMISSIONS clause when creating
the database. This lets you grant object-level permissions for
objects in the database in step 4.

```
CREATE DATABASE sales_db WITH PERMISSIONS FROM DATASHARE salesshare OF NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';
```

You can see databases that you created from the datashare by
querying the [SVV_REDSHIFT_DATABASES](r_SVV_REDSHIFT_DATABASES.md "r_SVV_REDSHIFT_DATABASES.md") view. You can connect
to these databases directly, or you can connect to a local database
on your consumer cluster and perform a cross-database query to
query the data from the datashare databases.

###### Note

You can't create a datashare on top of database objects
created from an existing datashare. However, you can copy the
data into a separate table on the consumer cluster, perform any
processing needed, and then share the new objects that were
created.

You can also use the Amazon Redshift console to create databases from
datashares. For more information, see [Creating databases from
datashares](query-datashare-console.md#create-database-from-datashare-console "query-datashare-console.md#create-database-from-datashare-console").
