# Check the replication progress when adding a new Region to a keyspace

Adding a new Region to an Amazon Keyspaces keyspace is a long running operation. To track progress you can use the queries shown in this
section.

Cassandra Query Language (CQL)

###### Using CQL to verify the add Region progress

- To verify the progress of the creation of the new table replicas in a given keyspace, you can query the `system_multiregion_info.keyspaces`
  table. The following CQL statement is an example of this.

```
SELECT keyspace_name, region, status, tables_replication_progress
FROM system_multiregion_info.keyspaces
WHERE keyspace_name = '`my_keyspace`';
```

While a replication operation is in progress, the status shows the progress of table
creation in the new Region. This is an example where 5 out of 10 tables have been
replicated to the new Region.

```
 `keyspace_name | region | status | tables_replication_progress
---------------+-----------+-----------+-------------------------
 my_keyspace | us-east-1 | Updating |
 my_keyspace | us-west-2 | Updating |
 my_keyspace | eu-west-1 | Creating | 50%`
```

After the replication process has completed successfully, the output should look like this example.

```
 `keyspace_name | region | status
---------------+-----------+-----------
 my_keyspace | us-east-1 | Active
 my_keyspace | us-west-2 | Active
 my_keyspace | eu-west-1 | Active`
```

CLI

###### Using the AWS CLI to verify the add Region progress

- To confirm the status of table replica creation for a given keyspace, you can use the following example.

```
aws keyspaces get-keyspace \
--keyspace-name `my_keyspace`
```

The output should look similar to this example.

```
`{
 "keyspaceName": "my_keyspace",
 "resourceArn": "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/my_keyspace/",
 "replicationStrategy": "MULTI_REGION",
 "replicationRegions": [
 "us-east-1",
 "eu-west-1"
 ]
 "replicationGroupStatus": [
 {
 "RegionName": "us-east-1",
 "KeyspaceStatus": "Active"
 },
 {
 "RegionName": "eu-west-1",
 "KeyspaceStatus": "Creating",
 "TablesReplicationProgress": "50.0%"
 }
 ]
}`
```
