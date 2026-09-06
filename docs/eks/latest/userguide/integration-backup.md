

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Back up your EKS Clusters with AWS Backup
<a name="integration-backup"></a>

 AWS Backup supports backups of Amazon EKS clusters, including Kubernetes cluster state and persistent storage attached to the EKS cluster via a persistent volume claim (EBS volumes, EFS file systems, and S3 buckets). An Amazon EKS backup will create a composite recovery point, where a child recovery point will be for each resource backed up.
+ How to back up resources: [Getting started with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/getting-started.html) 
+ Backup creation by Resource Type: [Amazon EKS Backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup.html) 
+ How to restore Amazon EKS clusters: [Amazon EKS Backups restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-a-backup.html) 

To get started via the EKS console, AWS Backup console, or CLI, ensure that your IAM role has the following permissions:
+ These can be found in AWS Backup’s Managed policy [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-backup/latest/devguide/security-iam-awsmanpol.html#AWSBackupServiceRolePolicyForBackup). This contains the required permissions to back up your Amazon EKS cluster and EBS and EFS persistent storage
+ If your EKS Cluster contains an S3 bucket you will need to ensure the following policies and prerequisites for your S3 bucket are added and enabled as documented:
+  [AWSBackupServiceRolePolicyForS3Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/security-iam-awsmanpol.html#AWSBackupServiceRolePolicyForS3Backup) 
+ Prerequisites for [S3 Backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html#s3-backup-prerequisites) 

Ensure your EKS Clusters have the following settings:
+ EKS Cluster [authorization mode](https://docs.aws.amazon.com/eks/latest/userguide/setting-up-access-entries.html) set to API or API\_AND\_CONFIG\_MAP for AWS Backup to create [Access Entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) to access the EKS cluster.