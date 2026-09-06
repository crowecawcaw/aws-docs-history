

# Managing automatic backups of EFS file systems
<a name="automatic-backups"></a>

When you create a file system using the Amazon EFS console, automatic backups are turned on by default. You can turn on automatic backups after creating your file system using the AWS CLI or API. 

You can edit the default backup plan settings using the AWS Backup console. For more information, see [Managing backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html) in the *AWS Backup Developer Guide*. You can see all of your automatic backups, and edit the default EFS backup plan settings using the [AWS Backup console](https://console.aws.amazon.com/backup).

Amazon EFS applies the `aws:elasticfilesystem:default-backup` system tag key with a value of `enabled` to EFS file systems when automatic backups are enabled.

After you create a file system, you can turn automatic backups on or off using the console, the AWS CLI, or the EFS API.

## Using the console
<a name="enable-autobkp-console-efs"></a>

1. Open the Amazon Elastic File System console at [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/).

1. In the **File systems** page, choose the file system that you want to turn automatic backups on or off for and display the **File system details** page.

1. Choose **Edit** in the **General** settings panel.

1. 
   + To turn on automatic backups, select **Enable automatic backups**.
   + To turn off automatic backups, clear **Enable automatic backups**.

1. Choose **Save changes**.

## Using the AWS CLI
<a name="enable-autobkp-cli-efs"></a>
+ Use the `put-backup-policy` CLI command (the corresponding API operation is [PutBackupPolicy](https://docs.aws.amazon.com/efs/latest/APIReference/API_PutBackupPolicy.html)) turn automatic backups on or off for an existing file system.
  + Use the following command to turn on automatic backups.

    ```
    $ aws efs put-backup-policy --file-system-id fs-01234567 \
    --backup-policy Status="ENABLED"
    ```

    Amazon EFS responds with the new backup policy.

    ```
    {
       "BackupPolicy": { 
          "Status": "ENABLING"
       }
    }
    ```
  + Use the following command to turn off automatic backups.

    ```
    $ aws efs put-backup-policy --file-system-id fs-01234567 \
    --backup-policy Status="DISABLED"
    ```

    Amazon EFS responds with the new backup policy.

    ```
    {
       "BackupPolicy": { 
          "Status": "DISABLING"
       }
    }
    ```