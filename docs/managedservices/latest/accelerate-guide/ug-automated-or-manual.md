# How continuity management works in AMS

AMS backup plans define how frequently your data is backed up and the retention policy
for your backups. AMS backup vaults keep your backup data organized. Once a resource is
associated with a backup plan, [compatible
resources](../../../aws-backup/latest/devguide/whatisbackup.md#features-by-resource "../../../aws-backup/latest/devguide/whatisbackup.md#features-by-resource") are incrementally backed up. The first backup is a full copy and
subsequent backups capture incremental changes. Depending on the resource and AMS backup
plan selected, [Point-in-time restore
(PITR)](../../../aws-backup/latest/devguide/point-in-time-recovery.md "../../../aws-backup/latest/devguide/point-in-time-recovery.md") allows you to rewind your resources by selecting a time for your recovery. To
get started with AMS Backup Management, simply select an AMS backup plan and tag your
resources.

###### Note

Ensure that AWS Backup is enabled for each account, AWS Region, and resource type by following the steps here:
[Getting Started 1: Service Opt-in](../../../aws-backup/latest/devguide/getting-started.md#service-opt-in "../../../aws-backup/latest/devguide/getting-started.md#service-opt-in").

You do not need to continue to _Getting started 2: Create on on-demand backup_.

**Related Topics from AWS Backup**

- [Working with backups (Create, Edit, Copy, Restore, Delete)](../../../aws-backup/latest/devguide/recovery-points.md "../../../aws-backup/latest/devguide/recovery-points.md")
- [Create an on-demand backup](../../../aws-backup/latest/devguide/create-on-demand-backup.md "../../../aws-backup/latest/devguide/create-on-demand-backup.md")
- [Creating backup copies across AWS Regions](../../../aws-backup/latest/devguide/cross-region-backup.md "../../../aws-backup/latest/devguide/cross-region-backup.md")
- [AWS Backup Supported Services](../../../aws-backup/latest/devguide/whatisbackup.md#supported-resources "../../../aws-backup/latest/devguide/whatisbackup.md#supported-resources")
- [Point-in-time restore](../../../aws-backup/latest/devguide/point-in-time-recovery.md "../../../aws-backup/latest/devguide/point-in-time-recovery.md")
- [AWS Backup Features](../../../aws-backup/latest/devguide/whatisbackup.md#features-for-all-resources "../../../aws-backup/latest/devguide/whatisbackup.md#features-for-all-resources")
