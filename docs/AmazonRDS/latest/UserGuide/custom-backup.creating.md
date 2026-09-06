

# Creating an RDS Custom for Oracle snapshot
<a name="custom-backup.creating"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

RDS Custom for Oracle creates a storage volume snapshot of your DB instance, backing up the entire DB instance and not just individual databases. When your DB instance contains a container database (CDB), the snapshot of the instance includes the root CDB and all PDBs.

When you create an RDS Custom for Oracle snapshot, specify which RDS Custom DB instance to back up. Give your snapshot a name so you can restore from it later.

When you create a snapshot, RDS Custom for Oracle creates an Amazon EBS snapshot for every volume attached to the DB instance. RDS Custom for Oracle uses the EBS snapshot of the root volume to register a new Amazon Machine Image (AMI). To make snapshots easy to associate with a specific DB instance, they're tagged with `DBSnapshotIdentifier`, `DbiResourceId`, and `VolumeType`.

Creating a DB snapshot results in a brief I/O suspension. This suspension can last from a few seconds to a few minutes, depending on the size and class of your DB instance. The snapshot creation time varies with the size of your database. Because the snapshot includes the entire storage volume, the size of files, such as temporary files, also affects snapshot creation time. To learn more about creating snapshots, see [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md).

Create an RDS Custom for Oracle snapshot using the console or the AWS CLI.

## Console
<a name="USER_CreateSnapshot.CON"></a>

**To create an RDS Custom snapshot**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. In the list of RDS Custom DB instances, choose the instance for which you want to take a snapshot.

1. For **Actions**, choose **Take snapshot**.

   The **Take DB snapshot** window appears.

1. For **Snapshot name**, enter the name of the snapshot.

1. Choose **Take snapshot**.

## AWS CLI
<a name="USER_CreateSnapshot.CLI"></a>

You create a snapshot of an RDS Custom DB instance by using the [create-db-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-snapshot.html) AWS CLI command.

Specify the following options:
+ `--db-instance-identifier` – Identifies which RDS Custom DB instance you are going to back up
+ `--db-snapshot-identifier` – Names your RDS Custom snapshot so you can restore from it later

In this example, you create a DB snapshot called {{`my-custom-snapshot`}} for an RDS Custom DB instance called `{{my-custom-instance}}`.

**Example**  
For Linux, macOS, or Unix:  

```
1. aws rds create-db-snapshot \
2.     --db-instance-identifier {{my-custom-instance}} \
3.     --db-snapshot-identifier {{my-custom-snapshot}}
```
For Windows:  

```
1. aws rds create-db-snapshot ^
2.     --db-instance-identifier {{my-custom-instance}} ^
3.     --db-snapshot-identifier {{my-custom-snapshot}}
```