

# COST03-BP03 Enforce data retention policies

 Every object, backup, snapshot, and log you keep occupies storage you pay for, and much of it outlives its usefulness. Data retention policies define how long each type of data must be kept and when to move it to cheaper storage or delete it. Automating those policies controls storage cost and improves your ability to meet retention requirements. 

 **Desired outcome:** 
+  Your data retention policies run automatically, without manual cleanup. 
+  Your storage costs reflect the value of the data, because aging data moves to cheaper tiers or is deleted. 
+  Your data retention meets organizational and regulatory requirements. 
+  Your outdated and unnecessary data is removed on a defined schedule. 

 **Common anti-patterns:** 
+  Teams manage data retention manually, so cleanup depends on manual follow-up. 
+  Data is kept well beyond the period any requirement calls for. 
+  Retention decisions ignore the cost of storing data to satisfy compliance rules. 
+  Critical and non-critical data are treated the same, so everything is retained at the same cost. 

 **Benefits of establishing this best practice:** 
+  Storage costs fall because expired data is removed automatically. 
+  Compliance improves because retention periods are enforced consistently rather than by hand. 
+  Data handling aligns with organizational policy across every storage service. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Data retention pulls in two directions. Some data has to be kept for years to meet compliance rules, and if you delete it too early you can fall out of compliance or lose the copy you needed to recover from. The other side of it is cost. Once data is past the point where anyone uses it, you're just paying to store it for no reason. This is what a retention policy is for. For each kind of data, you decide how long to keep it and when to delete it, and you set that up as automated rules so data ages out on its own instead of someone having to remember to go clean it up. 

 Retention starts with classification. Regulatory data has a mandated retention period you cannot shorten. Operational data such as logs decays in value quickly and can be deleted within weeks. Backups and snapshots exist for recovery, so their retention follows your recovery objectives. Group data by these needs and set a per-class policy. Otherwise, everything defaults to indefinite retention, the most expensive option. 

 When you inherit a system, audit its retention configuration within the first 30 days. Check for a missing noncurrent-version-expiration rule on versioned buckets, incomplete multipart upload cleanup, and storage-tier transitions that were never configured. Without a noncurrent-version-expiration rule, versioned buckets accumulate noncurrent objects indefinitely. 

 Move data you must keep but rarely access to colder, cheaper storage tiers to cut cost. The trade-off is retrieval: colder tiers cost less to store and more to read, and some impose minimum storage durations that make early deletion expensive. Match the tier to the access pattern. For unknown or changing access patterns, use automated tiering that moves objects by observed access. 

 Retention is scattered across every service that stores data. Object storage, block storage snapshots, database backups, and log stores each have their own retention mechanism. A policy applied to one does not carry to the others. A workload can enforce strict retention on its object storage while accumulating years of forgotten database snapshots and log data. Apply a single cross-service retention policy, adapted to each store. 

 AWS provides retention controls for each storage type. [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) transitions and expires objects, and [S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html) moves data between tiers based on access. [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html) applies retention to backups across services, and [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html) manages Amazon EBS snapshot retention. For databases and logs, [Amazon RDS automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.BackupRetention.html) and [Amazon CloudWatch Logs retention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SttingLogRetention) set periods per resource. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Classify data and define retention periods:** Before configuring any service, group your data by retention need, such as regulatory, operational, backup, and recovery, and set a required minimum and a cost-driven maximum for each group. Account for compliance requirements, business continuity needs, recovery objectives, and the performance implications of each storage tier. Record these decisions so every storage service enforces the same policy. 

1.  **Manage object storage lifecycle:** Configure [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) rules to transition objects between storage classes, expire temporary data, and manage object versions and delete markers. Enable [S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html) for buckets with unknown or changing access patterns. Use [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-lens/) for visibility into the usage patterns that inform your rules. 

1.  **Configure backup retention:** Use AWS Backup to define retention periods per backup type, transition backups to cold storage, delete expired backups automatically, and apply cross-Region copies where continuity or compliance requires them. Monitor adherence with [AWS Backup Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html). 

1.  **Manage snapshot lifecycle:** Configure [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html) to automate Amazon EBS snapshot and AMI creation and deletion, set cross-Region copies, define cleanup schedules, and tag snapshots for management. For retention logic beyond its built-in policies, use [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html). 

1.  **Set database backup retention:** Configure [Amazon RDS automated backup retention](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.BackupRetention.html), manage the manual snapshot lifecycle, apply cross-Region copies, and set point-in-time recovery periods to match your recovery objectives. For Aurora MySQL-Compatible Edition, use [Aurora Backtrack](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html) to reach specific recovery points without restoring a backup. 

1.  **Manage log retention:** Set [Amazon CloudWatch Logs retention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SttingLogRetention) periods on each log group, export logs to Amazon S3 for long-term storage, and clean up log streams and metric filters on a schedule. Analyze retained logs with [Amazon CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html). 

1.  **Apply service-specific retention features:** Extend retention policies to every service that stores data. Configure [Index State Management](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ism.html) for Amazon OpenSearch Service, [point-in-time recovery](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery_Howitworks.html) for Amazon DynamoDB, [backup and restore](https://docs.aws.amazon.com/documentdb/latest/devguide/backup_restore.html) for Amazon DocumentDB, [point-in-time policies](https://docs.aws.amazon.com/drs/latest/userguide/point-in-time.html) for AWS Elastic Disaster Recovery, [snapshots and backups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) for Amazon Redshift, and backups for Amazon FSx file systems ([FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html), [FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-backups-fsx.html), [FSx for ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-backups.html), and [FSx for OpenZFS](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/using-backups.html)). 

1.  **Audit inherited systems within 30 days:** When you take ownership of an existing system, audit its [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) configuration within the first 30 days. Specifically verify that noncurrent version expiration is configured on every versioned bucket, that incomplete multipart uploads are cleaned up, and that storage-tier transitions match the data's actual access pattern. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST03-BP01 Track resources over their lifetime](cost03-bp01.md) 
+  [COST03-BP02 Implement efficient resource lifecycle management](cost03-bp02.md) 

 **Related documents:** 
+  [Amazon S3 Lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) 
+  [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html) 
+  [Amazon RDS backup retention](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.BackupRetention.html) 
+  [Amazon CloudWatch Logs retention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SttingLogRetention) 

 **Related videos:** 
+  [AWS re:Invent 2024 - AWS storage best practices for cost optimization](https://www.youtube.com/watch?v=Nu-beEngBB4) 
+  [Understanding Amazon S3 Lifecycle management policies](https://www.youtube.com/watch?v=c5PKWc_n2Kc) 
+  [Empty an Amazon S3 bucket using a lifecycle configuration rule](https://www.youtube.com/watch?v=JfK9vamen9I) 
+  [Automate data administrative operations with Index State Management (ISM) policies](https://www.youtube.com/watch?v=WB2Z2u0IxjU) 

 **Related examples:** 
+  [How do I use a lifecycle configuration rule to empty an Amazon S3 bucket?](https://repost.aws/knowledge-center/s3-empty-bucket-lifecycle-rule) 
+  [S3 Lifecycle configuration examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html) 
+  [AWS Backup automation examples](https://github.com/aws-samples/aws-backup-automation) 

 **Related workshops:** 
+  [CFM Technical Implementation Playbooks (CFM TIPs): Service cost optimization playbooks](https://catalog.workshops.aws/awscff/) 