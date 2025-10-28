# Controls for AWS Backup

When you enable AWS Backup in your AWS Control Tower landing zone, some preventive controls are
activated in your environment. These controls protect the resources that AWS Backup needs to
operate with AWS Control Tower. You cannot enable these controls if AWS Backup is not enabled for your
landing zone.

###### Topics

- [[CT.BACKUP.PV.1] Disallow modification of a tag that AWS Control Tower applies to AWS Backup resources](ct-backup-pv-1.md "ct-backup-pv-1.md")
- [[CT.BACKUP.PV.2] Disallow modification of an AWS Backup report plan that AWS Control Tower manages](ct-backup-pv-2.md "ct-backup-pv-2.md")
- [[CT.BACKUP.PV.3] Disallow modification of an AWS Backup resource that AWS Control Tower manages](ct-backup-pv-3.md "ct-backup-pv-3.md")
- [[CT.IAM.PV.1] Disallow modification of an AWS IAM role that AWS Control Tower utilizes to manage AWS Backup resources](ct-iam-pv-1.md "ct-iam-pv-1.md")
- [[CT.S3.PV.1] Disallow modification of an Amazon S3 bucket that stores AWS Backup reports for AWS Control Tower](ct-s3-pv-1.md "ct-s3-pv-1.md")
