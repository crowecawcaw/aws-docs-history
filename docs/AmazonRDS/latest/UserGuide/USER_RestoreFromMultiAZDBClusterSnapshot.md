# Restoring from a Multi-AZ DB cluster snapshot to a

DB instance

A _Multi-AZ DB cluster snapshot_ is a storage volume snapshot of your DB cluster,
backing up the entire DB cluster and not just individual databases. You can restore a Multi-AZ DB cluster
snapshot to a Single-AZ deployment or Multi-AZ DB instance deployment. For information about Multi-AZ
deployments, see [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.md "Concepts.md").

###### Note

You can also restore a Multi-AZ DB cluster snapshot to a new Multi-AZ DB cluster. For instructions,
see [Restoring from a
snapshot to a Multi-AZ DB cluster](USER_RestoreFromMultiAZDBClusterSnapshot.md "USER_RestoreFromMultiAZDBClusterSnapshot.md").

For information about restoring a Multi-AZ DB cluster with an RDS Extended Support version, see [Restoring a DB instance or a Multi-AZ DB cluster with Amazon RDS Extended Support](extended-support-restoring-db-instance.md "extended-support-restoring-db-instance.md").

Use the AWS Management Console, the AWS CLI, or the RDS API to restore a Multi-AZ DB cluster snapshot to a
Single-AZ deployment or Multi-AZ DB instance deployment.

###### To restore a Multi-AZ DB cluster snapshot to a Single-AZ deployment or Multi-AZ DB instance deployment

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. Choose the Multi-AZ DB cluster snapshot that you want to restore from.
4. For **Actions**, choose **Restore snapshot**.
5. On the **Restore snapshot** page, in **Availability and durability**,
   choose one of the following:
   - **Single DB instance** – Restores the snapshot to one DB instance
     with no standby DB instance.
   - **Multi-AZ DB instance** – Restores the snapshot to a Multi-AZ DB instance deployment with one primary DB instance and one standby DB instance.

6. For **DB instance identifier**, enter the name for your
   restored DB instance.
7. For the remaining sections, specify your DB instance settings. For information about each setting, see
   [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
8. Choose **Restore DB instance**.
   To restore a Multi-AZ DB cluster snapshot to a DB instance deployment, use the AWS CLI command [restore-db-instance-from-db-snapshot](../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md "../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md").

In the following example, you restore from a previously created Multi-AZ DB cluster snapshot named
`myclustersnapshot`. You restore to a new Multi-AZ DB instance deployment
with a primary DB instance named `mynewdbinstance`. For the
`--db-cluster-snapshot-identifier` option, specify the name of the
Multi-AZ DB cluster snapshot.

For the `--db-instance-class` option, specify the DB instance class for the new
DB instance deployment. For more information about DB instance classes, see [DB instance classes](Concepts.md "Concepts.md").

You can also specify other options.

For Linux, macOS, or Unix:

```
aws rds restore-db-instance-from-db-snapshot \
    --db-instance-identifier `mynewdbinstance` \
    --db-cluster-snapshot-identifier `myclustersnapshot` \
    --engine mysql \
    --multi-az \
    --db-instance-class `db.r6g.xlarge`
```

For Windows:

```
aws rds restore-db-instance-from-db-snapshot ^
    --db-instance-identifier `mynewdbinstance` ^
    --db-cluster-snapshot-identifier `myclustersnapshot` ^
    --engine mysql ^
    --multi-az ^
    --db-instance-class `db.r6g.xlarge`
```

After you restore the DB instance, you can add it to the security group associated with the
Multi-AZ DB cluster that you used to create the snapshot, if applicable. Completing
this action provides the same functions of the previous Multi-AZ DB cluster.

To restore a Multi-AZ DB cluster snapshot to a DB instance deployment, call the RDS API
operation [RestoreDBInstanceFromDBSnapshot](../APIReference/API_RestoreDBInstanceFromDBSnapshot.md "../APIReference/API_RestoreDBInstanceFromDBSnapshot.md") with the following parameters:

- `DBInstanceIdentifier`
- `DBClusterSnapshotIdentifier`
- `Engine`
  You can also specify other optional parameters.

After you restore the DB instance, you can add it to the security group associated with the
Multi-AZ DB cluster that you used to create the snapshot, if applicable. Completing
this action provides the same functions of the previous Multi-AZ DB cluster.
