# Managing automatic backups of EFS file

systems

When you create a file system using the Amazon EFS console, automatic backups are turned on by
default. You can turn on automatic backups after creating your file system using the AWS CLI or
API.

You can edit the
default backup plan settings using the AWS Backup console. For more information, see [Managing backup plans](../../../aws-backup/latest/devguide/about-backup-plans.md "../../../aws-backup/latest/devguide/about-backup-plans.md") in the
_AWS Backup Developer Guide_. You can see
all of your automatic backups, and edit the default EFS backup plan settings using the [AWS Backup console](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").

Amazon EFS applies the `aws:elasticfilesystem:default-backup` system tag key with a value of `enabled` to
EFS file systems when automatic backups are enabled.

After you create a file system, you can turn automatic backups on or off using the console,
the AWS CLI, or the EFS API.

1. Open the Amazon Elastic File System console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. In the **File systems** page, choose the file system that you want to turn automatic backups on or off for and display the **File system details** page.
3. Choose **Edit** in the **General** settings panel.
4. - To turn on automatic backups, select **Enable automatic
     backups**.
   - To turn off automatic backups, clear **Enable automatic
     backups**.
5. Choose **Save changes**.

- Use the `put-backup-policy` CLI command (the corresponding API operation is
  [PutBackupPolicy](API_PutBackupPolicy.md "API_PutBackupPolicy.md")) turn automatic backups on or off
  for an existing file system.
  - Use the following command to turn on automatic backups.

  ```
  `$` aws efs put-backup-policy --file-system-id fs-01234567 \
  --backup-policy Status="ENABLED"
  ```

  Amazon EFS responds with the new backup policy.

  ```
  `{
   "BackupPolicy": {
   "Status": "ENABLING"
   }
  }`
  ```

  - Use the following command to turn off automatic backups.

  ```
  `$` aws efs put-backup-policy --file-system-id fs-01234567 \
  --backup-policy Status="DISABLED"
  ```

  Amazon EFS responds with the new backup policy.

  ```
  `{
   "BackupPolicy": {
   "Status": "DISABLING"
   }
  }`
  ```
