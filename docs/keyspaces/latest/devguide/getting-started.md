# Create a table in Amazon Keyspaces

In this section, you create a table using the
console, `cqlsh`, or the AWS CLI.

A table is where your data is organized and stored. The primary key of your table
determines how data is partitioned in your table. The primary key is composed of a
required partition key and one or more optional clustering columns. The combined values
that compose the primary key must be unique across all the table’s data. For more
information about tables, see the following topics:

- Partition key design: [How to use partition keys effectively in Amazon Keyspaces](bp-partition-key-design.md "bp-partition-key-design.md")
- Working with tables: [Check table creation status in Amazon Keyspaces](tables-create.md "tables-create.md")
- DDL statements in the CQL language reference: [Tables](cql.ddl.md "cql.ddl.md")
- Table resource management: [Managing serverless resources in
  Amazon Keyspaces (for Apache Cassandra)](serverless_resource_management.md "serverless_resource_management.md")
- Monitoring table resource utilization: [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md "quotas.md")
  When you create a table, you specify the following:

- The name of the table.
- The name and data type of each column in the table.
- The primary key for the table.

      + **Partition key** – Required
      + **Clustering columns** –
       Optional

  Use the following procedure to create a table with the specified columns, data
  types, partition keys, and clustering columns.

The following procedure creates the table `book_awards`
with these columns and data types.

```
year           int
award          text
rank           int
category       text
book_title     text
author         text
publisher      text
```

###### To create a table using the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Keyspaces**.
3. Choose `catalog` as the keyspace you want to create this table in.
4. Choose **Create table**.
5. In the **Table name** box, enter
   `book_awards` as a name for your table.

**Name constraints:**

    * The name can't be empty.
    * Allowed characters: alphanumeric characters and underscore ( `_` ).
    * Maximum length is 48 characters.

6. In the **Columns** section, repeat the following steps
   for each column that you want to add to this table.

Add the following columns and data types.

```
year           int
award          text
rank           int
category       text
book_title     text
author         text
publisher      text
```

    1. **Name** – Enter a name for the
     column.


    **Name constraints:**




    	* The name can't be empty.
    	* Allowed characters: alphanumeric characters and underscore ( `_` ).
    	* Maximum length is 48 characters.
    2. **Type** – In the list of data types,
     choose the data type for this column.
    3. To add another column, choose **Add column**.

7.  Choose `award` and `year` as the partition keys under **Partition
    Key**. A partition key is required for each table. A partition
    key can be made of one or more columns.
8.  Add `category` and `rank` as **Clustering columns**. Clustering columns are optional and
    determine the sort order within each partition.
    1. To add a clustering column, choose **Add clustering column**.
    2. In the **Column** list, choose
       **category**. In the **Order**
       list, choose **ASC** to sort in ascending order on
       the values in this column. (Choose **DESC** for
       descending order.)
    3. Then select **Add clustering column** and choose **rank**.

9.  In the **Table settings** section, choose **Default settings**.
10. Choose **Create table**.
11. Verify that your table was created.

        1. In the navigation pane, choose **Tables**.
        2. Confirm that your table is in the list of tables.
        3. Choose the name of your table.
        4. Confirm that all your columns and data types are correct.


        ###### Note

        The columns might not be listed in the same order that you
         added them to the table.

    This procedure creates a table with the following columns and data types using
    CQL. The `year` and `award` columns are partition keys with
    `category` and `rank` as clustering columns, together
    they make up the primary key of the table.

```
year           int
award          text
rank           int
category       text
book_title     text
author         text
publisher      text
```

###### To create a table using CQL

1. Open AWS CloudShell and connect to Amazon Keyspaces using the following command. Make sure to update `us-east-1` with your
   own Region.

```
cqlsh-expansion cassandra.`us-east-1`.amazonaws.com 9142 --ssl
```

The output of that command should look like this.

```
`Connected to Amazon Keyspaces at cassandra.us-east-1.amazonaws.com:9142
[cqlsh 6.1.0 | Cassandra 3.11.2 | CQL spec 3.4.4 | Native protocol v4]
Use HELP for help.
cqlsh current consistency level is ONE.`
```

2. At the keyspace prompt (`cqlsh:keyspace_name>`), create
   your table by entering the following code into your command window.

```
CREATE TABLE `catalog.book_awards` (
   year int,
   award text,
   rank int,
   category text,
   book_title text,
   author text,
   publisher text,
   PRIMARY KEY ((year, award), category, rank)
   );
```

###### Note

`ASC` is the default clustering order. You can also specify
`DESC` for descending order.

Note that the `year` and `award` are partition key columns. Then,
`category` and `rank` are the clustering columns ordered by ascending order
(`ASC`). Together, these columns form the primary key of the table. 3. Verify that your table was created.

```
SELECT * from system_schema.tables WHERE keyspace_name='catalog.book_awards' ;
```

The output should look similar to this.

```
 `keyspace_name | table_name | bloom_filter_fp_chance | caching | cdc | comment | compaction | compression | crc_check_chance | dclocal_read_repair_chance | default_time_to_live | extensions | flags | gc_grace_seconds | id | max_index_interval | memtable_flush_period_in_ms | min_index_interval | read_repair_chance | speculative_retry
---------------+------------+------------------------+---------+-----+---------+------------+-------------+------------------+----------------------------+----------------------+------------+-------+------------------+----+--------------------+-----------------------------+--------------------+--------------------+-------------------

(0 rows)`
```

4. Verify your table's structure.

```
SELECT * FROM system_schema.columns WHERE keyspace_name = 'catalog' AND table_name = 'book_awards';
```

The output of this statement should look similar to this example.

```
 `keyspace_name | table_name | column_name | clustering_order | column_name_bytes | kind | position | type
---------------+-------------+-------------+------------------+------------------------+---------------+----------+------
 catalog | book_awards | year | none | 0x79656172 | partition_key | 0 | int
 catalog | book_awards | award | none | 0x6177617264 | partition_key | 1 | text
 catalog | book_awards | category | asc | 0x63617465676f7279 | clustering | 0 | text
 catalog | book_awards | rank | asc | 0x72616e6b | clustering | 1 | int
 catalog | book_awards | author | none | 0x617574686f72 | regular | -1 | text
 catalog | book_awards | book_title | none | 0x626f6f6b5f7469746c65 | regular | -1 | text
 catalog | book_awards | publisher | none | 0x7075626c6973686572 | regular | -1 | text

(7 rows)`
```

Confirm that all the columns and data types are as you expected. The order
of the columns might be different than in the `CREATE`
statement.
This procedure creates a table with the following columns and data
types using the AWS CLI. The `year` and `award` columns make up the partition key with `category`
and `rank` as clustering columns.

```
year           int
award          text
rank           int
category       text
book_title     text
author         text
publisher      text
```

###### To create a table using the AWS CLI

The following command creates a table with the name _book_awards_.
The partition key of the table consists of the columns `year` and
`award` and the clustering key consists of the columns
`category` and `rank`, both clustering columns use the
ascending sort order. (For easier readability, the `schema-definition` of the table create command
in this section is broken into separate lines.)

1. You can create the table using the following statement.

```
aws keyspaces create-table --keyspace-name 'catalog' \
                      --table-name 'book_awards' \
                      --schema-definition 'allColumns=[{name=year,type=int},{name=award,type=text},{name=rank,type=int},
            {name=category,type=text}, {name=author,type=text},{name=book_title,type=text},{name=publisher,type=text}],
            partitionKeys=[{name=year},{name=award}],clusteringKeys=[{name=category,orderBy=ASC},{name=rank,orderBy=ASC}]'
```

This command results in the following output.

```
`{
 "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/catalog/table/book_awards"
}`
```

2. To confirm the metadata and properties of the table, you can use the following command.

```
aws keyspaces get-table --keyspace-name 'catalog' --table-name 'book_awards'
```

This command returns the following output.

```
`{
 "keyspaceName": "catalog",
 "tableName": "book_awards",
 "resourceArn": "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/catalog/table/book_awards",
 "creationTimestamp": "2024-07-11T15:12:55.571000+00:00",
 "status": "ACTIVE",
 "schemaDefinition": {
 "allColumns": [
 {
 "name": "year",
 "type": "int"
 },
 {
 "name": "award",
 "type": "text"
 },
 {
 "name": "category",
 "type": "text"
 },
 {
 "name": "rank",
 "type": "int"
 },
 {
 "name": "author",
 "type": "text"
 },
 {
 "name": "book_title",
 "type": "text"
 },
 {
 "name": "publisher",
 "type": "text"
 }
 ],
 "partitionKeys": [
 {
 "name": "year"
 },
 {
 "name": "award"
 }
 ],
 "clusteringKeys": [
 {
 "name": "category",
 "orderBy": "ASC"
 },
 {
 "name": "rank",
 "orderBy": "ASC"
 }
 ],
 "staticColumns": []
 },
 "capacitySpecification": {
 "throughputMode": "PAY_PER_REQUEST",
 "lastUpdateToPayPerRequestTimestamp": "2024-07-11T15:12:55.571000+00:00"
 },
 "encryptionSpecification": {
 "type": "AWS_OWNED_KMS_KEY"
 },
 "pointInTimeRecovery": {
 "status": "DISABLED"
 },
 "defaultTimeToLive": 0,
 "comment": {
 "message": ""
 },
 "replicaSpecifications": []
}`
```

To perform CRUD (create, read, update, and delete) operations on the data in your
table, proceed to [Create, read, update, and delete
data (CRUD) using CQL in Amazon Keyspaces](getting-started.md "getting-started.md").
