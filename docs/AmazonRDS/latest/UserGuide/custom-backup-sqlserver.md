# Creating an RDS Custom for SQL Server snapshot

RDS Custom for SQL Server creates a storage volume snapshot of your DB instance, backing up the entire DB instance and not just individual databases.
When you create a snapshot, specify which RDS Custom for SQL Server DB instance to back up. Give your snapshot a name so you can restore from it
later.

When you create a snapshot, RDS Custom for SQL Server creates an Amazon EBS snapshot for volume `(D:)`, which is the database volume attached
to the DB instance. To make snapshots easy to associate with a specific DB
instance, they're tagged with `DBSnapshotIdentifier`,
`DbiResourceId`, and `VolumeType`.

Creating a DB snapshot results in a brief I/O suspension. This suspension can last
from a few seconds to a few minutes, depending on the size and class of your DB
instance. The snapshot creation time varies with the total count and size of your databases.
To learn more about the number of databases eligible for a point in time restore (PITR) operation,
see [Number of databases eligible for PITR per instance class type](custom-backup.md#custom-backup.pitr.sqlserver.eligiblecountperinstance "custom-backup.md#custom-backup.pitr.sqlserver.eligiblecountperinstance").

Because the snapshot includes the entire storage volume, the size of files, such as temporary files,
also affects snapshot creation time. To learn more about creating snapshots,
see [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md").

Create an RDS Custom for SQL Server snapshot using the console or the AWS CLI.

###### To create an RDS Custom snapshot

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. In the list of RDS Custom DB instances, choose the instance for which you want to take a snapshot.
4. For **Actions**, choose **Take snapshot**.

The **Take DB snapshot** window appears. 5. For **Snapshot name**, enter the name of the snapshot. 6. Choose **Take snapshot**.
You create a snapshot of an RDS Custom DB instance by using the [create-db-snapshot](../../../cli/latest/reference/rds/create-db-snapshot.md "../../../cli/latest/reference/rds/create-db-snapshot.md") AWS CLI command.

Specify the following options:

- `--db-instance-identifier` – Identifies which RDS Custom DB instance you are going to
  back up
- `--db-snapshot-identifier` – Names your RDS Custom snapshot so you can restore from it later
  In this example, you create a DB snapshot called
  `my-custom-snapshot` for an RDS Custom
  DB instance called
  `my-custom-instance`.

For Linux, macOS, or Unix:

```
aws rds create-db-snapshot \
    --db-instance-identifier `my-custom-instance` \
    --db-snapshot-identifier `my-custom-snapshot`
```

For Windows:

```
aws rds create-db-snapshot ^
    --db-instance-identifier `my-custom-instance` ^
    --db-snapshot-identifier `my-custom-snapshot`
```
