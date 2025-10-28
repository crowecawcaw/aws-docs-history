# Create table with custom Time to Live (TTL) settings enabled

To create a new table with Time to Live custom settings that can be applied to rows and columns without
enabling TTL default settings for the entire table, you can use the following commands.

###### Note

If a table is created with `ttl` custom settings enabled, you can't disable the setting later.

Cassandra Query Language (CQL)

###### Create a new table with custom TTL setting using CQL

- ```
  CREATE TABLE `my_keyspace.my_table` (id int primary key) WITH CUSTOM_PROPERTIES={'ttl':{'status': 'enabled'}};
  ```

```


CLI
###### Create a new table with custom TTL setting using the AWS CLI

1. You can use the following command to create a new table with TTL enabled.



```

aws keyspaces create-table --keyspace-name 'myKeyspace' --table-name 'myTable' \
 --schema-definition 'allColumns=[{name=id,type=int},{name=name,type=text}, {name=date,type=timestamp}],partitionKeys=[{name=id}]' \
 --ttl 'status=ENABLED'

```
2. To confirm that TTL is enabled for the table, you can use the following statement.



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
 "lastUpdateToPayPerRequestTimestamp": "2024-09-02T11:18:55.796000+00:00"
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
 "defaultTimeToLive": 0,
 "comment": {
 "message": ""
 },
 "replicaSpecifications": []
}`

```

```
