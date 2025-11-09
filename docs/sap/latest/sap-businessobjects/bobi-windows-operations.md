# Operations

## Tagging AWS Resources

A tag is a label that you assign to an AWS resource. Each tag consists of a *key* and an optional *value*, both of which you define. Adding tags to the various AWS resources will not only make managing your SAP environment much easier but can also be used to quickly search for resources. Many Amazon EC2 API calls can be used in conjunction with a special tag filter. See [AWS Tagging Strategies](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/ "https://aws.amazon.com/answers/account-management/aws-tagging-strategies/") and use it as a starting point to define the tags you need for your resources. Below are the examples on how you can use tags for operational needs:

- You can tag your EBS volumes to identify their environment (for example Environment= DEV/QAS/PRD etc.) and use these tags to create backup policies for EBS volumes
- You can use similar tags as in above example with EC2 instances and use them for patching your operating systems or running scripts to stop/start application or EC2 instances.

## Monitoring

AWS provides multiple native services to monitor and manage your SAP environment. You can use services like [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") to monitor your underlying infrastructure and APIs, respectively. CloudWatch provides ready-to-use KPIs for CPU and disk utilization, and also allows you to create custom metrics if your specific KPIs that you would like to monitor. CloudTrail allows you to log the API calls made to your AWS infrastructure components.

## Operating System Maintenance

In general, operating system maintenance across large estates of EC2 instances can be managed by:

- tools specific to each operating system such as Microsoft System Center
- third-party products such as those available on AWS Marketplace
- using AWS Systems Manager

Here we outline some key operating system maintenance tasks.

### Patching

You can follow SAP recommended patching processes to update your landscape on AWS. For operating system patching, with [AWS Systems Manager Patch Manager](../../../systems-manager/latest/userguide/systems-manager-patch.md "../../../systems-manager/latest/userguide/systems-manager-patch.md") you can roll out OS patches as per your corporate policies. There are multiple key features like:

- scheduling based on tags
- auto-approving patches with lists of approved and rejected patches
- defining patch baselines

AWS Systems Manager Patch Manager integrates with AWS Identity and Access Management (IAM), AWS CloudTrail, and Amazon CloudWatch Events to provide a secure patching experience that includes event notifications and the ability to audit usage. For details about the process, see [How Patch Manager Operations Work](../../../systems-manager/latest/userguide/patch-manager-how-it-works.md "../../../systems-manager/latest/userguide/patch-manager-how-it-works.md"). If AWS Systems Manager Patch Manager does not fulfill your requirements, there are third-party products available as well. Some of these are available via the [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").

### Maintenance Window

[AWS Systems Manager Maintenance Windows](../../../systems-manager/latest/userguide/systems-manager-maintenance.md "../../../systems-manager/latest/userguide/systems-manager-maintenance.md") let you define a schedule for when to perform potentially disruptive actions on your instances such as patching an operating system, updating drivers, or installing software or patches.

### Administrator Access

You can access the backend SAP systems for administration purposes in a number of ways:

- AWS Systems Manager Session Manager
- Remote Desktop Protocol
- SSH

## Backup and Restore

### Snapshots and AMIs

A common approach for backing up your SAP NetWeaver application servers is using snapshots and AMIs.

All your data is stored on Amazon EBS volumes attached to the SAP NetWeaver application servers. You can back up the data on these volumes to Amazon S3 by taking point-in-time snapshots. Snapshots are incremental backups of Amazon EBS volumes, which means that only the blocks on the device that have changed after your most recent snapshot are saved. For more details on this, see [Creating an Amazon EBS Snapshot.](../../../AWSEC2/latest/UserGuide/ebs-creating-snapshot.md "../../../AWSEC2/latest/UserGuide/ebs-creating-snapshot.md")

An Amazon Machine Image (AMI) provides the information required to launch an instance along with a block device mapping of all EBS volumes attached to it.

Amazon EC2 powers down the instance before creating the AMI to ensure that everything on the instance is stopped and in a consistent state during the creation process. If you’re confident that your instance is in a consistent state appropriate for AMI creation, you can select the **No Reboot** option. You can use the AWS Systems Manager Run Command to take [application-consistent snapshots of all EBS volumes](../../../AWSEC2/latest/UserGuide/application-consistent-snapshots.md "../../../AWSEC2/latest/UserGuide/application-consistent-snapshots.md") attached to your instance using Windows Volume Shadow Copy Service (VSS) to make it safe to create the image without rebooting the instance.

You can use [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/") to centrally configure backup policies and monitor backup activity for these snapshots.

Once you have completed the SAP installation and post installation steps, you should create an image of the instance. AWS provides a very simple and quick way to copy an SAP system. You can use the AWS Management Console or the AWS CLI to create a new AMI of an existing SAP system. The new AMI contains a complete copy of the operating system and its configuration, software configurations, and all EBS volumes that are attached to the instance. From the new AMI you can launch exact copies of the original system. For more information, see [Creating an Amazon EBS Backed Windows AMI.](../../../AWSEC2/latest/WindowsGuide/Creating_EBSbacked_WinAMI.md "../../../AWSEC2/latest/WindowsGuide/Creating_EBSbacked_WinAMI.md")

Syntax:

```
aws ec2 create-image --instance-id i-1234567890abcdef0 --name "My server" --description "An AMI for my server"
```

###### Note

When you build an instance using an AMI, make sure you update the hostname and the `c:\Windows\System32\Drivers\etc\hosts` file with the new metadata. These details usually get copied from the source.

### File Backup to S3

You can perform traditional file-based backups to Amazon S3 from your EBS volumes. One way to do this is by using the AWS CLI and trigger this using AWS Systems Manager Run Command so that you can centrally manage these.

### Third-Party Options

There are many third-party backup products for AWS services, including a number that have been certified by SAP. For more information, see [AWS SAP Partner Solutions](https://aws.amazon.com/sap/partner-solutions/ "https://aws.amazon.com/sap/partner-solutions/").

### Amazon FSx Backup

With Amazon FSx, backups are file-system-consistent, highly durable, and incremental. To ensure file system consistency, Amazon FSx uses the Volume Shadow Copy Service (VSS) in Microsoft Windows. To ensure high durability, Amazon FSx stores backups in Amazon Simple Storage Service (Amazon S3). Amazon FSx backups are incremental, which means that only the changes after your most recent backup are saved.

Amazon FSx automatically takes backups of your file systems once a day. These daily backups are taken during the daily backup window that was established when you created the file system.

If you want to set up a custom backup schedule, you can [deploy our reference solution](../../../fsx/latest/WindowsGuide/custom-backup-schedule.md "../../../fsx/latest/WindowsGuide/custom-backup-schedule.md").

### Backing up SAP BOBI Platform

Backup of SAP BOBI should protect the following components. The backup of CMS database and FileStore should be taken at the same time to maintain consistency.

- CMS Database (Amazon RDS or Database on EC2)
- FileStore (Amazon FSx for multi-node install or Amazon EBS for standalone install)
- SAP BOBI installation directory

You can choose from following options for backup.

- For Amazon FSx, you can schedule the backups. For details, see [Working with Backups](../../../fsx/latest/WindowsGuide/using-backups.md "../../../fsx/latest/WindowsGuide/using-backups.md").
- When using Amazon RDS for CMS database and Windows operating system for application, you can use AWS Backup for Amazon EBS and database backups. AWS Backup is a fully managed backup service that makes it easy to centralize and automate the back up of data across AWS services in the cloud. You can configure backup policies based on tags from a central backup console, simplifying backup management and making it easy to ensure that your application data is backed up and protected. You can put database, FileStore, and installation directory resources in same policy to ensure consistency.
- When using Amazon RDS for CMS database and Windows operating system for application, you can use [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/") service for the backup of Amazon RDS and SAP BOBI Installation directory.
- You can use supported third-party backup tools that provide database and file system agents for backup and recovery of all SAP BOBI platform component.
- If the preceding AWS services and tools do not meet your requirements, you can also use standard database backup tools and scripts to create database backups, file system backups and EBS snapshots. Database and file system backups can be stored on an EBS volume attached to your database and application EC2 instances. For better durability and agility, we recommend that you move your backups to Amazon S3. Based on your business continuity and compliance requirements, you can choose to move your backups to Amazon S3 Glacier and use Amazon S3 Lifecycle policies. For details, see [How Do I Create a Lifecycle Policy for an S3 Bucket?](../../../AmazonS3/latest/user-guide/create-lifecycle.md "../../../AmazonS3/latest/user-guide/create-lifecycle.md"). Amazon S3 Lifecycle policies also let you delete older backups based on your backup retention requirements.
- If you use SAP HANA as the database for CMS, you can use AWS Backint Agent for SAP HANA to backup your data to Amazon S3. For more information, see [AWS Backint Agent for SAP HANA](../sap-hana/aws-backint-agent-sap-hana.md "../sap-hana/aws-backint-agent-sap-hana.md").

### Recovering the SAP BOBI Platform

The backups that you choose for the restore of CMS database and FileStore should have been created at the same time to maintain consistency. You can recover a database to a point-in-time using log files, but Amazon EFS (used for FileStore) does not have similar capabilities. In this case, recovering a database to most recent state but FileStore to an older state may cause inconsistencies between the two.

Based on the backup strategy, the following are options for restore.

- When you restore a backup in AWS Backup, a new resource is created based on the backup that you are restoring. Depending on the component that you restore, you can point you SAP BOBI Platform installation to the new resource or copy data to the original resource. For example, you can restore Amazon FSx and Amazon EBS on a different file system or EBS volume. After you have the new resource available, you can either copy a subset of the data or replace your original resource with the new one. See [Restoring a Backup](../../../aws-backup/latest/devguide/restoring-a-backup.md "../../../aws-backup/latest/devguide/restoring-a-backup.md") for details.
- When restoring using third-party software, refer to vendor- and application-specific documentation.
- If you are restoring from Amazon S3 using custom scripts, you will have to restore the backup to an EBS volume, and then use either database specific tools or native operating system features to restore your data back to SAP BOBI Platform installation.

## Compute

EBS volumes are exposed as NVMe block devices on [Nitro-based instances](../../../AWSEC2/latest/WindowsGuide/instance-types.md#ec2-nitro-instances "../../../AWSEC2/latest/WindowsGuide/instance-types.md#ec2-nitro-instances"). When changing EC2 instance types from a previous generation to a Nitro generation, if using a Windows Server 2008 R2 or later Windows AMI, the AWS NVMe driver is already included as per the [Amazon EBS and NVMe documentation](../../../AWSEC2/latest/WindowsGuide/nvme-ebs-volumes.md "../../../AWSEC2/latest/WindowsGuide/nvme-ebs-volumes.md"). If you are not using the latest AWS Windows AMIs provided by Amazon, see [Installing or Upgrading AWS NVMe Drivers](../../../AWSEC2/latest/WindowsGuide/aws-nvme-drivers.md#install-nvme-drivers "../../../AWSEC2/latest/WindowsGuide/aws-nvme-drivers.md#install-nvme-drivers").

Aside from operating system maintenance, there is also maintenance you can consider for EC2 instances themselves. This can be driven via AWS Systems Manager Automation documents. Some examples of this are:

- Use the `**AWS-StopEC2InstanceWithApproval**` document to request that one or more IAM users approve the instance stop action. After the approval is received, Automation stops the instance.
- Use the `**AWS-StopEC2Instance**` document to automatically stop instances on a schedule by using Amazon CloudWatch Events or by using a Maintenance Window task. For example, you can configure an Automation workflow to stop instances every Friday evening, and then restart them every Monday morning.
- Use the `**AWS-UpdateCloudFormationStackWithApproval**` document to update resources that were deployed by using AWS CloudFormation template. The update applies a new template. You can configure the Automation to request approval by one or more IAM users before the update begins.

Finally, use the [AWS Instance Scheduler](https://aws.amazon.com/solutions/instance-scheduler/ "https://aws.amazon.com/solutions/instance-scheduler/") Solution to easily configure custom start and stop schedules for their Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Relational Database Service (Amazon RDS) instances.

## Cost Optimization

Just as with right sizing, we recommend customers make cost optimization an ongoing process. This is an extensive topic with many AWS services that help with budgeting, cost control and proactive cost optimization recommendations.

For more details, see the [https://d1.awsstatic.com/whitepapers/architecture/](https://d1.awsstatic.com/whitepapers/architecture/ "https://d1.awsstatic.com/whitepapers/architecture/")
AWS-Cost-Optimization-Pillar.pdf[Cost Optimization Pillar] of the AWS Well-Architected Framework and the [SAP on AWS Pricing and Optimization Guide](../general/sap-on-aws-pricing-guide.md "../general/sap-on-aws-pricing-guide.md").

## Automation

### Automation using Infrastructure as Code with AWS CloudFormation

We recommend following the principle of Infrastructure as code (IaC) in automating and maintaining your workloads on AWS. [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") provides a common language for you to describe and provision all the infrastructure resources in your cloud environment in a repeatable and automated manner, and thus follow the principle of IaC.

### Automation using Documents

[AWS Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md") simplifies common maintenance and deployment tasks of Amazon EC2 instances and other AWS resources. Automation enables you to do the following:

- Build Automation workflows to configure and manage instances and AWS resources.
- Create custom workflows or use pre-defined workflows maintained by AWS.
- Receive notifications about Automation tasks and workflows by using Amazon CloudWatch Events.
- Monitor Automation progress and execution details by using the Amazon EC2 or the AWS Systems Manager console.

There are many AWS-provided documents specific to Windows already available.

## Integration with AWS Big Data Services

The SAP BOBI Platform product can use multiple AWS Big Data services as data sources for reporting purposes. When using SAP BOBI version 4.2, you can connect to the following AWS data sources:

| Table 2: AWS Big Data services support for SAP BusinessObjects Business Intelligence 4.2 | Use Case                    | Amazon Product | SAP BOBI 4.2 Supported |
| ---------------------------------------------------------------------------------------- | --------------------------- | -------------- | ---------------------- |
| Data source                                                                              | Amazon RDS Oracle           | Yes            |
| Data source                                                                              | Amazon Redshift             | Yes            |
| Data source                                                                              | Amazon EMR Hive (Hive1)     | Yes            |
| Data source                                                                              | Amazon EMR Hive (Hive2)     | Yes            |
| Data source                                                                              | Amazon EMR Hive 5.6 (Hive2) | Yes            |

See the [SAP Product Availability Matrix (PAM)](https://support.sap.com/pam "https://support.sap.com/pam") for the complete list of SAP BOBI Platform supported data sources specific to your version.
