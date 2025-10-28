# Use point-in-time recovery in Amazon Keyspaces

With Amazon Keyspaces (for Apache Cassandra), you can restore tables to a specific point in time using Point-in-Time Restore (PITR).
PITR enables you to restore a table to a prior state within the last 35 days, providing data
protection and recovery capabilities. This feature is valuable in cases such as accidental data deletion,
application errors, or for testing purposes. You can quickly and efficiently recover data,
minimizing downtime and data loss. The following sections guide you through the process of
restoring tables using PITR in Amazon Keyspaces, ensuring data integrity and business continuity.

###### Topics

- [Configure restore table IAM permissions for Amazon Keyspaces PITR](howitworks_restore_permissions.md "howitworks_restore_permissions.md")
- [Configure PITR for a table in Amazon Keyspaces](configure_PITR.md "configure_PITR.md")
- [Turn off PITR for an Amazon Keyspaces table](disable_PITR.md "disable_PITR.md")
- [Restore a table from backup to a specified point in time in Amazon Keyspaces](restoretabletopointintime.md "restoretabletopointintime.md")
- [Restore a deleted table using Amazon Keyspaces PITR](restoredeleted.md "restoredeleted.md")
