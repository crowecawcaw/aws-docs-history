# Restore a table from backup to a specified point in time in Amazon Keyspaces

The following section demonstrates how to restore an
existing Amazon Keyspaces table to a specified point in time.

###### Note

This procedure assumes that the table you're using has been configured with point-in-time recovery. To enable
PITR for a table, see [Configure PITR for a table in Amazon Keyspaces](configure_PITR.md "configure_PITR.md").

###### Important

While a restore is in progress, don't modify or delete the AWS Identity and Access Management (IAM)
policies that grant the IAM principal (for example, user, group, or role) permission
to perform the restore. Otherwise, unexpected behavior can result. For example,
if you remove write permissions for a table while that table is being
restored, the underlying `RestoreTableToPointInTime`
operation can't write any of the restored data to the table.

You can modify or delete permissions only after the restore operation is
complete.

Console

###### Restore a table to a specified point in time using the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane on the left side of the console, choose
   **Tables**.
3. In the list of tables, choose the table you want to restore.
4. On the **Backups** tab of the
   table, in the **Point-in-time recovery** section, choose
   **Restore**.
5. For the new table name, enter a new name for the restored table, for example `mytable_restored`.
6. To define the point in time for the restore operation, you can choose between two options:
   - Select the preconfigured **Earliest** time.
   - Select **Specify date and time** and enter the date and time you want to restore the new table to.###### Note

You can restore to any point in time within **Earliest** time and the current time. Amazon Keyspaces
restores your table data to the state based on the selected date and time
(day:hour:minute:second). 7. Choose **Restore** to start the restore process.

The table that is being restored is shown with the status
**Restoring**. After the restore process is finished, the
status of the restored table changes to
**Active**.

Cassandra Query Language (CQL)

###### Restore a table to a point in time using CQL

1. You can restore an active table to a point-in-time between
   `earliest_restorable_timestamp` and the current time. Current
   time is the default.

To confirm that point-in-time recovery is enabled for the
table, query the
`system_schema_mcs.tables` as shown in this example.

```
SELECT custom_properties
FROM system_schema_mcs.tables
WHERE keyspace_name = 'mykeyspace' AND table_name = 'mytable';
```

Point-in-time recovery is enabled as shown in the following sample output.

```
`custom_properties
-----------------
{
 ...,
 "point_in_time_recovery": {
 "earliest_restorable_timestamp":"2020-06-30T19:19:21.175Z"
 "status":"enabled"
 }
}`
```

2. - Restore the table to the current time. When you
     omit the `WITH restore_timestamp = ...` clause,
     the current timestamp is used.

   ```
   RESTORE TABLE mykeyspace.mytable_restored
   FROM TABLE mykeyspace.mytable;
   ```

   - You can also restore to a specific point in time, defined by a
     `restore_timestamp` in ISO 8601 format. You can specify any point in
     time during the last 35 days. For example, the following command restores the
     table to the `EarliestRestorableDateTime`.

   ```
   RESTORE TABLE mykeyspace.mytable_restored
   FROM TABLE mykeyspace.mytable
   WITH restore_timestamp = '2020-06-30T19:19:21.175Z';
   ```

   For a full syntax description, see [RESTORE TABLE](cql.ddl.md#cql.ddl.table.restore "cql.ddl.md#cql.ddl.table.restore") in
   the language reference.

3. To verify that the restore of the table was successful, query the
   `system_schema_mcs.tables` to confirm the status of the table.

```
SELECT status
FROM system_schema_mcs.tables
WHERE keyspace_name = 'mykeyspace' AND table_name = 'mytable_restored'
```

The query shows the following output.

```
`status
------
RESTORING`
```

The table that is being restored is shown with the status
**Restoring**. After the restore process is finished, the status of
the table changes to **Active**.

CLI

###### Restore a table to a point in time using the AWS CLI

1. Create a simple table named
   `myTable` that has PITR enabled. The command has been
   broken up into separate lines for readability.

```
aws keyspaces create-table --keyspace-name 'myKeyspace' --table-name 'myTable'
            --schema-definition 'allColumns=[{name=id,type=int},{name=name,type=text},{name=date,type=timestamp}],partitionKeys=[{name=id}]'
            --point-in-time-recovery 'status=ENABLED'
```

2. Confirm the properties of the new table and review the `earliestRestorableTimestamp` for PITR.

```
aws keyspaces get-table --keyspace-name 'myKeyspace' --table-name 'myTable'
```

The output of this command returns the following.

```
`{
 "keyspaceName": "myKeyspace",
 "tableName": "myTable",
 "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/myKeyspace/table/myTable",
 "creationTimestamp": "2022-06-20T14:34:57.049000-07:00",
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
 "lastUpdateToPayPerRequestTimestamp": "2022-06-20T14:34:57.049000-07:00"
 },
 "encryptionSpecification": {
 "type": "AWS_OWNED_KMS_KEY"
 },
 "pointInTimeRecovery": {
 "status": "ENABLED",
 "earliestRestorableTimestamp": "2022-06-20T14:35:13.693000-07:00"
 },
 "defaultTimeToLive": 0,
 "comment": {
 "message": ""
 }
}`
```

3. - To restore a table to a point in time, specify a `restore_timestamp` in ISO 8601 format.
     You can chose any point in time during the last 35 days in one second intervals. For example, the
     following command restores the table to the `EarliestRestorableDateTime`.

   ```
   aws keyspaces restore-table --source-keyspace-name 'myKeyspace' --source-table-name 'myTable' --target-keyspace-name 'myKeyspace' --target-table-name 'myTable_restored' --restore-timestamp "2022-06-20 21:35:14.693"
   ```

   The output of this command returns the ARN of the restored table.

   ```
   `{
    "restoredTableARN": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/myKeyspace/table/myTable_restored"
   }`
   ```

   - To restore the table to the current time, you can omit the `restore-timestamp` parameter.

   ```
   aws keyspaces restore-table --source-keyspace-name 'myKeyspace' --source-table-name 'myTable' --target-keyspace-name 'myKeyspace' --target-table-name 'myTable_restored1'"
   ```
