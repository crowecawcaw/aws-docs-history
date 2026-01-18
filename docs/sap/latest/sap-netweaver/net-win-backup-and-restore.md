# Backup and Restore

## Snapshots and AMIs

A common approach for backing up your SAP NetWeaver application servers is using snapshots and AMIs.

All your data is stored on Amazon EBS volumes attached to the SAP NetWeaver application servers. You can back up the data on these volumes to Amazon S3 by taking point-in-time snapshots. Snapshots are incremental backups of Amazon EBS volumes, which means that only the blocks on the device that have changed after your most recent snapshot are saved. For more details on this, see [Creating an Amazon EBS Snapshot.](../../../AWSEC2/latest/UserGuide/ebs-creating-snapshot.md "../../../AWSEC2/latest/UserGuide/ebs-creating-snapshot.md")

An Amazon Machine Image (AMI) provides the information required to launch an instance along with a block device mapping of all EBS volumes attached to it.

Amazon EC2 powers down the instance before creating the AMI to ensure that everything on the instance is stopped and in a consistent state during the creation process. If you’re confident that your instance is in a consistent state appropriate for AMI creation, you can check the No Reboot option.

To take application-consistent snapshots of all EBS volumes attached to your instance using Windows Volume Shadow Copy Service (VSS), see [Creating a VSS Application-Consistent Snapshot](../../../AWSEC2/latest/WindowsGuide/application-consistent-snapshots-creating-commands.md "../../../AWSEC2/latest/WindowsGuide/application-consistent-snapshots-creating-commands.md"). This allows you to create a copy of the image without rebooting the instance.

You can use [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/") to centrally configure backup policies and monitor backup activity for these snapshots.

After you have completed the SAP installation and post installation steps, you should create an image of the instance. AWS provides a very simple and quick way to copy an SAP system. You can use the AWS Management Console or the AWS CLI to create a new AMI of an existing SAP system. The new AMI contains a complete copy of the operating system and its configuration, software configurations, and all EBS volumes that are attached to the instance. From the new AMI, you can launch exact copies of the original system. For details on how to create an AMI of an existing EC2 instance, see [Creating a Custom Windows AMI](../../../AWSEC2/latest/WindowsGuide/Creating_EBSbacked_WinAMI.md "../../../AWSEC2/latest/WindowsGuide/Creating_EBSbacked_WinAMI.md").

Example:

```
  $ aws ec2 create-image --instance-id i-1234567890abcdef0
--name "My server" --description "An AMI for my server"
```

###### Note

When you build an instance using an AMI, make sure that you update the hostname and the `C:\Windows\System32\Drivers\etc\hosts` file with the new metadata. These details usually get copied from the source.

## File Backup to Amazon S3

You can perform traditional file-based backups from your EBS volumes to Amazon S3. One way to do this is by using the AWS CLI and trigger this using AWS Systems Manager Run Command so that you can centrally manage these.

## Third-party Options

There are many third-party backup products for AWS services, including many solutions that have been certified by SAP. For more information, see [AWS SAP Partner Solutions](https://aws.amazon.com/sap/partner-solutions/ "https://aws.amazon.com/sap/partner-solutions/").

## Amazon FSx Backup

With Amazon FSx, backups are file-system-consistent, highly durable, and incremental. To ensure file system consistency, Amazon FSx uses the Volume Shadow Copy Service (VSS) in Microsoft Windows. To ensure high durability, Amazon FSx stores backups in Amazon S3. Amazon FSx backups are incremental, which means that only the changes made after your most recent backup are saved.

Amazon FSx automatically takes backups of your file systems once a day. These daily backups are taken during the daily backup window that you established when you created the file system.

If you want to set up a custom backup schedule, you can [deploy our reference solution](../../../fsx/latest/WindowsGuide/custom-backup-schedule.md "../../../fsx/latest/WindowsGuide/custom-backup-schedule.md").
