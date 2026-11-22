

# REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources

 Not all data is equally valuable, and you can recreate some from an authoritative source rather than back it up. Decide what to protect, how often, and by which method to build a recovery strategy that meets your tolerance for loss. 

 **Desired outcome:** 
+  You have identified every data source in the workload and classified each one by criticality. 
+  Your recovery strategy defines, for each source, whether you back it up or reproduce it from another source. 
+  Your backup frequency and recovery method meet the recovery point objective (RPO) and recovery time objective (RTO) for each data source. 
+  You can restore or reproduce data within your defined RPO and RTO after a loss event. 

 **Common anti-patterns:** 
+  Teams remain unaware of all data sources in the workload or their relative criticality. 
+  Teams back up only some data sources without using criticality to decide what to protect. 
+  Teams operate without a defined RPO, or the backup frequency cannot meet the RPO. 
+  Teams back up data that could be reproduced more cheaply or quickly from an existing source. 
+  Teams treat backup and reproduction as equivalent without comparing recovery time against the RTO. 

 **Benefits of establishing this best practice:** 
+  Critical data stays protected because you know where it lives and how much loss you can tolerate. 
+  Recovery costs stay lower because you back up only what cannot be reproduced more efficiently. 
+  Recovery stays within your RTO because you match the recovery method to the time available. 
+  Recovery decisions are auditable because criticality and method are documented for each source. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Two objectives drive every backup decision: 
+  The *recovery point objective (RPO)* is the amount of data loss you can accept, measured as a window of time. 
+  The *recovery time objective (RTO)* is how long you can take to restore service. 

 A source with an RPO near zero needs frequent backup, while one that tolerates a day of loss needs backup far less often. Classify each source by criticality first, because criticality determines RPO and RTO. 

 When you can derive data from an authoritative source, a separate backup adds redundant cost and effort. A cache holds a copy of data from elsewhere, and a read replica mirrors a primary database. A data warehouse or analytics cluster often loads from durable object storage. In these cases, plan to reproduce the data rather than restore it. Reproducing data takes time too, and if rebuilding a large dataset exceeds your RTO, back it up instead despite the storage cost. 

 Archival storage tiers lower the cost of long-term backups but add retrieval delay that counts against your RTO. Match the tier to how fast you need the data, not to cost alone. Copying backups to a second Region protects against a Regional event but adds transfer time and cost. 

 On AWS, most data services provide native backup, and several offer point-in-time recovery (PITR) for restoring to any moment within a retention window. [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) centralizes and automates protection across many services. [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) replicates full server workloads with an RPO measured in seconds. For data outside AWS, [AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html) and [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) move on-premises data into [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html). Lower-cost S3 tiers such as [Amazon Glacier Flexible Retrieval and S3 Glacier Deep Archive](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-glacier) reduce long-term storage cost. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify all data sources for the workload:** Enumerate every place data is stored, including [databases](https://aws.amazon.com/products/databases/), [block volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html), [file systems](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html), [log stores](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html), and [object storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html). Record the backup capability each source provides. 

1.  **Classify each source by criticality and assign RPO and RTO:** Rank sources by how much their loss would harm the workload. Assign an RPO and RTO to each, recognizing that some data justifies an RPO near zero while other data tolerates loss and a longer recovery window. 

1.  **Back up the sources that require it:** Use [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) to centralize protection, native service capabilities such as [Amazon RDS snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html) and [DynamoDB point-in-time recovery](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/), or [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) for full server replication. Copy backups to a second Region where a Regional event is part of your threat model. 

1.  **Define a reproduction process for sources you choose not to back up:** For data that is cheaper or faster to rebuild, document how it is recreated and from where. For example, reload a [data warehouse](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorks.html) or analytics cluster from durable object storage, or rebuild a cache or read replica from its primary. Confirm the reproduction time fits within the RTO before relying on it. 

1.  **Set the backup cadence from the RPO:** Schedule each backup at a frequency that keeps potential data loss inside the source's RPO. Review the cadence when data criticality or the RPO changes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL09-BP03 Perform data backup automatically](rel09-bp03.md) 
+  [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](rel09-bp04.md) 
+  [REL13-BP01 Define recovery objectives for downtime and data loss](rel13-bp01.md) 
+  [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](rel13-bp02.md) 

 **Related documents:** 
+  [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) 
+  [What is AWS DataSync?](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) 
+  [What is Volume Gateway?](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html) 
+  [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html) 
+  [Backing up EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html) 
+  [Protecting your data with backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html) 
+  [Snapshot and restore](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups.html) 
+  [Creating a DB Cluster Snapshot in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-create-snapshot.html) 
+  [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html) 
+  [Using on-demand DynamoDB backup and restore](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorks.html) 
+  [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) 
+  [Exporting log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html) 
+  [Managing the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) 
+  [What is Elastic Disaster Recovery?](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) 
+  [Replicating objects within and across Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) 
+  [Restore testing](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Building resilience against ransomware using AWS Backup (STG412)](https://www.youtube.com/watch?v=ARkahJFwaZQ) 
+  [AWS Backup logically air-gapped vault demo \| Amazon Web Services](https://www.youtube.com/watch?v=Oncp7awcwj4) 
+  [AWS re:Invent 2024 - What's new with AWS Backup (STG203)](https://www.youtube.com/watch?v=YFcoAZQvcHM) 

 **Related examples:** 
+  [AWS Disaster Recovery Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/84b75b08-d9c9-4dfc-b9d8-7f4273e85da0/en-US) 