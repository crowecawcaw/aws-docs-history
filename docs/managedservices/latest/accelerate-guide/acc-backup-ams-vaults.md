# View backups in AMS vaults

You can control backup vault notifications at individual vault-level using tags. You can opt out of notifications for a specific vault by adding the
tag `AMSNotificationOptOut` and setting the value to `True` on a specific vault. To resume getting notifications from the vault,
remove the tag.

To view a list of your AMS backups, open the [AWS Backup console](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup"). In the navigation pane,
choose **Backup vaults** and select the one of the AMS backup vaults from the following tables. In the **Backups** section,
view the list of all the backups in the backup vault. Select a backup to edit, delete, or restore.

**Vaults for AMS Backup Plans**

| AMS Vault Name                       | AMS Backup Plan Tag Key                                                                                                                                                                         |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ams-automated-backups                | ams:rt:backup-orchestrator                                                                                                                                                                      |
| ams-automated-enhanced-backups       | ams:rt:backup-orchestrator-enhanced                                                                                                                                                             |
| ams-automated-data-sensitive-backups | ams:rt:backup-orchestrator-data-sensitive                                                                                                                                                       |
| ams-onboarding-backups               | ams:rt:backup-orchestrator-onboarding                                                                                                                                                           | **Other AMS Vaults**                                                                                                                                                                                                                                                                                                                                                                  |
| AMS Vault Name                       | Description                                                                                                                                                                                     |
| ---                                  | ---                                                                                                                                                                                             |
| ams-manual-backups                   | This vault contains manually started backups created by the `AWSManagedServices-StartBackupJob` SSM Automation document and pre-patch backups created by AMS patch automations before patching. |
| ams-custom-backups                   | This is the recommended vault for backups created outside of AMS backup plans.                                                                                                                  | **Related AWS Backup Topics** <br>• [View Backups by Resource](../../../aws-backup/latest/devguide/listing-backups.md#list-by-protected-resources "../../../aws-backup/latest/devguide/listing-backups.md#list-by-protected-resources") <br>• [Working with backups](../../../aws-backup/latest/devguide/recovery-points.md "../../../aws-backup/latest/devguide/recovery-points.md") |
