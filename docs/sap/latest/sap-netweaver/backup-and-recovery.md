# Backup and Recovery

You need to regularly back up your operating system and database to recover them in case of any failure. AWS provides various services and tools that you can use to back up your SQL Server database of SAP applications.

## Amazon Machine Images (AMIs)

You can use the AWS Management Console or the AWS CLI to create a new [AMI](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md") of your existing SAP system. This AMI can be used to recover your existing SAP system or to create a clone.

The AWS CLI `create image` command creates a new AMI based on an existing Amazon EC2 instance. The new AMI contains a complete copy of the operating system and its configuration, software configurations, and optionally all Amazon EBS volumes that are attached to the instance. For details on how to create an AMI of an existing Amazon EC2 instance, see [Creating an Amazon EBS Backed Windows AMI](../../../AWSEC2/latest/WindowsGuide/Creating_EBSbacked_WinAMI.md "../../../AWSEC2/latest/WindowsGuide/Creating_EBSbacked_WinAMI.md"). AMI creation and lifecycle can be centrally managed in [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md")
AWS Backup.

## Amazon EBS Snapshots

You can back up your Amazon EBS volumes to Amazon Simple Storage Service by taking point-in-time [snapshots](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md"). Snapshots are incremental backups, which means that only the blocks on the device that have changed after your most recent snapshot are saved.

Snapshots are suited to back up SAP file systems like `/usr/sap/` , `/sapmnt/`. If you decide to take snapshots of your EBS volumes containing data and log files, make sure to use [Volume Shadow Copy Service](<https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee923636(v=ws.10)> "https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee923636(v=ws.10)") or shut down your database before a snapshot is triggered for consistency. You can use [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md") to create backups using VSS functionalities.

The following command creates a snapshot of volume (with example `volume id vol-1234567890abcdef0`). You can use this command in AWS CLI to create your own volume snapshot.

```
aws ec2 create-snapshot --volume-id <vol-1234567890abcdef0> --description "This is my volume snapshot."
```

## Database Backups

For SQL Server database backup, you can use one of the following methods:

- **SQL native tools to take backup on disk:** Backup requires high throughput compared to IOPS. We recommend using [Throughput Optimized HDD (st1)](https://aws.amazon.com/ebs/features/ "https://aws.amazon.com/ebs/features/") which provides maximum throughput of 500 MB/s per volume. Once the backup completes on disk, you can use scripts to move it to an Amazon S3 bucket.
- **AWS Backup** for application-consistent backups via Microsoft’s Volume Shadow Copy Services (VSS). Ensure that the flag in the advanced backup settings is enabled:

![Advanced backup settings.](images/advanced-backup-settings.png)

- **Third-party backint tools:** Partners like Commvault, Veritas, and so on use SAP backint interface and store backups directly in Amazon S3 buckets.
