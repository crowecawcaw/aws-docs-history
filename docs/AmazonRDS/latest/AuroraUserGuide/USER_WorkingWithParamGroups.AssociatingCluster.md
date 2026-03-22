# Associating a DB cluster parameter group with a DB cluster in Amazon Aurora

You can create your own DB cluster parameter groups with customized settings. You can associate a DB cluster parameter group
with a DB cluster using the AWS Management Console, the AWS CLI, or the RDS API. You can do so when you create or modify a DB cluster.

For information about creating a DB cluster parameter group, see [Creating a DB cluster parameter groupin Amazon Aurora](USER_WorkingWithParamGroups.CreatingCluster.md "USER_WorkingWithParamGroups.CreatingCluster.md"). For information about creating a DB cluster, see
[Creating an Amazon Aurora DB cluster](Aurora.CreateInstance.md "Aurora.CreateInstance.md"). For information about modifying a DB cluster, see
[Modifying an Amazon Aurora DB cluster](Aurora.Modifying.md "Aurora.Modifying.md").

###### Note

For Aurora PostgreSQL 15.2, 14.7, 13.10, 12.14, and all 11 versions, when you change the DB cluster parameter group associated with a DB cluster, reboot each replica
instance to apply the changes.

To determine whether the primary DB instance of a DB cluster must be rebooted to
apply changes, run the following AWS CLI command:

`aws rds describe-db-clusters --db-cluster-identifier `db_cluster_identifier``

Check the `DBClusterParameterGroupStatus` value for the primary DB instance in the output. If the value is `pending-reboot`,
then reboot the primary DB instance of the DB cluster.

###### To associate a DB cluster parameter group with a DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane,
   choose **Databases**,
   and then select the DB cluster that you want to modify.
3. Choose **Modify**.
   The **Modify DB cluster** page appears.
4. Change the **DB cluster parameter group** setting.
5. Choose **Continue** and check the summary of modifications.

The change is applied immediately regardless of the **Scheduling of modifications**
setting. 6. On the confirmation page, review your changes.
If they are correct, choose **Modify cluster**
to save your changes.

Alternatively, choose **Back** to edit your changes,
or choose **Cancel** to cancel your changes.
To associate a DB cluster parameter group with a DB cluster, use the AWS CLI [`modify-db-cluster`](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") command with the following options:

- `--db-cluster-name`
- `--db-cluster-parameter-group-name`
  The following example associates the `mydbclpg` DB parameter group with the
  `mydbcluster` DB cluster.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier `mydbcluster` \
    --db-cluster-parameter-group-name `mydbclpg`
```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier `mydbcluster` ^
    --db-cluster-parameter-group-name `mydbclpg`
```

To associate a DB cluster parameter group with a DB cluster, use the RDS API [`ModifyDBCluster`](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md") operation with the following parameters:

- `DBClusterIdentifier`
- `DBClusterParameterGroupName`
