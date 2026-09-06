

# Restore a Neptune cluster
<a name="restoring-nep"></a>

## Use the AWS Backup console to restore Amazon Neptune recovery points
<a name="nep-restore-console"></a>

Restoring an Amazon Neptune database requires that you specify multiple restore options. For information about these options, see [ Restoring from a DB Cluster Snapshot](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-restore-snapshot.html) in the *Neptune User Guide*.

**To restore an Neptune database**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the navigation pane, choose **Protected resources** and the Neptune resource ID that you want to restore.

1. On the **Resource details** page, a list of recovery points for the selected resource ID is shown. To restore a resource, in the **Backups** pane, choose the radio button next to the recovery point ID of the resource. In the upper-right corner of the pane, choose **Restore**.

1. In the **Instance specifications** pane, accept the defaults or specify the **DB engine** and **Version**.

1. In the **Settings** pane, specify a name that is unique for all DB cluster instances owned by your AWS account in the current Region. The DB cluster identifier is case insensitive, but it is stored as all lowercase, as in "`mydbclusterinstance`". This is a required field. 

1. In the **Database options** pane, accept the defaults or specify the options for **Database port** and **DB cluster parameter group**. 

1. In the **Encryption** pane, accept the default or specify the options for the **Enable encryption** or **Disable encryption** settings.

1. In the **Log exports** pane, choose the log types to publish to Amazon CloudWatch Logs. The **IAM role** is already defined. 

1. In the **Restore role** pane, choose the IAM role that AWS Backup will assume for this restore.
**Note**  
If role manager is enabled in your account, AWS Backup selects the default service role for you, and a **Customize** option is available. For more information, see [IAM role creation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*.

1. After specifying all your settings, choose **Restore backup**.

   The **Restore jobs** pane appears. A message at the top of the page provides information about the restore job.

1. After your restore finishes, attach your restored Neptune cluster to an Amazon RDS instance.

## Use the AWS Backup API, CLI, or SDK to restore Neptune recovery points
<a name="nep-restore-cli"></a>

First, restore your cluster. Use `[StartRestoreJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartRestoreJob.html)`. You can specify the following metadata during Amazon DocumentDB restores:

```
availabilityZones
backtrackWindow
copyTagsToSnapshot // Boolean 
databaseName // string 
dbClusterIdentifier // string 
dbClusterParameterGroupName // string 
dbSubnetGroupName // string 
enableCloudwatchLogsExports // string 
enableIAMDatabaseAuthentication // Boolean 
engine // string 
engineMode // string 
engineVersion // string 
kmsKeyId // string 
port // integer 
optionGroupName // string 
scalingConfiguration
vpcSecurityGroupIds // string
```

Then, attach your restored Neptune cluster to an Amazon RDS instance using `create-db-instance`.
+ For Linux, macOS, or Unix:

  ```
  aws neptune create-db-instance --db-instance-identifier {{sample-instance}} \ 
                    --db-instance-class {{db.r5.large}} --engine neptune --engine-version {{1.0.5.0}} --db-cluster-identifier {{sample-cluster}} --region {{us-east-1}}
  ```
+ For Windows:

  ```
  aws neptune create-db-instance --db-instance-identifier {{sample-instance}} ^
                    --db-instance-class {{db.r5.large}} --engine neptune --engine-version {{1.0.5.0}} --db-cluster-identifier {{sample-cluster}} --region {{us-east-1}}
  ```

For more information, see [`RestoreDBClusterFromSnapshot`](https://docs.aws.amazon.com/neptune/latest/userguide/api-snapshots.html#RestoreDBClusterFromSnapshot) in the *Neptune Management API reference* and [`restore-db-cluster-from-snapshot`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/restore-db-cluster-from-snapshot.html) in the *Neptune CLI guide*.