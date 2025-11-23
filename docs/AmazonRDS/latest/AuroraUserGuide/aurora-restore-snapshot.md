# Restoring from a DB cluster snapshot

Amazon RDS creates a storage volume snapshot of your DB cluster, backing up the entire DB
cluster and not just individual databases. You can create a new DB cluster by restoring from
a DB snapshot. You provide the name of the DB cluster snapshot to restore from, and then
provide a name for the new DB cluster that is created from the restore. You can't restore
from a DB cluster snapshot to an existing DB cluster; a new DB cluster is created when you
restore.

###### Important

You can't restore a snapshot to a DB engine version that has passed its Aurora end of standard support date.
You can only access a database after it successfully upgrades to a supported version.
For more information on supported Aurora DB engine versions, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md "extended-support.md").

If an upgrade to a supported version for your cluster fails, the cluster status changes to `upgrade_failed` and Aurora creates a final snapshot with the prefix `rds-final`.
For access to your restored database on the deprecated version after an upgrade failure, contact AWS Support.

You can use the restored DB cluster as soon as its status is
`available`.

You can use CloudFormation to restore a DB cluster from a DB cluster snapshot. For more
information, see [AWS::RDS::DBCluster](../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.md") in the _AWS CloudFormation User Guide_.

###### Note

Sharing a manual DB cluster snapshot, whether encrypted or unencrypted, enables
authorized AWS accounts to directly restore a DB cluster from the snapshot instead of
taking a copy of it and restoring from that. For more information, see [Sharing a DB cluster snapshot](aurora-share-snapshot.md "aurora-share-snapshot.md").

For information about restoring an Aurora DB cluster or a global cluster with an RDS Extended Support version,
see [Restoring an
Aurora DB cluster or a global cluster with Amazon RDS Extended Support](extended-support-restoring-db-instance.md "extended-support-restoring-db-instance.md").

## Parameter group

considerations

We recommend that you retain the DB parameter group and DB cluster parameter group for
any DB cluster snapshots you create, so that you can associate your restored DB cluster
with the correct parameter groups.

The default DB parameter group and DB cluster parameter group are associated with the
restored cluster, unless you choose different ones. No custom parameter settings are
available in the default parameter groups.

You can specify the parameter groups when you restore the DB cluster.

For more information about DB parameter groups and DB cluster parameter groups, see
[Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

## Security group considerations

When you restore a DB cluster, the default virtual private cloud (VPC), DB subnet
group, and VPC security group are associated with the restored instance, unless you
choose different ones.

- If you're using the Amazon RDS console, you can specify a custom VPC security group
  to associate with the cluster or create a new VPC security group.
- If you're using the AWS CLI, you can specify a custom VPC security group to
  associate with the cluster by including the
  `--vpc-security-group-ids` option in the
  `restore-db-cluster-from-snapshot` command.
- If you're using the Amazon RDS API, you can include the
  `VpcSecurityGroupIds.VpcSecurityGroupId.N` parameter in the
  `RestoreDBClusterFromSnapshot` action.

As soon as the restore is complete and your new DB cluster is available, you can also
change the VPC settings by modifying the DB cluster. For more information, see [Modifying an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

## Amazon Aurora considerations

With Aurora, you restore a DB cluster snapshot to a DB cluster.

With both Aurora MySQL and Aurora PostgreSQL, you can also restore a DB cluster snapshot to
an Aurora Serverless DB cluster. For more information, see [Restoring an Aurora Serverless v1 DB cluster](aurora-serverless.md "aurora-serverless.md").

With Aurora MySQL, you can restore a DB cluster snapshot from a cluster without parallel
query to a cluster with parallel query. Because parallel query is typically used with
very large tables, the snapshot mechanism is the fastest way to ingest large volumes of
data to an Aurora MySQL parallel query-enabled cluster. For more information, see [Parallel query for Amazon Aurora MySQL](aurora-mysql-parallel-query.md "aurora-mysql-parallel-query.md").

## Restoring from a snapshot

You can restore a DB cluster from a DB cluster snapshot using the AWS Management Console, the
AWS CLI, or the RDS API.

###### To restore a DB cluster from a DB cluster snapshot

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. Choose the DB cluster snapshot that you want to restore from.
4. For **Actions**, choose **Restore
   snapshot**.

The **Restore snapshot** page displays. 5. Choose the DB engine version to which you want to restore the DB
cluster.

By default, the snapshot is restored to the same DB engine version as
the source DB cluster, if that version is available. 6. For **DB instance identifier**, enter the name for
your restored DB instance. Note that Amazon RDS derives the DB cluster identifier
from the DB instance identifier you specify. 7. Specify other settings, such as the DB cluster storage
configuration.

For information about each setting, see [Settings for Aurora DB clusters](Aurora.md#Aurora.CreateInstance.Settings "Aurora.md#Aurora.CreateInstance.Settings"). 8. Choose **Restore DB cluster**.
To restore a DB cluster from a DB cluster snapshot, use the AWS CLI command
[restore-db-cluster-from-snapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-cluster-from-snapshot.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-cluster-from-snapshot.html").

In this example, you restore from a previously created DB cluster snapshot
named `mydbclustersnapshot`. You restore to a new DB cluster named
`mynewdbcluster`.

You can specify other settings, such as the DB engine version. If you don't
specify an engine version, the DB cluster is restored to the default engine
version.

For information about each setting, see [Settings for Aurora DB clusters](Aurora.md#Aurora.CreateInstance.Settings "Aurora.md#Aurora.CreateInstance.Settings").

###### Example

For Linux, macOS, or Unix:

```
aws rds restore-db-cluster-from-snapshot \
    --db-cluster-identifier `mynewdbcluster` \
    --snapshot-identifier `mydbclustersnapshot` \
    --engine `aurora-mysql|aurora-postgresql`
```

For Windows:

```
aws rds restore-db-cluster-from-snapshot ^
    --db-cluster-identifier `mynewdbcluster` ^
    --snapshot-identifier `mydbclustersnapshot` ^
    --engine `aurora-mysql|aurora-postgresql`
```

After the DB cluster has been restored, you must add the DB cluster to the
security group used by the DB cluster used to create the DB cluster snapshot if
you want the same functionality as that of the previous DB cluster.

###### Important

If you use the console to restore a DB cluster, then Amazon RDS automatically
creates the primary DB instance (writer) for your DB cluster. If you use the
AWS CLI to restore a DB cluster, you must explicitly create the primary
instance for your DB cluster. The primary instance is the first instance
that is created in a DB cluster. If you don't create the primary DB
instance, the DB cluster endpoints remain in the `creating`
status.

Call the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") AWS CLI command to create the primary instance
for your DB cluster. Include the name of the DB cluster as the
`--db-cluster-identifier` option value.

To restore a DB cluster from a DB cluster snapshot, call the RDS API operation
[RestoreDBClusterFromSnapshot](../APIReference/API_RestoreDBClusterFromSnapshot.md "../APIReference/API_RestoreDBClusterFromSnapshot.md") with the following parameters:

- `DBClusterIdentifier`
- `SnapshotIdentifier`

###### Important

If you use the console to restore a DB cluster, then Amazon RDS automatically
creates the primary DB instance (writer) for your DB cluster. If you use the
RDS API to restore a DB cluster, you must explicitly create the primary
instance for your DB cluster. The primary instance is the first instance
that is created in a DB cluster. If you don't create the primary DB
instance, the DB cluster endpoints remain in the `creating`
status.

Call the RDS API operation [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md")
to create the primary instance for your DB cluster. Include the name of the
DB cluster as the `DBClusterIdentifier` parameter value.
