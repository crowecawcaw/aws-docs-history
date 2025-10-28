# Find backup settings in AMS

Backups and snapshots are managed by AMS through the native [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/") service.

The configuration is managed through AWS Backup plans. You can have multiple AWS Backup plans that associate
tagged resources with backup schedules and retention policies. To find your AMS account AWS Backup settings, use the
[https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup") console, or the _AWS CLI Command Reference_ for
[backup](../../../cli/latest/reference/backup/index.md "../../../cli/latest/reference/backup/index.md") commands.

For more information about AMS and AWS Backup, see
[Continuity Management](../userguide/continuity-mgmt.md "../userguide/continuity-mgmt.md").
