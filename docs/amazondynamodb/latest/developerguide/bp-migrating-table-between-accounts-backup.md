

# Migrate a table using AWS Backup for cross-account backup and restore
<a name="bp-migrating-table-between-accounts-backup"></a>

**Prerequisites**
+ Source and target AWS accounts must belong to the same organization in the AWS Organizations service
+ Valid AWS Identity and Access Management (IAM) permissions to create and use AWS Backup vaults

For more information about setting up cross-account backups, see [Creating backup copies across AWS accounts](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-cross-account-backup.html).

**Pricing information**

AWS charges for the backup (based on the table size), any data copying between AWS Regions (based on the amount of data), for the restore (based on the amount of data), and for any ongoing storage charges. To avoid ongoing charges, you can delete the backup if you don't need it after the restore.

For more information about pricing, see [AWS Backup pricing](https://aws.amazon.com/backup/pricing/) .

## Step 1: Enable advanced features for DynamoDB and cross-account backup
<a name="bp-migrating-table-between-accounts-backup-enable-advanced-features"></a>

1. In both the source and target AWS account, access the AWS Management Console and open the AWS Backup console.

1. Choose the **Settings** option.

1. Under **Advanced features for Amazon DynamoDB backups**, confirm that **Advanced features** is enabled. If it isn't, choose **Enable**.

1. Under **Cross-account management**, for **Cross-account backup**, choose **Turn On**.

## Step 2: Create a backup vault in the source account and target account
<a name="bp-migrating-table-between-accounts-backup-create-backup-vault"></a>

1. In the source AWS accounts, open the AWS Backup console.

1. Choose **Backup vaults**.

1. Choose **Create Backup vault**.

1. Copy and save the **Amazon Resource Name (ARN)** of the created backup vaults and the target AWS account.

1. You'll need the ARNs of both the source and target backup vaults when copying the DynamoDB table backup between accounts.

## Step 3: Create a DynamoDB table backup in the source account
<a name="bp-migrating-table-between-accounts-backup-create-table-backup"></a>

1. On the **AWS Backup Dashboard page**, choose **Create on-demand backup**.

1. In the **Settings** section, select **DynamoDB** as the **Resource type**, and then select the table name. 

1. In the **Backup vault** dropdown list, select the backup vault you created in the source account.

1. Select the desired **Retention period**.

1. Choose **Create on-demand backup**.

1. Monitor the status of the backup job on the **Backup Jobs** tab of the **AWS Backup Jobs** page. 

## Step 4: Copy the DynamoDB table backup from the source account to the target account
<a name="bp-migrating-table-between-accounts-backup-copy-table-backup"></a>

1. After the backup job completes, open the AWS Backup console in the source account and choose **Backup vaults**. 

1. Under **Backups**, choose the DynamoDB table backup. Choose **Actions** and then **Copy**.

1. Enter the AWS Region of the target account.

1. For **External vault ARN**, enter the ARN of the backup vault you created in the target account.

1.  In the target account backup vault, enable access from a source account to allow copying backups.

## Step 5: Restore the DynamoDB table backup in the target account
<a name="bp-migrating-table-between-accounts-restore-table-backup"></a>

1. In the target AWS account, open the AWS Backup console and choose **Backup vaults**

1. Under **Backups**, select the backup you copied from the source account. Choose **Actions**, then **Restore**.

1. Enter the name for the new DynamoDB table, the encryption that this new table will have, the key you want the restore to be encrypted with, and any other options.

1. When the restore is completed, the table status will show as **Active**.