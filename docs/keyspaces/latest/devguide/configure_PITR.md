# Configure PITR for a table in Amazon Keyspaces

You can configure a table in Amazon Keyspaces for backup and restore operations using PITR with the console, CQL, and the AWS CLI.

When creating a new table using CQL or the AWS CLI, you must explicitly enable PITR in the create table statement. When you
create a new table using the console, PITR will be enable by default.

To learn how to restore a table, see [Restore a table from backup to a specified point in time in Amazon Keyspaces](restoretabletopointintime.md "restoretabletopointintime.md").

Console

###### Configure PITR for a table using the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables** and select the
   table you want to edit.
3. On the **Backups** tab, choose
   **Edit**.
4. In the **Edit point-in-time recovery settings** section,
   select **Enable Point-in-time recovery**.
5. Choose **Save changes**.

Cassandra Query Language (CQL)

###### Configure PITR for a table using CQL

1. You can manage PITR settings for tables by using the
   `point_in_time_recovery` custom property.

To enable PITR when you're creating a new table, you must set the status of `point_in_time_recovery`
to `enabled`. You can use the following CQL
command as an example.

```
CREATE TABLE "my_keyspace1"."my_table1"(
	"id" int,
	"name" ascii,
	"date" timestamp,
	PRIMARY KEY("id"))
WITH CUSTOM_PROPERTIES = {
	'capacity_mode':{'throughput_mode':'PAY_PER_REQUEST'},
	'point_in_time_recovery':{'status':'enabled'}
}
```

###### Note

If no point-in-time recovery custom property is specified, point-in-time
recovery is disabled by default. 2. To enable PITR for an existing table using CQL, run the following CQL
command.

```
ALTER TABLE `mykeyspace.mytable`
WITH custom_properties = {'point_in_time_recovery': {'status': 'enabled'}}
```

CLI

###### Configure PITR for a table using the AWS CLI

1. You can manage PITR settings for tables by using the
   `UpdateTable` API.

To enable PITR when you're creating a new table, you must include `point-in-time-recovery 'status=ENABLED'`
in the create table command.
You can use the following AWS CLI
command as an example. The command has been broken into separate lines to improve readability.

```
aws keyspaces create-table --keyspace-name 'myKeyspace' --table-name 'myTable'
            --schema-definition 'allColumns=[{name=id,type=int},{name=name,type=text},{name=date,type=timestamp}],partitionKeys=[{name=id}]'
            --point-in-time-recovery 'status=ENABLED'
```

###### Note

If no point-in-time recovery value is specified, point-in-time
recovery is disabled by default. 2. To confirm the point-in-time recovery setting for a table, you can use the following AWS CLI command.

```
aws keyspaces get-table --keyspace-name 'myKeyspace' --table-name 'myTable'
```

3. To enable PITR for an existing table using the AWS CLI, run the following command.

```
aws keyspaces update-table --keyspace-name 'myKeyspace' --table-name 'myTable' --point-in-time-recovery 'status=ENABLED'
```
