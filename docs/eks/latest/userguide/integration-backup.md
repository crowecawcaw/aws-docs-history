**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Backup your EKS Clusters with AWS Backup

AWS Backup supports backups of Amazon EKS clusters, including Kubernetes cluster state and persistent storage attached to the EKS cluster via a persistent volume claim (EBS volumes, EFS file systems, and S3 buckets).
An Amazon EKS backup will create a composite recovery point, where a child recovery point will be for each resource backed up.

- How to back up resources: [Getting started with AWS Backup](../../../aws-backup/latest/devguide/getting-started.md "../../../aws-backup/latest/devguide/getting-started.md")
- Backup creation by Resource Type: [Amazon EKS Backups](../../../aws-backup/latest/devguide/creating-a-backup.md "../../../aws-backup/latest/devguide/creating-a-backup.md")
- How to restore Amazon EKS clusters: [Amazon EKS Backups restore](../../../aws-backup/latest/devguide/restoring-a-backup.md "../../../aws-backup/latest/devguide/restoring-a-backup.md")
  To get started via the EKS console, AWS Backup console or CLI ensure that your IAM role has the following permissions:

- These can be found in AWS Backup’s Managed policy [AWSBackupServiceRolePolicyForBackup](../../../aws-backup/latest/devguide/security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForBackup "../../../aws-backup/latest/devguide/security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForBackup"). This contains the required permissions to backup your Amazon EKS cluster and EBS and EFS persistent storage
- If your EKS Cluster contains an S3 bucket you will need to ensure the following policies and prequisites for your S3 bucket are added and enabled as documented:
- [AWSBackupServiceRolePolicyForS3Backup](../../../aws-backup/latest/devguide/security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForS3Backup "../../../aws-backup/latest/devguide/security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForS3Backup")
- Prerequisites for [S3 Backups](../../../aws-backup/latest/devguide/s3-backups.md#s3-backup-prerequisites#AWSBackupServiceRolePolicyForS3Backup "../../../aws-backup/latest/devguide/s3-backups.md#s3-backup-prerequisites#AWSBackupServiceRolePolicyForS3Backup")
  Ensure your EKS Clusters have the following settings:

- EKS Cluster [authorization mode](setting-up-access-entries.md "setting-up-access-entries.md") set to API or API_AND_CONFIG_MAP for AWS Backup to create [Access Entries](access-entries.md "access-entries.md") to access the EKS cluster.
