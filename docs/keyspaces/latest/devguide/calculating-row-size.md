# Estimate row size in Amazon Keyspaces

Amazon Keyspaces provides fully managed storage that offers single-digit millisecond read and write performance and stores data durably across multiple AWS Availability Zones.

Amazon Keyspaces attaches metadata to all rows and primary key columns to support efficient data access and high availability.

This topic provides details about how to estimate the encoded size of rows in Amazon Keyspaces.
The encoded row size is used when calculating your bill and quota use. You can also use
the encoded row size when estimating provisioned throughput capacity requirements for
tables.

To calculate the encoded size of rows in Amazon Keyspaces, you can use the following guidelines.

###### Topics

- [Estimate the encoded size of columns](#calculating-row-size-columns "#calculating-row-size-columns")
- [Estimate the encoded size of
  data values based on data type](#calculating-row-size-data-types "#calculating-row-size-data-types")
- [Consider the impact of Amazon Keyspaces features on row size](#calculating-row-size-features "#calculating-row-size-features")
- [Choose the right formula to calculate the encoded size of a row](#calculating-row-size-formula "#calculating-row-size-formula")
- [Row size calculation example](#calculating-row-size-example "#calculating-row-size-example")

## Estimate the encoded size of columns

This section shows how to estimate the encoded size of columns in Amazon Keyspaces.

- **Regular columns** – For regular columns, which are
  columns that aren't primary keys, clustering columns, or `STATIC`
  columns, use the raw size of the cell data based on the [data type](cql.md#cql.data-types "cql.md#cql.data-types") and add the required metadata. The data
  types and some key differences in how Amazon Keyspaces stores data type values and metadata
  are listed in the next section.
- **Partition key columns** – Partition keys can contain up to 2048 bytes of data. Each key column in the partition key
  requires up to 3 bytes of metadata. When calculating the size of your row, you
  should assume each partition key column uses the full 3 bytes of metadata.
- **Clustering columns** – Clustering columns can store up to 850 bytes of data. In addition to the size of the
  data value, each clustering column requires up to 20% of the data value size for
  metadata. When calculating the size of your row, you should add 1 byte of metadata for
  each 5 bytes of clustering column data value.

###### Note

To support efficient querying and built-in indexing, Amazon Keyspaces stores the data value of each partition key
and clustering key column twice.

- **Column names** – The space required for each column name is stored using a
  column identifier and added to each data value stored in the column. The storage value of the column identifier
  depends on the overall number of columns in your table:

      + 1–62 columns: 1 byte
      + 63–124 columns: 2 bytes
      + 125–186 columns: 3 bytes

  For each additional 62 columns add 1 byte. Note that in Amazon Keyspaces, up to 225 regular columns can
  be modified with a single `INSERT` or `UPDATE`
  statement. For more information, see [Amazon Keyspaces service quotas](quotas.md#table "quotas.md#table").

## Estimate the encoded size of

data values based on data type

This section shows how to estimate the encoded size of different data types in Amazon Keyspaces.

- **String types** – Cassandra `ASCII`, `TEXT`, and `VARCHAR` string data types are all stored in Amazon Keyspaces using
  Unicode with UTF-8 binary encoding. The size of a string in Amazon Keyspaces
  equals the number of UTF-8 encoded bytes.
- **Numeric types** – Cassandra `INT`, `BIGINT`, `SMALLINT`, `TINYINT`, and `VARINT` data types are stored
  in Amazon Keyspaces as data values with variable length, with up to 38 significant digits. Leading and trailing zeroes are trimmed.
  The size of any of these data types is approximately 1 byte per two significant digits + 1 byte.
- **Blob type** – A `BLOB` in Amazon Keyspaces is stored with the value's raw byte length.
- **Boolean type** – The size of a `Boolean` value or a `Null` value is 1 byte.
- **Collection types** – A column that stores collection data types like `LIST` or `MAP` requires
  3 bytes of metadata, regardless of its contents. The size of a `LIST`
  or `MAP` is (column id) + sum (size of nested elements) + (3 bytes).
  The size of an empty `LIST` or `MAP` is (column id) + (3
  bytes). Each individual `LIST` or `MAP` element also
  requires 1 byte of metadata.
- **User-defined types** – A [user-defined type (UDT)](udts.md "udts.md") requires 3 bytes for metadata, regardless of
  its contents. For each UDT element, Amazon Keyspaces requires an additional 1 byte of
  metadata.

To calculate the encoded size of a UDT, start with the `field name`
and the `field value` for the fields of a UDT:

    + **field name** – Each field name of the top-level UDT is stored
     using an identifier. The storage value of the identifier depends on the overall number of fields in your top-level
     UDT, and can vary between 1 and 3 bytes:




    	- 1–62 fields: 1 byte
    	- 63–124 fields: 2 bytes
    	- 125– max fields: 3 bytes
    + **field value** – The bytes required to store the field
     values of the top-level UDT depend on the data type stored:




    	- **Scalar data type** – The bytes required for storage are the same as for the same data type
    	 stored in a regular column.
    	- **Frozen UDT** – For each frozen nested UDT, the nested UDT has the same size as it
    	 would have in the CQL binary protocol. For a nested UDT, 4 bytes are stored for each field (including empty fields) and the value
    	 of the stored field is the CQL binary protocol serialization format of the field value.
    	- **Frozen collections**:




    		* **LIST** and **SET** – For a
    		 nested frozen `LIST` or `SET`,
    		 4 bytes are stored for each element of the collection plus the CQL binary protocol serialization format of the
    		 collection’s value.
    		* **MAP** – For a nested frozen `MAP`, each key-value pair has the
    		 following storage requirements:




    			+ For each key allocate 4 bytes, then add the CQL binary protocol serialization format of the
    			 key.
    			+ For each value allocate 4 bytes, then add the CQL binary protocol serialization format of the
    			 value.

- **FROZEN keyword** – For frozen collections nested within frozen collections, Amazon Keyspaces doesn't require any additional bytes for meta data.
- **STATIC keyword** – `STATIC` column data doesn't count towards the maximum row size of 1 MB. To calculate the data size of static
  columns, see [Calculate the static column size per logical
  partition in Amazon Keyspaces](static-columns-estimate.md "static-columns-estimate.md").

## Consider the impact of Amazon Keyspaces features on row size

This section shows how features in Amazon Keyspaces impact the encoded size of a row.

- **Client-side timestamps** – Client-side timestamps are stored for every column in
  each row when the feature is turned on. These timestamps take up approximately
  20–40 bytes (depending on your data), and contribute to the storage and
  throughput cost for the row. For more information about client-side timestamps, see [Client-side timestamps in Amazon Keyspaces](client-side-timestamps.md "client-side-timestamps.md").
- **Time to Live (TTL)** – TTL metadata takes up approximately 8
  bytes for a row when the feature is turned on. Additionally, TTL metadata is
  stored for every column of each row. The TTL metadata takes up approximately 8
  bytes for each column storing a scalar data type or a frozen collection. If the
  column stores a collection data type that's not frozen, for each element of the
  collection TTL requires approximately 8 additional bytes for metadata. For a
  column that stores a collection data type when TTL is enabled, you can use the
  following formula.

```
`**total encoded size of column** = (column id) + sum (nested elements + collection metadata (1 byte) + TTL metadata (8 bytes)) + collection column metadata (3 bytes)`
```

TTL metadata contributes to the storage and throughput
cost for the row. For more information about TTL, see [Expire data with Time to Live (TTL) for Amazon Keyspaces (for Apache Cassandra)](TTL.md "TTL.md").

## Choose the right formula to calculate the encoded size of a row

This section shows the different formulas that you can use to estimate either the storage or the capacity throughput
requirements for a row of data in Amazon Keyspaces.

The total encoded size of a row of data can be estimated based on one of the following
formulas, based on your goal:

- **Throughput capacity** – To estimate the encoded size of a row to
  assess the required read/write request units (RRUs/WRUs) or read/write capacity
  units (RCUs/WCUs):

```
`**total encoded size of row** = partition key columns + clustering columns + regular columns`
```

- **Storage size** – To estimate the encoded size of a row to
  predict the `BillableTableSizeInBytes`, add the required metadata for
  the storage of the row:

```
`**total encoded size of row** = partition key columns + clustering columns + regular columns + row metadata (100 bytes)`
```

###### Important

All column metadata, for example column ids, partition key metadata, clustering column metadata,
as well as client-side timestamps, TTL, and row metadata count towards the maximum row size of 1 MB.

## Row size calculation example

Consider the following example of a table where all columns are of type integer. The
table has two partition key columns, two clustering columns, and one regular column.
Because this table has five columns, the space required for the column name identifier is 1 byte.

```
CREATE TABLE mykeyspace.mytable(pk_col1 int, pk_col2 int, ck_col1 int, ck_col2 int, reg_col1 int, primary key((pk_col1, pk_col2),ck_col1, ck_col2));
```

In this example, we calculate the size of data when we write a row to the table as
shown in the following statement:

```
INSERT INTO mykeyspace.mytable (pk_col1, pk_col2, ck_col1, ck_col2, reg_col1) values(1,2,3,4,5);
```

To estimate the total bytes required by this write operation, you can use the
following steps.

1. Calculate the size of a partition key column by adding the bytes for the data type stored in
   the column and the metadata bytes. Repeat this for all partition key columns.
   1. Calculate the size of the first column of the partition key (pk_col1):

   ```
   `(2 bytes for the integer data type) x 2 + 1 byte for the column id + 3 bytes for partition key metadata = 8 bytes`
   ```

   2. Calculate the size of the second column of the partition key (pk_col2):

   ```
   `(2 bytes for the integer data type) x 2 + 1 byte for the column id + 3 bytes for partition key metadata = 8 bytes`
   ```

   3. Add both columns to get the total estimated size of the partition key columns:

   ```
   `8 bytes + 8 bytes = 16 bytes for the partition key columns`
   ```

2. Calculate the size of the clustering column by adding the bytes for the data type stored in
   the column and the metadata bytes. Repeat this for all clustering columns.
   1. Calculate the size of the first column of the clustering column (ck_col1):

   ```
   `(2 bytes for the integer data type) x 2 + 20% of the data value (2 bytes) for clustering column metadata + 1 byte for the column id = 6 bytes`
   ```

   2. Calculate the size of the second column of the clustering column (ck_col2):

   ```
   `(2 bytes for the integer data type) x 2 + 20% of the data value (2 bytes) for clustering column metadata + 1 byte for the column id = 6 bytes`
   ```

   3. Add both columns to get the total estimated size of the clustering columns:

   ```
   `6 bytes + 6 bytes = 12 bytes for the clustering columns`
   ```

3. Add the size of the regular columns. In this example we only have one column that stores a
   single digit integer, which requires 2 bytes with 1 byte for the column
   id.
4. Finally, to get the total encoded row size, add up the bytes for all columns. To estimate the
   billable size for storage, add the additional 100 bytes for row metadata:

```
`16 bytes for the partition key columns + 12 bytes for clustering columns + 3 bytes for the regular column + 100 bytes for row metadata = 131 bytes.`
```

To learn how to monitor serverless resources with Amazon CloudWatch, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
