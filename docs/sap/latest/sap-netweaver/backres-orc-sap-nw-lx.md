# Backup & restore

## Snapshots and AMIs

A common approach for backing up your SAP NetWeaver application servers is using snapshots and AMIs.

The SAP application data is stored on Amazon EBS volumes attached to the SAP NetWeaver application servers. You can backup the data on these volumes to Amazon S3 by taking point-in-time snapshots. Snapshots are incremental backups of Amazon EBS volumes, which means that only the blocks on the device that have changed after your most recent snapshot are saved. For more information, see [Create Amazon EBS snapshots](../../../AWSEC2/latest/UserGuide/ebs-creating-snapshot.md "../../../AWSEC2/latest/UserGuide/ebs-creating-snapshot.md").

An Amazon Machine Image (AMI) provides the information required to launch an instance along with a block device mapping of all Amazon EBS volumes attached to it.

Amazon EC2 powers down the instance before creating the AMI to ensure that everything on the instance is stopped and in a consistent state during the creation process. If you’re confident that your instance is in a consistent state appropriate for AMI creation, you can check the _No Reboot_ option.

You can use [AWS Backup](https://aws.amazon.com/backup "https://aws.amazon.com/backup") to centrally configure backup policies and monitor backup activity for these snapshots. Once you have completed the SAP installation and post installation steps, create an image of the instance.

-

```
aws ec2 create-image --instance-id i-1234567890abcdef0 --name "My server" --description "An AMI for my server"
```

AWS provides a very simple and quick way to copy an SAP system. You can use the AWS Console Home or the AWS CLI to create a new AMI of an existing SAP system. You can then launch exact copies of the original system from the new AMI. For more details, see [Amazon Machine Images (AMI)](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md").

## Backup to Amazon S3

You can perform traditional file-based backup to Amazon S3 from your Amazon EBS volumes. One way to take backup is to use AWS CLI and initiate it by using AWS Systems Manager `Run` command, so that you can centrally manage the backups.

## Backup with third-party products

There are many third-party products for AWS services, including a number that have been certified by SAP. Go to [SAP Partner Services and Solutions Directory](http://aws-sap-partners.s3-website-us-east-1.amazonaws.com/ "http://aws-sap-partners.s3-website-us-east-1.amazonaws.com/"), select **ISV Solutions** in _Service/Solution Type_, then **Backup and Recovery** in _Software Solution_.

## Amazon EFS backup

Using AWS Backup, you can centrally configure backup policies and monitor backup activity for AWS resources, including Amazon EFS file systems.

Alternatively, you can perform a file-level backup of your Amazon EFS file system to Amazon S3. You can do this by running a file-level copy to Amazon S3 from any Amazon EC2 instance running in the same region. This can be automated and scheduled using [AWS Systems Manager Run Command](../../../systems-manager/latest/userguide/execute-remote-commands.md "../../../systems-manager/latest/userguide/execute-remote-commands.md") in combination with CloudWatch Events.

## Backup and restore for Oracle database

You must to regularly backup your operating system and database to recover them in case of any failure. AWS Cloud provides various services and tools that you can use to backup your Oracle database.

**Storage snapshots**

You can backup your Amazon EBS volumes to Amazon S3 by taking point-in-time snapshots. Snapshots are incremental backups, which means that only blocks on the device that have changed after your most recent snapshot are saved. Snapshots of Amazon EBS volumes can be created for backup of Oracle database file systems like Oracle home and stage directories.

For complete Oracle database file backups using snapshots, you can use the Storage Snapshots Optimization feature by Oracle, supported from version 12c. For more details, see [Making Backups with Third-Party Snapshot Technologies](https://docs.oracle.com/database/121/BRADV/osbackup.htm#BRADV90019 "https://docs.oracle.com/database/121/BRADV/osbackup.htm#BRADV90019"). AWS customers can use this feature in combination with [Amazon EBS snapshots](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md") to perform Oracle database backups. Using snapshot backups may reduce the backup window as compared to the full database backup approach. To set up snapshot-based based database backup, you can use sample scripts and steps published in the blog [Improving Oracle backup and recovery performance with Amazon EBS multi-volume crash-consistent snapshots](https://aws.amazon.com/blogs/database/improving-oracle-backup-and-recovery-performance-with-amazon-ebs-multi-volume-crash-consistent-snapshots/ "https://aws.amazon.com/blogs/database/improving-oracle-backup-and-recovery-performance-with-amazon-ebs-multi-volume-crash-consistent-snapshots/").

**Oracle database backups**

Any one of the following methods can be used for Oracle database backup.

- Oracle database native tools (BRTOOLS) can be used to take backups on local storage. Once the backup is complete on local storage, it can be moved to Amazon S3 bucket via scripts.
- Oracle Secure Backup Cloud Module to backup your database directly to Amazon S3 using RMAN. For setup, see [Oracle Database Backup To Cloud: Amazon Simple Storage Service (S3)](https://www.oracle.com/technetwork/database/features/availability/twp-oracledbcloudbackup-130129.pdf "https://www.oracle.com/technetwork/database/features/availability/twp-oracledbcloudbackup-130129.pdf"). For licence requirements, see [Oracle Secure Backup Licensing Information](https://docs.oracle.com/cd/E55822_01/OBLIC/E21478-04.pdf "https://docs.oracle.com/cd/E55822_01/OBLIC/E21478-04.pdf").
- You can backup your Amazon EBS volumes to Amazon S3 by taking point-in-time snapshots. For more information, see the preceding Storage snapshots section.
- There are many third-party tools from partner like Commvault, NetBackup, etc. that use the SAP backint interface and have Oracle database agents, with the capability to backup the database directly to Amazon S3.

To configure and tune backups for your Oracle database, see [SAP on Oracle – Backup and Recovery](https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=448466928 "https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=448466928") and [Database Backup and Recovery User’s Guide - Tuning RMAN Performance](https://docs.oracle.com/database/121/BRADV/rcmtunin.htm#BRADV011 "https://docs.oracle.com/database/121/BRADV/rcmtunin.htm#BRADV011").
