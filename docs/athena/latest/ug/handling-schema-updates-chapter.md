# Handle schema updates

This section provides guidance on handling schema updates for various data formats. Athena
is a schema-on-read query engine. This means that when you create a table in Athena, it
applies schemas when reading the data. It does not change or rewrite the underlying data.

If you anticipate changes in table schemas, consider creating them in a data format that
is suitable for your needs. Your goals are to reuse existing Athena queries against evolving
schemas, and avoid schema mismatch errors when querying tables with partitions.

To achieve these goals, choose a table's data format based on the table in the following
topic.

###### Topics

- [Supported schema update operations by data format](#summary-of-updates "#summary-of-updates")
- [Understand index access for Apache ORC and Apache Parquet](#index-access "#index-access")
- [Make schema updates](make-schema-updates.md "make-schema-updates.md")
- [Update tables with partitions](updates-and-partitions.md "updates-and-partitions.md")

## Supported schema update operations by data format

The following table summarizes data storage formats and their supported schema
manipulations. Use this table to help you choose the format that will enable you to
continue using Athena queries even as your schemas change over time.

In this table, observe that Parquet and ORC are columnar formats with different
default column access methods. By default, Parquet will access columns by name and ORC
by index (ordinal value). Therefore, Athena provides a SerDe property defined when
creating a table to toggle the default column access method which enables greater
flexibility with schema evolution.

For Parquet, the `parquet.column.index.access` property may be set to
`true`, which sets the column access method to use the column's ordinal
number. Setting this property to `false` will change the column access method
to use column name. Similarly, for ORC use the `orc.column.index.access`
property to control the column access method. For more information, see [Understand index access for Apache ORC and Apache Parquet](#index-access "#index-access").

CSV and TSV allow you to do all schema manipulations except reordering of columns, or
adding columns at the beginning of the table. For example, if your schema evolution
requires only renaming columns but not removing them, you can choose to create your
tables in CSV or TSV. If you require removing columns, do not use CSV or TSV, and
instead use any of the other supported formats, preferably, a columnar format, such as
Parquet or ORC.

| Schema updates and data formats in Athena                                                                                                                               | Expected type of schema update                                                                                                                                                              | Summary | CSV (with and without headers) and TSV | JSON | AVRO | PARQUET: Read by name (default) | PARQUET: Read by index | ORC: Read by index (default) | ORC: Read by name |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------- | ---- | ---- | ------------------------------- | ---------------------- | ---------------------------- | ----------------- |
| [Rename columns](updates-renaming-columns.md "updates-renaming-columns.md")                                                                                             | Store your data in CSV and TSV, or in ORC and Parquet if they are<br>read by index.                                                                                                         | Y       | N                                      | N    | N    | Y                               | Y                      | N                            |
| [Add<br>columns at the beginning or in the middle of the<br>table](updates-add-columns-beginning-middle-of-table.md "updates-add-columns-beginning-middle-of-table.md") | Store your data in JSON, AVRO, or in Parquet and ORC if they are read<br>by name. Do not use CSV and TSV.                                                                                   | N       | Y                                      | Y    | Y    | N                               | N                      | Y                            |
| [Add columns at the end<br>of the table](updates-add-columns-end-of-table.md "updates-add-columns-end-of-table.md")                                                     | Store your data in CSV or TSV, JSON, AVRO, ORC, or Parquet.                                                                                                                                 | Y       | Y                                      | Y    | Y    | Y                               | Y                      | Y                            |
| [Remove<br>columns](updates-removing-columns.md "updates-removing-columns.md")                                                                                          | Store your data in JSON, AVRO, or Parquet and ORC, if they are read<br>by name. Do not use CSV and TSV.                                                                                     | N       | Y                                      | Y    | Y    | N                               | N                      | Y                            |
| [Reorder<br>columns](updates-reordering-columns.md "updates-reordering-columns.md")                                                                                     | Store your data in AVRO, JSON or ORC and Parquet if they are read by<br>name.                                                                                                               | N       | Y                                      | Y    | Y    | N                               | N                      | Y                            |
| [Change a column's data<br>type](updates-changing-column-type.md "updates-changing-column-type.md")                                                                     | Store your data in any format, but test your query in Athena to make<br>sure the data types are compatible. For Parquet and ORC, changing a data<br>type works only for partitioned tables. | Y       | Y                                      | Y    | Y    | Y                               | Y                      | Y                            |

## Understand index access for Apache ORC and Apache Parquet

PARQUET and ORC are columnar data storage formats that can be read by index, or by
name. Storing your data in either of these formats lets you perform all operations on
schemas and run Athena queries without schema mismatch errors.

- Athena _reads ORC by index by default_, as defined in
  `SERDEPROPERTIES ( 'orc.column.index.access'='true')`. For more
  information, see [ORC: Read by index](#orc-read-by-index "#orc-read-by-index").
- Athena reads _Parquet by name by default_, as defined in
  `SERDEPROPERTIES ( 'parquet.column.index.access'='false')`. For
  more information, see [Parquet: Read by name](#parquet-read-by-name "#parquet-read-by-name").

Since these are defaults, specifying these SerDe properties in your `CREATE
 TABLE` queries is optional, they are used implicitly. When used, they allow
you to run some schema update operations while preventing other such operations. To
enable those operations, run another `CREATE TABLE` query and change the
SerDe settings.

###### Note

The SerDe properties are _not_ automatically propagated to each
partition. Use `ALTER TABLE ADD PARTITION` statements to set the SerDe
properties for each partition. To automate this process, write a script that runs
`ALTER TABLE ADD PARTITION` statements.

The following sections describe these cases in detail.

### ORC: Read by index

A table in _ORC is read by index_, by default. This is defined
by the following syntax:

```
`WITH SERDEPROPERTIES (
 'orc.column.index.access'='true')`
```

_Reading by index_ allows you to rename columns. But then you
lose the ability to remove columns or add them in the middle of the table.

To make ORC read by name, which will allow you to add columns in the middle of the
table or remove columns in ORC, set the SerDe property
`orc.column.index.access` to `false` in the `CREATE
 TABLE` statement. In this configuration, you will lose the ability to
rename columns.

###### Note

In Athena engine version 2, when ORC tables are set to read by name, Athena requires that all
column names in the ORC files be in lower case. Because Apache Spark does not
lowercase field names when it generates ORC files, Athena might not be able to
read the data so generated. The workaround is to rename the columns to be in
lower case, or use Athena engine version 3.

The following example illustrates how to change the ORC to make it read by
name:

```
CREATE EXTERNAL TABLE orders_orc_read_by_name (
   `o_comment` string,
   `o_orderkey` int,
   `o_custkey` int,
   `o_orderpriority` string,
   `o_orderstatus` string,
   `o_clerk` string,
   `o_shippriority` int,
   `o_orderdate` string
)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.orc.OrcSerde'
`WITH SERDEPROPERTIES (
 'orc.column.index.access'='false')`
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat'
LOCATION 's3://amzn-s3-demo-bucket/orders_orc/';

```

### Parquet: Read by name

A table in _Parquet is read by name_, by default. This is
defined by the following syntax:

```
`WITH SERDEPROPERTIES (
 'parquet.column.index.access'='false')`
```

_Reading by name_ allows you to add columns in the middle of
the table and remove columns. But then you lose the ability to rename columns.

To make Parquet read by index, which will allow you to rename columns, you must
create a table with `parquet.column.index.access` SerDe property set to
`true`.
