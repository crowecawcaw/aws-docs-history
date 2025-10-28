# Backup drift in AWS Control Tower

Drift is not reported for AWS Backup configurations in AWS Control Tower. For more information about
drift in AWS Control Tower, see [Detect and resolve drift in
AWS Control Tower](drift.md "drift.md").

If you delete or modify the AWS Backup plan, your plan can enter a state of drift. Here are
some modifications to avoid.

- Do not move the **Backup Administrator** account from the
  Security OU.
- Do not move the **Central Backup** account from the Security
  OU.
- Do not remove the **Backup Administrator** account from the
  organization.
- Do not remove the **Central Backup** account from the
  organization.
- Do not detach, attach, or update the AWS Backup SCP that is applied to the Security
  OU.
- Do not detach, attach, or update the AWS Backup SCP that is applied to other
  OUs.
- Do not remove the **Backup Administrator** account's
  permission for AWS Backup.
- Do not update your cross-account backup settings to turn off cross-account
  backups. For more information about cross-account backups, see [`UpdateGlobalSettings`](../../../aws-backup/latest/devguide/API_UpdateGlobalSettings.md "../../../aws-backup/latest/devguide/API_UpdateGlobalSettings.md") in the _AWS Backup API
  Reference_.
- Do not delete your AWS KMS key.
- Do not modify your AWS KMS key policy after it is set.
- Do not disable the service's trusted access for AWS Backup.

###### Note

Drift is reported regarding the status of the SCP-based controls that protect
AWS Backup resources in AWS Control Tower.
