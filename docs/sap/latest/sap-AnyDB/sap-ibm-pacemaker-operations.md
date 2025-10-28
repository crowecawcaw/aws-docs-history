# Operations

In this section we will cover some of the native AWS services that help you with day-to-day operations of your IBM Db2 database for SAP applications.

## Monitoring

AWS provides multiple native services to monitor and manage your infrastructure and applications on AWS. Services like [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") can be leveraged to monitor your underlying infrastructure and APIs, respectively.

CloudWatch provides ready-to-use key performance indicators (KPIs) that you can use to monitor CPU utilization and disk utilization.

You can also create [custom metrics](https://aws.amazon.com/blogs/database/monitor-your-microsoft-sql-server-using-custom-metrics-with-amazon-cloudwatch-and-aws-systems-manager/ "https://aws.amazon.com/blogs/database/monitor-your-microsoft-sql-server-using-custom-metrics-with-amazon-cloudwatch-and-aws-systems-manager/") for monitoring IBM Db2.

With AWS CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. AWS CloudTrail is enabled on all AWS accounts, and records your account activity upon account creation. You can view and download the last 90 days of your account activity for create, modify, and delete operations of supported services without the need to manually set up CloudTrail.

## Backup and Recovery

You need to regularly back up your operating system and database to recover them in case of failure. AWS provides various services and tools that you can use to back up your IBM Db2 database of SAP applications.

### AWS Backup

[AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/") is a fully managed backup service centralizes and automates the backup of data across AWS services. Using AWS Backup, you can centrally configure backup policies and monitor backup activity for AWS resources, such as EBS volumes, Amazon EC2 instances, and [Amazon Elastic File System](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/") (Amazon EFS). AWS Backup automates and consolidates backup tasks previously performed service-by-service, removing the need to create custom scripts and manual processes. AWS Backup provides a fully managed, policy-based backup solution, simplifying your backup management and enabling you to meet your business and regulatory backup compliance requirements.

### AMI

You can use the [AWS Management Console](https://aws.amazon.com/console/ "https://aws.amazon.com/console/") or the AWS CLI to create a new [Amazon Machine Image](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md") (Amazon AMI) of your existing SAP system. This can be used to recover your existing SAP system or create a clone.

The AWS CLI create image command creates a new AMI based on an existing Amazon EC2 instance. The new AMI contains a complete copy of the operating system and its configuration, software configurations, and optionally all EBS volumes that are attached to the instance.

A simple command to create an AMI with reboot (if running) of your EC2 instance (with instance ID `i-0b09a25c58929de26` as example) including all attached EBS volumes:

```
       aws ec2 create-image --instance-id i-0b09a25c58929de26 --name "My server"
```

A simple command to create AMI without reboot (if running[underline]_)_ of your EC2 instance (with instance ID `i-0b09a25c58929de26` as example) including all attached EBS volumes:

```
aws ec2 create-image --instance-id i-0b09a25c58929de26 --name "My server" --no-reboot
```

### Amazon EBS Snapshots

You can back up your Amazon EBS volumes to Amazon S3 by taking point-in-time [snapshots](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md"). Snapshots are incremental backups, which means that only the blocks on the device that have changed after your most recent snapshot are saved.

Snapshots are suited to backup SAP file systems like `/usr/sap/* , /sapmnt/*`. We do not recommend using snapshots to back up your volumes containing data and log files. If you decide to take snapshots for your database volume snapshot, keep in mind that for consistency you should use Microsoft’s [Volume Shadow Copy Service](https://docs.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service "https://docs.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service") and use the [run command](../../../AWSEC2/latest/UserGuide/application-consistent-snapshots.md "../../../AWSEC2/latest/UserGuide/application-consistent-snapshots.md") to back up or shut down your database before Snapshots is triggered.

A simple command to create a snapshot of volume (with volume `id vol-1234567890abcdef0` as example):

```
        aws ec2 create-snapshot --volume-id vol-1234567890abcdef0 --description "This is my volume snapshot."
```

### Database Backups

One of following methods can be used for IBM Db2 database backup:

- **With native tools to take backup on disk**-- Backup requires high throughput compared to Input/Output Operations Per Second (IOPS). We recommend using [st1 disk](https://aws.amazon.com/ebs/features/ "https://aws.amazon.com/ebs/features/"), which provides maximum throughput of 500MB/s per volume. Once the backup completes on disk it can be moved to an Amazon S3 bucket via scripts.
- **With third party backint tools**-- There are many third-party tools from partners like Commvault and Veritas that use SAP backint interface and store backups directly in Amazon S3 buckets.

### Storage

The storage services we use across this guide are:

#### Amazon EBS

[Amazon EBS](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/") provides persistent storage for SAP applications and databases. EBS volume size can be increased or their type can be changed (for example, gp2 to io1) without downtime requirements. For more information, see [Modifying Amazon EBS volume.](../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md "../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md")

Once you have extended the volume, you need to extend the drive with your Linux volume manager software.

#### Amazon S3

[Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") does not need you to explicitly provision storage at all – you simply pay for what you use.

## Operating System Maintenance

Operating system maintenance across large estates of EC2 instances can be managed by:

- Tools specific to each operating system such as [SUSE Manager](https://www.suse.com/products/suse-manager/ "https://www.suse.com/products/suse-manager/") and [Red Hat Smart Management](https://www.redhat.com/en/blog/red-hat-smart-management-and-satellite-ask-me-anything-qa-march "https://www.redhat.com/en/blog/red-hat-smart-management-and-satellite-ask-me-anything-qa-march").
- 3rd party products such as those available on the [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").
- Using [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/").

Here are some key operating system maintenance tasks that can help with:

### Patching

Follow SAP recommended patching processes to update your landscape on AWS. For operating system patching, with AWS Systems Manager [Patch Manager](https://aws.amazon.com/systems-manager/features/ "https://aws.amazon.com/systems-manager/features/") you can roll out OS patches as per your corporate policies. There are multiple key features such as:

- Scheduling based on tags
- Auto-approving patches with lists of approved and rejected patches
- Defining patch baselines

AWS Systems Manager Patch Manager integrates with IAM, AWS CloudTrail, and Amazon CloudWatch Events to provide a secure patching experience that includes event notifications and the ability to audit usage. For details about the process, see [How Patch Manager Operations Work](../../../systems-manager/latest/userguide/patch-manager-how-it-works.md "../../../systems-manager/latest/userguide/patch-manager-how-it-works.md"). If AWS Systems Manager Patch Manager does not fulfil your requirements, there are third-party products available as well. Some of these are available via the [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").

### Maintenance Window

[AWS Systems Manager Maintenance Windows](../../../systems-manager/latest/userguide/systems-manager-maintenance.md "../../../systems-manager/latest/userguide/systems-manager-maintenance.md") enables you to define a schedule for when to perform potentially disruptive actions on your instances, such as patching an operating system, updating drivers, or installing software or patches.

### Automation Using Documents

[AWS Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md") simplifies common maintenance and deployment tasks of Amazon EC2 instances and other AWS resources. Automation enables you to do the following:

- Build automation workflows to configure and manage instances and AWS resources.
- Create custom workflows or use pre-defined workflows maintained by AWS.
- Receive notifications about Automation tasks and workflows by using Amazon CloudWatch Events.
- Monitor automation progress and execution details by using the Amazon EC2 or the AWS Systems Manager console.

### Business Continuity

AWS recommends periodically scheduling business continuity process validations by executing disaster recovery tests. This planned activity helps to flush out any potential unknowns, and helps the organization deal with any real disaster in a streamlined manner. Depending on your disaster recovery architecture it may include:

- Backup/Recovery of databases from S3.
- Creation of systems from AMI and point-in-time recovery via snapshots.
- Changing EC2 instance size of pilot light systems.
- Validation of integration (AD/DNS, email, 3^rd^ party, and more)

### Support

SAP requires customers to have a minimum [AWS Business Support](https://aws.amazon.com/premiumsupport/plans/business/ "https://aws.amazon.com/premiumsupport/plans/business/") plan with AWS. This ensures that any critical issues raised with SAP are also handled by AWS on priority. AWS business support provides a less than one-hour response time for production-down scenarios. You can also choose to have an AWS enterprise support plan, which provides a less than 15-minute response time for business-critical systems, along with other benefits. See [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/ "https://aws.amazon.com/premiumsupport/plans/enterprise/").

For any SAP application issues, AWS suggests raising an incident with SAP via the SAP support portal. After the first level of investigation, SAP can redirect the incident to AWS support if they find an infrastructure related issue which needs to be managed by AWS. However, if you choose to raise support issues for SAP applications with AWS support, we cannot redirect the tickets to SAP. For any infrastructure related issues, you can raise the issue directly with AWS support.

### Cost Optimization

Resources (CPU, memory, additional application servers, system copies for different tests/validations and more) required the SAP landscape change over time. AWS recommends monitoring system utilization, and the need for existing systems, on a regular basis to take actions that will reduce cost. In cases of databases like IBM Db2 as we cannot scale out only opportunity to right size database server is by scaling up/down or shutting it down if not required. A few suggestions to consider:

- Consider reserved instances or savings plans over on-demand instances if your requirement is to run 24-7, 365 days a year. Reserved instances provide up to 75% discount over on-demand instances. See [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/").
- Consider running occasionally required systems like training and sandbox on-demand for the duration required.
- Monitor CPU and memory utilization overtime for other non-production systems like Dev/QA, and right-size them when possible.
