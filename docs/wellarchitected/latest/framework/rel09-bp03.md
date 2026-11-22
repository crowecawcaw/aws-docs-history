

# REL09-BP03 Perform data backup automatically

 Manual backups fail in predictable ways. For example, people forget, schedules slip, and a missed backup goes unnoticed until someone needs to recover. Automating backups on a schedule tied to your tolerance for data loss removes the human step and produces a record of whether each backup succeeded. 

 **Desired outcome:** 
+  Backups run automatically on a schedule or in response to data changes, without manual action. 
+  Backup frequency is derived from the recovery point objective (RPO) for each data source. 
+  You receive an alert when a scheduled backup does not complete. 
+  Every data source that supports automated backup is included in your automation. 

 **Common anti-patterns:** 
+  Teams create backups manually. 
+  Teams use resources that support automated backup but leave those backups out of their automation. 
+  Teams set a single backup frequency without mapping it to each source's RPO. 

 **Benefits of establishing this best practice:** 
+  Backups happen reliably because no one has to remember to run them. 
+  Data loss stays within the RPO because frequency is set deliberately per source. 
+  Missed backups surface through alerting rather than during a failed recovery. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A manual backup depends on a person remembering to do it, and it produces no signal when skipped. An automated backup process runs on a defined trigger and can alert you when a run fails. The RPO sets how often the trigger fires. A source with a tight RPO needs frequent or continuous protection, while a source that tolerates more loss can run on a longer interval. 

 Continuous backup with point-in-time recovery (PITR) captures changes as they happen, so you can restore to any point within a retention window. Scheduled snapshots capture the state at fixed intervals. Continuous protection gives the smallest possible data loss but is available only for certain services, while scheduled snapshots apply broadly. Match the method to each source's RPO. 

 Automated backup support does nothing until you configure the backup. Sources outside a managed backup service, such as on-premises systems or message queues, need their own automation. A centralized, policy-based approach reduces these coverage gaps by managing many sources from one place and showing which resources are not covered. 

 On AWS, [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) provides policy-based backup plans across many services, in the cloud and on premises through Storage Gateway. Several services also offer native automation: [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html), [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery_Howitworks.html), and [Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery.html) support continuous backup with PITR, [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html) automates Amazon EBS snapshots and AMIs, and [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) performs continuous block-level replication. Amazon S3 versioning and replication add automatic copies once turned on. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify data sources still backed up manually:** List sources that rely on a person to trigger backups, and treat them as candidates for automation. For guidance on cataloging sources, see [REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources](rel09-bp01.md). 

1.  **Determine the RPO for each source:** Set the acceptable data loss window that will drive backup frequency. For guidance on setting recovery objectives, see [REL13-BP01 Define recovery objectives for downtime and data loss](rel13-bp01.md). 

1.  **Use a managed or automated backup solution:** Create [backup plans in AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup.html#creating-automatic-backups) that define which resources to protect and how often, setting the frequency from the RPO in the previous step. Where a service offers native automation, such as Amazon RDS automated backups with PITR, use it. 

1.  **Automate sources not covered by a managed service:** For on-premises systems, message queues, and other unsupported sources, build automation with the AWS CLI or SDKs, or use a trusted third-party solution. Define the backup logic in [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) or [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) and invoke it on an [Amazon EventBridge schedule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html) set to your RPO. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources](rel09-bp01.md) 
+  [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](rel09-bp04.md) 
+  [REL13-BP01 Define recovery objectives for downtime and data loss](rel13-bp01.md) 

 **Related documents:** 
+  [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) 
+  [Backup creation by resource type](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup.html#creating-automatic-backups) 
+  [Automate backups with Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html) 
+  [Creating a scheduled rule (legacy) in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html) 
+  [What is Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) 
+  [What is Elastic Disaster Recovery?](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - What's new with AWS Backup (STG203)](https://www.youtube.com/watch?v=YFcoAZQvcHM) 