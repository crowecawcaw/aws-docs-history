

# Restoring a continuous backup
<a name="point-in-time-recovery-restoring"></a>

**To restore a continuous backup using the AWS Backup console**
+ During the PITR restore process, the AWS Backup console displays a **Restore time** section. In this section, do one of the following:
  + Choose to restore to the **Latest restorable time**.
  + Choose **Specify date and time** to enter your own date and time within your retention period.

**To restore a continuous backup using the AWS Backup API**

1. For Amazon S3 see [ Use the AWS Backup API, CLI, or SDK to restore S3 recovery points](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-s3.html).

1. For Amazon RDS see [ Use the AWS Backup API, CLI, or SDK to restore Amazon RDS recovery points](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-rds.html).