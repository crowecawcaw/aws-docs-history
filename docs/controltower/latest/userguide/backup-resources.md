# Resources created for AWS Backup

**The tables on this page show resources that are created in AWS Control Tower accounts
when you enable AWS Backup.**

The following table shows the resources that AWS Control Tower creates in the AWS Control Tower
**Central Backup** account when you enable AWS Backup for the landing zone
organization.

| **Description**                                      | **Resources for the Central Backup<br>account**                  |
| ---------------------------------------------------- | ---------------------------------------------------------------- |
| **Which OU contains the account?**                   | Security OU                                                      |
| **What action created the resource?**                | Landing zone **Create\*<br>• or<br>**Update\*\*                  |
| **What resources are created?**                      | Central Backup<br>vault—`aws-controltower-central-backupvault-*` |
| **What Regions are included?**                       | All governed Regions                                             |
| **What controls are related to these<br>resources?** | `CT.BACKUP.PV.3`                                                 |

The following table shows the resources that AWS Control Tower creates in the AWS Control Tower
**Backup Administrator** account when you enable AWS Backup for the landing
zone organization.

| **Description**                                      | **Resources for the Backup Administrator account:<br>This is the delegated administrator account for AWS Backup**                                                                                                                                                                                                                     |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Which OU contains the account?**                   | Security OU                                                                                                                                                                                                                                                                                                                           |
| **What action created the resource?**                | Landing zone **Create\*<br>• or<br>**Update\*\*                                                                                                                                                                                                                                                                                       |
| **What resources are created?**                      | Backup Audit Manager (BAM)<br>• `aws_controltower_copy_report`<br>• `aws_controltower_backup_report`<br>• `aws_controltower_restore_report`<br>Amazon S3 bucket for storing BAM<br>logs—`aws-controltower-backup-reports-`{accountId}`-*`<br>Amazon S3 access logging<br>bucket—`aws-controltower-backup-reports-log-`{accountId}`-*` |
| **What Regions are included?**                       | Home Region                                                                                                                                                                                                                                                                                                                           |
| **What controls are related to these<br>resources?** | • `CT.BACKUP.PV.2`<br>• `CT.S3.PV.1`<br>• `CT.S3.PV.1`                                                                                                                                                                                                                                                                                |

The following table shows the resources that AWS Control Tower creates in the AWS Control Tower
**Audit** account and in the AWS Control Tower **Log Archive**
account when you enable AWS Backup for the Security OU.

| **Description**                                      | **Resources for Audit and Log Archive<br>accounts**                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Which OU contains the account?**                   | Security OU                                                                                                                                                                                                                                                                                                                                                                                                           |
| **What action created the resource?**                | Enabling the `BackupBaseline`                                                                                                                                                                                                                                                                                                                                                                                         |
| **What resources are created?**                      | • Local Backup<br>vault—`aws-controltower-local-backupvault-*`<br>• Local Backup<br>role—`aws-controltower-BackupRole`<br>• Four local Backup plans (hourly, weekly, monthly,<br>daily)<br>+ `aws-controltower-hourly-backup-plan`<br>+ `aws-controltower-daily-backup-plan`<br>+ `aws-controltower-weekly-backup-plan`<br>+ `aws-controltower-monthly-backup-plan`<br>• An IAM<br>role—`aws-controltower-BackupRole` |
| **What Regions are included?**                       | All governed Regions                                                                                                                                                                                                                                                                                                                                                                                                  |
| **What controls are related to these<br>resources?** | • `CT.BACKUP.PV.3`<br>• `CT.IAM.PV.1`<br>• `CT.BACKUP.PV.3`<br>• `CT.BACKUP.PV.1`                                                                                                                                                                                                                                                                                                                                     |

###### Note

When you apply the `BackupBaseline` to the Security OU, all member
accounts in that OU receive the AWS Backup resources, not just the **Audit**
and **Log Archive** accounts.

The following table shows the resources that AWS Control Tower creates in the AWS Control Tower **OU
member accounts** when you enable AWS Backup on a target OU.

| **Description**                                      | **Resources for member accounts in other<br>OUs**                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Which OU contains the account?**                   | Any OU other than the Security OU                                                                                                                                                                                                                                                                                                                                                                                     |
| **What action created the resource?**                | Enabling the `BackupBaseline`                                                                                                                                                                                                                                                                                                                                                                                         |
| **What resources are created?**                      | • Local Backup<br>vault—`aws-controltower-local-backupvault-*`<br>• Local Backup<br>role—`aws-controltower-BackupRole`<br>• Four local Backup plans (hourly, weekly, monthly,<br>daily)<br>+ `aws-controltower-hourly-backup-plan`<br>+ `aws-controltower-daily-backup-plan`<br>+ `aws-controltower-weekly-backup-plan`<br>+ `aws-controltower-monthly-backup-plan`<br>• An IAM<br>role—`aws-controltower-BackupRole` |
| **What Regions are included?**                       | All governed Regions                                                                                                                                                                                                                                                                                                                                                                                                  |
| **What controls are related to these<br>resources?** | • `CT.BACKUP.PV.3`<br>• `CT.IAM.PV.1`<br>• `CT.BACKUP.PV.3`<br>• `CT.BACKUP.PV.1`                                                                                                                                                                                                                                                                                                                                     |
