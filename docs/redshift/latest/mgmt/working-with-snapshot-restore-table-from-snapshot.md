Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Restoring a table from

a snapshot

You can restore a single table from a snapshot instead of restoring an entire cluster.
When you restore a single table from a snapshot, you specify the source snapshot, database,
schema, and table name, and the target database, schema, and a new table name for the
restored table.

###### Note

No-backup tables aren't supported for RA3 provisioned clusters and Amazon Redshift Serverless workgroups.
A table marked as no-backup in an RA3 cluster or serverless workgroup is treated as a permanent table that will
always be backed up while taking a snapshot, and always restored when restoring from a snapshot. However, selective restoration of no-backup tables isn't
supported.

The new table name cannot be the name of an existing table. To replace an existing table
with a restored table from a snapshot, rename or drop the existing table before you restore
the table from the snapshot.

The target table is created using the source table's column definitions, table
attributes, and column attributes except for foreign keys. To prevent conflicts due to
dependencies, the target table doesn't inherit foreign keys from the source table. Any
dependencies, such as views or permissions granted on the source table, aren't applied
to the target table.

If the owner of the source table exists, then that database user is the owner of the
restored table, provided that the user has sufficient permissions to become the owner of a
relation in the specified database and schema. Otherwise, the restored table is owned by
the admin user that was created when the cluster was launched.

The restored table returns to the state it was in at the time the backup was taken. This
includes transaction visibility rules defined by the Amazon Redshift adherence to [serializable isolation](../dg/c_serial_isolation.md "../dg/c_serial_isolation.md"), meaning that
data will be immediately visible to in flight transactions started after the backup.

Restoring a table from a snapshot has the following limitations:

- You can restore a table only to the current, active running cluster and from a
  snapshot that was taken of that cluster.
- You can restore only one table at a time.
- You can't restore a table from a cluster snapshot that was taken prior to a
  cluster being resized. An exception is that you
  can restore a table after an elastic resize if the node type didn't change.
- Any dependencies, such as views or permissions granted on the source table,
  aren't applied to the target table.
- If row-level security is turned on for a table being restored, Amazon Redshift restores
  the table with row-level security turned on.

###### To restore a table from a snapshot

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then choose the
   cluster that you want to use to restore a table.
3. For **Actions**, choose **Restore table** to
   display the **Restore table** page.
4. Enter the information about which snapshot, source table, and target table to use,
   and then choose **Restore table**.

###### Example: Restoring a table from a snapshot using the AWS CLI

The following example uses the `restore-table-from-cluster-snapshot` AWS CLI
command to restore the `my-source-table` table from the
`sample-database` schema in the `my-snapshot-id`. You can use
the AWS CLI command `describe-table-restore-status` to review the status of
your restore operation. The example restores the snapshot to the
`mycluster-example` cluster with a new table name of
`my-new-table`.

```

aws redshift restore-table-from-cluster-snapshot --cluster-identifier mycluster-example
                                                 --new-table-name my-new-table
                                                 --snapshot-identifier my-snapshot-id
                                                 --source-database-name sample-database
                                                 --source-table-name my-source-table

```
