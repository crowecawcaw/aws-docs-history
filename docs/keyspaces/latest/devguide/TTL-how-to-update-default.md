# Update the default Time to Live (TTL) value of a table

You can update an existing table with a new default TTL value. TTL values are set
in seconds, and the maximum configurable value is 630,720,000 seconds, which is the
equivalent of 20 years.

When you enable TTL on a table, Amazon Keyspaces begins to store additional TTL-related metadata
for each row. In addition, TTL uses expiration timestamps to track when rows or columns
expire. The timestamps are stored as row metadata and contribute to the storage cost for
the row.

After TTL has been enabled for a table, you can overwrite the table's default TTL setting for specific rows
or columns with CQL DML statements. For more information, see
[Use the INSERT statement to set custom Time to Live (TTL) values for new rows](TTL-how-to-insert-cql.md "TTL-how-to-insert-cql.md") and [Use the UPDATE statement to edit custom Time to Live (TTL)
settings for rows and columns](TTL-how-to-update-cql.md "TTL-how-to-update-cql.md").

After the TTL feature is enabled, you can't disable it for a
table. Setting the table’s `default_time_to_live` to 0 disables default
expiration times for new data, but it doesn't deactivate the TTL feature or revert the
table back to the original Amazon Keyspaces storage metadata or write behavior.

Follow these steps to update default Time to Live settings for existing tables using the console, CQL, or the AWS CLI.

Console

###### Update the default TTL value of a table using the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. Choose the table that you want to update, and then choose the **Additional settings** tab.
3. Continue to **Time to Live (TTL)** and choose **Edit**.
4. For the **Default TTL period**,
   enter the expiration time and choose the unit of time, for example seconds, days, or years. Amazon Keyspaces will store the value in seconds.
   This doesn't change the TTL value of existing rows.
5. When the TTL settings are defined, choose
   **Save changes**.

Cassandra Query Language (CQL)

###### Update the default TTL value of a table using CQL

1. You can use `ALTER TABLE` to edit default Time to Live (TTL)
   settings of a table. To update the default TTL settings of the table to 2,592,000 seconds, which represents
   30 days, you can use the following statement.

```
ALTER TABLE `my_table` WITH default_time_to_live = 2592000;
```

2. To confirm the TTL settings for the updated table, use the `cqlsh` `DESCRIBE`
   statement as shown in the following example. The output shows the default TTL setting
   for the table as `default_time_to_live`.

```
DESC TABLE `my_table`;
```

The output of the statement should look similar to this example.

```
`CREATE TABLE my_keyspace.my_table (
 id int PRIMARY KEY,
 date timestamp,
 name text
) WITH bloom_filter_fp_chance = 0.01
 AND caching = {'class': 'com.amazonaws.cassandra.DefaultCaching'}
 AND comment = ''
 AND compaction = {'class': 'com.amazonaws.cassandra.DefaultCompaction'}
 AND compression = {'class': 'com.amazonaws.cassandra.DefaultCompression'}
 AND crc_check_chance = 1.0
 AND dclocal_read_repair_chance = 0.0
 AND default_time_to_live = 2592000
 AND gc_grace_seconds = 7776000
 AND max_index_interval = 2048
 AND memtable_flush_period_in_ms = 3600000
 AND min_index_interval = 128
 AND read_repair_chance = 0.0
 AND speculative_retry = '99PERCENTILE';`
```

CLI

###### Update the default TTL value of a table using the AWS CLI

1. You can use `update-table` to edit the default TTL value a table.
   To update the default TTL settings of the table to 2,592,000 seconds, which represents
   30 days, you can use the following statement.

```
aws keyspaces update-table --keyspace-name 'myKeyspace' --table-name 'myTable' --default-time-to-live '2592000'
```

2. To confirm the updated default TTL value, you can use the following statement.

```
aws keyspaces get-table --keyspace-name 'myKeyspace' --table-name 'myTable'
```

The output of the statement should look like in the following example.

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
 "defaultTimeToLive": 2592000,
 "comment": {
 "message": ""
 },
 "replicaSpecifications": []
}`
```
