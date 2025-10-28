# Update table with custom Time to Live (TTL)

To enable Time to Live custom settings for a table so that TTL values can be applied to individual rows and columns without
setting a TTL default value for the entire table, you can use the following commands.

###### Note

After `ttl` is enabled, you can't disable it for the table.

Cassandra Query Language (CQL)

###### Enable custom TTL settings for a table using CQL

- ```
  ALTER TABLE `my_table` WITH CUSTOM_PROPERTIES={'ttl':{'status': 'enabled'}};
  ```

```


CLI
###### Enable custom TTL settings for a table using the AWS CLI

1. You can use the following command to update the custom TTL setting of a table.



```

aws keyspaces update-table --keyspace-name 'myKeyspace' --table-name 'myTable' --ttl 'status=ENABLED'

```
2. To confirm that TTL is now enabled for the table, you can use the following statement.



```

aws keyspaces get-table --keyspace-name 'myKeyspace' --table-name 'myTable'

```

The output of the statement should look like in the following example.



```

`{
 "keyspaceName": "myKeyspace",
 "tableName": "myTable",
 "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/myKeyspace/table/myTable",
 "creationTimestamp": "2024-09-02T11:32:27.349000+00:00",
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
 "lastUpdateToPayPerRequestTimestamp": "2024-09-02T11:32:27.349000+00:00"
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
