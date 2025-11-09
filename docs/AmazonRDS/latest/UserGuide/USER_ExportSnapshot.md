# File naming conventions for exports to Amazon S3 for Amazon RDS

Exported data for specific tables is stored in the format ``base_prefix`/`files``, where the base prefix is
the following:

```
`export_identifier`/`database_name`/`schema_name`.`table_name`/
```

For example:

```
export-1234567890123-459/rdststdb/rdststdb.DataInsert_7ADB5D19965123A2/
```

There are two conventions for how files are named.

- Current convention:

```
`batch_index`/part-`partition_index`-`random_uuid`.`format-based_extension`
```

The batch index is a sequence number that represents a batch of data read from the table. If we can't partition your
table into small chunks to be exported in parallel, there will be multiple batch indexes. The same thing happens if your
table is partitioned into multiple tables. There will be multiple batch indexes, one for each of the table partitions of
your main table.

If we can partition your table into small chunks to be read in parallel, there will be only the batch index
`1` folder.

Inside the batch index folder, there are one or more Parquet files that contain your table's data. The prefix of the
Parquet filename is `part-`partition_index``. If your table is partitioned,
 there will be multiple files starting with the partition index `00000`.

There can be gaps in the partition index sequence. This happens because each partition is obtained from a ranged query
in your table. If there is no data in the range of that partition, then that sequence number is skipped.

For example, suppose that the `id` column is the table's primary key, and its minimum and maximum values
are `100` and `1000`. When we try to export this table with nine partitions, we read it with
parallel queries such as the following:

```
SELECT * FROM table WHERE id <= 100 AND id < 200
SELECT * FROM table WHERE id <= 200 AND id < 300
```

This should generate nine files, from
`part-00000-`random_uuid`.gz.parquet` to
`part-00008-`random_uuid`.gz.parquet`. However, if there are no rows
with IDs between `200` and `350`, one of the completed partitions is empty, and no file is created
for it. In the previous example, `part-00001-`random_uuid`.gz.parquet` isn't
created.

- Older convention:

```
part-`partition_index`-`random_uuid`.`format-based_extension`
```

This is the same as the current convention, but without the `batch_index`
prefix, for example:

```
part-00000-c5a881bb-58ff-4ee6-1111-b41ecff340a3-c000.gz.parquet
part-00001-d7a881cc-88cc-5ab7-2222-c41ecab340a4-c000.gz.parquet
part-00002-f5a991ab-59aa-7fa6-3333-d41eccd340a7-c000.gz.parquet

```

The file naming convention is subject to change. Therefore, when reading target tables, we recommend that you read everything
inside the base prefix for the table.
