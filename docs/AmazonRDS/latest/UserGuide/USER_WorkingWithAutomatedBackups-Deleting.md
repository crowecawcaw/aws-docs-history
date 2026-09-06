

# Deleting retained automated backups
<a name="USER_WorkingWithAutomatedBackups-Deleting"></a>

You can delete retained automated backups when they are no longer needed.

## Console
<a name="USER_WorkingWithAutomatedBackups-Deleting.CON"></a>

**To delete a retained automated backup**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Automated backups**.

1. On the **Retained** tab, choose the retained automated backup that you want to delete.

1. For **Actions**, choose **Delete**.

1. On the confirmation page, enter **delete me** and choose **Delete**.

## AWS CLI
<a name="USER_WorkingWithAutomatedBackups-Deleting.CLI"></a>

You can delete a retained automated backup by using the AWS CLI command [delete-db-instance-automated-backup](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-db-instance-automated-backup.html) with the following option:
+ `--dbi-resource-id` – The resource identifier for the source DB instance.

  You can find the resource identifier for the source DB instance of a retained automated backup by running the AWS CLI command [describe-db-instance-automated-backups](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instance-automated-backups.html).

**Example**  
The following example deletes the retained automated backup with source DB instance resource identifier `db-123ABCEXAMPLE`.   
For Linux, macOS, or Unix:  

```
1. aws rds delete-db-instance-automated-backup \
2.     --dbi-resource-id {{db-123ABCEXAMPLE}}
```
For Windows:  

```
1. aws rds delete-db-instance-automated-backup ^
2.     --dbi-resource-id {{db-123ABCEXAMPLE}}
```

## RDS API
<a name="USER_WorkingWithAutomatedBackups-Deleting.API"></a>

You can delete a retained automated backup by using the Amazon RDS API operation [DeleteDBInstanceAutomatedBackup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBInstanceAutomatedBackup.html) with the following parameter:
+ `DbiResourceId` – The resource identifier for the source DB instance.

  You can find the resource identifier for the source DB instance of a retained automated backup using the Amazon RDS API operation [DescribeDBInstanceAutomatedBackups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstanceAutomatedBackups.html).

## Disabling automated backups
<a name="USER_WorkingWithAutomatedBackups.Disabling"></a>

You might want to temporarily disable automated backups in certain situations, for example while loading large amounts of data.

**Important**  
We highly discourage disabling automated backups because it disables point-in-time recovery. Disabling automatic backups for a DB instance or Multi-AZ DB cluster deletes all existing automated backups for the database. If you disable and then re-enable automated backups, you can restore starting only from the time you re-enabled automated backups. 

### Console
<a name="USER_WorkingWithAutomatedBackups.Disabling.CON"></a>

**To disable automated backups immediately**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the DB instance or Multi-AZ DB cluster that you want to modify.

1. Choose **Modify**.

1. For **Backup retention period**, choose **0 days**. 

1. Choose **Continue**.

1. Choose **Apply immediately**.

1. Choose **Modify DB instance** or **Modify cluster** to save your changes and disable automated backups.

### AWS CLI
<a name="USER_WorkingWithAutomatedBackups.Disabling.CLI"></a>

To disable automated backups immediately, use the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) or [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) command and set the backup retention period to 0 with `--apply-immediately`.

**Example**  
The following example immediately disables automatic backups on a Multi-AZ DB cluster.  
For Linux, macOS, or Unix:  

```
aws rds modify-db-cluster \
    --db-cluster-identifier {{mydbcluster}} \
    --backup-retention-period 0 \
    {{--apply-immediately}}
```
For Windows:  

```
aws rds modify-db-cluster ^
    --db-cluster-identifier {{mydbcluster}} ^
    --backup-retention-period 0 ^
    {{--apply-immediately}}
```

To know when the modification is in effect, call `describe-db-instances` for the DB instance (or `describe-db-clusters` for a Multi-AZ DB cluster) until the value for backup retention period is 0 and `mydbcluster` status is available.

```
aws rds describe-db-clusters --db-cluster-identifier {{mydcluster}}
```

### RDS API
<a name="USER_WorkingWithAutomatedBackups.Disabling.API"></a>

To disable automated backups immediately, call the [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) or [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) operation with the following parameters: 
+ `DBInstanceIdentifier = mydbinstance` (or `DBClusterIdentifier = mydbcluster`)
+ `BackupRetentionPeriod = 0`

**Example**  

```
https://rds.amazonaws.com/
    ?Action=ModifyDBInstance
    &DBInstanceIdentifier=mydbinstance
    &BackupRetentionPeriod=0
    &SignatureVersion=2
    &SignatureMethod=HmacSHA256
    &Timestamp=2009-10-14T17%3A48%3A21.746Z
    &AWSAccessKeyId=<&AWS; Access Key ID>
    &Signature=<Signature>
```