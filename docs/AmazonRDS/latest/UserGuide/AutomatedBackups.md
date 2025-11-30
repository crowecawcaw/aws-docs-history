# Using AWS Backup to manage automated backups for Amazon RDS

AWS Backup is a fully managed backup service that makes it easy to centralize and automate
the backup of data across AWS services in the cloud and on premises. You can manage
backups of your Amazon RDS databases in AWS Backup.

###### Note

Backups managed by AWS Backup are considered manual DB snapshots, but don't count toward the DB snapshot quota for
RDS. Backups that were created with AWS Backup have names ending in `awsbackup:`backup-job-number``.

For more information about AWS Backup, see the [_AWS Backup Developer Guide_](../../../aws-backup/latest/devguide.md "../../../aws-backup/latest/devguide.md").

###### To view backups managed by AWS Backup

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. Choose the **Backup service** tab.

Your AWS Backup backups are listed under **Backup service snapshots**.
