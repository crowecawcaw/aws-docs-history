Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Restoring a table

You can also restore a specific table from a snapshot or a recovery point When you do
so, you specify the source snapshot or recovery point, database, schema, table, the
target database, schema, and new table name. This new table can't have the same name as
an existing table. If you want to replace an existing table by restoring a table, you
must first rename or drop the table before you restore the table.

###### Note

No-backup tables aren't supported for RA3 provisioned clusters and Amazon Redshift Serverless workgroups.
A table marked as no-backup in an RA3 cluster or serverless workgroup is treated as a permanent table that will
always be backed up while taking a snapshot, and always restored when restoring from a snapshot. However, selective restoration of no-backup tables
isn't supported.

The target table is created using the source table's column definitions, table
attributes, and column attributes except for foreign keys. To prevent conflicts due to
dependencies, the target table doesn't inherit foreign keys from the source table. Any
dependencies, such as views or permissions granted on the source table, aren't
applied to the target table.

If the owner of the source table exists, then that user is the owner of the restored
table, provided that the user has sufficient permissions to become the owner of a
relation in the specified database and schema. Otherwise, the restored table is owned by
the admin user that was created when the cluster was launched.

The restored table returns to the state it was in at the time the backup was taken.
This includes transaction visibility rules defined by the Amazon Redshift adherence to [serializable
isolation](../dg/c_serial_isolation.md "../dg/c_serial_isolation.md"), meaning that data will be immediately visible to in flight
transactions started after the backup.

You can use the Amazon Redshift Serverless console
to restore tables from a snapshot.

Restoring a table from data backup has the following limitations:

- You can only restore one table at a time.
- Any dependencies, such as views or permissions granted on the source table,
  aren't applied to the target table.
- If row-level security is turned on for a table being restored, Amazon Redshift Serverless
  restores the table with row-level security turned on.
  To restore a table using the Amazon Redshift Serverless console

1. On the Amazon Redshift Serverless console, choose **Data backup**.
2. Choose the snapshot or recovery point that has the table to restore.
3. Choose **Actions**, **Restore table from
   snapshot** or **Restore table from recovery
   point**.
4. Enter information about the source snapshot or recovery point and target
   table, then choose **Restore table**.
