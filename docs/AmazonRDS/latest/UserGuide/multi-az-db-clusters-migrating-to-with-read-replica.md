# Migrating to a Multi-AZ DB cluster using a read replica

To migrate a Single-AZ deployment or Multi-AZ DB instance deployment to a Multi-AZ DB cluster deployment with reduced
downtime, you can create a Multi-AZ DB cluster read replica. For the source, you specify the DB instance in the Single-AZ
deployment or the primary DB instance in the Multi-AZ DB instance deployment. The DB instance can process write transactions
during the migration to a Multi-AZ DB cluster.

Consider the following before you create a Multi-AZ DB cluster read replica:

- The source DB instance must be on a version that supports Multi-AZ DB clusters. For more information, see
  [Supported
  Regions and DB engines for Multi-AZ DB clusters in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md").
- The Multi-AZ DB cluster read replica must be on the same major version as its source,
  and the same or higher minor version.
- You must turn on automatic backups on the source DB instance by setting the backup
  retention period to a value other than 0.
- The allocated storage of the source DB instance must be 100 GiB or higher.
- For RDS for MySQL, both the `gtid-mode` and `enforce_gtid_consistency`
  parameters must be set to `ON` for the source DB instance. You must
  use a custom parameter group, not the default parameter group. For more
  information, see [DB parameter groups for
  Amazon RDS DB instances](USER_WorkingWithDBInstanceParamGroups.md "USER_WorkingWithDBInstanceParamGroups.md").
- An active, long-running transaction can slow the process of creating the read replica. We
  recommend that you wait for long-running transactions to complete before creating a read replica.
- If you delete the source DB instance for a Multi-AZ DB cluster read replica, the read replica is promoted to
  a standalone Multi-AZ DB cluster.

## Creating and promoting the Multi-AZ DB cluster read replica

You can create and promote a Multi-AZ DB cluster read replica using the AWS Management Console, AWS CLI, or RDS API.

###### Note

We strongly recommend that you create all read replicas in the same virtual
private cloud (VPC) based on Amazon VPC of the source DB instance.

If you create a read replica in a different VPC from the source DB instance, Classless
Inter-Domain Routing (CIDR) ranges can overlap between the replica and the Amazon RDS
system. CIDR overlap makes the replica unstable, which can negatively impact
applications connecting to it. If you receive an error when creating the read
replica, choose a different destination DB subnet group. For more information,
see [Working with a DB instance in a VPC](USER_VPC.md "USER_VPC.md").

To migrate a Single-AZ deployment or Multi-AZ DB instance deployment to a Multi-AZ DB cluster using
a read replica, complete the following steps using the AWS Management Console.

1.  Sign in to the AWS Management Console and open the Amazon RDS console at
    [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2.  Create the Multi-AZ DB cluster read replica.
    1. In the navigation pane, choose **Databases**.
    2. Choose the DB instance that you want to use as the source for a read replica.
    3. For **Actions**, choose **Create read
       replica**.
    4. For **Availability and durability**, choose **Multi-AZ DB cluster**.
    5. For **DB instance identifier**, enter a name for the read replica.
    6. For the remaining sections, specify your DB cluster settings. For information about a setting, see
       [Settings for creating Multi-AZ DB clusters](create-multi-az-db-cluster.md#create-multi-az-db-cluster-settings "create-multi-az-db-cluster.md#create-multi-az-db-cluster-settings").
    7. Choose **Create read replica**.

3.  When you are ready, promote the read replica to be a standalone Multi-AZ DB cluster:

        1. Stop any transactions from being written to the source DB instance, and then wait for all updates
         to be made to the read replica.


        Database updates occur on the read replica after they have occurred on the primary DB
         instance. This replication lag can vary significantly. Use
         the `ReplicaLag` metric to determine when all
         updates have been made to the read replica. For more
         information about replica lag, see [Monitoring read replication](USER_ReadRepl.md "USER_ReadRepl.md").
        2. Sign in to the AWS Management Console and open the Amazon RDS console at
         [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
        3. In the Amazon RDS console, choose **Databases**.


        The **Databases** pane appears. Each read replica shows
         **Replica** in the **Role**
         column.
        4. Choose the Multi-AZ DB cluster read replica that you want to promote.
        5. For **Actions**, choose **Promote**.
        6. On the **Promote read replica** page, enter the backup
         retention period and the backup window for the newly promoted Multi-AZ DB cluster.
        7. When the settings are as you want them, choose
         **Promote read replica**.
        8. Wait for the status of the promoted Multi-AZ DB cluster to be
         `Available`.
        9. Direct your applications to use the promoted Multi-AZ DB cluster.Optionally, delete the Single-AZ deployment or Multi-AZ DB instance deployment if it is

    no longer needed. For instructions, see [Deleting a DB instance](USER_DeleteInstance.md "USER_DeleteInstance.md").
    To migrate a Single-AZ deployment or Multi-AZ DB instance deployment to a Multi-AZ DB cluster using
    a read replica, complete the following steps using the AWS CLI.

4.  Create the Multi-AZ DB cluster read replica.

To create a read replica from the source DB instance, use the AWS CLI command [`create-db-cluster`](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md"). For
`--replication-source-identifier`, specify the
Amazon Resource Name (ARN) of the source DB instance.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster \
  --db-cluster-identifier `mymultiazdbcluster` \
  --replication-source-identifier `arn:aws:rds:us-east-2:123456789012:db:mydbinstance`
  --engine postgres \
  --db-cluster-instance-class db.m5d.large \
  --storage-type io1 \
  --iops 1000 \
  --db-subnet-group-name `defaultvpc` \
  --backup-retention-period 1
```

For Windows:

```
aws rds create-db-cluster ^
  --db-cluster-identifier `mymultiazdbcluster` ^
  --replication-source-identifier `arn:aws:rds:us-east-2:123456789012:db:mydbinstance`
  --engine postgres ^
  --db-cluster-instance-class db.m5d.large ^
  --storage-type io1 ^
  --iops 1000 ^
  --db-subnet-group-name `defaultvpc` ^
  --backup-retention-period 1
```

2. Stop any transactions from being written to the source DB instance, and then wait for all updates
   to be made to the read replica.

Database updates occur on the read replica after they have occurred on the primary DB
instance. This replication lag can vary significantly. Use the
`Replica Lag` metric to determine when all updates
have been made to the read replica. For more information about
replica lag, see [Monitoring read replication](USER_ReadRepl.md "USER_ReadRepl.md"). 3. When you are ready, promote the read replica to be a standalone Multi-AZ DB cluster.

To promote a Multi-AZ DB cluster read replica, use the AWS CLI
command [`promote-read-replica-db-cluster`](../../../cli/latest/reference/rds/promote-read-replica-db-cluster.md "../../../cli/latest/reference/rds/promote-read-replica-db-cluster.md"). For `--db-cluster-identifier`,
specify the identifier of the Multi-AZ DB cluster read replica.

```
aws rds promote-read-replica-db-cluster --db-cluster-identifier `mymultiazdbcluster`
```

4. Wait for the status of the promoted Multi-AZ DB cluster to be
   `Available`.
5. Direct your applications to use the promoted Multi-AZ DB cluster.
   Optionally, delete the Single-AZ deployment or Multi-AZ DB instance deployment if it is
   no longer needed. For instructions, see [Deleting a DB instance](USER_DeleteInstance.md "USER_DeleteInstance.md").

To migrate a Single-AZ deployment or Multi-AZ DB instance deployment to a Multi-AZ DB cluster using
a read replica, complete the following steps using the RDS API.

1. Create the Multi-AZ DB cluster read replica.

To create a Multi-AZ DB cluster read replica, use the [`CreateDBCluster`](../APIReference/API_CreateDBCluster.md "../APIReference/API_CreateDBCluster.md") operation with the required
parameter `DBClusterIdentifier`. For
`ReplicationSourceIdentifier`, specify the Amazon
Resource Name (ARN) of the source DB instance. 2. Stop any transactions from being written to the source DB instance, and then wait for all updates
to be made to the read replica.

Database updates occur on the read replica after they have occurred on the primary DB
instance. This replication lag can vary significantly. Use the
`Replica Lag` metric to determine when all updates
have been made to the read replica. For more information about
replica lag, see [Monitoring read replication](USER_ReadRepl.md "USER_ReadRepl.md"). 3. When you are ready, promote read replica to be a standalone Multi-AZ DB cluster.

To promote a Multi-AZ DB cluster read replica, use the [`PromoteReadReplicaDBCluster`](../APIReference/API_PromoteReadReplicaDBCluster.md "../APIReference/API_PromoteReadReplicaDBCluster.md") operation with the required parameter `DBClusterIdentifier`.
Specify the identifier of the Multi-AZ DB cluster read replica. 4. Wait for the status of the promoted Multi-AZ DB cluster to be
`Available`. 5. Direct your applications to use the promoted Multi-AZ DB cluster.
Optionally, delete the Single-AZ deployment or Multi-AZ DB instance deployment if it is
no longer needed. For instructions, see [Deleting a DB instance](USER_DeleteInstance.md "USER_DeleteInstance.md").

## Limitations for creating a Multi-AZ DB cluster read replica

The following limitations apply to creating a Multi-AZ DB cluster read replica from a Single-AZ
deployment or Multi-AZ DB instance deployment.

- You can't create a Multi-AZ DB cluster read replica in an AWS account that is different from the
  AWS account that owns the source DB instance.
- You can't create a Multi-AZ DB cluster read replica in a different AWS Region from the source DB instance.
- You can't recover a Multi-AZ DB cluster read replica to a point in time.
- Storage encryption must have the same settings on the source DB instance and Multi-AZ DB cluster.
- If the source DB instance is encrypted, the Multi-AZ DB cluster read replica must be encrypted
  using the same KMS key.
- If the source DB instance uses General Purpose SSD (gp3) storage and has less
  than 400 GiB of allocated storage, you can't modify the provisioned IOPS for
  the Multi-AZ DB cluster read replica.
- To perform a minor version upgrade on the source DB instance, you must first perform the minor
  version upgrade on the Multi-AZ DB cluster read replica.
- When you perform a minor version upgrade on an RDS for PostgreSQL Multi-AZ DB cluster read replica, the
  reader DB instance doesn't switch to the writer DB instance after the upgrade.
  Therefore, your DB cluster might experience downtime while Amazon RDS upgrades the
  writer instance.
- You can't perform a major version upgrade on a Multi-AZ DB cluster read replica.
- You can perform a major version upgrade on the source DB instance of a Multi-AZ DB cluster read
  replica, but replication to the read replica stops and can't be restarted.
- The Multi-AZ DB cluster read replica doesn't support cascading read replicas.
- For RDS for PostgreSQL, Multi-AZ DB cluster read replicas can't fail over.
