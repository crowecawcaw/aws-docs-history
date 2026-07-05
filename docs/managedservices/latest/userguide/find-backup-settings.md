End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](SunsetPlan.md "SunsetPlan.md").

# Find backup settings in AMS

Backups and snapshots are managed by AMS through the native [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/") service.

The configuration is managed through AWS Backup plans. You can have multiple AWS Backup plans that associate
tagged resources with backup schedules and retention policies. To find your AMS account AWS Backup settings, use the
[https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup") console, or the _AWS CLI Command Reference_ for
[backup](../../../cli/latest/reference/backup/index.md "../../../cli/latest/reference/backup/index.md") commands.

For more information about AMS and AWS Backup, see
[Continuity Management](continuity-mgmt.md "continuity-mgmt.md").
