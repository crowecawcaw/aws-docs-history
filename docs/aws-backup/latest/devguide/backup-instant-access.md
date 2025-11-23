# Backup instant access permissions

When using Amazon GuardDuty Malware Protection for AWS Backup with S3 backups, Amazon GuardDuty accesses your S3 backups through three APIs: CreateBackupAccessPoint, DescribeBackupAccessPoint, and DeleteBackupAccessPoint.

Amazon GuardDuty uses CreateBackupAccessPoint to access your encrypted backup data. During the scan job, GuardDuty uses DescribeBackupAccessPoint to verify successful access point creation. Once the scan completes, GuardDuty calls DeleteBackupAccessPoint to remove its access to your backup.

This workflow applies to both S3 backups and EC2/EBS backups stored in a logically air-gapped vault.
