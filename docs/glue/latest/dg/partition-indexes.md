# Creating partition indexes

Over time, hundreds of thousands of partitions get added to a table. The [GetPartitions API](../webapi/API_GetPartitions.md "../webapi/API_GetPartitions.md") is used to fetch the partitions in the table.
The API returns partitions that match the expression provided in the request.

Lets take a _sales_data_ table as an example which is partitioned by the
keys _Country_, _Category_, _Year_,
_Month_, and _creationDate_. If you want to obtain
sales data for all the items sold for the _Books_ category in the year
2020 after _2020-08-15_, you have to make a `GetPartitions`
request with the expression "Category = 'Books' and creationDate > '2020-08-15'" to the
Data Catalog.

If no partition indexes are present on the table, AWS Glue loads all the partitions of the table, and then filters the loaded partitions using the query expression provided by the user in the `GetPartitions` request. The query takes more time to run as the number of partitions increase on a table with no indexes. With an index, the `GetPartitions` query will try to fetch a subset of the partitions instead of loading all the partitions in the table.

###### Topics

- [About partition indexes](#partition-index-1 "#partition-index-1")
- [Creating a table with partition indexes](#partition-index-creating-table "#partition-index-creating-table")
- [Adding a partition index to an existing table](#partition-index-existing-table "#partition-index-existing-table")
- [Describing partition indexes on a table](#partition-index-describing "#partition-index-describing")
- [Limitations on using partition indexes](#partition-index-limitations "#partition-index-limitations")
- [Using indexes for an optimized GetPartitions call](#partition-index-getpartitions "#partition-index-getpartitions")
- [Integration with engines](#partition-index-integration-engines "#partition-index-integration-engines")

## About partition indexes

When you create a partition index, you specify a list of partition keys that already exist
on a given table. Partition index is sub list of partition keys defined in the table. A
partition index can be created on any permutation of partition keys defined on the
table. For the above _sales_data_ table, the possible indexes are
(country, category, creationDate), (country, category, year), (country, category),
(country), (category, country, year, month), and so on.

The Data Catalog will concatenate the partition values in the order provided at the time of
index creation. The index is built consistently as partitions are added to the table.
Indexes can be created for String (string, char, and varchar), Numeric (int, bigint,
long, tinyint, and smallint), and Date (yyyy-MM-dd) column types.

**Supported data types**

- Date – A date in ISO format, such as `YYYY-MM-DD`. For example, date `2020-08-15`.
  The format uses hyphens (‐) to separate the year, month, and day. The permissible range for dates for indexing spans from `0000-01-01` to `9999-12-31`.
- String – A string literal enclosed in single or double quotes.
- Char – Fixed length character data, with a specified length between 1 and 255, such as char(10).
- Varchar – Variable length character data, with a specified length between 1 and 65535, such as varchar(10).
- Numeric – int, bigint, long, tinyint, and smallint

Indexes on Numeric, String, and Date data types support =, >, >=, <, <= and between
operators. The indexing solution currently only supports the `AND` logical
operator. Sub-expressions with the operators "LIKE", "IN", "OR", and "NOT" are ignored
in the expression for filtering using an index. Filtering for the ignored sub-expression
is done on the partitions fetched after applying index filtering.

For each partition added to a table, there is a corresponding index item created. For a table with ‘n’ partitions, 1 partition index will result in 'n' partition index items. 'm' partition index on same table will result into 'm\*n' partition index items. Each partition index item will be charged according to the current AWS Glue pricing policy for data catalog storage. For details on storage object pricing, see [AWS Glue pricing](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

## Creating a table with partition indexes

You can create a partition index during table creation. The `CreateTable`
request takes a list of [`PartitionIndex` objects](aws-glue-api-catalog-tables.md#aws-glue-api-catalog-tables-PartitionIndex "aws-glue-api-catalog-tables.md#aws-glue-api-catalog-tables-PartitionIndex") as an input. A maximum of 3 partition indexes can be created on a given table. Each partition index requires a name and a list of `partitionKeys` defined for the table. Created indexes on a table can be fetched using the [`GetPartitionIndexes` API](aws-glue-api-catalog-tables.md#aws-glue-api-catalog-tables-GetPartitionIndexes "aws-glue-api-catalog-tables.md#aws-glue-api-catalog-tables-GetPartitionIndexes")

## Adding a partition index to an existing table

To add a partition index to an existing table, use the `CreatePartitionIndex` operation. You can create one `PartitionIndex` per `CreatePartitionIndex` operation. Adding an index does not affect the availability of a table, as the table continues to be available while indexes are being created.

The index status for an added partition is set to CREATING and the creation of the index data is started. If the process for creating the indexes is successful, the indexStatus is updated to ACTIVE and for an unsuccessful process, the index status is updated to FAILED. Index creation can fail for multiple reasons, and you can use the `GetPartitionIndexes` operation to retrieve the failure details. The possible failures are:

- ENCRYPTED_PARTITION_ERROR — Index creation on a table with encrypted partitions is not supported.
- INVALID_PARTITION_TYPE_DATA_ERROR — Observed when the `partitionKey` value is not a valid value for the corresponding `partitionKey` data type. For example: a `partitionKey` with the 'int' datatype has a value 'foo'.
- MISSING_PARTITION_VALUE_ERROR — Observed when the `partitionValue` for an `indexedKey` is not present. This can happen when a table is not partitioned consistently.
- UNSUPPORTED_PARTITION_CHARACTER_ERROR — Observed when the value for an indexed partition key contains the characters \u0000, \u0001 or \u0002
- INTERNAL_ERROR — An internal error occurred while indexes were being created.

## Describing partition indexes on a table

To fetch the partition indexes created on a table, use the `GetPartitionIndexes` operation. The response returns all the indexes on the table, along with the current status of each index (the `IndexStatus`).

The `IndexStatus` for a partition index will be one of the following:

- `CREATING` — The index is currently being created, and is not yet available for use.
- `ACTIVE` — The index is ready for use. Requests can use the index to perform an optimized query.
- `DELETING` — The index is currently being deleted, and can no longer be used. An index in the active state can be deleted using the `DeletePartitionIndex` request, which moves the status from ACTIVE to DELETING.
- `FAILED` — The index creation on an existing table failed. Each table stores the last 10 failed indexes.

The possible state transitions for indexes created on an existing table are:

- CREATING → ACTIVE → DELETING
- CREATING → FAILED

## Limitations on using partition indexes

Once you have created a partition index, note these changes to table and partition functionality:

###### New partition creation (after Index Addition)

After a partition index is created on a table, all new partitions added to the table will be validated for the data type checks for indexed keys. The partition value of the indexed keys will be validated for data type format. If the data type check fails, the create partition operation will fail. For the _sales_data_ table, if an index is created for keys (category, year) where the category is of type `string` and year of type `int`, the creation of the new partition with a value of YEAR as "foo" will fail.

After indexes are enabled, the addition of partitions with indexed key values having the characters U+0000, U+00001, and U+0002 will start to fail.

###### Table updates

Once a partition index is created on a table, you cannot modify the partition key names for existing partition keys, and you cannot change the type, or order, of keys which are registered with the index.

## Using indexes for an optimized GetPartitions call

When you call `GetPartitions` on a table with an index, you can include an expression, and if applicable the Data Catalog will use an index if possible. The first key of the index should be passed in the expression for the indexes to be used in filtering. Index optimization in filtering is applied as a best effort. The Data Catalog tries to use index optimization as much as possible, but in case of a missing index, or unsupported operator, it falls back to the existing implementation of loading all partitions.

For the _sales_data_ table above, lets add the index [Country, Category, Year]. If "Country" is not passed in the expression, the registered index will not be able to filter partitions using indexes. You can add up to 3 indexes to support various query patterns.

Lets take some example expressions and see how indexes work on them:

| Expressions                                                                       | How index will be used                                                                                                                                            |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Country = 'US'                                                                    | Index will be used to filter partitions.                                                                                                                          |
| Country = 'US' and Category = 'Shoes'                                             | Index will be used to filter partitions.                                                                                                                          |
| Category = 'Shoes'                                                                | Indexes will not be used as "country" is not provided in the expression. All partitions will be loaded to return a response.                                      |
| Country = 'US' and Category = 'Shoes' and Year > '2018'                           | Index will be used to filter partitions.                                                                                                                          |
| Country = 'US' and Category = 'Shoes' and Year > '2018' and month = 2             | Index will be used to fetch all partitions with country = "US" and category = "shoes" and year > 2018. Then, filtering on the month expression will be performed. |
| Country = 'US' AND Category = 'Shoes' OR Year > '2018'                            | Indexes will not be used as an `OR` operator is present in the expression.                                                                                        |
| Country = 'US' AND Category = 'Shoes' AND (Year = 2017 OR Year = '2018')          | Index will be used to fetch all partitions with country = "US" and category = "shoes", and then filtering on the year expression will be performed.               |
| Country in ('US', 'UK') AND Category = 'Shoes'                                    | Indexes will not be used for filtering as the `IN` operator is not supported currently.                                                                           |
| Country = 'US' AND Category in ('Shoes', 'Books')                                 | Index will be used to fetch all partitions with country = "US", and then filtering on the Category expression will be performed.                                  |
| Country = 'US' AND Category in ('Shoes', 'Books') AND (creationDate > '2023-9-01' | Index will be used to fetch all partitions with country = "US", with creationDate > '2023-9-01', and then filtering on the Category expression will be performed. | ## Integration with engines Redshift Spectrum, Amazon EMR and AWS Glue ETL Spark DataFrames are able to utilize indexes for fetching partitions after indexes are in an ACTIVE state in AWS Glue. [Athena](../../../athena/latest/ug/glue-best-practices.md#glue-best-practices-partition-index "../../../athena/latest/ug/glue-best-practices.md#glue-best-practices-partition-index") and [AWS Glue ETL Dynamic frames](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-cat-predicates "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-cat-predicates") require you to follow extra steps to utilize indexes for query improvement. ### Enable partition filtering To enable partition filtering in Athena, you need to update the table properties as follows: 1. In the AWS Glue console, under **Data Catalog**, choose **Tables**. 2. Choose a table. 3. Under **Actions**, choose **Edit table**. 4. Under **Table properties**, add the following: <br>• Key –`partition_filtering.enabled` <br>• Value – `true` 5. Choose **Apply**. Alternatively, you can set this parameter by running an [ALTER TABLE SET PROPERTIES](../../../athena/latest/ug/alter-table-set-tblproperties.md "../../../athena/latest/ug/alter-table-set-tblproperties.md") query in Athena. `ALTER TABLE partition_index.table_with_index SET TBLPROPERTIES ('partition_filtering.enabled' = 'true')` |
