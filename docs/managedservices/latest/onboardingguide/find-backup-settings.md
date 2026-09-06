

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Find backup settings in AMS
<a name="find-backup-settings"></a>

Backups and snapshots are managed by AMS through the native [AWS Backup](https://aws.amazon.com/backup/) service.

The configuration is managed through AWS Backup plans. You can have multiple AWS Backup plans that associate tagged resources with backup schedules and retention policies. To find your AMS account AWS Backup settings, use the [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup) console, or the *AWS CLI Command Reference* for [backup](https://docs.aws.amazon.com/cli/latest/reference/backup/index.html) commands.

For more information about AMS and AWS Backup, see [Continuity Management](https://docs.aws.amazon.com/managedservices/latest/userguide/continuity-mgmt.html).