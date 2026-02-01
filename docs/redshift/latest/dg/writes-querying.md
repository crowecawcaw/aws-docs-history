Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Querying data in a datashare in Amazon Redshift

With Amazon Redshift, you can query data across datashares from producer clusters to
securely access live data without copying or transferring it. The following
section covers querying datashares in your Amazon Redshift environment.

Users and roles with permissions on consumer databases and schemas on consumer
clusters can explore and navigate the metadata of any shared objects. They can
also explore and navigate local objects in a consumer cluster. To do this, they
use JDBC or ODBC drivers or SVV_ALL and SVV_REDSHIFT views.

Producer clusters might have many schemas in the database, tables, and views
within each schema. The users on the consumer side can see only the subset of
objects that are made available through the datashare. These users can't see
the entire metadata from the producer cluster. This approach helps provide
granular metadata security control with data sharing.

You continue to connect to local cluster databases. But now, you can also read
from the databases and schemas that are created from the datashare using the
three-part database.schema.table notation. You can perform queries that span
across any and all databases that are visible to you. These can be local databases
on the cluster or databases created from the datashares. Consumer clusters
can't connect to the databases created from the datashares.

You can access the data using full qualification. For more information, see
[Cross-database query examples](cross-database_example.md "cross-database_example.md").

SQL

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
create tables in the consumer cluster by querying the data from the
shared objects in a different local database.
