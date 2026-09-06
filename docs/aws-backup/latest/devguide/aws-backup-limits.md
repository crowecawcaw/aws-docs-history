

# AWS Backup quotas
<a name="aws-backup-limits"></a>

The following quotas apply when working with AWS Backup.

**Topics**
+ [Backup](#aws-backup-quotas-table)
+ [Backup index and search quotas](#aws-backup-search-quotas-table)
+ [Policy quotas](#aws-backup-policies-quotas-table)
+ [Malware scanning quotas](#backup-scanning-quotas-table)
+ [Amazon Timestream resource quotas](#backup-timestream-quotas-table)
+ [AWS Backup Audit Manager quotas](#backup-audit-manager-quotas-table)
+ [[Restore testing](restore-testing.md) plan quotas](#backup-restore-testing-quotas-table)
+ [AWS Backup gateway quotas](#backup-gateway-quotas-table)
+ [Amazon EKS quotas](#backup-eks-quotas-table)
+ [Logically air-gapped vault quotas](#lag-vault-quotas-table)
+ [Related quotas](#backup-related-quotas)

## Backup
<a name="aws-backup-quotas-table"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Total vaults (backup and logically air-gapped) per Region per account | 300 | Yes | 
| Recovery points per backup vault | 1,000,000 | Yes | 
| Backup plans per Region per account | 300 | Yes | 
| Versions per backup plan | 2,000 | Yes | 
| Resource assignments per backup plan | 100 | No | 
| Concurrent cross-Region or in-Region copy jobs per account in destination Region | 1002 | No | 
| Additional cross-Region copy jobs per vault in a destination Region after the limit in row above entry has been reached.1 | 52 | No | 
| Concurrent cross-account copies that can be made of the same resource to the same destination Region | 30 | No | 
| Concurrent backup and copy jobs per resource | 1 | No | 
| Tags per resource selection in a cross account backup policy | 30 | No. Include additional tags using multiple resource assignments or backups plans. | 
| Hypervisors | 20 | No | 
| Legal holds per account | 50 | No | 
| Nested backup layers of application stacks | 10 | No | 

1The limit for concurrent copy jobs from one Region to another Region is 100 per account per Region. Once this limit is reached, if a specific vault in the destination Region has fewer than 5 concurrent copy jobs, new copy jobs can begin, up to a maximum of 5 concurrently.

2Limit only apply to resource types [fully managed by AWS Backup](backup-feature-availability.md).

## Backup index and search quotas
<a name="aws-backup-search-quotas-table"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Concurrent indexing jobs in account (most AWS Regions) | 40 | Yes | 
| Concurrent indexing jobs in account in Asia Pacific (Malaysia), Canada (Central), Asia Pacific (Thailand), and Mexico (Central) AWS Regions. | 10 | Yes | 
| Concurrent indexing jobs for each resource | 5 | No | 
| Concurrent on-demand indexing job | 1 | No | 
| Concurrent search jobs in account | 10 |  | 
| Concurrent export jobs | 5 |  | 
| Number of recovery points included in search job | 20 |  | 
| Concurrent Amazon EBS file level restore jobs (most AWS Regions) | 25 |  | 
| Concurrent Amazon EBS file level restore jobs in Asia Pacific (Malaysia), Canada (Central), Asia Pacific (Thailand), and Mexico (Central) AWS Regions. | 5 |  | 

## Policy quotas
<a name="aws-backup-policies-quotas-table"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Resource assignments per backup plan | 100 | No | 
| Tags in a resource selection | 30 | No | 
| Resource selections that use tags in a plan | 10 | No | 
| Backup plan rules in a plan | 10 | No | 
| Tags added to a recovery point | 10 | No | 
| Copy actions per backup rule | 5 | No | 
| Conditions in a resource assignment in a backup plan | 30 | No | 

## Malware scanning quotas
<a name="backup-scanning-quotas-table"></a>

The following table lists quotas for AWS Backup malware scanning with Amazon GuardDuty.


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Running scan jobs per resource per account | 5 | Yes | 
| Running scan jobs per recovery point per account | 1 | No | 
| Running scan jobs per account | 150 | Yes | 
| Created scan jobs per resource per account | 10 | No | 
| Incremental scan base constraint | 1 | No | 

When you hit your created scan jobs per resource per account limit, we will fail oldest queued job.

You might also encounter quotas imposed by Amazon GuardDuty. For more information, see [Amazon GuardDuty quotas](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_limits.html) in the *AWS General Reference*.

## Amazon Timestream resource quotas
<a name="backup-timestream-quotas-table"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Concurrent Timestream backup jobs per account | 4 | Yes | 
| Concurrent Timestream restore jobs per account | 1 | Yes | 

## AWS Backup Audit Manager quotas
<a name="backup-audit-manager-quotas-table"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Frameworks per account per Region | 15 | Yes | 
| Controls per account per Region | 50 | Yes | 
| Report plans per account | 20 | Yes | 
| Frameworks per report plan | 1,000 | No | 
| [Number of accounts] multiplied by [number of Regions in a report plan] multiplied by [number of daily jobs plus evaluations in a report plan] | 100,000 | No | 

## [Restore testing](restore-testing.md) plan quotas
<a name="backup-restore-testing-quotas-table"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Restore testing plans | 100 | No | 
| Tags per plan | 50 | No | 
| Selections per plan | 30 | No | 
| ARNs per restore testing selection | 30 | No | 
| Conditions per selection (both StringEquals and StringNotEquals) | 30 | No | 
| Vault selectors per restore testing selection | 30 | No | 
| Maximum value (in days) of selection window | 365 days | No | 
| Boundaries of start window hours | Minimum: 1 hour; Maximum: 168 hours | No | 
| Maximum character length of restore testing plan name | 50 characters (alphanumeric and underscores, no white spaces) | No | 
| Maximum character length of restore testing selection name | 50 characters (alphanumeric and underscores, no white spaces) | No | 

Each resource type has a limit on the number of concurrent restore jobs that can exist at one time for restore jobs that are created through a restore testing plan. Once this limit is reached, no new restore jobs for that resource type will be created until a job in a state of `RUNNING` transitions to `COMPLETED`.

If a scheduled restore job did not start due to this quota, that job will result in a `FAILED` status with the status message `"Restore job was unable to start within the specified start window. Try increasing your start window."`. If you receive a failed job with this status message, the best practice is to first increase your start window with sufficient time to allow jobs to finish. Then, retry the jobs.

Note quotas do not apply to on-demand restore jobs, but to restore jobs created by a [restore testing plan](restore-testing.md#restore-testing-create). For some resource types, you may request an increase in the quota limit.


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Amazon Aurora | 40 | Yes | 
| Amazon DocumentDB | 40 | Yes | 
| Amazon DynamoDB | 40 | No | 
| Amazon EBS | 100 | Yes | 
| Amazon EC2 | 100 | Yes | 
| Amazon EFS | 30 | Yes | 
| Amazon FSx | 40 | Yes | 
| Amazon Neptune | 40 | Yes | 
| Amazon RDS | 40 | Yes | 
| Amazon S3 | 30 | Yes | 

## AWS Backup gateway quotas
<a name="backup-gateway-quotas-table"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Backup or restore jobs per gateway | 4 | No. Create more gateways and connect them to your hypervisor. | 
| VMware tags to resource tags mapping per hypervisor | 10 | No | 

## Amazon EKS quotas
<a name="backup-eks-quotas-table"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Namespaces per EKS cluster backup | 10,000 | Yes | 
| Persistent Storage backups per EKS cluster backup | 1,200 | Yes | 
| Restore jobs per target EKS cluster | 1 | No | 
| EKS Restore jobs per account | 5 | Yes | 

## Logically air-gapped vault quotas
<a name="lag-vault-quotas-table"></a>


| Resource type | Maximum number of concurrent copies | 
| --- | --- | 
| EC2 | The EBS concurrent copy limit applies to any snapshots being copied as part of an AMI copy. | 
| EBS | 20 | 
| Aurora | 20 | 
| DocumentDB | 20 | 
| Neptune | 20 | 
| Storage Gateway | 5 | 
| FSx | 5 | 

## Related quotas
<a name="backup-related-quotas"></a>

There are [ quotas on a single resource assignment](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-quotas) in a single backup rule. You can create a backup plan with multiple backup rules.

When you manage backups across multiple accounts using AWS Organizations, you might encounter quotas that AWS Organizations imposes. For these quotas, see [Quotas for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) in the *AWS Organizations User Guide*.

You might also encounter quotas imposed by a AWS Backup-supported service, including the following:
+ [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/limits.html)
+ [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-resource-quotas.html)
+ [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html)
+ [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html)
+ [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html)
+ [AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/resource-gateway-limits.html)
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html)
+ [Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/limits.html)
+ [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-user-quotas.html)
+ [Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/limits.html)
+ [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/limits.html)
+ [Amazon Simple Storage Service](https://docs.aws.amazon.com/general/latest/gr/s3.html#limits_s3)
+ [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/backups-limits.html)