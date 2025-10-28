# Configure client-side timestamps for a table in Amazon Keyspaces

Follow these examples to turn on client-side timestamps for existing tables using the Amazon Keyspaces AWS Management Console, Cassandra Query Language (CQL), or the AWS Command Line Interface.

Console

###### To turn on client-side timestamps for an existing table (console)

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. Choose the table that you want to update, and then choose **Additional settings** tab.
3. On the **Additional settings** tab, go to **Modify client-side timestamps** and select **Turn on client-side timestamps**
4. Choose **Save changes** to change the settings of the table.

Cassandra Query Language (CQL)

###### Using a CQL statement

1. Turn on client-side timestamps for an existing table with the `ALTER TABLE` CQL statement.

```
ALTER TABLE `my_table` WITH custom_properties = {'client_side_timestamps': {'status': 'enabled'}};;
```

2. To confirm the client-side timestamps settings for the new table, use a `SELECT` statement to review the `custom_properties` as shown in the
   following example.

```
SELECT custom_properties from system_schema_mcs.tables where keyspace_name = '`my_keyspace`' and table_name = '`my_table`';
```

The output of this statement shows the status for client-side timestamps.

```
`'client_side_timestamps': {'status': 'enabled'}`
```

AWS CLI

###### Using the AWS CLI

1. You can turn on client-side timestamps for an existing table using the AWS CLI using the following example.

```
./aws keyspaces update-table \
--keyspace-name `my_keyspace` \
--table-name `my_table` \
--client-side-timestamps 'status=ENABLED'
```

2. To confirm that client-side timestamps are turned on for the table, run the following code.

```
./aws keyspaces get-table \
--keyspace-name `my_keyspace` \
--table-name `my_table`
```

The output should look similar to this example and state the status for client-side timestamps as `ENABLED`.

```
`{
 "keyspaceName": "my_keyspace",
 "tableName": "my_table",
 "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/table/my_table",
 "creationTimestamp": 1662681312.906,
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
 "lastUpdateToPayPerRequestTimestamp": 1662681312.906
 },
 "encryptionSpecification": {
 "type": "AWS_OWNED_KMS_KEY"
 },
 "pointInTimeRecovery": {
 "status": "DISABLED"
 },
 "clientSideTimestamps": {
 "status": "ENABLED"
 },
 "ttl": {
 "status": "ENABLED"
 },
 "defaultTimeToLive": 0,
 "comment": {
 "message": ""
 }
}`
```
