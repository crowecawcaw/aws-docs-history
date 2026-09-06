

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Customer-managed backup and restore
<a name="influxdb2-customer-managed-backup-restore"></a>

Customer-managed backup and restore lets you create, manage, and restore database backups for your Amazon Timestream for InfluxDB DB instances and clusters. You can create on-demand or automated scheduled backups, and restore databases without opening AWS support tickets.

## Overview
<a name="influxdb2-backup-overview"></a>

Customer-managed backup and restore provides self-service backup capabilities for Amazon Timestream for InfluxDB:
+ **InfluxDB v2** (standalone instances)
+ **InfluxDB v2 Read Replicas** (multi-node clusters)

For InfluxDB v3 backup and restore, see [Customer-managed backup and restore](influxdb3-customer-managed-backup-restore.md).

The first backup creates a complete copy of your database. Subsequent backups are incremental and capture only the data that changed since the last backup, reducing storage costs and backup time.

## Key concepts
<a name="influxdb2-backup-concepts"></a>


| Concept | Description | 
| --- | --- | 
| DbBackup | A backup of your database containing the instance or cluster configuration at the time of backup. | 
| DbBackupConfiguration | Automated recurring backups at a defined frequency and retention. | 
| Restore | Creates a new DB from a DbBackup or restores an existing resource back to the provided DbBackup. | 
| RetentionDays | Defines the number of days a backup is kept before automatic deletion. | 
| On Demand Backup | Triggers a one-time backup of the database at a point in time. | 
| Custom Schedule Backup | Defines a custom AWS cron schedule when the DB will be backed up automatically. | 

## Creating a DbBackup
<a name="influxdb2-backup-creating"></a>

### On-demand backup (AWS CLI)
<a name="influxdb2-backup-creating-cli"></a>

Create an on-demand backup of a DB instance or cluster:

```
aws timestream-influxdb create-db-backup \
    --db-resource-id {{my-resource-id}} \
    --name {{my-db-backup-2026-07-07}} \
    --retention-days 7
```

For Read Replicas clusters, use the DB cluster ID as the resource identifier.

### On-demand backup (AWS Management Console)
<a name="influxdb2-backup-creating-console"></a>

1. Open the Amazon Timestream for InfluxDB console.

1. Choose your database instance or cluster.

1. Choose **Actions**, **Create backup**.

1. Enter a backup name and retention period.

1. Choose **Create backup**.

## Configuring automated backups
<a name="influxdb2-backup-scheduling"></a>

Automated backups can be enabled at resource creation time or updated afterwards. Only one DbBackupConfiguration is allowed per type per resource, and a maximum of 4 DbBackupConfigurations can be enabled per resource.

### Enable automated backups on create (AWS CLI)
<a name="influxdb2-backup-scheduling-create"></a>

For a DB instance:

```
aws timestream-influxdb create-db-instance \
    --name {{my-db-instance}} \
    --db-instance-type db.influx.medium \
    --db-storage-type InfluxIOIncludedT1 \
    --allocated-storage 100 \
    --vpc-subnet-ids {{subnet-0123456789abcdef0}} \
    --vpc-security-group-ids {{sg-0123456789abcdef0}} \
    --password {{MySecurePassword123!}} \
    --db-backup-configurations '[{
       "enabled": true,
       "type": "HOURLY",
       "retentionDays": 1
      },
      {
       "enabled": true,
       "type": "DAILY",
       "retentionDays": 7
      },
      {
       "enabled": true,
       "type": "WEEKLY",
       "retentionDays": 30
      },
      {
       "enabled": true,
       "type": "MONTHLY",
       "retentionDays": 365
      }]'
```

For a Read Replicas cluster:

```
aws timestream-influxdb create-db-cluster \
    --name {{my-db-cluster}} \
    --db-instance-type db.influx.medium \
    --db-storage-type InfluxIOIncludedT1 \
    --allocated-storage 100 \
    --vpc-subnet-ids {{subnet-0123456789abcdef0}} \
    --vpc-security-group-ids {{sg-0123456789abcdef0}} \
    --password {{MySecurePassword123!}} \
    --deployment-type MULTI_NODE_READ_REPLICAS \
    --db-backup-configurations '[{
       "enabled": true,
       "type": "HOURLY",
       "retentionDays": 1
      },
      {
       "enabled": true,
       "type": "DAILY",
       "retentionDays": 7
      },
      {
       "enabled": true,
       "type": "WEEKLY",
       "retentionDays": 30
      },
      {
       "enabled": true,
       "type": "MONTHLY",
       "retentionDays": 365
      }]'
```

### Enable automated backups on update (AWS CLI)
<a name="influxdb2-backup-scheduling-update"></a>

DbBackupConfigurations can be enabled, disabled, and retention can be changed after creation:

```
aws timestream-influxdb update-db-instance \
    --identifier {{my-db-instance-id}} \
    --db-backup-configurations '[{
       "enabled": true,
       "type": "HOURLY",
       "retentionDays": 1
      },
      {
       "enabled": true,
       "type": "DAILY",
       "retentionDays": 7
      },
      {
       "enabled": false,
       "type": "WEEKLY",
       "retentionDays": 30
      }]'
```

For a Read Replicas cluster:

```
aws timestream-influxdb update-db-cluster \
    --db-cluster-id {{my-db-cluster-id}} \
    --db-backup-configurations '[{
       "enabled": true,
       "type": "HOURLY",
       "retentionDays": 1
      },
      {
       "enabled": true,
       "type": "DAILY",
       "retentionDays": 7
      },
      {
       "enabled": false,
       "type": "WEEKLY",
       "retentionDays": 30
      }]'
```

### DbBackupConfiguration types
<a name="influxdb2-backup-scheduling-types"></a>


| Type | Description | 
| --- | --- | 
| HOURLY | Creates a DbBackup every hour | 
| DAILY | Creates a DbBackup every day at midnight in the timezone of the Region | 
| WEEKLY | Creates a DbBackup every week on Sunday at midnight in the timezone of the Region | 
| MONTHLY | Creates a DbBackup every month on the 1st at midnight in the timezone of the Region | 
| CUSTOM | Use an AWS Cron Expression for a custom frequency. Must be at a daily frequency or less. | 

**Example CUSTOM type:**

```
--db-backup-configurations '[{
     "enabled": true,
     "type": "CUSTOM",
     "retentionDays": 7,
     "customSchedule": "cron(00 18 * * * *)"
    }]'
```

This creates a backup that runs at 18:00 every day in the local timezone.

**Note**  
Automated backups can start anytime within an hour of the scheduled time.

### Best practices for scheduling
<a name="influxdb2-backup-scheduling-best-practices"></a>
+ Use shorter frequencies like `HOURLY` with shorter retention days.
+ Use longer frequencies like `WEEKLY` or `MONTHLY` with longer retention days.
+ If using a custom schedule, schedule the backup during low-traffic windows.

## Listing and viewing backups
<a name="influxdb2-backup-listing"></a>

List all backups for a resource:

```
aws timestream-influxdb list-db-backups \
    --db-resource-id {{my-resource-id}}
```

List all backups in the account:

```
aws timestream-influxdb list-db-backups
```

Get backup details:

```
aws timestream-influxdb get-db-backup \
    --identifier {{my-db-backup-id}}
```

### DbBackup statuses
<a name="influxdb2-backup-statuses"></a>


| Status | Description | 
| --- | --- | 
| IN\_PROGRESS | Backup is being created (database remains available) | 
| COMPLETED | Backup is completed and available to use for restore | 
| FAILED | Backup creation failed | 
| DELETING | Backup is being deleted | 
| DELETED | Backup has been deleted | 

## Restoring from a DbBackup
<a name="influxdb2-backup-restoring"></a>

A DbBackup can be restored to a new resource, or it can replace the existing resource where the backup was taken.

### Restore to a new resource
<a name="influxdb2-backup-restoring-new"></a>

This is the default and recommended restore mode since it does not impact any existing resources.

```
aws timestream-influxdb restore-from-db-backup \
    --name {{my-new-restored-database}} \
    --db-backup-id {{my-backup-id}} \
    --restore-mode NEW_RESOURCE
```

If no additional parameters are provided, the new resource inherits all parameters from the DbBackup. A subset of these parameters can be overridden during restore if provided.

A backup of a DB instance can be restored to a Read Replicas cluster. A backup of a cluster cannot be restored to a standalone DB instance.

#### Restoring a standalone instance backup to a Read Replicas cluster
<a name="influxdb2-backup-restoring-saz-to-rr"></a>

You can restore a backup from a standalone instance (Single-AZ or Multi-AZ) to a Read Replicas cluster. This operation is a **migration**, not a point-in-time restore, because of differences in the internal storage format.

**Warning**  
Standalone instances use a Write-Ahead Log (WAL) that periodically flushes to TSM storage files. When restoring to a Read Replicas cluster, only data that has been persisted to TSM files is included. Data still in the WAL at the time of the backup is not restored. WAL data is flushed to TSM after approximately 10 minutes of write inactivity or when the in-memory cache reaches 25 MB. These thresholds are configurable via parameter groups.  
If your instance has never generated TSM files, the restore to a Read Replicas cluster results in an empty database with no data. This can occur when:  
The instance is new and has received little or no data.
Write volume is very low (below 25 MB per shard) and writes arrive continuously without a 10-minute pause—preventing both the size-based and time-based flush triggers from firing.

To minimize data not yet persisted to TSM, stop writes to the source instance and wait at least 10 minutes before creating the backup. Restoring to another standalone instance (Single-AZ or Multi-AZ) does not have this limitation—all data including WAL contents is preserved.

### Restore to an existing resource
<a name="influxdb2-backup-restoring-existing"></a>

```
aws timestream-influxdb restore-from-db-backup \
    --name {{my-existing-resource-name}} \
    --db-backup-id {{my-backup-id}} \
    --restore-mode REPLACE_EXISTING
```

When restoring to an existing resource, no additional parameters are accepted and no changes to the existing database configuration will be made besides restoring the data.

**Warning**  
Restoring to an existing resource is a **destructive operation**. The resource will not be available during this operation. Existing data will be deleted and replaced with the data from the time of the backup. If there are failures during the operation, the service will attempt to roll back the resource with the original data. It is highly recommended to take an on-demand DbBackup prior to performing this action. After the operation completes, the original data is deleted and not recoverable unless a DbBackup was taken.

You can restrict this operation using an IAM policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "timestream-influxdb:RestoreFromDbBackup",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "timestream-influxdb:RestoreMode": "REPLACE_EXISTING"
                }
            }
        }
    ]
}
```

### Restore (AWS Management Console)
<a name="influxdb2-backup-restoring-console"></a>

1. Open the Amazon Timestream for InfluxDB console.

1. In the navigation pane, choose **Backups**.

1. Select the backup you want to restore from.

1. Choose **Actions**, **Restore backup**.

1. Choose the restore mode (**New resource** or **Replace existing**).

1. Configure settings as needed and choose **Restore**.

## Deleting backups
<a name="influxdb2-backup-deleting"></a>

```
aws timestream-influxdb delete-db-backup \
    --identifier {{my-db-backup-id}}
```

If `retentionDays` is set, the DbBackup is automatically deleted on that day.

### Retaining backups when deleting a resource
<a name="influxdb2-backup-deleting-on-resource-delete"></a>

When deleting a resource, by default all automated DbBackups are deleted and on-demand backups are retained. To retain automated backups on resource deletion, use the `--retain-automated-backups` flag:

```
aws timestream-influxdb delete-db-instance \
    --identifier {{my-db-instance-id}} \
    --retain-automated-backups
```

```
aws timestream-influxdb delete-db-cluster \
    --db-cluster-id {{my-db-cluster-id}} \
    --retain-automated-backups
```

Retained automated backups are automatically deleted at their configured expiry day depending on the retention policy.

## Performance impact
<a name="influxdb2-backup-performance"></a>

Taking a backup has minimal impact to the performance of the database. However, if the database is under high CPU and memory load, the backup may take longer to complete. It is recommended to schedule backups during low-traffic hours.

The first backup may take longer since it creates a full database backup. Subsequent backups are incremental and only capture changed data.

## Relationship to service-managed backups
<a name="influxdb2-snapshots-vs-service-backups"></a>

Customer-managed backups **complement** (not replace) the service-managed backups that AWS maintains:


| Feature | Service-managed backups | Customer-managed backups | 
| --- | --- | --- | 
| Control | Managed by AWS | Managed by you | 
| Access | Via AWS support ticket | Self-service (Console, CLI, API) | 
| Frequency | Hourly (automatic) | On-demand or custom schedule | 
| Retention | Managed by AWS | Defined by you | 
| Restore method | Support ticket required | Self-service restore (new resource or replace existing) | 

Both backup mechanisms can be active simultaneously, providing multiple layers of data protection.

## Security and encryption
<a name="influxdb2-backup-security"></a>
+ All backups are encrypted at rest using service-managed AWS KMS keys.
+ For resources with customer managed keys (CMK) enabled, backups are encrypted with the same AWS KMS key.
+ Access to backup operations is controlled through IAM policies.
+ Backup data remains in the same AWS Region as your database.

## Limitations
<a name="influxdb2-backup-limitations"></a>
+ Backups can only be restored within the same AWS account and Region where they were created.
+ Cross-Region and cross-account restore is not supported.
+ A backup of a DB cluster cannot be restored to a standalone DB instance.
+ Restoring a standalone instance (Single-AZ or Multi-AZ) backup to a Read Replicas cluster only includes data persisted to TSM files. See [Restoring a standalone instance backup to a Read Replicas cluster](#influxdb2-backup-restoring-saz-to-rr).
+ A maximum of 4 DbBackupConfigurations can be enabled per resource.
+ Custom schedule frequency must be at a daily frequency or less.

## Pricing
<a name="influxdb2-backup-pricing"></a>

There is no additional charge for the customer-managed backup and restore feature. You pay only for the Amazon EBS storage used by your backups. Incremental backups reduce storage costs by capturing only changed data. Restores are charged based on volume size. For Amazon EBS storage pricing, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/).