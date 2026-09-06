

# How continuity management works in AMS
<a name="ug-automated-or-manual"></a>

 AMS backup plans define how frequently your data is backed up and the retention policy for your backups. AMS backup vaults keep your backup data organized. Once a resource is associated with a backup plan, [compatible resources](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-resource) are incrementally backed up. The first backup is a full copy and subsequent backups capture incremental changes. Depending on the resource and AMS backup plan selected, [Point-in-time restore (PITR)](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html) allows you to rewind your resources by selecting a time for your recovery. To get started with AMS Backup Management, simply select an AMS backup plan and tag your resources.

**Note**  
Ensure that AWS Backup is enabled for each account, AWS Region, and resource type by following the steps here: [ Getting Started 1: Service Opt-in](https://docs.aws.amazon.com/aws-backup/latest/devguide/getting-started.html#service-opt-in).  
You do not need to continue to *Getting started 2: Create on on-demand backup*.

**Related Topics from AWS Backup**
+ [Working with backups (Create, Edit, Copy, Restore, Delete)](https://docs.aws.amazon.com/aws-backup/latest/devguide/recovery-points.html)
+ [Create an on-demand backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-on-demand-backup.html)
+ [Creating backup copies across AWS Regions](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html)
+ [AWS Backup Supported Services](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#supported-resources)
+ [Point-in-time restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html)
+ [AWS Backup Features](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-for-all-resources)