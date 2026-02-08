# MSFTREL05-BP02 Implement backup automation

Backup automation is critical for Microsoft workloads running on
AWS, maintaining consistent data protection without manual
intervention. Microsoft applications like SQL Server, Exchange, and
SharePoint require application-aware backup strategies that maintain
data integrity and support reliable recovery scenarios.

**Desired outcome:** Implement
automated, application-consistent backups for Microsoft workloads on
AWS to provide for reliable data protection, reduce manual effort,
and enhance disaster recovery capabilities, ultimately improving
system resilience and recoverability.

**Common anti-patterns:**

- Relying solely on manual, unplanned backups of Windows instances
  and databases, leading to inconsistent backup schedules, missed
  backups, and potential data loss during critical application
  states.
- Using basic snapshot mechanisms without VSS integration,
  resulting in crash-inconsistent backups that may not properly
  capture the state of running applications and could cause data
  corruption during restoration.

**Benefits of establishing this best
practice:**

- Application-consistent backups captures data accurately,
  including in-memory and in-flight transactions, which reduces
  the risk of data corruption or loss.
- Automated backup processes reduce manual effort, minimize human
  errors, and free up IT staff to focus on more strategic tasks.
- Regular, automated backups with cross-region replication provide
  a robust foundation for quick and reliable recovery in case of
  system failures or disasters, minimizing downtime and data loss.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Configure automated backups for servers, databases, and storage
volumes with defined schedules and retention policies. Enable
application-consistent snapshots for data integrity, implement
backup verification, and set up cross-Region copies for
resilience. This strategy provides for comprehensive protection
while maintaining application and file system consistency.

Configure AWS Backup with automated plans targeting Windows
workloads and setting appropriate retention policies. Start with
critical systems, establish backup windows during off-peak hours,
and implement cross-region replication for essential workloads.
Test backup integrity and recovery procedures regularly, and
monitor backup success rates through AWS Backup reports.

### Implementation steps

1. Define backup requirements and policies for SQL Server
   databases (EC2 and RDS), Active Directory domain
   controllers, Exchange Server mailbox databases, FSx for Windows File Server, SharePoint farms, and Windows file
   server volumes, considering RPO/RTO requirements for each
   service.
2. Configure AWS Backup plans with VSS-aware schedules for SQL
   Server transaction log backups, AD System State backups,
   Exchange VSS backups, FSx automatic backups, and SharePoint
   farm-level backups with appropriate retention rules. For
   advanced Microsoft workload backup scenarios, consider AWS
   Partner solutions available in AWS Marketplace.
3. Set up cross-Region backup replication for critical SQL
   Server databases, AD domain controllers, Exchange databases,
   and FSx file systems to maintain disaster recovery
   capabilities. Additionally, configure cross-region
   replication for customer-managed S3 buckets containing
   backup data to enhance resilience.
4. Implement automated backup integrity checks using SQL Server
   CHECKDB, AD database verification, Exchange database
   consistency checks, FSx backup validation, and SharePoint
   content database consistency checks.
5. Establish and test recovery procedures for SQL Server
   point-in-time recovery, AD authoritative restore, Exchange
   mailbox recovery, FSx file system restoration, SharePoint
   farm recovery, and Windows file server volume recovery
   scenarios.

## Resources

**Related documents:**

- [Create
  a backup plan](../../../aws-backup/latest/devguide/creating-a-backup-plan.md "../../../aws-backup/latest/devguide/creating-a-backup-plan.md")
- [Create
  Windows VSS backups](../../../aws-backup/latest/devguide/windows-backups.md "../../../aws-backup/latest/devguide/windows-backups.md")
- [Application-consistent
  backup for Windows application on Amazon EC2 with AWS Backup](https://aws.amazon.com/blogs/storage/application-consistent-backup-for-windows-application-on-amazon-ec2-with-aws-backup/ "https://aws.amazon.com/blogs/storage/application-consistent-backup-for-windows-application-on-amazon-ec2-with-aws-backup/")
- [How
  to simplify Microsoft SQL Server backup using AWS Backup and
  VSS](https://aws.amazon.com/blogs/storage/how-to-simplify-microsoft-sql-server-backup-using-aws-backup-and-vss/ "https://aws.amazon.com/blogs/storage/how-to-simplify-microsoft-sql-server-backup-using-aws-backup-and-vss/")
- [Automating
  SQL Server Point-in-Time Recovery Using EBS Snapshots](https://aws.amazon.com/blogs/modernizing-with-aws/automating-sql-server-point-in-time-recovery-using-ebs-snapshots/ "https://aws.amazon.com/blogs/modernizing-with-aws/automating-sql-server-point-in-time-recovery-using-ebs-snapshots/")

**Related tools:**

- [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/")
- [Amazon EBS snapshots](../../../ebs/latest/userguide/ebs-snapshots.md "../../../ebs/latest/userguide/ebs-snapshots.md")
