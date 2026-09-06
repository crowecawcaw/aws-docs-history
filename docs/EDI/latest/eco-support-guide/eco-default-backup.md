

# ECO default backup plan
<a name="eco-default-backup"></a>

AWS Backup doesn't support "continuous backups" for ECO default backup plans. For information about different types of backup plans, see [Continuous backups and point-in-time recovery (PITR)](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html).

Use the following tag key–value pair to identify EDI resources that you want ECO to back up.

 `TAG key: ams:rt:backup-orchestrator TAG value: true`

**Important**  
Backup monitoring and reporting are only available in EDI supported regions.