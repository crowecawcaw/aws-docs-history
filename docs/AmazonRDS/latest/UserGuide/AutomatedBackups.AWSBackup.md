

# Using AWS Backup to manage automated backups for Amazon RDS
<a name="AutomatedBackups.AWSBackup"></a>

AWS Backup is a fully managed backup service that makes it easy to centralize and automate the backup of data across AWS services in the cloud and on premises. You can manage backups of your Amazon RDS databases in AWS Backup.

**Note**  
Backups managed by AWS Backup are considered manual DB snapshots, but don't count toward the DB snapshot quota for RDS. Backups that were created with AWS Backup have names ending in `awsbackup:{{backup-job-number}}`.

For more information about AWS Backup, see the [*AWS Backup Developer Guide*](https://docs.aws.amazon.com/aws-backup/latest/devguide).

**To view backups managed by AWS Backup**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Snapshots**.

1. Choose the **Backup service** tab.

   Your AWS Backup backups are listed under **Backup service snapshots**.