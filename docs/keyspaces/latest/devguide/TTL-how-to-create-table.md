# Create a new table with default Time to Live (TTL) settings

In Amazon Keyspaces, you can set a default TTL value for all rows in a table when the table is
created.

The default TTL value for a
table is zero, which means that data doesn't expire automatically. If the default TTL
value for a table is greater than zero, an expiration timestamp is added to each
row.

TTL values are set
in seconds, and the maximum configurable value is 630,720,000 seconds, which is the
equivalent of 20 years.

After table creation, you can overwrite the table's default TTL setting for specific rows
or columns with CQL DML statements. For more information, see
[Use the INSERT statement to set custom Time to Live (TTL) values for new rows](TTL-how-to-insert-cql.md "TTL-how-to-insert-cql.md") and [Use the UPDATE statement to edit custom Time to Live (TTL)
settings for rows and columns](TTL-how-to-update-cql.md "TTL-how-to-update-cql.md").

When you enable TTL on a table, Amazon Keyspaces begins to store additional TTL-related metadata
for each row. In addition, TTL uses expiration timestamps to track when rows or columns
expire. The timestamps are stored as row metadata and contribute to the storage cost for
the row.

After the TTL feature is enabled, you can't disable it for a
table. Setting the table’s `default_time_to_live` to 0 disables default
expiration times for new data, but it doesn't deactivate the TTL feature or revert the
table back to the original Amazon Keyspaces storage metadata or write behavior.

The following examples show how to create a new table with a default TTL value.

Console

###### Create a new table with a Time to Live default value using the console.

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**, and then choose
   **Create table**.
3. On the **Create table** page in the **Table
   details** section, select a keyspace and provide a name for the new
   table.
4. In the **Schema** section, create the schema for your
   table.
5. In the **Table settings** section, choose **Customize
   settings**.
6. Continue to **Time to Live (TTL)**.

In this step, you select the default TTL settings for the table.

For the **Default TTL period**,
enter the expiration time and choose the unit of time you entered, for example seconds, days, or years. Amazon Keyspaces will store the value in seconds. 7. Choose **Create table**. Your table is created with the
specified default TTL value.

Cassandra Query Language (CQL)

###### Create a new table with a default TTL value using CQL

1. The following statement creates a new table with the default TTL value set to
   3,024,000 seconds, which represents 35 days.

```
CREATE TABLE `my_table` (
                userid uuid,
                time timeuuid,
                subject text,
                body text,
                user inet,
                PRIMARY KEY (userid, time)
                ) WITH default_time_to_live = 3024000;
```

2. To confirm the TTL settings for the new table, use the `cqlsh` `DESCRIBE`
   statement as shown in the following example. The output shows the default TTL setting
   for the table as `default_time_to_live`.

```
DESC TABLE `my_table`;
```

```
`CREATE TABLE my_keyspace.my_table (
 userid uuid,
 time timeuuid,
 body text,
 subject text,
 user inet,
 PRIMARY KEY (userid, time)
) WITH CLUSTERING ORDER BY (time ASC)
 AND bloom_filter_fp_chance = 0.01
 AND caching = {'class': 'com.amazonaws.cassandra.DefaultCaching'}
 AND comment = ''
 AND compaction = {'class': 'com.amazonaws.cassandra.DefaultCompaction'}
 AND compression = {'class': 'com.amazonaws.cassandra.DefaultCompression'}
 AND crc_check_chance = 1.0
 AND dclocal_read_repair_chance = 0.0
 AND default_time_to_live = 3024000
 AND gc_grace_seconds = 7776000
 AND max_index_interval = 2048
 AND memtable_flush_period_in_ms = 3600000
 AND min_index_interval = 128
 AND read_repair_chance = 0.0
 AND speculative_retry = '99PERCENTILE';`
```

CLI

###### Create a new table with a default TTL value using the AWS CLI

1. You can use the following command to create a new table with the default TTL value set to one year.

```
aws keyspaces create-table --keyspace-name 'myKeyspace' --table-name 'myTable' \
            --schema-definition 'allColumns=[{name=id,type=int},{name=name,type=text},{name=date,type=timestamp}],partitionKeys=[{name=id}]' \
            --default-time-to-live '31536000'
```

2. To confirm the TTL status of the table, you can use the following command.

```
aws keyspaces get-table --keyspace-name 'myKeyspace' --table-name 'myTable'
```

The output of the command looks like in the following example

```
`{
 "keyspaceName": "myKeyspace",
 "tableName": "myTable",
 "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/myKeyspace/table/myTable",
 "creationTimestamp": "2024-09-02T10:52:22.190000+00:00",
 "status": "ACTIVE",
 "schemaDefinition": {
 "allColumns": [
 {
 "name": "id",
 "type": "int"
 },
 {
 "name": "date",
 "type": "timestamp"
 },
 {
 "name": "name",
 "type": "text"
 }
 ],
 "partitionKeys": [
 {
 "name": "id"
 }
 ],
 "clusteringKeys": [],
 "staticColumns": []
 },
 "capacitySpecification": {
 "throughputMode": "PAY_PER_REQUEST",
 "lastUpdateToPayPerRequestTimestamp": "2024-09-02T10:52:22.190000+00:00"
 },
 "encryptionSpecification": {
 "type": "AWS_OWNED_KMS_KEY"
 },
 "pointInTimeRecovery": {
 "status": "DISABLED"
 },
 "ttl": {
 "status": "ENABLED"
 },
 "defaultTimeToLive": 31536000,
 "comment": {
 "message": ""
 },
 "replicaSpecifications": []
}`
```
