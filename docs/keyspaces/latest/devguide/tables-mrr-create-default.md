# Create a multi-Region table with default settings in Amazon Keyspaces

This section provides examples of how to create a multi-Region table in on-demand mode with all default settings. You can
do this on the Amazon Keyspaces console, using CQL or the AWS CLI. All tables that you create in a
multi-Region keyspace automatically inherit the multi-Region settings from the keyspace.

To create a multi-Region keyspace, see [Create a multi-Region keyspace in Amazon Keyspaces](keyspaces-mrr-create.md "keyspaces-mrr-create.md").

Console

###### Create a multi-Region table with default settings (console)

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. Choose a multi-Region keyspace.
3. On the **Tables** tab, choose **Create
   table**.
4. For **Table name**, enter the name for the table. The
   AWS Regions that this table is being replicated in are shown in the info
   box.
5. Continue with the table schema.
6. Under **Table settings**, continue with the **Default
   settings** option. Note the following default settings for
   multi-Region tables.
   - **Capacity mode** – The default
     capacity mode is **On-demand**. For more
     information about configuring
     **provisioned** mode, see [Create a multi-Region table in provisioned mode with auto scaling in Amazon Keyspaces](tables-mrr-create-provisioned.md "tables-mrr-create-provisioned.md").
   - **Encryption key management** – Only the
     **AWS owned key** option is supported.
   - **Client-side timestamps** – This feature is
     required for multi-Region tables.
   - Choose **Customize settings** if you need to turn on
     Time to Live (TTL) for the table and all its replicas.

   ###### Note

   You won't be able to change TTL settings on an existing
   multi-Region table.

7. To finish, choose **Create table**.

Cassandra Query Language (CQL)

###### Create a multi-Region table in on-demand mode with default settings

- To create a multi-Region table with default settings, you can use the following
  CQL statement.

```
CREATE TABLE mykeyspace.mytable(pk int, ck int, PRIMARY KEY (pk, ck))
    WITH CUSTOM_PROPERTIES = {
	'capacity_mode':{
		'throughput_mode':'PAY_PER_REQUEST'
	},
	'point_in_time_recovery':{
		'status':'enabled'
	},
	'encryption_specification':{
		'encryption_type':'AWS_OWNED_KMS_KEY'
	},
	'client_side_timestamps':{
		'status':'enabled'
	}
};
```

CLI

###### Using the AWS CLI

1. To create a multi-Region table with default settings, you only need to specify the
   schema. You can use the following example.

```
aws keyspaces create-table --keyspace-name mykeyspace --table-name mytable \
--schema-definition 'allColumns=[{name=pk,type=int}],partitionKeys={name= pk}'
```

The output of the command is:

```
`{
 "resourceArn": "arn:aws:cassandra:us-east-1:`111122223333`:/keyspace/mykeyspace/table/mytable"
}`
```

2. To confirm the table's settings, you can use the following statement.

```
aws keyspaces get-table --keyspace-name mykeyspace --table-name mytable
```

The output shows all default settings of a multi-Region table.

```
`{
 "keyspaceName": "mykeyspace",
 "tableName": "mytable",
 "resourceArn": "arn:aws:cassandra:us-east-1:`111122223333`:/keyspace/mykeyspace/table/mytable",
 "creationTimestamp": "2023-12-19T16:50:37.639000+00:00",
 "status": "ACTIVE",
 "schemaDefinition": {
 "allColumns": [
 {
 "name": "pk",
 "type": "int"
 }
 ],
 "partitionKeys": [
 {
 "name": "pk"
 }
 ],
 "clusteringKeys": [],
 "staticColumns": []
 },
 "capacitySpecification": {
 "throughputMode": "PAY_PER_REQUEST",
 "lastUpdateToPayPerRequestTimestamp": "2023-12-19T16:50:37.639000+00:00"
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
 "clientSideTimestamps": {
 "status": "ENABLED"
 },
 "replicaSpecifications": [
 {
 "region": "us-east-1",
 "status": "ACTIVE",
 "capacitySpecification": {
 "throughputMode": "PAY_PER_REQUEST",
 "lastUpdateToPayPerRequestTimestamp": 1702895811.469
 }
 },
 {
 "region": "eu-north-1",
 "status": "ACTIVE",
 "capacitySpecification": {
 "throughputMode": "PAY_PER_REQUEST",
 "lastUpdateToPayPerRequestTimestamp": 1702895811.121
 }
 }
 ]
}`
```
