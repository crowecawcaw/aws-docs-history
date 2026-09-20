

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CREATE MATERIALIZED VIEW
<a name="materialized-view-create-sql-command"></a>

Creates a materialized view based on one or more Amazon Redshift tables. You can also base materialized views on external tables created using Spectrum or federated query. For information about Spectrum, see [Amazon Redshift Spectrum](c-using-spectrum.md). For information about federated query, see [Querying data with federated queries in Amazon Redshift](federated-overview.md).

## Syntax
<a name="mv_CREATE_MATERIALIZED_VIEW-synopsis"></a>

```
CREATE MATERIALIZED VIEW mv_name
[ BACKUP { YES | NO } ]
[ table_attributes ]
[ AUTO REFRESH { YES | NO } ]
AS query
```

The following syntax creates a materialized view that stores its data as an Apache Iceberg table. For more information, see [Materialized views stored as Apache Iceberg tables](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-iceberg.html).

```
CREATE MATERIALIZED VIEW mv_name
USING ICEBERG
[LOCATION 's3://bucket/path/']
[PARTITIONED BY (partition_transform [, ...])]
[TABLE PROPERTIES ('property_name' = 'property_value' [, ...])]
AS query
```

where *partition\_transform* is:

```
    column_name |
    YEAR( column_name ) |
    MONTH( column_name ) |
    DAY( column_name ) |
    HOUR( column_name ) |
    BUCKET( integer, column_name ) |
    TRUNCATE( integer, column_name )
```

## Parameters
<a name="mv_CREATE_MATERIALIZED_VIEW-parameters"></a>

BACKUP  
A clause that specifies whether the materialized view should be included in automated and manual cluster snapshots.   
For materialized views that don't contain critical data, specify BACKUP NO to save processing time when creating snapshots and restoring from snapshots and to reduce storage space on Amazon Simple Storage Service. The BACKUP NO setting has no affect on automatic replication of data to other nodes within the cluster, so materialized views with BACKUP NO specified are restored in the event of a node failure. The default is BACKUP YES.

 *table\_attributes*   
A clause that specifies how the data in the materialized view is distributed, including the following:  
+  The distribution style for the materialized view, in the format `DISTSTYLE { EVEN | ALL | KEY }`. If you omit this clause, the distribution style is `EVEN`. For more information, see [Distribution styles](c_choosing_dist_sort.md).
+ The distribution key for the materialized view, in the format `DISTKEY ( distkey_identifier )`. For more information, see [Designating distribution styles](t_designating_distribution_styles.md).
+ The sort key for the materialized view, in the format `SORTKEY ( column_name [, ...] )`. For more information, see [Sort keys](t_Sorting_data.md).

AS *query*  
A valid `SELECT` statement that defines the materialized view and its content. The result set from the query defines the columns and rows of the materialized view. For information about limitations when creating materialized views, see [Limitations](#mv_CREATE_MATERIALIZED_VIEW-limitations).  
Furthermore, specific SQL language constructs used in the query determines whether the materialized view can be incrementally or fully refreshed. For information about the refresh method, see [REFRESH MATERIALIZED VIEW](materialized-view-refresh-sql-command.md). For information about the limitations for incremental refresh, see [Limitations for incremental refresh](materialized-view-refresh-sql-command.md#mv_REFRESH_MARTERIALIZED_VIEW_limitations).  
If the query contains an SQL command that doesn't support incremental refresh, Amazon Redshift displays a message indicating that the materialized view will use a full refresh. The message may or may not be displayed, depending on the SQL client application. Check the `state` column of the [STV\_MV\_INFO](r_STV_MV_INFO.md) to see the refresh type used by a materialized view.

AUTO REFRESH  
A clause that defines whether the materialized view should be automatically refreshed with latest changes from its base tables. The default value is `NO`. For more information, see [Refreshing a materialized view](materialized-view-refresh.md).

USING ICEBERG  
Specifies that the materialized view stores its data as an Apache Iceberg table in Amazon S3. When you specify USING ICEBERG, the materialized view data is written as Parquet files in Iceberg format and registered in the AWS Glue Data Catalog. For more information, see [Materialized views stored as Apache Iceberg tables](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-iceberg.html).

 *mv\_name*   
When you use USING ICEBERG, the materialized view name must use catalog-qualified notation. You can use three-part notation (`awsdatacatalog.{{database}}.{{mv_name}}`), Amazon S3 Tables notation (`"{{bucket}}@s3tablescatalog".{{database}}.{{mv_name}}`), or two-part notation with an external schema (`{{external_schema}}.{{mv_name}}`). The target database must exist in the AWS Glue Data Catalog.

LOCATION  
The Amazon S3 path where Iceberg data and metadata files are stored. The path must point to an empty location. The Amazon S3 bucket must be in the same AWS Region as the Amazon Redshift cluster or workgroup. Omit this parameter when using Amazon S3 Table Buckets, because Amazon S3 Tables manages the storage location automatically. For tables created using external schemas or the `awsdatacatalog` root catalog, LOCATION is required.

PARTITIONED BY (partition\_transform [, ...])  
Specifies one or more Iceberg partition transforms for the materialized view. Amazon Redshift supports all Iceberg v2 partition transforms except `void`. A single column cannot appear in multiple transforms.

TABLE PROPERTIES ('property\_name' = 'property\_value' [, ...])  
Specifies Iceberg table properties. For example, use `'write.parquet.compression-codec' = 'zstd'` to set the Parquet compression codec.

## Usage notes
<a name="mv_CREATE_MARTERIALIZED_VIEW_usage"></a>

To create a materialized view, you must have the following privileges:
+ CREATE privileges for a schema.
+ Table-level or column-level SELECT privilege on the base tables to create a materialized view. If you have column-level privileges on specific columns, you can create a materialized view on only those columns.

 You can create a materialized view from a remote datasharing cluster by providing the external database name at the `mv_name`. 

### Iceberg materialized views
<a name="mv_CREATE_MATERIALIZED_VIEW_iceberg_usage"></a>

To create an Iceberg materialized view, you must have CREATE TABLE permission in the target AWS Glue Data Catalog database. The IAM role associated with the external schema (the MV definer role) must have SELECT permission via AWS Lake Formation on all source tables referenced in the query.

All identifiers in the materialized view definition (table names, column names, aliases) must be lowercase. The AWS Glue Data Catalog stores identifiers in lowercase for Hive compatibility. Amazon Redshift rejects CREATE MATERIALIZED VIEW statements with USING ICEBERG that contain uppercase identifiers.

Creating or refreshing Iceberg materialized views is not supported when `enable_case_sensitive_identifier` is set to `true`. This restriction exists because the AWS Glue Data Catalog does not support case-sensitive identifiers. If your cluster or workgroup has `enable_case_sensitive_identifier` enabled, set it to `false` for the session before creating or refreshing Iceberg materialized views:

```
SET enable_case_sensitive_identifier TO false;
```

Source tables must be in Apache Iceberg format version 2 or lower. Non-Iceberg tables cannot be used as source tables for Iceberg materialized views.

You can't use the following with Iceberg materialized views:
+ BACKUP clause
+ DISTSTYLE, DISTKEY, or SORTKEY clauses
+ References to Amazon Redshift native tables, temporary tables, or system tables

For more information about Iceberg materialized view capabilities and limitations, see [Materialized views stored as Apache Iceberg tables](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-iceberg.html).

## Incremental refresh for materialized views in a datashare
<a name="mv_CREATE_MARTERIALIZED_VIEW_datashare"></a>

 Amazon Redshift supports automatic and incremental refresh for materialized views in a consumer datashare when the base tables are shared. Incremental refresh is an operation where Amazon Redshift identifies changes in the base table or tables that happened after the previous refresh and updates only the corresponding records in the materialized view. This runs more quickly than a full refresh and improves workload performance. You don't have to change your materialized-view definition to take advantage of incremental refresh. 

There are a couple limitations to note for taking advantage of incremental refresh with a materialized view: 
+ The materialized view must reference only one database, either local or remote. 
+ Incremental refresh is available only on new materialized views. Therefore, you must drop existing materialized views and recreate them for incremental refresh to occur.

For more information about creating materialized views in a datashare, see [Working with views in Amazon Redshift data sharing](https://docs.aws.amazon.com/redshift/latest/dg/datashare-views), which contains several query examples.

## DDL updates to materialized views or base tables
<a name="materialized-view-ddl"></a>

When using materialized views in Amazon Redshift, follow these usage notes for data definition language (DDL) updates to materialized views or base tables.
+ You can add columns to a base table without affecting any materialized views that reference the base table.
+ Some operations can leave the materialized view in a state that can't be refreshed at all. Examples are operations such as renaming or dropping a column, changing the type of a column, and changing the name of a schema. Such materialized views can be queried but can't be refreshed. In this case, you must drop and recreate the materialized view. 
+ In general, you can't alter a materialized view's definition (its SQL statement).
+ You can't rename a materialized view. 

## Limitations
<a name="mv_CREATE_MATERIALIZED_VIEW-limitations"></a>

You can't define a materialized view that references or includes any of the following:
+ Standard views, or system tables and views.
+ Temporary tables.
+ User-defined functions.
+ The ORDER BY, LIMIT, or OFFSET clause.
+ Late-binding references to base tables. In other words, any base tables or related columns referenced in the defining SQL query of the materialized view must exist and must be valid. 
+ Leader node-only functions: CURRENT\_SCHEMA, CURRENT\_SCHEMAS, HAS\_DATABASE\_PRIVILEGE, HAS\_SCHEMA\_PRIVILEGE, HAS\_TABLE\_PRIVILEGE.
+ You can't use the AUTO REFRESH YES option when the materialized view definition includes mutable functions or external schemas. You also can't use it when you define a materialized view on another materialized view.
+ You don't have to manually run [ANALYZE](r_ANALYZE.md) on materialized views. This happens currently only by using AUTO ANALYZE. For more information, see [Analyzing tables](t_Analyzing_tables.md).
+ RLS-protected or DDM-protected tables. 
+ Materialized view creation from remote datasharing clusters does not support references on other materialized views, Spectrum tables, tables defined in a different Redshift cluster and UDFs. These are supported for materialized view creation from the local (producer) cluster. 

For Iceberg materialized views created with USING ICEBERG, the following additional limitations apply:
+ Source tables must be in Apache Iceberg format.
+ All identifiers must be lowercase.
+ User-defined functions and mutable functions are not allowed.
+ Source tables must be in the same AWS Region and account as the materialized view.
+ AWS Lake Formation filtered (FGAC) tables cannot be used as source tables.

## Examples
<a name="mv_CREATE_MARTERIALIZED_VIEW_examples"></a>

The following example creates a materialized view from three base tables that are joined and aggregated. Each row represents a category with the number of tickets sold. When you query the tickets\_mv materialized view, you directly access the precomputed data in the tickets\_mv materialized view.

```
CREATE MATERIALIZED VIEW tickets_mv AS
    select   catgroup,
    sum(qtysold) as sold
    from     category c, event e, sales s
    where    c.catid = e.catid
    and      e.eventid = s.eventid
    group by catgroup;
```

The following example creates a materialized view similar to the previous example and uses the aggregate function MAX(). 

```
CREATE MATERIALIZED VIEW tickets_mv_max AS
    select   catgroup,
    max(qtysold) as sold
    from     category c, event e, sales s
    where    c.catid = e.catid
    and      e.eventid = s.eventid
    group by catgroup;

SELECT name, state FROM STV_MV_INFO;
```

The following example uses a UNION ALL clause to join the Amazon Redshift `public_sales` table and the Redshift Spectrum `spectrum.sales` table to create a material view `mv_sales_vw`. For information about the CREATE EXTERNAL TABLE command for Amazon Redshift Spectrum, see [CREATE EXTERNAL TABLE](r_CREATE_EXTERNAL_TABLE.md). The Redshift Spectrum external table references the data on Amazon S3.

```
CREATE MATERIALIZED VIEW mv_sales_vw as
select salesid, qtysold, pricepaid, commission, saletime from public.sales
union all
select salesid, qtysold, pricepaid, commission, saletime from spectrum.sales
```

The following example creates a materialized view `mv_fq` based on a federated query external table. For information about federated query, see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md).

```
CREATE MATERIALIZED VIEW mv_fq as select firstname, lastname from apg.mv_fq_example;

select firstname, lastname from mv_fq;
 firstname | lastname
-----------+----------
 John      | Day
 Jane      | Doe
(2 rows)
```

The following example shows the definition of a materialized view.

```
SELECT pg_catalog.pg_get_viewdef('mv_sales_vw'::regclass::oid, true);

pg_get_viewdef
---------------------------------------------------
create materialized view mv_sales_vw as select a from t;
```

 The following sample shows how to set AUTO REFRESH in the materialized view definition and also specifies a DISTSTYLE. First, create a simple base table. 

```
CREATE TABLE baseball_table (ball int, bat int);
```

Then, create a materialized view.

```
CREATE MATERIALIZED VIEW mv_baseball DISTSTYLE ALL AUTO REFRESH YES AS SELECT ball AS baseball FROM baseball_table;
```

Now you can query the mv\_baseball materialized view. To check if AUTO REFRESH is turned on for a materialized view, see [STV\_MV\_INFO](r_STV_MV_INFO.md).

The following sample creates a materialized view that references a source table in another database. It assumes that the database containing the source table, database\_A, is in the same cluster or workgroup as your materialized view, which you create in database\_B. (You can substitute your own databases for the sample.) First, create a table in database\_A called *cities*, with a *cityname* column. Make the column's data type a VARCHAR. After you create the source table, run the following command in database\_B to create a materialized view whose source is your *cities* table. Make sure to specify the source table's database and schema in the FROM clause:

```
CREATE MATERIALIZED VIEW cities_mv AS
SELECT  cityname
FROM    database_A.public.cities;
```

Query the materialized view you created. The query retrieves records whose original source is the *cities* table in database\_A:

```
select * from cities_mv;
```

When you run the SELECT statement, *cities\_mv* returns the records. Records are refreshed from the source table only when a REFRESH statement is run. Also, note that you can't update records directly in the materialized view. For information about refreshing the data in a materialized view, see [REFRESH MATERIALIZED VIEW](materialized-view-refresh-sql-command.md).

For details about materialized view overview and SQL commands used to refresh and drop materialized views, see the following topics:
+ [Materialized views in Amazon Redshift](materialized-view-overview.md)
+ [REFRESH MATERIALIZED VIEW](materialized-view-refresh-sql-command.md)
+ [DROP MATERIALIZED VIEW](materialized-view-drop-sql-command.md)

The following example creates an Iceberg materialized view in an Amazon S3 Table Bucket with partitioning.

```
CREATE MATERIALIZED VIEW "my-bucket@s3tablescatalog".analytics.sales_by_region
USING ICEBERG
PARTITIONED BY (region)
AS SELECT region, count(*) as order_count, sum(amount) as total_sales
   FROM "my-bucket@s3tablescatalog".production.orders
   GROUP BY region;
```

The following example creates an Iceberg materialized view in a general-purpose Amazon S3 bucket with a partition transform and compression specified.

```
CREATE MATERIALIZED VIEW awsdatacatalog.mydb.daily_revenue
USING ICEBERG
LOCATION 's3://my-analytics-bucket/mvs/daily_revenue/'
PARTITIONED BY (day(order_date))
TABLE PROPERTIES ('write.parquet.compression-codec' = 'zstd')
AS SELECT order_date, sum(amount) as revenue, count(*) as num_orders
   FROM awsdatacatalog.mydb.orders
   GROUP BY order_date;
```

The following example creates an Iceberg materialized view using an external schema with two-part notation.

```
CREATE MATERIALIZED VIEW my_ext_schema.customer_totals
USING ICEBERG
LOCATION 's3://my-analytics-bucket/mvs/customer_totals/'
AS SELECT customer_id, count(*) as order_count, sum(amount) as total_spent
   FROM my_ext_schema.orders
   GROUP BY customer_id;
```