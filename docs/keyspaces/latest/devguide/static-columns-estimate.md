# Calculate the static column size per logical

partition in Amazon Keyspaces

This section provides details about how to estimate the encoded size of static
columns in Amazon Keyspaces. The encoded size is used when you're calculating your bill and
quota use. You should also use the encoded size when you calculate provisioned
throughput capacity requirements for tables. To calculate the encoded size of static
columns in Amazon Keyspaces, you can use the following guidelines.

- Partition keys can contain up to 2048 bytes of data. Each key column in
  the partition key requires up to 3 bytes of metadata. These metadata bytes
  count towards your static data size quota of 1 MB per partition.
  When calculating the size of your static data, you should assume that each
  partition key column uses the full 3 bytes of metadata.
- Use the raw size of the static column data values based on the data type.
  For more information about data types, see [Data types](cql.md#cql.data-types "cql.md#cql.data-types").
- Add 104 bytes to the size of the static data for metadata.
- Clustering columns and regular, nonprimary key columns do not count
  towards the size of static data. To learn how to estimate the size of
  nonstatic data within rows, see [Estimate row size in Amazon Keyspaces](calculating-row-size.md "calculating-row-size.md").
  The total encoded size of a static column is based on the following
  formula:

```
partition key columns + static columns + metadata = **total encoded size of static data**
```

Consider the following example of a table where all columns are of type integer.
The table has two partition key columns, two clustering columns, one regular column,
and one static column.

```
CREATE TABLE mykeyspace.mytable(pk_col1 int, pk_col2 int, ck_col1 int, ck_col2 int, reg_col1 int, static_col1 int static, primary key((pk_col1, pk_col2),ck_col1, ck_col2));
```

In this example, we calculate the size of static data of the following
statement:

```
INSERT INTO mykeyspace.mytable (pk_col1, pk_col2, static_col1) values(1,2,6);
```

To estimate the total bytes required by this write operation, you can use the
following steps.

1. Calculate the size of a partition key column by adding the bytes for the
   data type stored in the column and the metadata bytes. Repeat this for all
   partition key columns.
   1. Calculate the size of the first column of the partition key
      (pk_col1):

   ```
   4 bytes for the integer data type + 3 bytes for partition key metadata = 7 bytes
   ```

   2. Calculate the size of the second column of the partition key
      (pk_col2):

   ```
   4 bytes for the integer data type + 3 bytes for partition key metadata = 7 bytes
   ```

   3. Add both columns to get the total estimated size of the partition
      key columns:

   ```
   7 bytes + 7 bytes = 14 bytes for the partition key columns
   ```

2. Add the size of the static columns. In this example, we only have one
   static column that stores an integer (which requires 4 bytes).
3. Finally, to get the total encoded size of the static column data, add up
   the bytes for the primary key columns and static columns, and add the
   additional 104 bytes for metadata:

```
14 bytes for the partition key columns + 4 bytes for the static column + 104 bytes for metadata = 122 bytes.
```

You can also update static and nonstatic data with the same statement. To estimate
the total size of the write operation, you must first calculate the size of the
nonstatic data update. Then calculate the size of the row update as shown in the
example at [Estimate row size in Amazon Keyspaces](calculating-row-size.md "calculating-row-size.md"), and add the results.

In this case, you can write a total of 2 MB—1 MB is the maximum
row size quota, and 1 MB is the quota for the maximum static data size per
logical partition.

To calculate the total size of an update of static and nonstatic data in the same
statement, you can use the following formula:

```
(partition key columns + static columns + metadata = **total encoded size of static data**) + (partition key columns + clustering columns + regular columns + row metadata = **total encoded size of row**)
= **total encoded size of data written**
```

Consider the following example of a table where all columns are of type integer.
The table has two partition key columns, two clustering columns, one regular column,
and one static column.

```
CREATE TABLE mykeyspace.mytable(pk_col1 int, pk_col2 int, ck_col1 int, ck_col2 int, reg_col1 int, static_col1 int static, primary key((pk_col1, pk_col2),ck_col1, ck_col2));
```

In this example, we calculate the size of data when we write a row to the table,
as shown in the following statement:

```
INSERT INTO mykeyspace.mytable (pk_col1, pk_col2, ck_col1, ck_col2, reg_col1, static_col1) values(2,3,4,5,6,7);
```

To estimate the total bytes required by this write operation, you can use the
following steps.

1. Calculate the total encoded size of static data as shown earlier. In this
   example, it's 122 bytes.
2. Add the size of the total encoded size of the row based on the update of
   nonstatic data, following the steps at [Estimate row size in Amazon Keyspaces](calculating-row-size.md "calculating-row-size.md"). In this example, the total size of the row update is 134 bytes.

```
122 bytes for static data + 134 bytes for nonstatic data = 256 bytes.
```
