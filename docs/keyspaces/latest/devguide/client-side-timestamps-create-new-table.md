# Create a new table with client-side timestamps in Amazon Keyspaces

Follow these examples to create a new Amazon Keyspaces table with client-side timestamps enabled using the Amazon Keyspaces AWS Management Console, Cassandra Query Language (CQL), or the AWS Command Line Interface

Console

###### Create a new table with client-side timestamps (console)

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
6. Continue to **Client-side timestamps**.

Choose **Turn on client-side timestamps** to turn on client-side timestamps for the table. 7. Choose **Create table**. Your table is created with client-side timestamps
turned on.

Cassandra Query Language (CQL)

###### Create a new table using CQL

1. To create a new table with client-side timestamps enabled using CQL, you can use the following example.

```
CREATE TABLE `my_keyspace`.`my_table` (
   userid uuid,
   time timeuuid,
   subject text,
   body text,
   user inet,
   PRIMARY KEY (userid, time)
) WITH CUSTOM_PROPERTIES = {'client_side_timestamps': {'status': 'enabled'}};
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

###### Create a new table using the AWS CLI

1. To create a new table with client-side timestamps enabled, you can use the following example.

```
./aws keyspaces create-table \
--keyspace-name `my_keyspace` \
--table-name `my_table` \
--client-side-timestamps 'status=ENABLED' \
--schema-definition 'allColumns=[{name=id,type=int},{name=date,type=timestamp},{name=name,type=text}],partitionKeys=[{name=id}]'
```

2. To confirm that client-side timestamps are turned on for the new table, run the following code.

```
./aws keyspaces get-table \
--keyspace-name `my_keyspace` \
--table-name `my_table`
```

The output should look similar to this example.

```
`{
 "keyspaceName": "my_keyspace",
 "tableName": "my_table",
 "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/table/my_table",
 "creationTimestamp": 1662681206.032,
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
 "lastUpdateToPayPerRequestTimestamp": 1662681206.032
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
