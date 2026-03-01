# Restoring an Amazon Aurora cluster

## Use the AWS Backup console to restore Aurora recovery points

AWS Backup restores your Aurora cluster; it does not create or attach an Amazon RDS instance to
your cluster. In the following steps, you will create and attach an Amazon RDS instance to your
restored Aurora cluster using the CLI.

Restoring an Aurora cluster requires that you specify multiple restore options. For
information about these options, see [Overview of Backing Up and Restoring an Aurora DB Cluster](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.md") in the
_Amazon Aurora User Guide_. Specifications for the restore options can be
found in the API guide for [`RestoreDBClusterFromSnapshot`](../../../AmazonRDS/latest/APIReference/API_RestoreDBClusterFromSnapshot.md "../../../AmazonRDS/latest/APIReference/API_RestoreDBClusterFromSnapshot.md").

###### To restore an Amazon Aurora cluster

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources** and the
   Aurora resource ID that you want to restore.
3. On the **Resource details** page, a list of recovery points for
   the selected resource ID is shown. To restore a resource, in the
   **Backups** pane, choose the radio button next to the recovery
   point ID of the resource. In the upper-right corner of the pane, choose
   **Restore**.
4. In the **Instance specifications** pane, accept the defaults or
   specify the options for the **DB engine**, **DB engine
   version**, and **Capacity type** settings.

###### Note

If **Serverless** capacity type is selected, a
**Capacity settings** pane appears. Specify the options for the
**Minimum Aurora capacity unit** and **Maximum Aurora
capacity unit** settings, or choose different options from the
**Additional scaling configuration** section. 5. In the **Settings** pane, specify a name that is unique for all
DB cluster instances owned by your AWS account in the current Region. 6. In the **Network & Security** pane, accept the defaults or
specify the options for the **Virtual Private Cloud (VPC)**,
**Subnet group**, and **Availability zone**
settings. 7. In the **Database options** pane, accept the defaults or specify
the options for **Database port**, **DB cluster parameter
group**, and **IAM DB Authentication Enabled** settings. 8. In the **Backup** pane, accept the default or specify the option
for the **Copy tags to snapshots** setting. 9. In the **Backtrack** pane, accept the default or specify the
options for the **Enable Backtrack** or **Disable
Backtrack** settings. 10. In the **Encryption** pane, accept the default or specify the
options for the **Enable encryption** or **Disable
encryption** settings. 11. In the **Log exports** pane, choose the log types to publish to
Amazon CloudWatch Logs. The **IAM role** is already defined. 12. In the **Restore role** pane, choose the IAM role that AWS Backup
will assume for this restore. 13. After specifying all your settings, choose **Restore
backup**.

The **Restore jobs** pane appears. A message at the top of the
page provides information about the restore job. 14. After your restore finishes, attach your restored Aurora cluster to an Amazon RDS
instance.

Using the AWS CLI:

    * For Linux, macOS, or Unix:



    ```
    aws rds create-db-instance --db-instance-identifier `sample-instance` \
                  --db-cluster-identifier `sample-cluster` --engine aurora-mysql --db-instance-class db.`r4.large`
    ```
    * For Windows:



    ```
    aws rds create-db-instance --db-instance-identifier `sample-instance` ^
                  --db-cluster-identifier `sample-cluster` --engine aurora-mysql --db-instance-class db.`r4.large`
    ```

See [continuous backups and
point-in-time restore (PITR)](point-in-time-recovery.md "point-in-time-recovery.md") for information about continuous backups and
restoring to a chosen point in time.

## Use the AWS Backup API, CLI, or SDK to restore Amazon Aurora recovery points

Use `StartRestoreJob`. The metadata you can include for a restore job will
depend if you are restoring a continuous backup to a point in time (PITR) or if you are
restoring a snapshot.

###### Restore a cluster from a snapshot

You can specify the following metadata for an Aurora snapshot restore job. See [`RestoreDBClusterFromSnapshot`](../../../AmazonRDS/latest/APIReference/API_RestoreDBClusterFromSnapshot.md "../../../AmazonRDS/latest/APIReference/API_RestoreDBClusterFromSnapshot.md") in the _Amazon Relational Database Service API
Reference_ for additional information and accepted values.

```
// Required metadata:
dbClusterIdentifier // string
engine // string

// Optional metadata:
availabilityZones // array of strings
backtrackWindow // long
copyTagsToSnapshot // Boolean
databaseName // string
dbClusterParameterGroupName // string
dbSubnetGroupName // string
enableCloudwatchLogsExports // array of strings
enableIAMDatabaseAuthentication // Boolean
engineMode // string
engineVersion // string
kmsKeyId // string
optionGroupName // string
port // integer
scalingConfiguration // object
vpcSecurityGroupIds // array of strings
```

Example:

```
"restoreMetadata":"{\"EngineVersion\":\"5.6.10a\",\"KmsKeyId\":\"arn:aws:kms:us-east-`1:234567890123:key/45678901-ab23-4567-8cd9-012d345e6f7`\",\"EngineMode\":\"serverless\",\"AvailabilityZones\":\"[\\\"us-east-1b\\\",\\\"us-east-1e\\\",\\\"us-east-1c\\\"]\",\"Port\":\"3306\",\"DatabaseName\":\"\",\"DBSubnetGroupName\":\"default-vpc-05a3b07cf6e193e1g\",\"VpcSecurityGroupIds\":\"[\\\"sg-012d52c68c6e88f00\\\"]\",\"ScalingConfiguration\":\"{\\\"MinCapacity\\\":2,\\\"MaxCapacity\\\":64,\\\"AutoPause\\\":true,\\\"SecondsUntilAutoPause\\\":300,\\\"TimeoutAction\\\":\\\"RollbackCapacityChange\\\"}\",\"EnableIAMDatabaseAuthentication\":\"false\",\"DBClusterParameterGroupName\":\"default.aurora5.6\",\"CopyTagsToSnapshot\":\"true\",\"Engine\":\"aurora\",\"EnableCloudwatchLogsExports\":\"[]\"}"
```

###### Restore a cluster to a point in time (PITR)

You can specify the following metadata when you want to restore an Aurora continuous
backup (recovery point) to a specific point in time (PITR). See [`RestoreDBClusterToPointInTime`](../../../AmazonRDS/latest/APIReference/API_RestoreDBClusterToPointInTime.md "../../../AmazonRDS/latest/APIReference/API_RestoreDBClusterToPointInTime.md") in the _Amazon Relational Database Service API
Reference_ for additional information and accepted values.

```
// Required metadata:
dbClusterIdentifier // string
engine // string
restoreToTime // timestamp; must be specified if UseLatestRestorableTime parameter isn't provided

// Optional metadata:
backtrackWindow // long
copyTagsToSnapshot // Boolean
dbClusterParameterGroupName // string
dbSubnetGroupName // string
enableCloudwatchLogsExports // array of strings
enableIAMDatabaseAuthentication // Boolean
engineMode // string
engineVersion // string
kmsKeyId // string
optionGroupName // string
port // integer
scalingConfiguration // object
vpcSecurityGroupIds // array of strings
```
