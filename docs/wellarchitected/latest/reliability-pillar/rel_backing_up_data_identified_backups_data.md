# REL09-BP01 Identify and back up all data that needs to be

backed up, or reproduce the data from sources

Understand and use the backup capabilities of the data services and resources used by the workload. Most services provide capabilities to back up workload data.

**Desired outcome:** Data sources have been identified and classified based on
criticality. Then, establish a strategy for data recovery based on
the RPO. This strategy involves either backing up these data
sources, or having the ability to reproduce data from other sources.
In the case of data loss, the strategy implemented allows recovery
or the reproduction of data within the defined RPO and RTO.

**Cloud maturity phase:**
Foundational

**Common anti-patterns:**

- Not aware of all data sources for the workload and their
  criticality.
- Not taking backups of critical data sources.
- Taking backups of only some data sources without using
  criticality as a criterion.
- No defined RPO, or backup frequency cannot meet RPO.
- Not evaluating if a backup is necessary or if data can be
  reproduced from other sources.

**Benefits of establishing this best
practice:** Identifying the places where backups are
necessary and implementing a mechanism to create backups, or being
able to reproduce the data from an external source improves the
ability to restore and recover data during an outage.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

All AWS data stores offer backup capabilities. Services such as Amazon RDS and Amazon DynamoDB additionally support automated backup that allows point-in-time recovery (PITR), which allows you to restore a backup to any time up to five minutes or less before the current time. Many AWS services offer the ability to copy backups to another AWS Region. AWS Backup is a tool that gives you the ability to centralize and automate data protection across AWS services. [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/ "https://aws.amazon.com/disaster-recovery/") allows you to copy full server workloads and maintain continuous data protection from on-premise, cross-AZ or cross-Region, with a Recovery Point Objective (RPO) measured in seconds.

Amazon S3 can be used as a backup destination for self-managed and AWS-managed data sources. AWS services such as Amazon EBS, Amazon RDS, and Amazon DynamoDB have built in capabilities to create backups. Third-party backup software can also be used.

On-premises data can be backed up to the AWS Cloud using [AWS Storage Gateway](../../../storagegateway/latest/vgw/WhatIsStorageGateway.md "../../../storagegateway/latest/vgw/WhatIsStorageGateway.md") or [AWS DataSync](../../../datasync/latest/userguide/what-is-datasync.md "../../../datasync/latest/userguide/what-is-datasync.md"). Amazon S3 buckets can be used to store this data on AWS. Amazon S3 offers multiple storage tiers such as [Amazon Glacier or Amazon Glacier Deep Archive](../../../prescriptive-guidance/latest/backup-recovery/amazon-s3-glacier.md "../../../prescriptive-guidance/latest/backup-recovery/amazon-s3-glacier.md") to reduce cost of data storage.

You might be able to meet data recovery needs by reproducing the data from other sources. For example, [Amazon ElastiCache replica nodes](../../../AmazonElastiCache/latest/red-ug/Replication.Redis.md "../../../AmazonElastiCache/latest/red-ug/Replication.Redis.md") or [Amazon RDS read replicas](../../../AmazonRDS/latest/UserGuide/USER_ReadRepl.md "../../../AmazonRDS/latest/UserGuide/USER_ReadRepl.md") could be used to reproduce data if the primary is lost. In cases where sources like this can be used to meet your [Recovery Point Objective (RPO) and Recovery Time Objective (RTO)](disaster-recovery-dr-objectives.md "disaster-recovery-dr-objectives.md"), you might not require a backup. Another example, if working with Amazon EMR, it might not be necessary to backup your HDFS data store, as long as you can [reproduce the data into Amazon EMR from Amazon S3](https://aws.amazon.com/premiumsupport/knowledge-center/copy-s3-hdfs-emr/ "https://aws.amazon.com/premiumsupport/knowledge-center/copy-s3-hdfs-emr/").

When selecting a backup strategy, consider the time it takes to recover data. The time needed to recover data depends on the type of backup (in the case of a backup strategy), or the complexity of the data reproduction mechanism. This time should fall within the RTO for the workload.

**Implementation steps**

1. **Identify all data sources for the
   workload**. Data can be stored on a number of
   resources such as
   [databases](https://aws.amazon.com/products/databases/ "https://aws.amazon.com/products/databases/"),
   [volumes](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md"),
   [filesystems](../../../efs/latest/ug/whatisefs.md "../../../efs/latest/ug/whatisefs.md"),
   [logging
   systems](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md"), and
   [object
   storage](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md"). Refer to the
   **Resources** section to find
   **Related documents** on
   different AWS services where data is stored, and the backup
   capability these services provide.
2. **Classify data sources based on
   criticality**. Different data sets will have
   different levels of criticality for a workload, and therefore
   different requirements for resiliency. For example, some data
   might be critical and require a RPO near zero, while other
   data might be less critical and can tolerate a higher RPO and
   some data loss. Similarly, different data sets might have
   different RTO requirements as well.
3. **Use AWS or third-party services to
   create backups of the data**.
   [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md") is a managed service that allows creating
   backups of various data sources on AWS. [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/ "https://aws.amazon.com/disaster-recovery/") handles automated sub-second data
   replication to an AWS Region. Most AWS services
   also have native capabilities to create backups. The AWS Marketplace has many solutions that provide these capabilites
   as well. Refer to the
   **Resources** listed below for
   information on how to create backups of data from various AWS
   services.
4. **For data that is not backed up,
   establish a data reproduction mechanism**. You might
   choose not to backup data that can be reproduced from other
   sources for various reasons. There might be a situation where
   it is cheaper to reproduce data from sources when needed
   rather than creating a backup as there may be a cost
   associated with storing backups. Another example is where
   restoring from a backup takes longer than reproducing the data
   from sources, resulting in a breach in RTO. In such
   situations, consider tradeoffs and establish a well-defined
   process for how data can be reproduced from these sources when
   data recovery is necessary. For example, if you have loaded
   data from Amazon S3 to a data warehouse (like Amazon Redshift), or MapReduce cluster (like Amazon EMR) to do
   analysis on that data, this may be an example of data that can
   be reproduced from other sources. As long as the results of
   these analyses are either stored somewhere or reproducible,
   you would not suffer a data loss from a failure in the data
   warehouse or MapReduce cluster. Other examples that can be
   reproduced from sources include caches (like Amazon ElastiCache) or RDS read replicas.
5. **Establish a cadence for backing up
   data**. Creating backups of data sources is a
   periodic process and the frequency should depend on the RPO.

**Level of effort for the Implementation
Plan:** Moderate

## Resources

**Related Best Practices:**

[REL13-BP01 Define recovery objectives for downtime and data
loss](rel_planning_for_recovery_objective_defined_recovery.md "rel_planning_for_recovery_objective_defined_recovery.md")

[REL13-BP02 Use defined recovery strategies to meet the recovery
objectives](rel_planning_for_recovery_disaster_recovery.md "rel_planning_for_recovery_disaster_recovery.md")

**Related documents:**

- [What
  Is AWS Backup?](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md")
- [What
  is AWS DataSync?](../../../datasync/latest/userguide/what-is-datasync.md "../../../datasync/latest/userguide/what-is-datasync.md")
- [What
  is Volume Gateway?](../../../storagegateway/latest/vgw/WhatIsStorageGateway.md "../../../storagegateway/latest/vgw/WhatIsStorageGateway.md")
- [APN
  Partner: partners that can help with backup](https://aws.amazon.com/partners/find/results/?keyword=Backup "https://aws.amazon.com/partners/find/results/?keyword=Backup")
- [AWS Marketplace: products that can be used for backup](https://aws.amazon.com/marketplace/search/results?searchTerms=Backup "https://aws.amazon.com/marketplace/search/results?searchTerms=Backup")
- [Amazon EBS Snapshots](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md")
- [Backing
  Up Amazon EFS](../../../efs/latest/ug/efs-backup-solutions.md "../../../efs/latest/ug/efs-backup-solutions.md")
- [Backing
  up Amazon FSx for Windows File Server](../../../fsx/latest/WindowsGuide/using-backups.md "../../../fsx/latest/WindowsGuide/using-backups.md")
- [Backup
  and Restore for ElastiCache for Redis](../../../AmazonElastiCache/latest/red-ug/backups.md "../../../AmazonElastiCache/latest/red-ug/backups.md")
- [Creating
  a DB Cluster Snapshot in Neptune](../../../neptune/latest/userguide/backup-restore-create-snapshot.md "../../../neptune/latest/userguide/backup-restore-create-snapshot.md")
- [Creating
  a DB Snapshot](../../../AmazonRDS/latest/UserGuide/USER_CreateSnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_CreateSnapshot.md")
- [Creating
  an EventBridge Rule That Triggers on a Schedule](../../../eventbridge/latest/userguide/create-eventbridge-scheduled-rule.md "../../../eventbridge/latest/userguide/create-eventbridge-scheduled-rule.md")
- [Cross-Region
  Replication](../../../AmazonS3/latest/dev/crr.md "../../../AmazonS3/latest/dev/crr.md") with Amazon S3
- [EFS-to-EFS
  AWS Backup](https://aws.amazon.com/solutions/efs-to-efs-backup-solution/ "https://aws.amazon.com/solutions/efs-to-efs-backup-solution/")
- [Exporting
  Log Data to Amazon S3](../../../AmazonCloudWatch/latest/logs/S3Export.md "../../../AmazonCloudWatch/latest/logs/S3Export.md")
- [Object
  lifecycle management](../../../AmazonS3/latest/dev/object-lifecycle-mgmt.md "../../../AmazonS3/latest/dev/object-lifecycle-mgmt.md")
- [On-Demand
  Backup and Restore for DynamoDB](../../../amazondynamodb/latest/developerguide/backuprestore_HowItWorks.md "../../../amazondynamodb/latest/developerguide/backuprestore_HowItWorks.md")
- [Point-in-time
  recovery for DynamoDB](../../../amazondynamodb/latest/developerguide/PointInTimeRecovery.md "../../../amazondynamodb/latest/developerguide/PointInTimeRecovery.md")
- [Working
  with Amazon OpenSearch Service Index Snapshots](../../../elasticsearch-service/latest/developerguide/es-managedomains-snapshots.md "../../../elasticsearch-service/latest/developerguide/es-managedomains-snapshots.md")
- [What is AWS Elastic Disaster Recovery?](../../../drs/latest/userguide/what-is-drs.md "../../../drs/latest/userguide/what-is-drs.md")

**Related videos:**

- [AWS re:Invent 2021 - Backup, disaster recovery, and ransomware
  protection with AWS](https://www.youtube.com/watch?v=Ru4jxh9qazc "https://www.youtube.com/watch?v=Ru4jxh9qazc")
- [AWS Backup Demo: Cross-Account and Cross-Region Backup](https://www.youtube.com/watch?v=dCy7ixko3tE "https://www.youtube.com/watch?v=dCy7ixko3tE")
- [AWS re:Invent
  2019: Deep dive on AWS Backup, ft. Rackspace (STG341)](https://youtu.be/av8DpL0uFjc "https://youtu.be/av8DpL0uFjc")
