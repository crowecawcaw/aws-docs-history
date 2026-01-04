# Tutorial: Restore an Amazon Aurora DB cluster from a DB cluster snapshot

A common scenario when working with Amazon Aurora is to have a DB instance that you work with occasionally but that you don't need
full time. For example, you might use a DB cluster to hold the data for a report that you run only quarterly. One way to save money
on such a scenario is to take a DB cluster snapshot of the DB cluster after the report is completed. Then you delete the DB cluster,
and restore it when you need to upload new data and run the report during the next quarter.

When you restore a DB cluster, you provide the name of the DB cluster snapshot to restore
from. You then provide a name for the new DB cluster that's created from the restore
operation. For more detailed information on restoring DB clusters from snapshots, see [Restoring from a DB cluster snapshot](aurora-restore-snapshot.md "aurora-restore-snapshot.md").

In this tutorial, we also upgrade the restored DB cluster from Aurora MySQL version 2 (compatible with MySQL 5.7) to Aurora MySQL
version 3 (compatible with MySQL 8.0).

Restore a DB cluster to a specified time from a DB cluster snapshot using the Amazon RDS console or the AWS CLI.

For information about AWS KMS key management for Amazon RDS, see [AWS KMS key management](Overview.Encryption.md "Overview.Encryption.md").

###### Topics

- [Tutorial: Restoring a DB cluster from a DB cluster snapshot using the Amazon RDS console](tut-restore-cluster.md "tut-restore-cluster.md")
- [Tutorial: Restoring a DB cluster from a DB cluster snapshot using the AWS CLI](tut-restore-cluster.md "tut-restore-cluster.md")
