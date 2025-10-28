# ECO default backup plan

AWS Backup doesn't support "continuous backups" for ECO default backup plans. For information about different types of backup plans, see
[Continuous backups and point-in-time recovery (PITR)](../../../aws-backup/latest/devguide/point-in-time-recovery.md "../../../aws-backup/latest/devguide/point-in-time-recovery.md").

Use the following tag key–value pair to identify EDI resources that you want ECO to back up.

`TAG key: ams:rt:backup-orchestrator 
 TAG value: true`

###### Important

Backup monitoring and reporting are only available in EDI supported regions.
