# How point-in-time recovery works in

Amazon Keyspaces

This section provides an overview of how Amazon Keyspaces point-in-time recovery (PITR) works. For more information about pricing,
see [Amazon Keyspaces (for Apache Cassandra)
pricing](https://aws.amazon.com/keyspaces/pricing "https://aws.amazon.com/keyspaces/pricing").

###### Topics

- [Time window for PITR continuous backups](#howitworks_backup_window "#howitworks_backup_window")
- [PITR restore settings](#howitworks_backup_settings "#howitworks_backup_settings")
- [PITR restore of encrypted tables](#howitworks_backup_encryption "#howitworks_backup_encryption")
- [PITR restore of multi-Region
  tables](#howitworks_backup_multiRegion "#howitworks_backup_multiRegion")
- [PITR restore of tables with user-defined types (UDTs)](#howitworks_backup_udt "#howitworks_backup_udt")
- [Table restore time with PITR](#howitworks_restore_time "#howitworks_restore_time")
- [Amazon Keyspaces PITR and integration with AWS
  services](#howitworks_integration "#howitworks_integration")

## Time window for PITR continuous backups

Amazon Keyspaces PITR uses two timestamps to maintain the time frame for which restorable backups
are available for a table.

- Earliest restorable time – Marks the time of the earliest restorable
  backup. The earliest restorable backup goes back up to 35 days or when PITR was
  enabled, whichever is more recent. The maximum backup window of 35 days can't be
  modified.
- Current time – The timestamp for the latest restorable backup is the
  current time. If no timestamp is provided during a restore, current time is
  used.

When PITR is enabled, you can restore to any point in time between
`EarliestRestorableDateTime` and `CurrentTime`. You can only
restore table data to a time when PITR was enabled.

If you disable PITR and later reenable it again, you reset the start time for the
first available backup to when PITR was reenabled. This means that disabling PITR erases
your backup history.

###### Note

Data definition language (DDL) operations on tables, such as schema changes, are
performed asynchronously. You can only see completed operations in your restored
table data, but you might see additional actions on your source table if they were
in progress at the time of the restore. For a list of DDL statements, see [DDL statements (data definition language) in Amazon Keyspaces](cql.md "cql.md").

A table doesn't have to be active to be restored. You can also restore deleted tables
if PITR was enabled on the deleted table and the deletion occurred within the backup
window (or within the last 35 days).

###### Note

If a new table is created with the same qualified name (for example,
mykeyspace.mytable) as a previously deleted table, the deleted table will no longer
be restorable. If you attempt to do this from the console, a warning is
displayed.

## PITR restore settings

When you restore a table using PITR, Amazon Keyspaces restores your source table's schema and
data to the state based on the selected timestamp (`day:hour:minute:second`)
to a new table. PITR doesn't overwrite existing tables.

In addition to the table's schema and data, PITR restores the
`custom_properties` from the source table. Unlike the table's data, which
is restored based on the selected timestamp between earliest restore time and current
time, custom properties are always restored based on the table's settings as of the
current time.

The settings of the restored table match the settings of the source table with the
timestamp of when the restore was initiated. If you want to overwrite these settings
during restore, you can do so using `WITH custom_properties`. Custom
properties include the following settings.

- Read/write capacity mode
- Provisioned throughput capacity settings
- PITR settings

If the table is in provisioned capacity mode with auto scaling enabled, the restore
operation also restores the table's auto scaling settings. You can overwrite them using
the `autoscaling_settings` parameter in CQL or
`autoScalingSpecification` with the CLI. For more information on auto
scaling settings, see [Manage throughput capacity automatically with Amazon Keyspaces auto scaling](autoscaling.md "autoscaling.md").

When you do a full table restore, all table settings for the restored table come from
the current settings of the source table at the time of the restore.

For example, suppose that a table's provisioned throughput was recently lowered to 50
read capacity units and 50 write capacity units. You then restore the table's state to
three weeks ago. At this time, its provisioned throughput was set to 100 read capacity
units and 100 write capacity units. In this case, Amazon Keyspaces restores your table data to that
point in time, but uses the current provisioned throughput settings (50 read capacity
units and 50 write capacity units).

The following settings are not restored, and you must configure them manually for the
new table.

- Amazon Keyspaces change data capture (CDC) streams
- AWS Identity and Access Management (IAM) policies
- Amazon CloudWatch metrics and alarms
- Tags (can be added to the CQL `RESTORE` statement using `WITH
TAGS`)

## PITR restore of encrypted tables

When you restore a table using PITR, Amazon Keyspaces restores your source table's encryption
settings. If the table was encrypted with an AWS owned key (default), the table is
restored with the same setting automatically. If the table you want to restore was
encrypted using a customer managed key, the same customer managed key needs to be accessible to Amazon Keyspaces to
restore the table data.

You can change the encryption settings of the table at the time of restore. To change
from an AWS owned key to a customer managed key, you need to supply a valid and accessible
customer managed key at the time of restore.

If you want to change from a customer managed key to an AWS owned key, confirm that Amazon Keyspaces has
access to the customer managed key of the source table to restore the table with an
AWS owned key. For more information about encryption at rest settings for tables, see
[Encryption at rest: How it works in Amazon Keyspaces](encryption.md "encryption.md").

###### Note

If the table was deleted because Amazon Keyspaces lost access to your customer managed key, you need to
ensure the customer managed key is accessible to Amazon Keyspaces before trying to restore the table. A
table that was encrypted with a customer managed key can't be restored if Amazon Keyspaces doesn't have
access to that key. For more information, see [Troubleshooting key
access](../../../kms/latest/developerguide/policy-evaluation.md "../../../kms/latest/developerguide/policy-evaluation.md") in the AWS Key Management Service Developer Guide.

## PITR restore of multi-Region

tables

You can restore a multi-Region table using PITR. For the restore operation to be
successful, PITR has to be enabled on all replicas of the source table and both the source and the destination table
have to be replicated to the same AWS Regions.

Amazon Keyspaces restores the settings of the source table in each of the replicated Regions that
are part of the keyspace. You can also override settings during the restore operation.
For more information about settings that can be changed during the restore, see [PITR restore settings](#howitworks_backup_settings "#howitworks_backup_settings").

For more information about multi-Region replication, see [How multi-Region replication works in Amazon Keyspaces](multiRegion-replication_how-it-works.md "multiRegion-replication_how-it-works.md").

## PITR restore of tables with user-defined types (UDTs)

You can restore a table that uses UDTs. For the restore operation to be successful, the referenced
UDTs have to exist and be valid in the keyspace.

If any required UDT is missing when you attempt to restore a table, Amazon Keyspaces tries to restore the UDT schema automatically
and then continues to restore the table.

If you removed and recreated the UDT, Amazon Keyspaces restores the UDT with the new schema of the UDT and rejects the request
to restore the table using the original UDT schema. In this case, if you wish to restore the table with the old UDT schema,
you can restore the table to a new keyspace. When you delete and recreate a UDT, even if the schema of the recreated UDT is
the same as the schema of the deleted UDT, the recreated UDT is considered a new UDT. In this case, Amazon Keyspaces rejects the
request to restore the table with the old UDT schema.

If the UDT is missing and Amazon Keyspaces attempts to restore the UDT, the attempt fails if you
have reached the maximum number of UDTs for the account in the Region.

For more information about UDT quotas and default values, see [Quotas and default values for user-defined types (UDTs) in Amazon Keyspaces](quotas.md#quotas-udts "quotas.md#quotas-udts"). For more information about working with UDTs, see [User-defined types (UDTs) in Amazon Keyspaces](udts.md "udts.md").

## Table restore time with PITR

The time it takes you to restore a table is based on multiple factors and isn't always
correlated directly to the size of the table.

The following are some considerations for restore times.

- You restore backups to a new table. It can take up to 20 minutes (even if the
  table is empty) to perform all the actions to create the new table and initiate
  the restore process.
- Restore times for large tables with well-distributed data models can be
  several hours or longer.
- If your source table contains data that is significantly skewed, the time to restore might increase.
  For example, if your table’s primary key is using the month of the year as a partition key, and all your
  data is from the month of December, you have skewed data.

A best practice when planning for disaster recovery is to regularly document average restore completion times
and establish how these times affect your overall Recovery Time Objective.

## Amazon Keyspaces PITR and integration with AWS

services

The following PITR operations are logged using AWS CloudTrail to enable continuous
monitoring and auditing.

- Create a new table with PITR enabled or disabled.
- Enable or disable PITR on an existing table.
- Restore an active or a deleted table.

For more information, see [Logging Amazon Keyspaces API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

You can perform the following PITR actions using CloudFormation.

- Create a new table with PITR enabled or disabled.
- Enable or disable PITR on an existing table.

For more information, see the [Cassandra Resource Type Reference](../../../AWSCloudFormation/latest/UserGuide/AWS_Cassandra.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Cassandra.md")
in the [CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md").
