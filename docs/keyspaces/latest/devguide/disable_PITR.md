# Turn off PITR for an Amazon Keyspaces table

You can turn off PITR for an Amazon Keyspaces table at any time using the console, CQL, or the AWS CLI.

###### Important

Disabling PITR deletes your backup history immediately, even if you reenable
PITR on the table within 35 days.

To learn how to restore a table, see [Restore a table from backup to a specified point in time in Amazon Keyspaces](restoretabletopointintime.md "restoretabletopointintime.md").

Console

###### Disable PITR for a table using the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables** and select the
   table you want to edit.
3. On the **Backups** tab, choose
   **Edit**.
4. In the **Edit point-in-time recovery settings** section,
   clear the **Enable Point-in-time recovery** check
   box.
5. Choose **Save changes**.

Cassandra Query Language (CQL)

###### Disable PITR for a table using CQL

- To disable PITR for an existing table, run the following CQL command.

```
ALTER TABLE `mykeyspace.mytable`
WITH custom_properties = {'point_in_time_recovery': {'status': 'disabled'}}
```

CLI

###### Disable PITR for a table using the AWS CLI

- To disable PITR for an existing table, run the following AWS CLI command.

```
aws keyspaces update-table --keyspace-name 'myKeyspace' --table-name 'myTable' --point-in-time-recovery 'status=DISABLED'
```
