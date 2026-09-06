

# How to perform an in-place upgrade
<a name="AuroraMySQL.Upgrading.Procedure"></a>

We recommend that you review the background material in [How the Aurora MySQL in-place major version upgrade works](AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Sequence).

Perform any preupgrade planning and testing, as described in [Planning a major version upgrade for an Aurora MySQL cluster](AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Planning).

## Console
<a name="AuroraMySQL.Upgrading.ModifyingDBCluster.CON"></a>

The following example upgrades the `mydbcluster-cluster` DB cluster to Aurora MySQL version 3.04.1.

**To upgrade the major version of an Aurora MySQL DB cluster**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. If you used a custom parameter group for the original DB cluster, create a corresponding parameter group compatible with the new major version. Make any necessary adjustments to the configuration parameters in that new parameter group. For more information, see [How in-place upgrades affect the parameter groups for a cluster](#AuroraMySQL.Upgrading.ParamGroups).

1.  In the navigation pane, choose **Databases**. 

1.  In the list, choose the DB cluster that you want to modify. 

1.  Choose **Modify**. 

1.  For **Version**, choose a new Aurora MySQL major version.

   We generally recommend using the latest minor version of the major version. Here, we choose the current default version.  
![In-place upgrade of an Aurora MySQL DB cluster from version 2 to version 3.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/ams-upgrade-v2-v3.png)

1.  Choose **Continue**. 

1.  On the next page, specify when to perform the upgrade. Choose **During the next scheduled maintenance window** or **Immediately**. 

1.  (Optional) Periodically examine the **Events** page in the RDS console during the upgrade. Doing so helps you to monitor the progress of the upgrade and identify any issues. If the upgrade encounters any issues, consult [Troubleshooting for Aurora MySQL in-place upgrade](AuroraMySQL.Upgrading.Troubleshooting.md) for the steps to take. 

1. If you created a new parameter group at the start of this procedure, associate the custom parameter group with your upgraded cluster. For more information, see [How in-place upgrades affect the parameter groups for a cluster](#AuroraMySQL.Upgrading.ParamGroups).
**Note**  
 Performing this step requires you to restart the cluster again to apply the new parameter group. 

1.  (Optional) After you complete any post-upgrade testing, delete the manual snapshot that Aurora created at the beginning of the upgrade. 

## AWS CLI
<a name="AuroraMySQL.Upgrading.ModifyingDBCluster.CLI"></a>

To upgrade the major version of an Aurora MySQL DB cluster, use the AWS CLI [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) command with the following required parameters:
+ `--db-cluster-identifier`
+ `--engine-version`
+ `--allow-major-version-upgrade`
+  `--apply-immediately` or `--no-apply-immediately`

If your cluster uses any custom parameter groups, also include one or both of the following options:
+ `--db-cluster-parameter-group-name`, if the cluster uses a custom cluster parameter group
+ `--db-instance-parameter-group-name`, if any instances in the cluster use a custom DB parameter group

The following example upgrades the `sample-cluster` DB cluster to Aurora MySQL version 3.04.1. The upgrade happens immediately, instead of waiting for the next maintenance window.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-db-cluster \
          --db-cluster-identifier sample-cluster \
          --engine-version 8.0.mysql_aurora.3.04.1 \
          --allow-major-version-upgrade \
          --apply-immediately
```
For Windows:  

```
aws rds modify-db-cluster ^
          --db-cluster-identifier sample-cluster ^
          --engine-version 8.0.mysql_aurora.3.04.1 ^
          --allow-major-version-upgrade ^
          --apply-immediately
```
You can combine other CLI commands with `modify-db-cluster` to create an automated end-to-end process for performing and verifying upgrades. For more information and examples, see [Aurora MySQL in-place upgrade tutorial](AuroraMySQL.Upgrading.Tutorial.md).

**Note**  
If your cluster is part of an Aurora global database, the in-place upgrade procedure is slightly different. You call the [modify-global-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-global-cluster.html) command operation instead of `modify-db-cluster`. For more information, see [In-place major upgrades for global databases](#AuroraMySQL.Upgrading.GlobalDB).

## RDS API
<a name="AuroraMySQL.Upgrading.ModifyingDBCluster.API"></a>

To upgrade the major version of an Aurora MySQL DB cluster, use the RDS API operation [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) with the following required parameters:
+ `DBClusterIdentifier`
+ `Engine`
+ `EngineVersion`
+ `AllowMajorVersionUpgrade`
+ `ApplyImmediately` (set to `true` or `false`)

**Note**  
If your cluster is part of an Aurora global database, the in-place upgrade procedure is slightly different. You call the [ModifyGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyGlobalClusterParameterGroup.html) operation instead of `ModifyDBCluster`. For more information, see [In-place major upgrades for global databases](#AuroraMySQL.Upgrading.GlobalDB).

## How in-place upgrades affect the parameter groups for a cluster
<a name="AuroraMySQL.Upgrading.ParamGroups"></a>

Aurora parameter groups have different sets of configuration settings for clusters that are compatible with different MySQL versions. When you perform an in-place upgrade, the upgraded cluster and all its instances must use the corresponding cluster and instance parameter groups that are compatible with the new major version.

If your cluster and instances use the default parameter groups for the source version, the upgraded cluster and instances automatically start with the default parameter groups for the target version. If your cluster and instances use any custom parameter groups, make sure to create corresponding parameter groups that are compatible with the target version. Also make sure to specify those during the upgrade process.

The following table shows the default parameter group mapping for each upgrade path:


| Upgrade path | Source default parameter group | Target default parameter group | 
| --- | --- | --- | 
| Aurora MySQL version 2 to version 3 | default.aurora-mysql5.7 | default.aurora-mysql8.0 | 
| Aurora MySQL version 3 to version 8.4 | default.aurora-mysql8.0 | default.aurora-mysql8.4 | 

**Note**  
For most parameter settings, you can choose the custom parameter group at two points. These are when you create the cluster or associate the parameter group with the cluster later.  
However, if you use a nondefault setting for the `lower_case_table_names` parameter, you must set up the custom parameter group with this setting in advance. Then specify the parameter group when you perform the snapshot restore to create the cluster. Any change to the `lower_case_table_names` parameter has no effect after the cluster is created.  
We recommend that you use the same setting for `lower_case_table_names` when you perform a major version upgrade.  
With an Aurora global database based on Aurora MySQL, you can perform an in-place major version upgrade only if you set the `lower_case_table_names` parameter to default and reboot your global database. For more information on the methods that you can use, see [Major version upgrades](aurora-global-database-upgrade.md#aurora-global-database-upgrade.major).

## Changes to cluster properties between Aurora MySQL versions
<a name="AuroraMySQL.Upgrading.Attrs"></a>

When you perform a major version upgrade, make sure to check any applications or scripts that you use to set up or manage Aurora MySQL clusters and DB instances.

Also, change your code that manipulates parameter groups to account for the fact that the default parameter group names are different for each major version.

**Aurora MySQL version 2 to version 3**

For example, you might have code like the following that applies to your cluster before an upgrade.

```
# Check the default parameter values for MySQL 5.7–compatible clusters.
aws rds describe-db-parameters {{--db-parameter-group-name default.aurora-mysql5.7}} --region us-east-1
```

After upgrading the major version of the cluster, modify that code as follows.

```
# Check the default parameter values for MySQL 8.0–compatible clusters.
aws rds describe-db-parameters {{--db-parameter-group-name default.aurora-mysql8.0}} --region us-east-1
```

**Aurora MySQL version 3 to version 8.4**

Similarly, if you have code referencing the version 3 default parameter group, update it after the upgrade.

```
# Before upgrade: Check the default parameter values for MySQL 8.0–compatible clusters.
aws rds describe-db-parameters {{--db-parameter-group-name default.aurora-mysql8.0}} --region us-east-1
```

```
# After upgrade: Check the default parameter values for MySQL 8.4–compatible clusters.
aws rds describe-db-parameters {{--db-parameter-group-name default.aurora-mysql8.4}} --region us-east-1
```

## In-place major upgrades for global databases
<a name="AuroraMySQL.Upgrading.GlobalDB"></a>

 For an Aurora global database, you upgrade the global database cluster. Aurora automatically upgrades all of the clusters at the same time and makes sure that they all run the same engine version. This requirement is because any changes to system tables, data file formats, and so on, are automatically replicated to all the secondary clusters. 

Follow the instructions in [How the Aurora MySQL in-place major version upgrade works](AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Sequence). When you specify what to upgrade, make sure to choose the global database cluster instead of one of the clusters it contains.

If you use the AWS Management Console, choose the item with the role **Global database**.

![Upgrading global database cluster.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-global-databases-major-upgrade-global-cluster.png)


 If you use the AWS CLI or RDS API, start the upgrade process by calling the [modify-global-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-global-cluster.html) command or [ModifyGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyGlobalCluster.html) operation. You use one of these instead of `modify-db-cluster` or `ModifyDBCluster`.

**Note**  
You can't specify a custom parameter group for the global database cluster while you're performing a major version upgrade of that Aurora global database. Create your custom parameter groups in each Region of the global cluster. Then apply them manually to the Regional clusters after the upgrade.

 To upgrade the major version of an Aurora MySQL global database cluster by using the AWS CLI, use the [modify-global-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-global-cluster.html) command with the following required parameters: 
+  `--global-cluster-identifier` 
+  `--engine aurora-mysql` 
+  `--engine-version` 
+  `--allow-major-version-upgrade` 

The following example upgrades the global database cluster to Aurora MySQL version 3.04.2.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-global-cluster \
          --global-cluster-identifier {{global_cluster_identifier}} \
          --engine aurora-mysql \
          --engine-version 8.0.mysql_aurora.3.04.2 \
          --allow-major-version-upgrade
```
For Windows:  

```
aws rds modify-global-cluster ^
          --global-cluster-identifier {{global_cluster_identifier}} ^
          --engine aurora-mysql ^
          --engine-version 8.0.mysql_aurora.3.04.2 ^
          --allow-major-version-upgrade
```

## In-place upgrades for DB clusters with cross-Region read replicas
<a name="AuroraMySQL.Upgrading.XRRR"></a>

You can upgrade an Aurora DB cluster that has a cross-Region read replica using the in-place upgrade procedure, but there are certain considerations:
+ You must upgrade the read replica DB cluster first. If you try to upgrade the primary cluster first, you will receive an error message such as the following:

  Unable to upgrade DB cluster test-xr-primary-cluster because the associated Aurora cross-Region replica test-xr-replica-cluster isn't patched yet. Upgrade the Aurora cross-Region replica and try again.

  This means that the primary DB cluster can't have a higher DB engine version than the replica cluster.
+ Before you upgrade the primary DB cluster, stop the write workload and disable any new connection requests to the writer DB instance of the primary cluster.
+ When you upgrade the primary cluster, choose a custom DB cluster parameter group with the `binlog_format` parameter set to a value that supports binary logging replication, such as `MIXED`.

  For more information about using binary logging with Aurora MySQL, see [Replication between Aurora and MySQL or between Aurora and another Aurora DB cluster (binary log replication)](AuroraMySQL.Replication.MySQL.md). For more information about modifying Aurora MySQL configuration parameters, see [Aurora MySQL configuration parameters](AuroraMySQL.Reference.ParameterGroups.md) and [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md).
+ Don't wait a long time to upgrade the primary DB cluster after you upgrade the replica cluster. We recommend not waiting longer than the next maintenance window.
+ After you upgrade the primary DB cluster, reboot its writer DB instance. The custom DB cluster parameter group that enables binlog replication doesn't take effect until the writer DB instance is rebooted.
+ Don't resume the write workload or enable connections to the writer DB instance until you confirm that cross-Region replication has restarted, and that the replica lag in the secondary AWS Region is 0.