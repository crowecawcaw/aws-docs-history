# SUS04-BP05 Remove unneeded or redundant data

Remove unneeded or redundant data to minimize the storage resources required to store your
datasets.

**Common anti-patterns:**

- You duplicate data that can be easily obtained or recreated.
- You back up all data without considering its criticality.
- You only delete data irregularly, on operational events, or not at all.
- You store data redundantly irrespective of the storage service's durability.
- You turn on Amazon S3 versioning without any business justification.

**Benefits of establishing this best practice:** Removing unneeded
data reduces the storage size required for your workload and the workload environmental impact.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

When you remove unneeded and redundant datasets, you can reduce storage cost and environmental footprint. This practice may also make computing more efficient, as compute resources only process important data instead of unneeded data. Automate the deletion of unneeded data. Use technologies that deduplicate data at the file and block level. Use service features for native data replication and redundancy.

### Implementation steps

- **Evaluate public datasets:** Evaluate if you can avoid storing data by using existing publicly available datasets
  in [AWS Data Exchange](https://aws.amazon.com/data-exchange/ "https://aws.amazon.com/data-exchange/") and [Open Data on AWS](https://registry.opendata.aws/ "https://registry.opendata.aws/").
- **De-deplicate data:** Use mechanisms that can deduplicate data at the block and object level. Here are some
  examples of how to deduplicate data on AWS:

| Storage service                                                                                                                             | Deduplication mechanism                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")                                                                        | Use [AWS Lake Formation FindMatches](https://aws.amazon.com/blogs/big-data/integrate-and-deduplicate-datasets-using-aws-lake-formation-findmatches/ "https://aws.amazon.com/blogs/big-data/integrate-and-deduplicate-datasets-using-aws-lake-formation-findmatches/") to find matching records across a dataset<br>(including ones without identifiers) by using the new FindMatches ML<br>Transform. |
| [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/")                                                                     | Use [data deduplication](../../../fsx/latest/WindowsGuide/using-data-dedup.md "../../../fsx/latest/WindowsGuide/using-data-dedup.md")<br>on Amazon FSx for Windows.                                                                                                                                                                                                                                   |
| [Amazon Elastic Block Store snapshots](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md") | Snapshots are incremental backups, which means that only the blocks on the<br>device that have changed after your most recent snapshot are saved.                                                                                                                                                                                                                                                     |

- **Use lifecycle policies:** Use lifecycle policies to automate unneeded data deletion. Use native service features like [Amazon DynamoDB Time To Live](../../../amazondynamodb/latest/developerguide/TTL.md "../../../amazondynamodb/latest/developerguide/TTL.md"),
  [Amazon S3 Lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md"), or [Amazon CloudWatch log
  retention](../../../managedservices/latest/userguide/log-customize-retention.md "../../../managedservices/latest/userguide/log-customize-retention.md") for deletion.
- **Use data virtualization:** Use data virtualization capabilities on AWS to maintain data at its source and
  avoid data duplication.
  - [Cloud Native Data
    Virtualization on AWS](https://www.youtube.com/watch?v=BM6sMreBzoA "https://www.youtube.com/watch?v=BM6sMreBzoA")
  - [Optimize Data Pattern Using Amazon Redshift Data Sharing](https://catalog.workshops.aws/well-architected-sustainability/en-US/3-data/optimize-data-pattern-using-redshift-data-sharing "https://catalog.workshops.aws/well-architected-sustainability/en-US/3-data/optimize-data-pattern-using-redshift-data-sharing")

- **Use incremental backup:** Use backup technology that can make incremental backups.
- **Use native durability:** Leverage the durability of [Amazon S3](../../../AmazonS3/latest/userguide/DataDurability.md "../../../AmazonS3/latest/userguide/DataDurability.md") and [replication of
  Amazon EBS](../../../AWSEC2/latest/UserGuide/ebs-volumes.md "../../../AWSEC2/latest/UserGuide/ebs-volumes.md") to meet your durability goals instead of self-managed technologies (such
  as a redundant array of independent disks (RAID)).
- **Use efficient logging:** Centralize log and trace data, deduplicate identical log entries, and establish
  mechanisms to tune verbosity when needed.
- **Use efficient caching:** Pre-populate caches only where justified.
- Establish cache monitoring and automation to resize the cache accordingly.
- **Remove old version assets:** Remove out-of-date deployments and assets from object stores and edge caches when
  pushing new versions of your workload.

## Resources

**Related documents:**

- [Change log data retention in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention")
- [Data
  deduplication on Amazon FSx for Windows File Server](../../../fsx/latest/WindowsGuide/using-data-dedup.md "../../../fsx/latest/WindowsGuide/using-data-dedup.md")
- [Features of
  Amazon FSx for ONTAP including data deduplication](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md#features-overview "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md#features-overview")
- [Invalidating Files on Amazon CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/Invalidation.md "../../../AmazonCloudFront/latest/DeveloperGuide/Invalidation.md")
- [Using AWS Backup to back up
  and restore Amazon EFS file systems](../../../efs/latest/ug/awsbackup.md "../../../efs/latest/ug/awsbackup.md")
- [What is
  Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md")
- [Working with
  backups on Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md")
- [Integrate and deduplicate datasets using AWS Lake Formation](https://aws.amazon.com/blogs/big-data/integrate-and-deduplicate-datasets-using-aws-lake-formation-findmatches/ "https://aws.amazon.com/blogs/big-data/integrate-and-deduplicate-datasets-using-aws-lake-formation-findmatches/")

**Related videos:**

- [Amazon Redshift Data Sharing Use
  Cases](https://www.youtube.com/watch?v=sIoTB8B5nn4 "https://www.youtube.com/watch?v=sIoTB8B5nn4")

**Related examples:**

- [How do
  I analyze my Amazon S3 server access logs using Amazon Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/analyze-logs-athena/ "https://aws.amazon.com/premiumsupport/knowledge-center/analyze-logs-athena/")
