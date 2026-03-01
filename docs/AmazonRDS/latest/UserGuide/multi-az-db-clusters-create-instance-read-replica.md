# Creating a DB instance read replica from a Multi-AZ DB cluster

You can create a DB instance read replica from a Multi-AZ DB cluster in order to scale beyond the compute
or I/O capacity of the cluster for read-heavy database workloads. You can direct this
excess read traffic to one or more DB instance read replicas. You can also use read
replicas to migrate from a Multi-AZ DB cluster to a DB instance.

To create a read replica, specify a Multi-AZ DB cluster as the replication source. One of the reader
instances of the Multi-AZ DB cluster is always the source of replication, not the writer instance.
This condition ensures that the replica is always in sync with the source cluster, even
in cases of failover.

###### Topics

- [Comparing reader DB instances and DB instance read replicas](#multi-az-db-clusters-readerdb-vs-dbrr "#multi-az-db-clusters-readerdb-vs-dbrr")
- [Considerations](#multi-az-db-clusters-instance-read-replica-considerations "#multi-az-db-clusters-instance-read-replica-considerations")
- [Creating a DB instance read replica](#multi-az-db-clusters-instance-read-replica-create "#multi-az-db-clusters-instance-read-replica-create")
- [Promoting the DB instance read replica](#multi-az-db-clusters-promote-instance-read-replica "#multi-az-db-clusters-promote-instance-read-replica")
- [Limitations for creating a DB instance read replica from a Multi-AZ DB cluster](#multi-az-db-clusters-create-instance-read-replica-limitations "#multi-az-db-clusters-create-instance-read-replica-limitations")

## Comparing reader DB instances and DB instance read replicas

A _DB instance read replica_ of a Multi-AZ DB cluster is different than
the _reader DB instances_ of the Multi-AZ DB cluster in the
following ways:

- The reader DB instances act as automatic failover targets, while DB
  instance read replicas do not.
- Reader DB instances must acknowledge a change from the writer DB instance
  before the change can be committed. For DB instance read replicas, however,
  updates are asynchronously copied to the read replica without requiring
  acknowledgement.
- Reader DB instances always share the same instance class, storage type, and engine
  version as the writer DB instance of the Multi-AZ DB cluster. DB instance read replicas,
  however, don’t necessarily have to share the same configurations as the
  source cluster.
- You can promote a DB instance read replica to a standalone DB instance. You can’t promote
  a reader DB instance of a Multi-AZ DB cluster to a standalone instance.
- The reader endpoint only routes requests to the reader DB instances of the Multi-AZ DB cluster. It
  never routes requests to a DB instance read replica.

For more information about reader and writer DB instances, see [Multi-AZ DB cluster architecture](multi-az-db-clusters-concepts.md#multi-az-db-clusters-concepts-overview "multi-az-db-clusters-concepts.md#multi-az-db-clusters-concepts-overview").

## Considerations

Consider the following before you create a DB instance read replica from a Multi-AZ DB cluster:

- When you create the DB instance read replica, it must be on the same major version as its
  source cluster, and the same or higher minor version. After you create it, you
  can optionally upgrade the read replica to a higher minor version than the
  source cluster.
- When you create the DB instance read replica, the allocated storage must be the same as
  the allocated storage of the source Multi-AZ DB cluster. You can change the allocated
  storage after the read replica is created.
- For RDS for MySQL, the `gtid-mode` parameter must be set to `ON` for
  the source Multi-AZ DB cluster. For more information, see [Working with DB cluster parameter groups for Multi-AZ DB clusters](USER_WorkingWithDBClusterParamGroups.md "USER_WorkingWithDBClusterParamGroups.md").
- An active, long-running transaction can slow the process of creating the read replica. We
  recommend that you wait for long-running transactions to complete before creating a read replica.
- If you delete the source Multi-AZ DB cluster for a DB instance read replica, any read
  replicas that it's writing to are promoted to standalone DB instances.

## Creating a DB instance read replica

You can create a DB instance read replica from a Multi-AZ DB cluster using the AWS Management Console, AWS CLI, or RDS
API.

###### Note

We strongly recommend that you create all read replicas in the same virtual
private cloud (VPC) based on Amazon VPC of the source Multi-AZ DB cluster.

If you create a read replica in a different VPC from the source Multi-AZ DB cluster,
Classless Inter-Domain Routing (CIDR) ranges can overlap between the replica and
the RDS system. CIDR overlap makes the replica unstable, which can negatively
impact applications connecting to it. If you receive an error when creating the
read replica, choose a different destination DB subnet group. For more
information, see [Working with a DB instance in a VPC](USER_VPC.md "USER_VPC.md").

To create a DB instance read replica from a Multi-AZ DB cluster, complete the following steps using the
AWS Management Console.

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose
   **Databases**.
3. Choose the Multi-AZ DB cluster that you want to use as the source
   for a read replica.
4. For **Actions**, choose **Create read
   replica**.
5. For **Replica source**, make sure that the correct Multi-AZ DB cluster is
   selected.
6. For **DB identifier**, enter a name for the read
   replica.
7. For the remaining sections, specify your DB instance settings. For
   information about a setting, see [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

###### Note

The allocated storage for the DB instance read replica must be the same as the
allocated storage for the source Multi-AZ DB cluster. 8. Choose **Create read replica**.
To create a DB instance read replica from a Multi-AZ DB cluster, use the AWS CLI command [`create-db-instance-read-replica`](../../../cli/latest/reference/rds/create-db-instance-read-replica.md "../../../cli/latest/reference/rds/create-db-instance-read-replica.md"). For
`--source-db-cluster-identifier`, specify the identifier of
the Multi-AZ DB cluster.

For Linux, macOS, or Unix:

```
aws rds create-db-instance-read-replica \
  --db-instance-identifier `myreadreplica` \
  --source-db-cluster-identifier `mymultiazdbcluster`
```

For Windows:

```
aws rds create-db-instance-read-replica ^
  --db-instance-identifier `myreadreplica` ^
  --source-db-cluster-identifier `mymultiazdbcluster`
```

To create a DB instance read replica from a Multi-AZ DB cluster, use the [`CreateDBInstanceReadReplica`](../APIReference/API_CreateDBInstanceReadReplica.md "../APIReference/API_CreateDBInstanceReadReplica.md") operation.

## Promoting the DB instance read replica

If you no longer need the DB instance read replica, you can promote it into a standalone DB
instance. When you promote a read replica, the DB instance is rebooted before it
becomes available. For instructions, see [Promoting a read replica to be a standalone DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

If you're using the read replica to migrate a Multi-AZ DB cluster deployment to a Single-AZ or Multi-AZ
DB instance deployment, make sure to stop any transactions that are being written to
the source DB cluster. Then, wait for all updates to be made to the read replica.
Database updates occur on the read replica after they occur on one of the reader DB
instances of the Multi-AZ DB cluster. This replication lag can vary significantly. Use the
`ReplicaLag` metric to determine when all updates have been made to
the read replica. For more information about replica lag, see [Monitoring read replication](USER_ReadRepl.md "USER_ReadRepl.md").

After you promote the read replica, wait for the status of the promoted DB
instance to be `Available` before you direct your applications to use the
promoted DB instance. Optionally, delete the Multi-AZ DB cluster deployment if you
no longer need it. For instructions, see [Deleting a Multi-AZ DB cluster for Amazon RDS](USER_DeleteMultiAZDBCluster.md "USER_DeleteMultiAZDBCluster.md").

## Limitations for creating a DB instance read replica from a Multi-AZ DB cluster

The following limitations apply to creating a DB instance read replica from a Multi-AZ DB cluster
deployment.

- You can't create a DB instance read replica in an AWS account that's different from the
  AWS account that owns the source Multi-AZ DB cluster.
- You can't create a DB instance read replica in a different AWS Region from the source
  Multi-AZ DB cluster.
- You can't recover a DB instance read replica to a point in time.
- Storage encryption must have the same settings on the source Multi-AZ DB cluster and DB instance read
  replica.
- If the source Multi-AZ DB cluster is encrypted, the DB instance read replica must be
  encrypted using the same KMS key.
- To perform a minor version upgrade on the source Multi-AZ DB cluster, you must first
  perform the minor version upgrade on the DB instance read replica.
- The DB instance read replica doesn't support cascading read replicas.
- For RDS for PostgreSQL, the source Multi-AZ DB cluster must be running PostgreSQL version 13.11, 14.8, or
  15.2.R2 or higher in order to create a DB instance read replica.
- You can perform a major version upgrade on the source Multi-AZ DB cluster of a DB instance read
  replica, but replication to the read replica stops and can't be restarted.
