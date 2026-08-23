# AWS Backup and AWS Control Tower

AWS Backup is a service that allows you to create plans for backing up your AWS resources
automatically. To set up backups for your AWS Control Tower resources, you must follow four main
steps:

1. Enable AWS Backup for your landing zone. You can do this on the **Landing zone
   settings** page in the AWS Control Tower console. When you turn on AWS Backup,
   resources are created in several accounts. For more information, see [Resources created for AWS Backup](backup-resources.md "backup-resources.md").
2. Opt-in to backups for AWS Control Tower in the AWS Backup console. For more information, see
   [Working with supported services](../../../aws-backup/latest/devguide/working-with-supported-services.md#opt-in "../../../aws-backup/latest/devguide/working-with-supported-services.md#opt-in") in the _AWS Backup Developer
   Guide_.
3. Enable AWS Backup on the individual OUs you wish to include. You can do this task on
   the **OU details** page in the console, after you've enabled AWS Backup
   at the landing zone level. When you enable AWS Backup on an OU, the accounts in that OU
   receive local AWS Backup vaults.
4. Tag the selected resources to include in the backups. The tag denotes the
   frequency of backups for that resource. Your backup plan follows the schedule
   specified by the resource tags on each resource.
   For more information, see [_The AWS Backup Developer
   Guide_](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md"). No cost is incurred when you configure AWS Backup with
   AWS Control Tower. You will incur cost from AWS Backup. For information about pricing, see [AWS Backup pricing](https://aws.amazon.com/backup/pricing/ "https://aws.amazon.com/backup/pricing/").

For more details about the AWS Backup resources that AWS Control Tower creates in your AWS Control Tower landing
zone, see [Resources created for AWS Backup](backup-resources.md "backup-resources.md")

###### Note

AWS Control Tower does not support setting up backup plans for AWS Control Tower resources through the
AWS Backup service directly, without also enabling it in the AWS Control Tower service.
