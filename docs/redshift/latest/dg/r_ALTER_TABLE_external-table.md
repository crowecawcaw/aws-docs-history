Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER EXTERNAL TABLE examples

The following examples use an Amazon S3 bucket located in the US East (N. Virginia) Region
(`us-east-1`) AWS Region and the example tables created in [Examples](r_CREATE_EXTERNAL_TABLE_examples.md "r_CREATE_EXTERNAL_TABLE_examples.md") for CREATE TABLE. For more
information about how to use partitions with external tables, see [Partitioning Redshift Spectrum external
tables](c-spectrum-external-tables.md#c-spectrum-external-tables-partitioning "c-spectrum-external-tables.md#c-spectrum-external-tables-partitioning").

The following example sets the numRows table property for the SPECTRUM.SALES external
table to 170,000 rows.

```
alter table spectrum.sales
set table properties ('numRows'='170000');
```

The following example changes the location for the SPECTRUM.SALES external
table.

```
alter table spectrum.sales
set location 's3://redshift-downloads/tickit/spectrum/sales/';
```

The following example changes the format for the SPECTRUM.SALES external table to
Parquet.

```
alter table spectrum.sales
set file format parquet;
```

The following example adds one partition for the table SPECTRUM.SALES_PART.

```
alter table spectrum.sales_part
add if not exists partition(saledate='2008-01-01')
location 's3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-01/';
```

The following example adds three partitions for the table SPECTRUM.SALES_PART.

```
alter table spectrum.sales_part add if not exists
partition(saledate='2008-01-01')
location 's3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-01/'
partition(saledate='2008-02-01')
location 's3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-02/'
partition(saledate='2008-03-01')
location 's3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-03/';
```

The following example alters SPECTRUM.SALES_PART to drop the partition with
`saledate='2008-01-01''`.

```
alter table spectrum.sales_part
drop partition(saledate='2008-01-01');
```

The following example sets a new Amazon S3 path for the partition with
`saledate='2008-01-01'`.

```
alter table spectrum.sales_part
partition(saledate='2008-01-01')
set location 's3://redshift-downloads/tickit/spectrum/sales_partition/saledate=2008-01-01/';
```

The following example changes the name of `sales_date` to
`transaction_date`.

```
alter table spectrum.sales rename column sales_date to transaction_date;
```

The following example sets the column mapping to position mapping for an external
table that uses optimized row columnar (ORC) format.

```
alter table spectrum.orc_example
set table properties('orc.schema.resolution'='position');
```

The following example sets the column mapping to name mapping for an external table
that uses ORC format.

```
alter table spectrum.orc_example
set table properties('orc.schema.resolution'='name');
```
