# Restoring a backup of a DynamoDB table from AWS Backup

This section describes how to restore a backup of a DynamoDB table from AWS Backup.

######

- [Restoring a DynamoDB table from AWS Backup](#Restore.TutorialAWS.simple "#Restore.TutorialAWS.simple")
- [Restoring a DynamoDB table to another Region or account](#Restore.TutorialAWS.another "#Restore.TutorialAWS.another")

## Restoring a DynamoDB table from AWS Backup

To restore your DynamoDB tables from AWS Backup, follow these steps:

1. Sign in to the AWS Management Console and open the DynamoDB console at
   [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/")
2. In the navigation pane on the left side of the console, choose **Tables.**
3. Choose the **Backups** tab.
4. Select the check box next to the previous backup that you want to restore from.
5. Choose **Restore**. You will be taken to the **Restore table from backup** screen.
6. Enter the name for the newly restored table, the encryption that this new table will have, the key you want
   the restore to be encryped with, and other options.
7. When you're finished, choose **Restore.**

## Restoring a DynamoDB table to another Region or account

To restore a DynamoDB table to another Region or account, you will first need to copy the backup to that new Region or account.
In order to copy to another account, that account must first grant you permission. After you have copied your DynamoDB
backup to the new Region or account, it can be restored with the process in the previous section.
