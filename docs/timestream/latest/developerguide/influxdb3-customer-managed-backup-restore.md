For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Customer-managed backup and restore

Customer-managed backup and restore lets you create, manage, and restore database backups for your
Amazon Timestream for InfluxDB 3 clusters (Core and Enterprise). You can create on-demand backups, configure
automated scheduled backups, or enable continuous backups for point-in-time restore—all without
opening AWS support tickets.

## Overview

The first backup creates a complete copy of your database. Subsequent backups are incremental and
capture only the data that changed since the last backup, reducing storage costs and backup time.

InfluxDB 3 also supports **continuous backups**, which back up the
database in the background at all times, enabling point-in-time restore to any moment within the
retention window.

###### Note

Data written within the last 15 minutes might not be included in the backup. To recover the
most recent data, use point-in-time restore with a timestamp at least 15 minutes in the
past.

## Key concepts

| Concept                | Description                                                                                                                     |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| DbBackup               | A backup of your database containing the cluster<br>configuration at the time of backup.                                        |
| DbBackupConfiguration  | Automated recurring backups at a defined frequency<br>and retention.                                                            |
| Restore                | Creates a new DB from a DbBackup or restores an existing resource<br>back to the provided DbBackup.                             |
| RetentionDays          | Defines the number of days a backup is kept before<br>automatic deletion.                                                       |
| On Demand Backup       | Triggers a one-time backup of the database at a point in<br>time.                                                               |
| Continuous Backup      | The database backs up in the background at all times and<br>is available for point-in-time restore within the retention window. |
| Custom Schedule Backup | Defines a custom AWS cron schedule when the<br>DB will be backed up automatically.                                              |

## Creating a DbBackup

### On-demand backup (AWS CLI)

Create an on-demand backup of a cluster:

```
aws timestream-influxdb create-db-backup \
    --db-resource-id `my-db-cluster-id` \
    --name `my-db-backup-2026-07-07` \
    --retention-days 7
```

### On-demand backup (AWS Management Console)

1. Open the Amazon Timestream for InfluxDB console.
2. Choose your InfluxDB 3 cluster.
3. Choose **Actions**, **Create
   backup**.
4. Enter a backup name and retention period.
5. Choose **Create backup**.

## Configuring automated backups

Automated backups can be enabled at resource creation time or updated afterwards. Only one
DbBackupConfiguration is allowed per type per resource, and a maximum of 4 DbBackupConfigurations
can be enabled per resource.

### Enable automated backups on create (AWS CLI)

```
aws timestream-influxdb create-db-cluster \
    --name `my-db-cluster` \
    --db-instance-type db.influx.medium \
    --vpc-subnet-ids `subnet-0123456789abcdef0` \
    --vpc-security-group-ids `sg-0123456789abcdef0` \
    --db-parameter-group-identifier InfluxDBV3Core \
    --db-backup-configurations '[{
       "enabled": true,
       "type": "CONTINUOUS",
       "retentionDays": 30
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

DbBackupConfigurations can be enabled, disabled, and retention can be changed after creation:

```
aws timestream-influxdb update-db-cluster \
    --db-cluster-id `my-db-cluster-id` \
    --db-backup-configurations '[{
       "enabled": true,
       "type": "CONTINUOUS",
       "retentionDays": 30
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

| Type         | Description                                                                                                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CONTINUOUS` | Creates a continuous backup that can be restored<br>to any point in time within the last 15 minutes up to the creation date or retention date<br>(whichever is later). Maximum retention is 35 days. |
| `HOURLY`     | Creates a DbBackup every hour                                                                                                                                                                        |
| `DAILY`      | Creates a DbBackup every day at midnight in the<br>timezone of the Region                                                                                                                            |
| `WEEKLY`     | Creates a DbBackup every week on Sunday at midnight<br>in the timezone of the Region                                                                                                                 |
| `MONTHLY`    | Creates a DbBackup every month on the 1st at midnight<br>in the timezone of the Region                                                                                                               |
| `CUSTOM`     | Use an AWS Cron Expression for a custom frequency.<br>Must be at a daily frequency or less.                                                                                                          |

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

###### Note

Automated backups can start anytime within an hour of the scheduled time.

### Best practices for scheduling

- Use `CONTINUOUS` for maximum coverage with point-in-time restore and
  up to 35-day retention.
- Use longer frequencies like `WEEKLY` or `MONTHLY` with longer
  retention days for extended archival.

## Listing and viewing backups

List all backups for a resource:

```
aws timestream-influxdb list-db-backups \
    --db-resource-id `my-resource-id`
```

List all backups in the account:

```
aws timestream-influxdb list-db-backups
```

Get backup details:

```
aws timestream-influxdb get-db-backup \
    --identifier `my-db-backup-id`
```

### DbBackup statuses

| Status        | Description                                             |
| ------------- | ------------------------------------------------------- |
| `IN_PROGRESS` | Backup is being created (cluster remains<br>available)  |
| `COMPLETED`   | Backup is completed and available to use for<br>restore |
| `FAILED`      | Backup creation failed                                  |
| `DELETING`    | Backup is being deleted                                 |
| `DELETED`     | Backup has been deleted                                 |

## Restoring from a DbBackup

A DbBackup can be restored to a new resource, or it can replace the existing resource where the
backup was taken.

### Restore to a new resource

This is the default and recommended restore mode since it does not impact any existing
resources.

```
aws timestream-influxdb restore-from-db-backup \
    --name `my-new-restored-database` \
    --db-backup-id `my-backup-id` \
    --restore-mode NEW_RESOURCE
```

If no additional parameters are provided, the new resource inherits all parameters from the
DbBackup. A subset of these parameters can be overridden during restore if provided.

#### Point-in-time restore (continuous backups)

For a `CONTINUOUS` backup, you can specify a `--restore-to-time`
parameter for the exact UNIX epoch timestamp in seconds to restore the database. The timestamp
must be between the last 15 minutes up to the retention days or time of backup creation
(whichever is later).

```
aws timestream-influxdb restore-from-db-backup \
    --name `my-pitr-restored-database` \
    --db-backup-id `my-continuous-backup-id` \
    --restore-mode NEW_RESOURCE \
    --restore-to-time `1751382000`
```

### Restore to an existing resource

```
aws timestream-influxdb restore-from-db-backup \
    --name `my-existing-resource-name` \
    --db-backup-id `my-backup-id` \
    --restore-mode REPLACE_EXISTING
```

When restoring to an existing resource, no additional parameters are accepted and no changes
to the existing database configuration will be made besides restoring the data.

###### Warning

Restoring to an existing resource is a **destructive operation**.
The resource will not be available during this operation. Existing data will be deleted and
replaced with the data from the time of the backup. If there are failures during the operation,
the service will attempt to roll back the resource with the original data. It is highly
recommended to take an on-demand DbBackup prior to performing this action. After the operation
completes, the original data is deleted and not recoverable unless a DbBackup was taken.

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

1. Open the Amazon Timestream for InfluxDB console.
2. In the navigation pane, choose **Backups**.
3. Select the backup you want to restore from.
4. Choose **Actions**, **Restore
   backup**.
5. Choose the restore mode (**New resource** or
   **Replace existing**).
6. For continuous backups, optionally specify the point-in-time to restore to.
7. Configure settings as needed and choose **Restore**.

## Deleting backups

```
aws timestream-influxdb delete-db-backup \
    --identifier `my-db-backup-id`
```

If `retentionDays` is set, the DbBackup is automatically deleted on that day.

### Retaining backups when deleting a resource

When deleting a resource, by default all automated DbBackups are deleted and on-demand backups
are retained. To retain automated backups on resource deletion, use the
`--retain-automated-backups` flag:

```
aws timestream-influxdb delete-db-cluster \
    --db-cluster-id `my-db-cluster-id` \
    --retain-automated-backups
```

Retained automated backups are automatically deleted at their configured expiry day depending
on the retention policy.

## Performance impact

Backups on Amazon Timestream for InfluxDB v3 do not have any notable impact to the performance of
the database.

The first backup may take longer since it creates a full database backup. Subsequent backups are
incremental and only capture changed data.

The backup start time can be delayed due to scheduling but should generally start within one hour
of the on-demand backup or scheduled time.

## Relationship to service-managed backups

With customer-managed backup and restore, you have full control over your backup strategy
including continuous backups for point-in-time restore:

| Feature               | Service-managed backups | Customer-managed backups                                |
| --------------------- | ----------------------- | ------------------------------------------------------- |
| Control               | Managed by AWS          | Managed by you                                          |
| Access                | Via AWS support ticket  | Self-service (Console, CLI, API)                        |
| Frequency             | Automatic               | On-demand, scheduled, or continuous                     |
| Point-in-time restore | Not available           | Available with CONTINUOUS type (up to 35-day window)    |
| Retention             | Managed by AWS          | Defined by you (per configuration)                      |
| Restore method        | Support ticket required | Self-service restore (new resource or replace existing) |

## Security and encryption

- All backups are encrypted at rest using service-managed AWS KMS keys.
- For resources with customer managed keys (CMK) enabled, backups are encrypted
  with the same AWS KMS key.
- Access to backup operations is controlled through IAM policies.
- Backup data remains in the same AWS Region as your cluster.

## Limitations

- Backups can only be restored within the same AWS account and Region where they
  were created.
- Cross-Region and cross-account restore is not supported.
- A maximum of 4 DbBackupConfigurations can be enabled per resource.
- Custom schedule frequency must be at a daily frequency or less.
- Continuous backup maximum retention is 35 days.
- Point-in-time restore is only available for continuous backups, not scheduled backups.
- In-place restore (`REPLACE_EXISTING` mode) is not supported for clusters
  encrypted with a customer managed key (CMK). Use `NEW_RESOURCE` mode instead.

## Pricing

There is no additional charge for the customer-managed backup and restore feature. You pay only for the
Amazon S3 storage used by your backups. Incremental backups reduce storage costs by capturing only
changed data. For Amazon S3 storage pricing, see [Amazon S3
pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").
