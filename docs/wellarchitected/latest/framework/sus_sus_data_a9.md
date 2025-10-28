# SUS04-BP08 Back up data only when difficult to

recreate

Avoid backing up data that has no business value to minimize storage resources requirements
for your workload.

**Common anti-patterns:**

- You do not have a backup strategy for your data.
- You back up data that can be easily recreated.

**Benefits of establishing this best practice:** Avoiding back-up
of non-critical data reduces the required storage resources for the workload and lowers its
environmental impact.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Avoiding the back up of unnecessary data can help lower cost and reduce the storage
resources used by the workload. Only back up data that has business value or is needed to
satisfy compliance requirements. Examine backup policies and exclude ephemeral storage that
doesn’t provide value in a recovery scenario.

### Implementation steps

- **Classify data:** Implement data classification policy as outlined in [SUS04-BP01 Implement a data classification policy](sus_sus_data_a2.md "sus_sus_data_a2.md").
- **Design a backup strategy:** Use the criticality of your data classification and design backup strategy based on
  your [recovery time objective (RTO) and recovery point objective (RPO](../reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.md "../reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.md")). Avoid backing
  up non-critical data.
  - Exclude data that can be easily recreated.
  - Exclude ephemeral data from your backups.
  - Exclude local copies of data, unless the time required to restore that data from
    a common location exceeds your service-level agreements (SLAs).

- **Use automated backup:** Use an automated solution or managed service to back up business-critical data.
  - [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md") is a fully-managed service that makes it easy to centralize and
    automate data protection across AWS services, in the cloud, and on premises. For
    hands-on guidance on how to create automated backups using AWS Backup, see [Well-Architected Labs - Testing Backup and Restore of Data](https://catalog.workshops.aws/well-architected-reliability/en-US/4-failure-management/1-backup/30-testing-backup-and-restore-of-data "https://catalog.workshops.aws/well-architected-reliability/en-US/4-failure-management/1-backup/30-testing-backup-and-restore-of-data").
  - [Automate backups and optimize backup costs for Amazon EFS using AWS Backup](https://aws.amazon.com/blogs/storage/automating-backups-and-optimizing-backup-costs-for-amazon-efs-using-aws-backup/ "https://aws.amazon.com/blogs/storage/automating-backups-and-optimizing-backup-costs-for-amazon-efs-using-aws-backup/").

## Resources

**Related best practices:**

- [REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the
  data from sources](../reliability-pillar/rel_backing_up_data_identified_backups_data.md "../reliability-pillar/rel_backing_up_data_identified_backups_data.md")
- [REL09-BP03 Perform data backup automatically](../reliability-pillar/rel_backing_up_data_automated_backups_data.md "../reliability-pillar/rel_backing_up_data_automated_backups_data.md")
- [REL13-BP02 Use defined recovery strategies to meet the recovery
  objectives](../reliability-pillar/rel_planning_for_recovery_disaster_recovery.md "../reliability-pillar/rel_planning_for_recovery_disaster_recovery.md")

**Related documents:**

- [Using AWS Backup to back up
  and restore Amazon EFS file systems](../../../efs/latest/ug/awsbackup.md "../../../efs/latest/ug/awsbackup.md")
- [Amazon EBS
  snapshots](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md")
- [Working with
  backups on Amazon Relational Database Service](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md")
- [APN
  Partner: partners that can help with backup](https://partners.amazonaws.com/search/partners?keyword=Backup "https://partners.amazonaws.com/search/partners?keyword=Backup")
- [AWS Marketplace: products that can be used for backup](https://aws.amazon.com/marketplace/search/results?searchTerms=Backup "https://aws.amazon.com/marketplace/search/results?searchTerms=Backup")
- [Backing Up
  Amazon EFS](../../../efs/latest/ug/efs-backup-solutions.md "../../../efs/latest/ug/efs-backup-solutions.md")
- [Backing
  Up Amazon FSx for Windows File Server](../../../fsx/latest/WindowsGuide/using-backups.md "../../../fsx/latest/WindowsGuide/using-backups.md")
- [Backup
  and Restore for Amazon ElastiCache (Redis OSS)](../../../AmazonElastiCache/latest/red-ug/backups.md "../../../AmazonElastiCache/latest/red-ug/backups.md")

**Related videos:**

- [AWS re:Invent 2023 -
  Backup and disaster recovery strategies for increased resilience](https://www.youtube.com/watch?v=E073XISxrSU "https://www.youtube.com/watch?v=E073XISxrSU")
- [AWS re:Invent 2023 - What's
  new with AWS Backup](https://www.youtube.com/watch?v=QIffkOyTf7I "https://www.youtube.com/watch?v=QIffkOyTf7I")
- [AWS re:Invent 2021 -
  Backup, disaster recovery, and ransomware protection with AWS](https://www.youtube.com/watch?v=Ru4jxh9qazc "https://www.youtube.com/watch?v=Ru4jxh9qazc")
