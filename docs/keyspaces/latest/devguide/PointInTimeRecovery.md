# Backup and restore data with point-in-time recovery for Amazon Keyspaces

Point-in-time recovery (PITR) helps protect your Amazon Keyspaces tables from accidental write or
delete operations by providing you continuous backups of your table data.

For example, suppose that a test script writes accidentally to a production Amazon Keyspaces table.
With point-in-time recovery, you can restore that table's data to any second in time since
PITR was enabled within the last 35 days. If you delete a table with point-in-time recovery
enabled, you can query for the deleted table's data for 35 days (at no additional cost), and
restore it to the state it was in just before the point of deletion.

You can restore an Amazon Keyspaces table to a point in time by using the console, the AWS SDK and the AWS Command Line Interface (AWS CLI), or Cassandra
Query Language (CQL). For more information, see [Use point-in-time recovery in Amazon Keyspaces](PointInTimeRecovery_Tutorial.md "PointInTimeRecovery_Tutorial.md").

Point-in-time operations have no performance or availability impact on the base table, and
restoring a table doesn't consume additional throughput.

For information about PITR quotas, see [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md "quotas.md").

For information about pricing, see [Amazon Keyspaces (for Apache Cassandra) pricing](https://aws.amazon.com/keyspaces/pricing "https://aws.amazon.com/keyspaces/pricing").

###### Topics

- [How point-in-time recovery works in
  Amazon Keyspaces](PointInTimeRecovery_HowItWorks.md "PointInTimeRecovery_HowItWorks.md")
- [Use point-in-time recovery in Amazon Keyspaces](PointInTimeRecovery_Tutorial.md "PointInTimeRecovery_Tutorial.md")
