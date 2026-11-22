

# REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes

 Backups can be incomplete, corrupted, or slower to restore than your recovery targets allow, and you may only find out when you try to restore the backup. Regular recovery testing verifies you can restore a working system from backups within your recovery objectives. 

 **Desired outcome:** 
+  You recover data from backups on a regular schedule using defined mechanisms. 
+  Recovery tests confirm the restored data is complete, uncorrupted, and accessible. 
+  Recovery time is measured and compared against the recovery time objective (RTO). 
+  Data loss observed in tests falls within the recovery point objective (RPO). 

 **Common anti-patterns:** 
+  Teams restore a backup but never query the data to confirm it is usable. 
+  Teams assume a backup exists without verifying it. 
+  Teams assume the restored data is complete and uncorrupted. 
+  Teams assume restore time falls within the RTO without measuring it. 
+  Teams recover only during real incidents, without a runbook or automated procedure. 

 **Benefits of establishing this best practice:** 
+  You gain confidence that data can be restored when it is needed. 
+  You know whether your restore process meets the RTO because you have measured it. 
+  Recovery becomes repeatable through documented, automated procedures. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 When testing recovery, the restored data must be complete and uncorrupted, the recovery must finish within the RTO, and any data lost must fall within the RPO. A backup can appear healthy in a console yet meet none of these criteria, so verify by running the actual restore, not by inspecting metadata. 

 Before you test, define what "correct" looks like for each data source. A checksum comparison between the source at backup time and the restored copy catches silent corruption. Row counts, record formats, and the presence of the most recent transaction confirm completeness. 

 Run recovery tests in an isolated environment so a drill never affects production. Restore into a separate location, validate there, and measure the elapsed time from restore start through validation. Compare that measured time against the RTO. Continuous backup and point-in-time recovery (PITR) let you test recovery to a specific moment, which confirms your RPO assumptions. 

 Manual, occasional tests drift out of date as the workload changes. Automate the restore, validation, and failure notification to keep tests current and run them on a schedule. The following figure shows such a workflow where a scheduler triggers the restore, validation logic checks the recovered data, and a notification fires on failure or RTO breach. 

![Workflow diagram showing a scheduler triggering a backup restore, validation logic checking the recovered data, and a notification firing on failure or RTO breach.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/automated-backup-restore-process.png)

*Automated backup restore and validation workflow*


 On AWS, [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/create-policy.html) monitors your configuration against your RTO and RPO targets and alerts you when changes introduce posture drift. [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-a-backup.html) restores a backup into a new resource, and [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) launches recovery drills without redirecting traffic. [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) timestamps API calls so you can measure restore time, and [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) delivers alerts on test failure. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify the data sources and where their backups are stored:** List each source being backed up and the location and format of its backups. For guidance on cataloging sources, see [REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources](rel09-bp01.md). 

1.  **Establish validation criteria for each source:** Define how you will confirm a restore is correct, using properties such as data type, format, checksum, record count, or size, combined with custom logic where needed. For example, compare the checksum of the restored resource against the source at the time the backup was taken. 

1.  **Establish RTO and RPO for the restore:** Set the recovery time and data loss targets the test will measure against, based on data criticality. For guidance, see [REL13-BP01 Define recovery objectives for downtime and data loss](rel13-bp01.md). 

1.  **Assess your recovery capability:** Review the backup and restore strategy against those targets and adjust it where it falls short. Use [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/create-policy.html) to continuously evaluate your configuration against a resilience policy. It monitors for posture drift over time and alerts you when changes put your RTO or RPO targets at risk. 

1.  **Perform a test restore:** Restore into an isolated environment using the same process you would use in production. With [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-a-backup.html), restore the backup into a new resource. With [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/), launch a recovery drill. 

1.  **Validate the recovered data:** Apply your validation criteria to confirm the restored data is complete, uncorrupted, and current, and that any loss falls within the RPO. 

1.  **Measure restore and recovery time:** Compare the elapsed time against your RTO, using [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) timestamps for the restore start and your validation logic for the completion time. AWS Backup records restore jobs with timestamp metadata you can use for this measurement. 

1.  **Notify stakeholders and automate the test:** Send an alert with [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) when validation fails or the RTO is exceeded, and route findings to [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/) where useful. Schedule the whole workflow with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) or [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) invoked by [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources](rel09-bp01.md) 
+  [REL09-BP03 Perform data backup automatically](rel09-bp03.md) 
+  [REL13-BP01 Define recovery objectives for downtime and data loss](rel13-bp01.md) 
+  [REL13-BP03 Test disaster recovery implementation to validate the implementation](rel13-bp03.md) 

 **Related documents:** 
+  [Restore a backup by resource type](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-a-backup.html) 
+  [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) 
+  [Creating resiliency policies](https://docs.aws.amazon.com/resilience-hub/latest/userguide/create-policy.html) 
+  [Creating a scheduled rule (legacy) in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html) 
+  [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) 
+  [What is Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) 
+  [Create OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems.html) 
+  [What is Elastic Disaster Recovery?](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) 

 **Related examples:** 
+  [Automate data recovery validation with AWS Backup](https://aws.amazon.com/blogs/storage/automate-data-recovery-validation-with-aws-backup/) 