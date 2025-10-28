# Backup & restore

## Snapshots and AMIs

A common approach for backing up your SAP NetWeaver application servers is using snapshots and AMIs.

The SAP application data is stored on Amazon EBS volumes attached to the SAP NetWeaver application servers. You can back up the data on these volumes to Amazon S3 by taking point-in-time snapshots. Snapshots are incremental backups of Amazon EBS volumes, which means that only the blocks on the device that have changed after your most recent snapshot are saved. For more information, see [Create Amazon EBS snapshots](../../../AWSEC2/latest/UserGuide/ebs-creating-snapshot.md "../../../AWSEC2/latest/UserGuide/ebs-creating-snapshot.md").

An Amazon Machine Image (AMI) provides the information required to launch an instance along with a block device mapping of all Amazon EBS volumes attached to it.

Amazon EC2 powers down the instance before creating the AMI to ensure that everything on the instance is stopped and in a consistent state during the creation process. If you’re confident that your instance is in a consistent state appropriate for AMI creation, you can check the _No Reboot_ option.

You can use [AWS Backup](https://aws.amazon.com/backup "https://aws.amazon.com/backup") to centrally configure backup policies and monitor backup activity for these snapshots. Once you have completed the SAP installation and post-installation steps, create an image of the instance.

```
aws ec2 create-image --instance-id i-1234567890abcdef0 --name "My server" --description "An AMI for my server"
```

AWS provides a very simple and quick way to copy an SAP system. You can use the [AWS Console Home](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2") or the AWS CLI to create a new AMI of an existing SAP system. You can then launch exact copies of the original system from the new AMI. For more details, see [Amazon Machine Images (AMI)](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md").

## Backup to Amazon S3

You can perform traditional file-based backup to Amazon S3 from your Amazon EBS volumes. One way to take backup is to use AWS CLI and initiate it by using AWS Systems Manager `Run` command, so that you can centrally manage the backups.

## Backup with third-party products

Many third-part products for AWS services are certified by SAP. For more information, see [AWS SAP Competency Partners](https://aws.amazon.com/sap/partner-solutions/ "https://aws.amazon.com/sap/partner-solutions/").

## Amazon EFS backup

Using AWS Backup, you can centrally configure backup policies and monitor backup activity for AWS resources, including Amazon EFS file systems.

Alternatively, you can perform a file-level backup of your Amazon EFS file system to Amazon S3. You can do this by running a file-level copy to Amazon S3 from any Amazon EC2 instance running in the same region. This can be automated and scheduled using [AWS Systems Manager Run Command](../../../systems-manager/latest/userguide/execute-remote-commands.md "../../../systems-manager/latest/userguide/execute-remote-commands.md") in combination with CloudWatch Events.

## Backup and restore for ASE database

You must to regularly backup your operating system and database to recover them in case of any failure. AWS Cloud provides various services and tools that you can use to backup your SAP ASE database.

### Storage snapshots

You can backup your Amazon EBS volumes to Amazon S3 by taking point-in-time snapshots. Snapshots are incremental backups, which means that only blocks on the device that have changed after your most recent snapshot are saved. Snapshots of Amazon EBS volumes can be created for backup of SAP ASE database file systems.

See [How to use snapshots to create an automated recovery procedure for SAP ASE databases](https://aws.amazon.com/blogs/awsforsap/how-to-use-snapshots-to-create-an-automated-recovery-procedure-for-sap-ase-databases/ "https://aws.amazon.com/blogs/awsforsap/how-to-use-snapshots-to-create-an-automated-recovery-procedure-for-sap-ase-databases/") to learn more.

### SAP ASE database backups

You can configure your SAP ASE database to store backups on Amazon EFS or local Amazon EBS volumes. You must configure regular backups for Amazon EFS. For more information, see [Backing up your Amazon EFS file systems](../../../efs/latest/ug/efs-backup-solutions.md "../../../efs/latest/ug/efs-backup-solutions.md"). You can reduce costs by enabling Amazon EFS storage classes to retain cold backups in infrequent access. For more information, see [Amazon EFS Infrequent Access](https://aws.amazon.com/efs/features/infrequent-access/ "https://aws.amazon.com/efs/features/infrequent-access/").

You can also configure backups to be store on Amazon EFS volumes and to be regularly uploaded to Amazon S3. Use `DBACOCKPIT` to schedule backup frequency. You can also use [AWS Systems Manager Maintenance Windows](../../../systems-manager/latest/userguide/systems-manager-maintenance.md "../../../systems-manager/latest/userguide/systems-manager-maintenance.md") to schedule backup frequency.

Amazon SNS enables you to setup push notifications for success or failure. Once backups are stored in Amazon S3, you can use lifecycle policies to define data retention timeline. For more information, see [Managing your storage lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md").

You can improve Amazon S3 data upload performance with Gateway endpoints and AWS CLI. For more information, see [Gateway endpoints for Amazon S3](../../../vpc/latest/privatelink/vpc-endpoints-s3.md "../../../vpc/latest/privatelink/vpc-endpoints-s3.md") and [AWS CLI S3 Configuration](../../../cli/latest/topic/s3-config.md "../../../cli/latest/topic/s3-config.md").

Review the following SAP Notes (portal access required) for more details.

- [SAP Note 1585981 - SYB: Ensuring Recoverability for SAP ASE](https://launchpad.support.sap.com/#/notes/1585981 "https://launchpad.support.sap.com/#/notes/1585981")
- [SAP Note 1887068 - SYB: Using external backup and restore with SAP ASE](https://launchpad.support.sap.com/#/notes/1887068 "https://launchpad.support.sap.com/#/notes/1887068")
- [SAP Note 1588316 - SYB: Configure automatic database and log backups](https://launchpad.support.sap.com/#/notes/1588316 "https://launchpad.support.sap.com/#/notes/1588316")
- [SAP Note 1618817 - SYB: How to restore an SAP ASE database server (UNIX)](https://launchpad.support.sap.com/#/notes/1618817 "https://launchpad.support.sap.com/#/notes/1618817")

To use third-party tools to backup your SAP ASE database, see [AWS Storage Competency Partners](https://aws.amazon.com/backup-recovery/partner-solutions "https://aws.amazon.com/backup-recovery/partner-solutions").
