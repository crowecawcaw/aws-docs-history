

# Modifying an Amazon Aurora DB cluster
<a name="Aurora.Modifying"></a>

You can change the settings of a DB cluster to accomplish tasks such as changing its backup retention period or its database port. You can also modify DB instances in a DB cluster to accomplish tasks such as changing its DB instance class or enabling Performance Insights for it. This topic guides you through modifying an Aurora DB cluster and its DB instances, and describes the settings for each.

We recommend that you test any changes on a test DB cluster or DB instance before modifying a production DB cluster or DB instance, so that you fully understand the impact of each change. This is especially important when upgrading database versions.

**Topics**
+ [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster)
+ [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance)
+ [Changing the password for the database master user](#Aurora.Modifying.Password)
+ [Settings for Amazon Aurora](#Aurora.Modifying.Settings)
+ [Settings that don't apply to Amazon Aurora DB clusters](#Aurora.Modifying.SettingsNotApplicableDBClusters)
+ [Settings that don't apply to Amazon Aurora DB instances](#Aurora.Modifying.SettingsNotApplicable)

## Modifying the DB cluster by using the console, CLI, and API
<a name="Aurora.Modifying.Cluster"></a><a name="modify_cluster"></a>

You can modify a DB cluster using the AWS Management Console, the AWS CLI, or the RDS API.

**Note**  
Most modifications can be applied immediately or during the next scheduled maintenance window. Some modifications, such as turning on deletion protection, are applied immediately—regardless of when you choose to apply them.  
Changing the master password in the AWS Management Console is always applied immediately.  
If you're using SSL endpoints and change the DB cluster identifier, stop and restart the DB cluster to update the SSL endpoints. For more information, see [Stopping and starting an Amazon Aurora DB cluster](aurora-cluster-stop-start.md).

### Console
<a name="Aurora.Modifying.Cluster.Console"></a>

**To modify a DB cluster**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then select the DB cluster that you want to modify.

1. Choose **Modify**. The **Modify DB cluster** page appears.

1. Change any of the settings that you want. For information about each setting, see [Settings for Amazon Aurora](#Aurora.Modifying.Settings). 
**Note**  
In the AWS Management Console, some instance level changes only apply to the current DB instance, while others apply to the entire DB cluster. For information about whether a setting applies to the DB instance or the DB cluster, see the scope for the setting in [Settings for Amazon Aurora](#Aurora.Modifying.Settings). To change a setting that modifies the entire DB cluster at the instance level in the AWS Management Console, follow the instructions in [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).

1. When all the changes are as you want them, choose **Continue** and check the summary of modifications.

1. To apply the changes immediately, select **Apply immediately**.

1. On the confirmation page, review your changes. If they are correct, choose **Modify cluster** to save your changes. 

   Alternatively, choose **Back** to edit your changes, or choose **Cancel** to cancel your changes. 

### AWS CLI
<a name="Aurora.Modifying.Cluster.CLI"></a>

To modify a DB cluster using the AWS CLI, call the [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) command. Specify the DB cluster identifier, and the values for the settings that you want to modify. For information about each setting, see [Settings for Amazon Aurora](#Aurora.Modifying.Settings). 

**Note**  
Some settings only apply to DB instances. To change those settings, follow the instructions in [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).

**Example**  
The following command modifies `mydbcluster` by setting the backup retention period to 1 week (7 days).   
For Linux, macOS, or Unix:  

```
aws rds modify-db-cluster \
    --db-cluster-identifier {{mydbcluster}} \
    --backup-retention-period {{7}}
```
For Windows:  

```
aws rds modify-db-cluster ^
    --db-cluster-identifier {{mydbcluster}} ^
    --backup-retention-period {{7}}
```

### RDS API
<a name="Aurora.Modifying.Cluster.API"></a>

To modify a DB cluster using the Amazon RDS API, call the [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) operation. Specify the DB cluster identifier, and the values for the settings that you want to modify. For information about each parameter, see [Settings for Amazon Aurora](#Aurora.Modifying.Settings). 

**Note**  
Some settings only apply to DB instances. To change those settings, follow the instructions in [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).

## Modifying a DB instance in a DB cluster
<a name="Aurora.Modifying.Instance"></a><a name="modify_instance"></a>

You can modify a DB instance in a DB cluster using the AWS Management Console, the AWS CLI, or the RDS API.

When you modify a DB instance, you can apply the changes immediately. To apply changes immediately, you select the **Apply Immediately** option in the AWS Management Console, you use the `--apply-immediately` parameter when calling the AWS CLI, or you set the `ApplyImmediately` parameter to `true` when using the Amazon RDS API. 

If you don't choose to apply changes immediately, the changes are deferred until the next maintenance window. During the next maintenance window, any of these deferred changes are applied. If you choose to apply changes immediately, your new changes and any previously deferred changes are applied.

To see the modifications that are pending for the next maintenance window, use the [describe-db-clusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-clusters.html) AWS CLI command and check the `PendingModifiedValues` field.

**Important**  
If any of the deferred modifications require downtime, choosing **Apply immediately** can cause unexpected downtime for the DB instance. There is no downtime for the other DB instances in the DB cluster.  
Modifications that you defer aren't listed in the output of the `describe-pending-maintenance-actions` CLI command. Maintenance actions only include system upgrades that you schedule for the next maintenance window.

### Console
<a name="Aurora.Modifying.Instance.Console"></a>

**To modify a DB instance in a DB cluster**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then select the DB instance that you want to modify.

1. For **Actions**, choose **Modify**. The **Modify DB instance** page appears.

1. Change any of the settings that you want. For information about each setting, see [Settings for Amazon Aurora](#Aurora.Modifying.Settings).
**Note**  
Some settings apply to the entire DB cluster and must be changed at the cluster level. To change those settings, follow the instructions in [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).  
 In the AWS Management Console, some instance level changes only apply to the current DB instance, while others apply to the entire DB cluster. For information about whether a setting applies to the DB instance or the DB cluster, see the scope for the setting in [Settings for Amazon Aurora](#Aurora.Modifying.Settings).

1. When all the changes are as you want them, choose **Continue** and check the summary of modifications.

1. To apply the changes immediately, select **Apply immediately**.

1. On the confirmation page, review your changes. If they are correct, choose **Modify DB instance** to save your changes.

   Alternatively, choose **Back** to edit your changes, or choose **Cancel** to cancel your changes.

### AWS CLI
<a name="Aurora.Modifying.Instance.CLI"></a>

To modify a DB instance in a DB cluster by using the AWS CLI, call the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command. Specify the DB instance identifier, and the values for the settings that you want to modify. For information about each parameter, see [Settings for Amazon Aurora](#Aurora.Modifying.Settings).

**Note**  
Some settings apply to the entire DB cluster. To change those settings, follow the instructions in [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).

**Example**  
The following code modifies `mydbinstance` by setting the DB instance class to `db.r4.xlarge`. The changes are applied during the next maintenance window by using `--no-apply-immediately`. Use `--apply-immediately` to apply the changes immediately.   
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{mydbinstance}} \
    --db-instance-class {{db.r4.xlarge}} \
    {{--no-apply-immediately}}
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{mydbinstance}} ^
    --db-instance-class {{db.r4.xlarge}} ^
    {{--no-apply-immediately}}
```

### RDS API
<a name="Aurora.Modifying.Instance.API"></a>

To modify a DB instance by using the Amazon RDS API, call the [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) operation. Specify the DB instance identifier, and the values for the settings that you want to modify. For information about each parameter, see [Settings for Amazon Aurora](#Aurora.Modifying.Settings). 

**Note**  
Some settings apply to the entire DB cluster. To change those settings, follow the instructions in [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).

## Changing the password for the database master user
<a name="Aurora.Modifying.Password"></a>

You can use the AWS Management Console or the AWS CLI to change the master user password.

### Console
<a name="Aurora.Modifying.Password.CON"></a>

You modify the writer DB instance to change the master user password using the AWS Management Console.

**To change the master user password**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then select the DB instance that you want to modify.

1. For **Actions**, choose **Modify**.

   The **Modify DB instance** page appears.

1. Enter a **New master password**.

1. For **Confirm master password**, enter the same new password.  
![The master user password field and confirmation.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aur_new_master_password.png)

1. Choose **Continue** and check the summary of modifications.
**Note**  
Password changes are always applied immediately.

1. On the confirmation page, choose **Modify DB instance**.

### CLI
<a name="Aurora.Modifying.Password.CLI"></a>

You call the [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) command to change the master user password using the AWS CLI. Specify the DB cluster identifier and the new password, as shown in the following examples.

You don't need to specify `--apply-immediately|--no-apply-immediately`, because password changes are always applied immediately.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier {{mydbcluster}} \
    --master-user-password {{mynewpassword}}
```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier {{mydbcluster}} ^
    --master-user-password {{mynewpassword}}
```

## Settings for Amazon Aurora
<a name="Aurora.Modifying.Settings"></a>

The following table contains details about which settings you can modify, the methods for modifying the setting, and the scope of the setting. The scope determines whether the setting applies to the entire DB cluster or if it can be set only for specific DB instances. 

**Note**  
Additional settings are available if you are modifying an Aurora serverless DB cluster. For information about these settings, see [Managing Aurora serverless DB clusters](aurora-serverless-v2-administration.md).  
Some settings aren't available for Aurora serverless because of their limitations. For more information, see [Requirements and limitations for Aurora serverless](aurora-serverless-v2.requirements.md).



| Setting and description | Method | Scope | Downtime notes | 
| --- | --- | --- | --- | 
| **Auto minor version upgrade**<br />Whether you want the DB instance to receive preferred minor engine version upgrades automatically when they become available. Upgrades are installed only during your scheduled maintenance window. <br />For more information about engine updates, see [Database engine updates for Amazon Aurora PostgreSQL](AuroraPostgreSQL.Updates.md) and [Database engine updates for Amazon Aurora MySQL](AuroraMySQL.Updates.md). For more information about the **Auto minor version upgrade** setting for Aurora MySQL, see [Enabling automatic upgrades between minor Aurora MySQL versions](AuroraMySQL.Updates.AMVU.md).  |  This setting is enabled by default. For each new cluster, choose the appropriate value for this setting based on its importance, expected lifetime, and the amount of verification testing that you do after each upgrade. When you change this setting, perform this modification for every DB instance in your Aurora cluster. If any DB instance in your cluster has this setting turned off, the cluster isn't automatically upgraded.<br />Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and set the `--auto-minor-version-upgrade\|--no-auto-minor-version-upgrade` option.<br />Using the RDS API, call [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and set the `AutoMinorVersionUpgrade` parameter. | The entire DB cluster | An outage doesn't occur during this change. Outages do occur during future maintenance windows when Aurora applies automatic upgrades. | 
| **Backup retention period**<br />The number of days that automatic backups are retained. The minimum value is `1`. <br />For more information, see [Backups](Aurora.Managing.Backups.md#Aurora.Managing.Backups.Backup).  | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--backup-retention-period` option.<br />Using the RDS API, call [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `BackupRetentionPeriod` parameter. | The entire DB cluster | An outage doesn't occur during this change. | 
| **Backup window (Start time)**<br />The time range during which automated backups of your database occurs. The backup window is a start time in Universal Coordinated Time (UTC), and a duration in hours. <br />Aurora backups are continuous and incremental, but the backup window is used to create a daily system backup that is preserved within the backup retention period. You can copy it to preserve it outside of the retention period.<br />The maintenance window and the backup window for the DB cluster can't overlap.<br />For more information, see [Backup window](Aurora.Managing.Backups.md#Aurora.Managing.Backups.BackupWindow). | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--preferred-backup-window` option.<br />Using the RDS API, call [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `PreferredBackupWindow` parameter. | The entire DB cluster. | An outage doesn't occur during this change. | 
| **Capacity settings**<br />The scaling properties of an Aurora serverless DB cluster. You can only modify scaling properties for DB clusters in `serverless` DB engine mode. | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--scaling-configuration` option.<br />Using the RDS API, call [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `ScalingConfiguration` parameter. | The entire DB cluster | An outage doesn't occur during this change.<br />The change occurs immediately. This setting ignores the apply immediately setting. | 
| **Certificate authority**<br />The certificate authority (CA) for the server certificate used by the DB instance. | Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and set the `--ca-certificate-identifier` option.<br />Using the RDS API, call [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and set the `CACertificateIdentifier` parameter. | Only the specified DB instance | An outage only occurs if the DB engine doesn't support rotation without restart. You can use the [ describe-db-engine-versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html) AWS CLI command to determine whether the DB engine supports rotation without restart. | 
| **Cluster storage configuration**<br />The storage type for the DB cluster: **Aurora I/O-Optimized** or **Aurora Standard**.<br />For more information, see [Storage configurations for Amazon Aurora DB clusters](Aurora.Overview.StorageReliability.md#aurora-storage-type). | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--storage-type` option.<br />Using the RDS API, call [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `StorageType` parameter. | The entire DB cluster | Changing the storage type of an Aurora PostgreSQL DB cluster with Optimized Reads instance classes causes an outage. This does not occur when changing storage types for clusters with other instance class types. For more information on the DB instance class types, see [DB instance class types](Concepts.DBInstanceClass.Types.md). | 
| Copy tags to snapshotsSelect to specify that tags defined for this DB cluster are copied to DB snapshots created from this DB cluster. For more information, see [Tagging Amazon Aurora andAmazon RDS resources](USER_Tagging.md). | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--copy-tags-to-snapshot` or `--no-copy-tags-to-snapshot` option.<br />Using the RDS API, call [https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `CopyTagsToSnapshot` parameter. | The entire DB cluster | An outage doesn't occur during this change. | 
| Database authenticationThe database authentication you want to use.<br />For MySQL:+  Choose **Password authentication** to authenticate database users with database passwords only. <br />+  Choose **Password and IAM database authentication** to authenticate database users with database passwords and user credentials through IAM users and roles. For more information, see [IAM database authentication ](UsingWithRDS.IAMDBAuth.md). <br />For PostgreSQL:+  Choose **IAM database authentication** to authenticate database users with database passwords and user credentials through users and roles. For more information, see [IAM database authentication ](UsingWithRDS.IAMDBAuth.md). <br />+  Choose **Kerberos authentication** to authenticate database passwords and user credentials using Kerberos authentication. For more information, see [Using Kerberos authentication with Aurora PostgreSQL](postgresql-kerberos.md).  | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [ modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the following options:+  For IAM authentication, set the `--enable-iam-database-authentication\|--no-enable-iam-database-authentication` option. <br />+  For Kerberos authentication, set the `--domain` and `--domain-iam-role-name` options. <br />Using the RDS API, call [ ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the following parameters:+  For IAM authentication, set the `EnableIAMDatabaseAuthentication` parameter. <br />+  For Kerberos authentication, set the `Domain` and `DomainIAMRoleName` parameters.  | The entire DB cluster | An outage doesn't occur during this change. | 
| **Database port**<br />The port that you want to use to access the DB cluster.  | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--port` option.<br />Using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `Port` parameter. | The entire DB cluster | An outage occurs during this change. All of the DB instances in the DB cluster are rebooted immediately. | 
| **DB cluster identifier**<br />The DB cluster identifier. This value is stored as a lowercase string.<br />When you change the DB cluster identifier, the DB cluster endpoints change. The endpoints of the DB instances in the DB cluster don't change. | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--new-db-cluster-identifier` option.<br />Using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `NewDBClusterIdentifier` parameter. | The entire DB cluster | An outage doesn't occur during this change. | 
| **DB cluster parameter group**<br />The DB cluster parameter group that you want associated with the DB cluster. <br />For more information, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md).  | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--db-cluster-parameter-group-name` option.<br />Using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `DBClusterParameterGroupName` parameter. | The entire DB cluster | An outage doesn't occur during this change. When you change the parameter group, changes to some parameters are applied to the DB instances in the DB cluster immediately without a reboot. Changes to other parameters are applied only after the DB instances in the DB cluster are rebooted. | 
| **DB instance class**<br />The DB instance class that you want to use. <br />For more information, see [Amazon AuroraDB instance classes](Concepts.DBInstanceClass.md).  | Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and set the `--db-instance-class` option.<br />Using the RDS API, call [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and set the `DBInstanceClass` parameter. | Only the specified DB instance | An outage occurs during this change. | 
| **DB instance identifier**<br />The DB instance identifier. This value is stored as a lowercase string.  | Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and set the `--new-db-instance-identifier` option.<br />Using the RDS API, call [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and set the `NewDBInstanceIdentifier` parameter. | Only the specified DB instance | Downtime occurs during this change.<br />RDS restarts the DB instance to update the following:+  Aurora MySQL – `SERVER_ID` column in the `information_schema.replica_host_status` table <br />+  Aurora PostgreSQL – `server_id` column in the `aurora_replica_status()` function  | 
| **DB parameter group**<br />The DB parameter group that you want associated with the DB instance. <br />For more information, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md).  | Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and set the `--db-parameter-group-name` option.<br />Using the RDS API, call [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and set the `DBParameterGroupName` parameter. | Only the specified DB instance | An outage doesn't occur during this change.<br />When you associate a new DB parameter group with a DB instance, the modified static and dynamic parameters are applied only after the DB instance is rebooted. However, if you modify dynamic parameters in the DB parameter group after you associate it with the DB instance, these changes are applied immediately without a reboot.<br />For more information, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md) and [Rebooting an Amazon Aurora DB cluster or Amazon Aurora DB instance](USER_RebootCluster.md).  | 
| **Deletion protection**<br />**Enable deletion protection** to prevent your DB cluster from being deleted. For more information, see [Deletion protection for Aurora clusters](USER_DeleteCluster.md#USER_DeletionProtection).  | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--deletion-protection\|--no-deletion-protection` option.<br />Using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `DeletionProtection` parameter. | The entire DB cluster | An outage doesn't occur during this change. | 
| **Engine version**<br />The version of the DB engine that you want to use. Before you upgrade your production DB cluster, we recommend that you test the upgrade process on a test DB cluster to verify its duration and to validate your applications.  | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--engine-version` option.<br />Using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `EngineVersion` parameter. | The entire DB cluster | An outage occurs during this change. | 
| **Enhanced monitoring**<br />**Enable enhanced monitoring** to enable gathering metrics in real time for the operating system that your DB instance runs on. <br />For more information, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.OS.md).  | Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and set the `--monitoring-role-arn` and `--monitoring-interval` options.<br />Using the RDS API, call [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and set the `MonitoringRoleArn` and `MonitoringInterval` parameters. | Only the specified DB instance | An outage doesn't occur during this change. | 
| **Log exports**<br />Select the log types to publish to Amazon CloudWatch Logs. <br />For more information, see [AuroraMySQL database log files](USER_LogAccess.Concepts.MySQL.md).  | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--cloudwatch-logs-export-configuration` option.<br />Using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `CloudwatchLogsExportConfiguration` parameter. | The entire DB cluster | An outage doesn't occur during this change. | 
| **Maintenance window**<br />The time range during which system maintenance occurs. System maintenance includes upgrades, if applicable. The maintenance window is a start time in Universal Coordinated Time (UTC), and a duration in hours. <br />If you set the window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure any pending changes are applied. <br />You can set the maintenance window independently for the DB cluster and for each DB instance in the DB cluster. When the scope of a modification is the entire DB cluster, the modification is performed during the DB cluster maintenance window. When the scope of a modification is the a DB instance, the modification is performed during maintenance window of that DB instance.<br />The maintenance window and the backup window for the DB cluster can't overlap.<br />For more information, see [Amazon RDS maintenance window](USER_UpgradeDBInstance.Maintenance.md#Concepts.DBMaintenance).  | To change the maintenance window for the DB cluster using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />To change the maintenance window for a DB instance using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />To change the maintenance window for the DB cluster using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--preferred-maintenance-window` option.<br />To change the maintenance window for a DB instance using the AWS CLI, run [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and set the `--preferred-maintenance-window` option.<br />To change the maintenance window for the DB cluster using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `PreferredMaintenanceWindow` parameter.<br />To change the maintenance window for a DB instance using the RDS API, call [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and set the `PreferredMaintenanceWindow` parameter. | The entire DB cluster or a single DB instance | If there are one or more pending actions that cause an outage, and the maintenance window is changed to include the current time, then those pending actions are applied immediately, and an outage occurs. | 
|  **Manage master credentials in AWS Secrets Manager**<br />Select **Manage master credentials in AWS Secrets Manager** to manage the master user password in a secret in Secrets Manager.<br />Optionally, choose a KMS key to use to protect the secret. Choose from the KMS keys in your account, or enter the key from a different account.<br />For more information, see [Password management with Amazon Aurora and AWS Secrets Manager](rds-secrets-manager.md).<br />If Aurora is already managing the master user password for the DB cluster, you can rotate the master user password by choosing **Rotate secret immediately**.<br />For more information, see [Password management with Amazon Aurora and AWS Secrets Manager](rds-secrets-manager.md). | Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--manage-master-user-password \| --no-manage-master-user-password` and `--master-user-secret-kms-key-id` options. To rotate the master user password immediately, set the `--rotate-master-user-password` option.<br />Using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `ManageMasterUserPassword` and `MasterUserSecretKmsKeyId` parameters. To rotate the master user password immediately, set the `RotateMasterUserPassword` parameter to `true`. | The entire DB cluster | An outage doesn't occur during this change. | 
| **Network type**<br />The IP addressing protocols supported by the DB cluster.<br />**IPv4** to specify that resources can communicate with the DB cluster only over the IPv4 addressing protocol.<br />**Dual-stack mode** to specify that resources can communicate with the DB cluster over IPv4, IPv6, or both. Use dual-stack mode if you have any resources that must communicate with your DB cluster over the IPv6 addressing protocol. To use dual-stack mode, make sure at least two subnets spanning two Availability Zones that support both the IPv4 and IPv6 network protocol. Also, make sure you associate an IPv6 CIDR block with subnets in the DB subnet group you specify.<br />For more information, see [Amazon Aurora IP addressing](USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.IP_addressing). | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--network-type` option.<br />Using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `NetworkType` parameter. | The entire DB cluster | An outage doesn't occur during this change. | 
| **New master password**<br />The password for your master user. + For Aurora MySQL, the password must contain 8–41 printable ASCII characters.<br />+ For Aurora PostgreSQL, it must contain 8–99 printable ASCII characters.<br />+ It can't contain `/`, `"`, `@`, or a space. | Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--master-user-password` option.<br />Using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `MasterUserPassword` parameter. | The entire DB cluster | An outage doesn't occur during this change. | 
| **Performance Insights**<br />Whether to enable Performance Insights, a tool that monitors your DB instance load so that you can analyze and troubleshoot your database performance. <br />For more information, see [Monitoring DB load with Amazon CloudWatch Database Insights on Amazon Aurora](USER_PerfInsights.md).  | Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and set the `--enable-performance-insights\|--no-enable-performance-insights` option.<br />Using the RDS API, call [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and set the `EnablePerformanceInsights` parameter. | Only the specified DB instance | An outage doesn't occur during this change. | 
| **Performance Insights AWS KMS key**<br />The AWS KMS key identifier for encryption of Performance Insights data. The KMS key identifier is the Amazon Resource Name (ARN), key identifier, or key alias for the KMS key. <br />For more information, see [Enabling and disabling detailed per-query and database counter metrics](USER_PerfInsights.Enabling.md).  | Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and set the `--performance-insights-kms-key-id` option.<br />Using the RDS API, call [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and set the `PerformanceInsightsKMSKeyId` parameter. | Only the specified DB instance | An outage doesn't occur during this change. | 
| **Performance Insights retention period**<br />The amount of time, in days, to retain Performance Insights data. The retention setting is **Default (7 days)**. To retain your performance data for longer, specify 1–24 months. For more information about retention periods, see [Pricing and data retention for Database Insights](USER_PerfInsights.Overview.cost.md). <br />For more information, see [Enabling and disabling detailed per-query and database counter metrics](USER_PerfInsights.Enabling.md).  | Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and set the `--performance-insights-retention-period` option.<br />Using the RDS API, call [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and set the `PerformanceInsightsRetentionPeriod` parameter. | Only the specified DB instance | An outage doesn't occur during this change. | 
| **Promotion tier**<br />A value that specifies the order in which an Aurora Replica is promoted to the primary instance in a DB cluster, after a failure of the existing primary instance. <br />For more information, see [Fault tolerance for an Aurora DB cluster](Concepts.AuroraHighAvailability.md#Aurora.Managing.FaultTolerance).  | Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and set the `--promotion-tier` option.<br />Using the RDS API, call [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and set the `PromotionTier` parameter. | Only the specified DB instance | An outage doesn't occur during this change. | 
| **Public access**<br />**Publicly accessible** to give the DB instance a public IP address, meaning that it's accessible outside the VPC. To be publicly accessible, the DB instance also has to be in a public subnet in the VPC.<br />**Not publicly accessible** to make the DB instance accessible only from inside the VPC.<br />For more information, see [Hiding a DB cluster in a VPC from the internet](USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.Hiding). <br />To connect to a DB instance from outside of its Amazon VPC, the DB instance must be publicly accessible, access must be granted using the inbound rules of the DB instance's security group, and other requirements must be met. For more information, see [Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting).<br />If your DB instance is isn't publicly accessible, you can also use an AWS Site-to-Site VPN connection or an Direct Connect connection to access it from a private network. For more information, see [Internetwork traffic privacy](inter-network-traffic-privacy.md). | Using the AWS Management Console, [Modifying a DB instance in a DB cluster](#Aurora.Modifying.Instance).<br />Using the AWS CLI, run [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and set the `--publicly-accessible\|--no-publicly-accessible` option.<br />Using the RDS API, call [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and set the `PubliclyAccessible` parameter. | Only the specified DB instance | An outage doesn't occur during this change. | 
| **Serverless v2 capacity settings**<br />The database capacity of an Aurora serverless DB cluster, measured in Aurora Capacity Units (ACUs).<br />For more information, see [Setting the Aurora serverless capacity range for a cluster](aurora-serverless-v2-administration.md#aurora-serverless-v2-setting-acus). | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--serverless-v2-scaling-configuration` option.<br />Using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `ServerlessV2ScalingConfiguration` parameter. | The entire DB cluster | An outage doesn't occur during this change.<br />The change occurs immediately. This setting ignores the apply immediately setting. | 
| **Security group**<br />The security group you want associated with the DB cluster. <br />For more information, see [Controlling access with security groups](Overview.RDSSecurityGroups.md).  | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--vpc-security-group-ids` option.<br />Using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `VpcSecurityGroupIds` parameter. | The entire DB cluster | An outage doesn't occur during this change. | 
| **Target Backtrack window**<br />The amount of time you want to be able to backtrack your DB cluster, in seconds. This setting is available only for Aurora MySQL and only if the DB cluster was created with Backtrack enabled.  | Using the AWS Management Console, [Modifying the DB cluster by using the console, CLI, and API](#Aurora.Modifying.Cluster).<br />Using the AWS CLI, run [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and set the `--backtrack-window` option.<br />Using the RDS API, call [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) and set the `BacktrackWindow` parameter. | The entire DB cluster | An outage doesn't occur during this change. | 

## Settings that don't apply to Amazon Aurora DB clusters
<a name="Aurora.Modifying.SettingsNotApplicableDBClusters"></a>

The following settings in the AWS CLI command [`modify-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) and the RDS API operation [`ModifyDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) don't apply to Amazon Aurora DB clusters.

**Note**  
You can't use the AWS Management Console to modify these settings for Aurora DB clusters.



| AWS CLI setting | RDS API setting | 
| --- | --- | 
| `--allocated-storage` | `AllocatedStorage` | 
| `--auto-minor-version-upgrade \| --no-auto-minor-version-upgrade` | `AutoMinorVersionUpgrade` | 
| `--db-cluster-instance-class` | `DBClusterInstanceClass` | 
| `--enable-performance-insights \| --no-enable-performance-insights` | `EnablePerformanceInsights` | 
| `--iops` | `Iops` | 
| `--monitoring-interval` | `MonitoringInterval` | 
| `--monitoring-role-arn` | `MonitoringRoleArn` | 
| `--option-group-name` | `OptionGroupName` | 
| `--performance-insights-kms-key-id` | `PerformanceInsightsKMSKeyId` | 
| `--performance-insights-retention-period` | `PerformanceInsightsRetentionPeriod` | 

## Settings that don't apply to Amazon Aurora DB instances
<a name="Aurora.Modifying.SettingsNotApplicable"></a>

The following settings in the AWS CLI command [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) and the RDS API operation [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) don't apply to Amazon Aurora DB instances.

**Note**  
You can't use the AWS Management Console to modify these settings for Aurora DB instances.



| AWS CLI setting | RDS API setting | 
| --- | --- | 
| `--allocated-storage` | `AllocatedStorage` | 
| `--allow-major-version-upgrade\|--no-allow-major-version-upgrade` | `AllowMajorVersionUpgrade` | 
| `--copy-tags-to-snapshot\|--no-copy-tags-to-snapshot` | `CopyTagsToSnapshot` | 
| `--domain` | `Domain` | 
| `--db-security-groups` | `DBSecurityGroups` | 
| `--db-subnet-group-name` | `DBSubnetGroupName` | 
| `--domain-iam-role-name` | `DomainIAMRoleName` | 
| `--multi-az\|--no-multi-az` | `MultiAZ` | 
| `--iops` | `Iops` | 
| `--license-model` | `LicenseModel` | 
| `--network-type` | `NetworkType` | 
| `--option-group-name` | `OptionGroupName` | 
| `--processor-features` | `ProcessorFeatures` | 
| `--storage-type` | `StorageType` | 
| `--tde-credential-arn` | `TdeCredentialArn` | 
| `--tde-credential-password` | `TdeCredentialPassword` | 
| `--use-default-processor-features\|--no-use-default-processor-features` | `UseDefaultProcessorFeatures` | 