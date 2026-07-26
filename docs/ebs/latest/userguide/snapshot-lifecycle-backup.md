# AWS Backup for Amazon Elastic Block Store

AWS Backup is a fully managed service that centralizes and automates data protection
across your entire AWS environment. Rather than managing snapshot schedules and retention
per resource, you define a single backup policy and apply it across accounts and Regions.
Tag your resources and AWS Backup protects them automatically, with no per-team configuration
required. The service supports many AWS services including Amazon EBS, Amazon EC2, Amazon S3, Amazon EFS,
Amazon RDS, and Aurora, so one policy can protect volumes, databases, file systems, and
object stores together without separate backup tools per workload.

For Amazon EBS, AWS Backup delivers crash-consistent, multi-volume snapshots that coordinate
point-in-time backups across all volumes attached to an Amazon EC2 instance. This is essential
for databases and clustered applications that span multiple volumes. AWS Backup Search takes
recovery a step further by enabling item-level recovery. You can locate and restore
individual files or directories from Amazon EBS snapshots without restoring the entire
volume.

AWS Backup also adds enterprise-grade security and compliance to your snapshots. Logically
air-gapped vaults isolate recovery points from your production environment. Vault Lock
enforces immutability. Amazon GuardDuty integration scans backups for malware. Backup Audit
Manager continuously evaluates your backup posture and generates audit-ready compliance
reports.

To get started, see the following resources:

- [AWS Backup Developer Guide](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md")
- [Create
  multi-volume, crash-consistent backups](../../../aws-backup/latest/devguide/multi-volume-crash-consistent.md "../../../aws-backup/latest/devguide/multi-volume-crash-consistent.md")
- [Restore
  Amazon EBS volumes](../../../aws-backup/latest/devguide/restoring-ebs.md "../../../aws-backup/latest/devguide/restoring-ebs.md")
- [Search
  and recover individual files from Amazon EBS snapshots](https://aws.amazon.com/blogs/storage/streamline-search-and-item-level-recovery-with-aws-backup/ "https://aws.amazon.com/blogs/storage/streamline-search-and-item-level-recovery-with-aws-backup/")
