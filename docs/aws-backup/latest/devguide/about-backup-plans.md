

# Backup plans
<a name="about-backup-plans"></a>

In AWS Backup, a *backup plan* is a policy expression that defines when and how you want to back up your AWS resources, such as Amazon DynamoDB tables or Amazon Elastic File System (Amazon EFS) file systems. You can assign resources to backup plans, and AWS Backup automatically backs up and retains backups for those resources according to the backup plan. You can create multiple backup plans if you have workloads with different backup requirements. By default, backup windows are optimized by AWS Backup. You can customize the backup window in the console or programmatically.

AWS Backup efficiently stores your periodic backups incrementally for supported resource types. The first backup of an AWS resource backs up a full copy of your data. For each successive incremental backup, only the changes to your AWS resources are backed up. Incremental backups enable you to benefit from the data protection of frequent backups while minimizing storage costs.

**Important**  
Not all resource types support incremental backups. For resources that do not support incremental backups, each backup is a full copy, which can result in higher storage costs. For a list of which resources support incremental backups, see [Feature availability by resource](backup-feature-availability.md#features-by-resource).

AWS Backup also seamlessly manages your backup plan's lifecycle based on your retention settings, which allows you to restore when needed.

The following sections provide the basics of managing your backup strategy in AWS Backup.

**Topics**
+ [Create a backup plan](creating-a-backup-plan.md)
+ [Understanding backup plan summary](understanding-backup-plan-summaries.md)
+ [Select AWS services to backup](assigning-resources.md)