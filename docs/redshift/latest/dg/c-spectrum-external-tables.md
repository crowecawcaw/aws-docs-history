Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# External tables for Redshift Spectrum

This topic describes how to create and use external tables with Redshift Spectrum.
External tables are tables that you use as references to access data outside your
Amazon Redshift cluster. These tables contain metadata about the external data that Redshift Spectrum reads.

You create an external table in an external schema. To create external tables, you must
be the owner of the external schema or a superuser. To transfer ownership of an external
schema, use [ALTER SCHEMA](r_ALTER_SCHEMA.md "r_ALTER_SCHEMA.md") to change the
owner. The following example changes the owner of the `spectrum_schema` schema
to `newowner`.

```
alter schema spectrum_schema owner to newowner;
```

To run a Redshift Spectrum query, you need the following permissions:

- Usage permission on the schema
- Permission to create temporary tables in the current database
  The following example grants usage permission on the schema `spectrum_schema`
  to the `spectrumusers` user group.

```
grant usage on schema spectrum_schema to group spectrumusers;
```

The following example grants temporary permission on the database
`spectrumdb` to the `spectrumusers` user group.

```
grant temp on database spectrumdb to group spectrumusers;
```

You can create an external table in Amazon Redshift, AWS Glue, Amazon Athena, or an Apache Hive metastore.
For more information, see [Getting Started
Using AWS Glue](../../../glue/latest/dg/getting-started.md "../../../glue/latest/dg/getting-started.md") in the _AWS Glue Developer Guide_, [Getting Started](../../../athena/latest/ug/getting-started.md "../../../athena/latest/ug/getting-started.md") in the _Amazon Athena User Guide_, or [Apache Hive](../../../emr/latest/ReleaseGuide/emr-hive.md "../../../emr/latest/ReleaseGuide/emr-hive.md") in the
_Amazon EMR Developer Guide_.

If your external table is defined in AWS Glue, Athena, or a Hive metastore, you first create
an external schema that references the external database. Then you can reference the
external table in your SELECT statement by prefixing the table name with the schema name,
without needing to create the table in Amazon Redshift. For more information, see [External schemas in Amazon Redshift
Spectrum](c-spectrum-external-schemas.md "c-spectrum-external-schemas.md").

To allow Amazon Redshift to view tables in the AWS Glue Data Catalog, add `glue:GetTable` to the
Amazon Redshift IAM role. Otherwise you might get an error similar to the following.

```
RedshiftIamRoleSession is not authorized to perform: glue:GetTable on resource: *;
```

For example, suppose that you have an external table named `lineitem_athena`
defined in an Athena external catalog. In this case, you can define an external schema named
`athena_schema`, then query the table using the following SELECT
statement.

```
select count(*) from athena_schema.lineitem_athena;
```

To define an external table in Amazon Redshift, use the [CREATE EXTERNAL TABLE](r_CREATE_EXTERNAL_TABLE.md "r_CREATE_EXTERNAL_TABLE.md") command. The external table statement defines
the table columns, the format of your data files, and the location of your data in Amazon S3.
Redshift Spectrum scans the files in the specified folder and any subfolders. Redshift
Spectrum ignores hidden files and files that begin with a period, underscore, or hash mark
( . , \_, or #) or end with a tilde (~).

The following example creates a table named SALES in the Amazon Redshift external schema named
`spectrum`. The data is in tab-delimited text files.

```
create external table spectrum.sales(
salesid integer,
listid integer,
sellerid integer,
buyerid integer,
eventid integer,
dateid smallint,
qtysold smallint,
pricepaid decimal(8,2),
commission decimal(8,2),
saletime timestamp)
row format delimited
fields terminated by '\t'
stored as textfile
location 's3://redshift-downloads/tickit/spectrum/sales/'
table properties ('numRows'='172000');
```

To view external tables, query the [SVV_EXTERNAL_TABLES](r_SVV_EXTERNAL_TABLES.md "r_SVV_EXTERNAL_TABLES.md") system view.

## Pseudocolumns

By default, Amazon Redshift creates external tables with the pseudocolumns `$path`,
`$size`, and `$spectrum_oid`. Select the `$path`
column to view the path to the data files on
Amazon S3,
and select the `$size` column to view the size of the data files for each row
returned by a query. The `$spectrum_oid` column provides the ability to
perform correlated queries with Redshift Spectrum. For an example, see [Example: Performing correlated subqueries in Redshift Spectrum](c_performing-correlated-subqueries-spectrum.md "c_performing-correlated-subqueries-spectrum.md"). You must delimit the `$path`,
`$size`, and `$spectrum_oid` column names with double quotation
marks. A SELECT \* clause doesn't return the pseudocolumns. You must explicitly
include the `$path`, `$size`, and `$spectrum_oid`
column names in your query, as the following example shows.

```
select "$path", "$size", "$spectrum_oid"
from spectrum.sales_part where saledate = '2008-12-01';
```

You can disable
the
creation of pseudocolumns for a session by setting the
`spectrum_enable_pseudo_columns` configuration parameter to `false`. For
more information, see [spectrum_enable_pseudo_columns](r_spectrum_enable_pseudo_columns.md "r_spectrum_enable_pseudo_columns.md"). You can also disable only the
`$spectrum_oid` pseudocolumn by setting the
`enable_spectrum_oid` to `false`.
For more information, see [enable_spectrum_oid](r_spectrum_enable_spectrum_oid.md "r_spectrum_enable_spectrum_oid.md"). However, disabling the
`$spectrum_oid` pseudocolumn also disables support for correlated queries with Redshift Spectrum.

###### Important

Selecting `$size`, `$path`, or `$spectrum_oid` incurs charges because Redshift Spectrum scans the
data files on Amazon S3 to determine the size of the result set. For
more information, see [Amazon Redshift
Pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").

### Pseudocolumns

example

The following example returns the total size of related data files for an external
table.

```
select distinct "$path", "$size"
from spectrum.sales_part;

 $path                                                                    | $size
--------------------------------------------------------------------------+-------
s3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-01/ |  1616
s3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-02/ |  1444
s3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-03/ |  1644
```

## Partitioning Redshift Spectrum external

tables

When you partition your data, you can restrict the amount of data that Redshift
Spectrum scans by filtering on the partition key. You can partition your data by any
key.

A common practice is to partition the data based on time. For example, you might
choose to partition by year, month, date, and hour. If you have data coming from
multiple sources, you might partition by a data source identifier and date.

The following procedure describes how to partition your data.

###### To partition your data

1. Store your data in folders in Amazon S3 according to your partition key.

Create one folder for each partition value and name the folder with the
partition key and value. For example, if you partition by date, you might have
folders named `saledate=2017-04-01`, `saledate=2017-04-02`,
and so on. Redshift Spectrum scans the files in the partition folder and any
subfolders. Redshift Spectrum ignores hidden files and files that begin with a
period, underscore, or hash mark ( . , \_, or #) or end with a tilde (~). 2. Create an external table and specify the partition key in the PARTITIONED BY
clause.

The partition key can't be the name of a table column. The data type can
be SMALLINT, INTEGER, BIGINT, DECIMAL, REAL, DOUBLE PRECISION, BOOLEAN, CHAR, VARCHAR, DATE, or TIMESTAMP data type. 3. Add the partitions.

Using [ALTER TABLE](r_ALTER_TABLE.md "r_ALTER_TABLE.md") … ADD
PARTITION, add each partition, specifying the partition column and key value, and
the location of the partition folder in Amazon S3. You can add multiple partitions in a
single ALTER TABLE … ADD statement. The following example adds partitions for
`'2008-01'` and `'2008-03'`.

```
alter table spectrum.sales_part add
partition(saledate='2008-01-01')
location 's3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-01/'
partition(saledate='2008-03-01')
location 's3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-03/';
```

###### Note

If you use the AWS Glue catalog, you can add up to 100 partitions using a
single ALTER TABLE statement.

### Partitioning data

examples

In this example, you create an external table that is partitioned by a single
partition key and an external table that is partitioned by two partition keys.

The sample data for this example is located in an Amazon S3 bucket that gives read
access to all authenticated AWS users. Your cluster and your external data files must
be in the same AWS Region. The sample data bucket is in the US East (N. Virginia) Region
(us-east-1). To access the data using Redshift Spectrum, your cluster must also be in
us-east-1. To list the folders in Amazon S3, run the following command.

```
aws s3 ls s3://redshift-downloads/tickit/spectrum/sales_partition/
```

```
PRE saledate=2008-01/
PRE saledate=2008-03/
PRE saledate=2008-04/
PRE saledate=2008-05/
PRE saledate=2008-06/
PRE saledate=2008-12/
```

If you don't already have an external schema, run the following command.
Substitute the Amazon Resource Name (ARN) for your AWS Identity and Access Management (IAM) role.

```
create external schema spectrum
from data catalog
database 'spectrumdb'
iam_role 'arn:aws:iam::123456789012:role/myspectrumrole'
create external database if not exists;
```

#### Example 1:

Partitioning with a single partition key

In the following example, you create an external table that is partitioned by
month.

To create an external table partitioned by month, run the following
command.

```
create external table spectrum.sales_part(
salesid integer,
listid integer,
sellerid integer,
buyerid integer,
eventid integer,
dateid smallint,
qtysold smallint,
pricepaid decimal(8,2),
commission decimal(8,2),
saletime timestamp)
partitioned by (saledate char(10))
row format delimited
fields terminated by '|'
stored as textfile
location 's3://redshift-downloads/tickit/spectrum/sales_partition/'
table properties ('numRows'='172000');
```

To add the partitions, run the following ALTER TABLE command.

```
alter table spectrum.sales_part add
partition(saledate='2008-01')
location 's3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-01/'

partition(saledate='2008-03')
location 's3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-03/'

partition(saledate='2008-04')
location 's3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-04/';
```

To select data from the partitioned table, run the following query.

```
select top 5 spectrum.sales_part.eventid, sum(spectrum.sales_part.pricepaid)
from spectrum.sales_part, event
where spectrum.sales_part.eventid = event.eventid
  and spectrum.sales_part.pricepaid > 30
  and saledate = '2008-01'
group by spectrum.sales_part.eventid
order by 2 desc;
```

```
eventid | sum
--------+---------
   4124 | 21179.00
   1924 | 20569.00
   2294 | 18830.00
   2260 | 17669.00
   6032 | 17265.00
```

To view external table partitions, query the [SVV_EXTERNAL_PARTITIONS](r_SVV_EXTERNAL_PARTITIONS.md "r_SVV_EXTERNAL_PARTITIONS.md")
system view.

```
select schemaname, tablename, values, location from svv_external_partitions
where tablename = 'sales_part';
```

```
schemaname | tablename  | values      | location
-----------+------------+-------------+-------------------------------------------------------------------------
spectrum   | sales_part | ["2008-01"] | s3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-01
spectrum   | sales_part | ["2008-03"] | s3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-03
spectrum   | sales_part | ["2008-04"] | s3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-04
```

#### Example 2:

Partitioning with a multiple partition key

To create an external table partitioned by `date` and
`eventid`, run the following command.

```
create external table spectrum.sales_event(
salesid integer,
listid integer,
sellerid integer,
buyerid integer,
eventid integer,
dateid smallint,
qtysold smallint,
pricepaid decimal(8,2),
commission decimal(8,2),
saletime timestamp)
partitioned by (salesmonth char(10), event integer)
row format delimited
fields terminated by '|'
stored as textfile
location 's3://redshift-downloads/tickit/spectrum/salesevent/'
table properties ('numRows'='172000');
```

To add the partitions, run the following ALTER TABLE command.

```
alter table spectrum.sales_event add
partition(salesmonth='2008-01', event='101')
location 's3://redshift-downloads/tickit/spectrum/salesevent/salesmonth=2008-01/event=101/'

partition(salesmonth='2008-01', event='102')
location 's3://redshift-downloads/tickit/spectrum/salesevent/salesmonth=2008-01/event=102/'

partition(salesmonth='2008-01', event='103')
location 's3://redshift-downloads/tickit/spectrum/salesevent/salesmonth=2008-01/event=103/'

partition(salesmonth='2008-02', event='101')
location 's3://redshift-downloads/tickit/spectrum/salesevent/salesmonth=2008-02/event=101/'

partition(salesmonth='2008-02', event='102')
location 's3://redshift-downloads/tickit/spectrum/salesevent/salesmonth=2008-02/event=102/'

partition(salesmonth='2008-02', event='103')
location 's3://redshift-downloads/tickit/spectrum/salesevent/salesmonth=2008-02/event=103/'

partition(salesmonth='2008-03', event='101')
location 's3://redshift-downloads/tickit/spectrum/salesevent/salesmonth=2008-03/event=101/'

partition(salesmonth='2008-03', event='102')
location 's3://redshift-downloads/tickit/spectrum/salesevent/salesmonth=2008-03/event=102/'

partition(salesmonth='2008-03', event='103')
location 's3://redshift-downloads/tickit/spectrum/salesevent/salesmonth=2008-03/event=103/';
```

Run the following query to select data from the partitioned table.

```
select spectrum.sales_event.salesmonth, event.eventname, sum(spectrum.sales_event.pricepaid)
from spectrum.sales_event, event
where spectrum.sales_event.eventid = event.eventid
  and salesmonth = '2008-02'
	and (event = '101'
	or event = '102'
	or event = '103')
group by event.eventname, spectrum.sales_event.salesmonth
order by 3 desc;
```

```
salesmonth | eventname       | sum
-----------+-----------------+--------
2008-02    | The Magic Flute | 5062.00
2008-02    | La Sonnambula   | 3498.00
2008-02    | Die Walkure     |  534.00
```

## Mapping external table columns to ORC

columns

You use Amazon Redshift Spectrum external tables to query data from files in ORC format.
Optimized row columnar (ORC) format is a columnar storage file format that supports
nested data structures. For more information about querying nested data, see [Querying Nested Data with Amazon Redshift
Spectrum](tutorial-query-nested-data.md#tutorial-nested-data-overview "tutorial-query-nested-data.md#tutorial-nested-data-overview").

When you create an external table that references data in an ORC file, you map each
column in the external table to a column in the ORC data. To do so, you use one of the
following methods:

- [Mapping by position](#orc-mapping-by-position "#orc-mapping-by-position")
- [Mapping by column name](#orc-mapping-by-name "#orc-mapping-by-name")

Mapping by column name is the default.

### Mapping by position

With position mapping, the first column defined in the external table maps to the
first column in the ORC data file, the second to the second, and so on. Mapping by
position requires that the order of columns in the external table and in the ORC file
match. If the order of the columns doesn't match, then you can map the columns by
name.

###### Important

In earlier releases, Redshift Spectrum used position mapping by default. If you
need to continue using position mapping for existing tables, set the table
property `orc.schema.resolution` to `position`, as the
following example shows.

```
alter table spectrum.orc_example
set table properties('orc.schema.resolution'='position');
```

For example, the table `SPECTRUM.ORC_EXAMPLE` is defined as follows.

```
create external table spectrum.orc_example(
int_col int,
float_col float,
nested_col struct<
  "int_col" : int,
  "map_col" : map<int, array<float >>
   >
) stored as orc
location 's3://example/orc/files/';
```

The table structure can be abstracted as follows.

```
• 'int_col' : int
• 'float_col' : float
• 'nested_col' : struct
   o 'int_col' : int
   o 'map_col' : map
      - key : int
      - value : array
         - value : float
```

The underlying ORC file has the following file structure.

```
• ORC file root(id = 0)
   o 'int_col' : int (id = 1)
   o 'float_col' : float (id = 2)
   o 'nested_col' : struct (id = 3)
      - 'int_col' : int (id = 4)
      - 'map_col' : map (id = 5)
         - key : int (id = 6)
         - value : array (id = 7)
            - value : float (id = 8)
```

In this example, you can map each column in the external table to a column in ORC
file strictly by position. The following shows the mapping.

| External table column name    | ORC column ID | ORC column name |
| ----------------------------- | ------------- | --------------- |
| int_col                       | 1             | int_col         |
| float_col                     | 2             | float_col       |
| nested_col                    | 3             | nested_col      |
| nested_col.int_col            | 4             | int_col         |
| nested_col.map_col            | 5             | map_col         |
| nested_col.map_col.key        | 6             | NA              |
| nested_col.map_col.value      | 7             | NA              |
| nested_col.map_col.value.item | 8             | NA              |

### Mapping by column name

Using name mapping, you map columns in an external table to named columns in ORC
files on the same level, with the same name.

For example, suppose that you want to map the table from the previous example,
`SPECTRUM.ORC_EXAMPLE`, with an ORC file that uses the following file
structure.

```
• ORC file root(id = 0)
   o 'nested_col' : struct (id = 1)
      - 'map_col' : map (id = 2)
         - key : int (id = 3)
         - value : array (id = 4)
            - value : float (id = 5)
      - 'int_col' : int (id = 6)
   o 'int_col' : int (id = 7)
   o 'float_col' : float (id = 8)
```

Using position mapping, Redshift Spectrum attempts the following mapping.

| External table column name | ORC column ID | ORC column name |
| -------------------------- | ------------- | --------------- |
| int_col                    | 1             | struct          |
| float_col                  | 7             | int_col         |
| nested_col                 | 8             | float_col       |

When you query a table with the preceding position mapping, the SELECT command
fails on type validation because the structures are different.

You can map the same external table to both file structures shown in the previous
examples by using column name mapping. The table columns `int_col`,
`float_col`, and `nested_col` map by column name to columns
with the same names in the ORC file. The column named `nested_col` in the
external table is a `struct` column with subcolumns named
`map_col` and `int_col`. The subcolumns also map correctly
to the corresponding columns in the ORC file by column name.

## Creating external tables for data managed in

Apache Hudi

To query data in Apache Hudi Copy On Write (CoW) format, you can use Amazon Redshift Spectrum external
tables. A Hudi Copy On Write table is a collection of Apache Parquet files stored in
Amazon S3.

You can read Copy On Write (CoW) tables in Apache Hudi versions 0.5.2, 0.6.0, 0.7.0, 0.8.0, 0.9.0, 0.10.0, 0.10.1, 0.11.0, and 0.11.1
that are created and modified with insert, delete, and upsert write operations.
For example, bootstrap tables are not supported.
For more information, see
[Copy On Write
Table](https://hudi.apache.org/docs/next/table_types#copy-on-write-table "https://hudi.apache.org/docs/next/table_types#copy-on-write-table")

in the open source Apache Hudi documentation.

When you create an external table that references data in Hudi CoW format, you map each
column in the external table to a column in the Hudi data. Mapping is done by column.

The data definition language (DDL) statements for partitioned and unpartitioned Hudi
tables are similar to those for other Apache Parquet file formats. For Hudi tables, you
define `INPUTFORMAT` as
`org.apache.hudi.hadoop.HoodieParquetInputFormat`. The
`LOCATION` parameter must point to the Hudi table base folder that
contains the `.hoodie` folder, which is required to establish the Hudi commit
timeline. In some cases, a SELECT operation on a Hudi table might fail with the message
**`No valid Hudi commit timeline found`**. If so, check if the
`.hoodie` folder is in the correct location and contains a valid Hudi
commit timeline.

###### Note

Apache Hudi format is only supported when you use an AWS Glue Data Catalog. It's not supported when you
use an Apache Hive metastore as the external catalog.

The DDL to define an unpartitioned table has the following format.

```
CREATE EXTERNAL TABLE *tbl\_name* (*columns*)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS
INPUTFORMAT 'org.apache.hudi.hadoop.HoodieParquetInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://*s3-bucket*/*prefix*'
```

The DDL to define a partitioned table has the following format.

```
CREATE EXTERNAL TABLE *tbl\_name* (*columns*)
PARTITIONED BY(*pcolumn1* *pcolumn1-type*[,...])
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS
INPUTFORMAT 'org.apache.hudi.hadoop.HoodieParquetInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://*s3-bucket*/*prefix*'
```

To add partitions to a partitioned Hudi table, run an ALTER TABLE ADD PARTITION command
where the `LOCATION` parameter points to the Amazon S3 subfolder with the files
that belong to the partition.

The DDL to add partitions has the following format.

```
ALTER TABLE *tbl\_name*
ADD IF NOT EXISTS PARTITION(*pcolumn1*=*pvalue1*[,...])
LOCATION 's3://*s3-bucket*/*prefix*/*partition-path*'
```

## Creating external tables for data managed in

Delta Lake

To query data in Delta Lake tables, you can use Amazon Redshift Spectrum external tables.

To access a Delta Lake table from Redshift Spectrum, generate a manifest before the query. A
Delta Lake _manifest_ contains a listing of files that
make up a consistent snapshot of the Delta Lake table. In a partitioned table, there is
one manifest per partition. A Delta Lake table is a collection of Apache
Parquet files stored in Amazon S3.

For more information, see [Delta Lake](https://delta.io "https://delta.io") in the
open source Delta Lake documentation.

When you create an external table that references data in Delta Lake tables, you map
each column in the external table to a column in the Delta Lake table. Mapping is done
by column name.

The DDL for partitioned and unpartitioned Delta Lake tables is similar to that for other
Apache Parquet file formats. For Delta Lake tables, you define `INPUTFORMAT`
as `org.apache.hadoop.hive.ql.io.SymlinkTextInputFormat` and
`OUTPUTFORMAT` as
`org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat`. The
`LOCATION` parameter must point to the manifest folder in the table base
folder. If a SELECT operation on a Delta Lake table fails, for possible reasons see
[Limitations and
troubleshooting for Delta Lake tables](#c-spectrum-column-mapping-delta-limitations "#c-spectrum-column-mapping-delta-limitations").

The DDL to define an unpartitioned table has the following format.

```
CREATE EXTERNAL TABLE *tbl\_name* (*columns*)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS
INPUTFORMAT 'org.apache.hadoop.hive.ql.io.SymlinkTextInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://*s3-bucket*/*prefix*/_symlink_format_manifest'
```

The DDL to define a partitioned table has the following format.

```
CREATE EXTERNAL TABLE *tbl\_name* (*columns*)
PARTITIONED BY(*pcolumn1* *pcolumn1-type*[,...])
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS
INPUTFORMAT 'org.apache.hadoop.hive.ql.io.SymlinkTextInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://*s3-bucket*>/*prefix*/_symlink_format_manifest'
```

To add partitions to a partitioned Delta Lake table, run an ALTER TABLE ADD PARTITION
command where the `LOCATION` parameter points to the Amazon S3 subfolder that
contains the manifest for the partition.

The DDL to add partitions has the following format.

```
ALTER TABLE *tbl\_name*
ADD IF NOT EXISTS PARTITION(*pcolumn1*=*pvalue1*[,...])
LOCATION
's3://*s3-bucket*/*prefix*/_symlink_format_manifest/*partition-path*'
```

Or run DDL that points directly to the Delta Lake manifest file.

```
ALTER TABLE *tbl\_name*
ADD IF NOT EXISTS PARTITION(*pcolumn1*=*pvalue1*[,...])
LOCATION
's3://*s3-bucket*/*prefix*/_symlink_format_manifest/*partition-path*/manifest'
```

### Limitations and

troubleshooting for Delta Lake tables

Consider the following when querying Delta Lake tables from Redshift Spectrum:

- If a manifest points to a snapshot or partition that no longer exists, queries fail until a
  new valid manifest has been generated. For example, this might result from a
  VACUUM operation on the underlying table,
- Delta Lake manifests only provide partition-level consistency.

The following table explains some potential reasons for certain errors when you query a
Delta Lake table.

| Error message                                                                                        | Possible reason                                                                                         |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **`Delta Lake manifest in bucket *s3-bucket-1*<br>cannot contain entries in bucket *s3-bucket-2*.`** | The manifest entries point to files in a different Amazon S3 bucket than the specified one.             |
| **`Delta Lake files are expected to be in the same folder.`**                                        | The manifest entries point to files that have a different Amazon S3 prefix than the specified<br>one.   |
| **`File *filename<br>• listed in Delta Lake manifest *manifest-path<br>• was not found.`**           | A file listed in the manifest wasn't found in Amazon S3.                                                |
| **`Error fetching Delta Lake manifest.`**                                                            | The manifest wasn't found in Amazon S3.                                                                 |
| **`Invalid S3 Path.`**                                                                               | An entry in the manifest file isn't a valid Amazon S3 path, or the manifest file has been<br>corrupted. |
