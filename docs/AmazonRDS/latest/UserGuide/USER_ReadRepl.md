# Creating a read replica

You can create a read replica from an existing DB instance using the AWS Management Console, AWS CLI, or RDS
API. You create a read replica by specifying `SourceDBInstanceIdentifier`, which
is the DB instance identifier of the source DB instance that you want to replicate from.

When you create a read replica, Amazon RDS takes a DB snapshot of your source DB instance and begins
replication. The source DB instance experiences a very brief I/O suspension when the DB snapshot operation
begins. The I/O suspension typically lasts about one second. You can avoid the I/O suspension if
the source DB instance is a Multi-AZ deployment, because in that case the snapshot is taken from the
secondary DB instance.

An active, long-running transaction can slow the process of creating the read replica. We
recommend that you wait for long-running transactions to complete before creating a read
replica. If you create multiple read replicas in parallel from the same source DB instance, Amazon RDS
takes only one snapshot at the start of the first create action.

When creating a read replica, there are a few things to consider. First, you must enable
automatic backups on the source DB instance by setting the backup retention period to a value
other than 0. This requirement also applies to a read replica that is the source DB instance for
another read replica. To enable automatic backups on an RDS for MySQL read replica, first
create the read replica, then modify the read replica to enable automatic backups.

###### Note

Within an AWS Region, we strongly recommend that you create all read replicas in the
same virtual private cloud (VPC) based on Amazon VPC as the source DB instance. If you create a
read replica in a different VPC from the source DB instance, classless inter-domain routing
(CIDR) ranges can overlap between the replica and the RDS system. CIDR overlap makes the
replica unstable, which can negatively impact applications connecting to it. If you
receive an error when creating the read replica, choose a different destination DB
subnet group. For more information, see [Working with a DB instance in a VPC](USER_VPC.md "USER_VPC.md").

There is no direct way to create a read replica in another AWS account using the
console or AWS CLI.

###### To create a read replica from a source DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB instance that you want to use as the source for a read
   replica.
4. For **Actions**, choose **Create read
   replica**.
5. For **DB instance identifier**, enter a name for the read
   replica.
6. Choose your instance configuration. We recommend that you use the same or
   larger DB instance class and storage type as the source DB instance for the read
   replica.
7. For **AWS Region**, specify the destination
   Region for the read replica.
8. For **Storage**, specify the allocated storage size and
   whether you want to use storage autoscaling.

If your source DB instance isn't on the latest storage configuration, the
**Upgrade storage file system configuration** option is
available. You can enable this setting to upgrade the storage file system of
the read replica to the preferred configuration. For more information, see
[Upgrading the storage file system for a DB
instance](USER_PIOPS.md "USER_PIOPS.md"). 9. For **Availability**, choose whether to create a standby
of your replica in another Availability Zone for failover support for the
replica.

###### Note

Creating your read replica as a Multi-AZ DB instance is independent of
whether the source database is a Multi-AZ DB instance. 10. Specify other DB instance settings. For information about each available
setting, see [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md"). 11. To create an encrypted read replica, expand **Additional
configuration** and specify the following settings:

    1. Choose **Enable encryption**.
    2. For **AWS KMS key**, choose the AWS KMS key
     identifier of the KMS key.###### Note

The source DB instance must be encrypted. To learn more about encrypting
the source DB instance, see [Encrypting Amazon RDS
resources](Overview.md "Overview.md"). 12. Choose **Create read replica**.
After the read replica is created, you can see it on the
**Databases** page in the RDS console. It shows
**Replica** in the **Role** column.

To create a read replica from a source DB instance, use the AWS CLI command [create-db-instance-read-replica](../../../cli/latest/reference/rds/create-db-instance-read-replica.md "../../../cli/latest/reference/rds/create-db-instance-read-replica.md"). This example also sets the allocated
storage size, enables storage autoscaling, and upgrades the file system to the
preferred configuration.

You can specify other settings. For information about each setting, see [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

###### Example

For Linux, macOS, or Unix:

```
aws rds create-db-instance-read-replica \
    --db-instance-identifier `myreadreplica` \
    --source-db-instance-identifier `mydbinstance` \
    --allocated-storage `100` \
    --max-allocated-storage `1000` \
    --upgrade-storage-config
```

For Windows:

```
aws rds create-db-instance-read-replica ^
    --db-instance-identifier `myreadreplica` ^
    --source-db-instance-identifier `mydbinstance` ^
    --allocated-storage `100` ^
    --max-allocated-storage `1000` ^
    --upgrade-storage-config
```

To create a read replica from a source Db2, MySQL, MariaDB, Oracle, PostgreSQL, or
SQL Server DB instance, call the Amazon RDS API [CreateDBInstanceReadReplica](../APIReference/API_CreateDBInstanceReadReplica.md "../APIReference/API_CreateDBInstanceReadReplica.md") operation with the following required
parameters:

- `DBInstanceIdentifier`
- `SourceDBInstanceIdentifier`

###### Note

To create an RDS for Db2 standby replica, set the optional
`ReplicaMode` operation to `mounted`.
