

# AWS Backup
<a name="aws-backint-agent-backup"></a>

This section provides information about setting up and using to backup and restore your SAP HANA databases to AWS Backup.

**Topics**
+ [Prerequisites](#backint-backup-prerequisites)
+ [Install and configure AWS Backint Agent for SAP HANA](#backint-backup-install)
+ [Backup and restore your SAP HANA system with AWS Backup](#backint-backup-restore)

## Prerequisites
<a name="backint-backup-prerequisites"></a>

The following prerequisites must be completed before to use to backup and restore SAP HANA databases to AWS Backup. For more information, see [Get started with AWS Systems Manager for SAP](https://docs.aws.amazon.com/ssm-sap/latest/userguide/get-started.html) and [Register your SAP HANA databases with AWS Systems Manager for SAP](https://docs.aws.amazon.com/ssm-sap/latest/userguide/register-database.html).
+  [Set up required permissions for Amazon EC2 instance running SAP HANA database](https://docs.aws.amazon.com/ssm-sap/latest/userguide/get-started.html#ec2-permissions) 
+  [Set up required permissions for Amazon EC2 instance for backup and restore of SAP HANA database](https://docs.aws.amazon.com/ssm-sap/latest/userguide/get-started.html#backup-permissions) 
+  [Register SAP HANA database credentials in AWS Secrets Manager](https://docs.aws.amazon.com/ssm-sap/latest/userguide/get-started.html#register-secrets) 
+  [Verify AWS Systems Manager Agent (SSM Agent) is running](https://docs.aws.amazon.com/ssm-sap/latest/userguide/get-started.html#verify-ssm-agent) 
+  [Verify parameters before registering your SAP HANA database](https://docs.aws.amazon.com/ssm-sap/latest/userguide/get-started.html#verification) 
+  [Register your SAP HANA databases with AWS Systems Manager for SAP](https://docs.aws.amazon.com/ssm-sap/latest/userguide/register-database.html) 

## Install and configure AWS Backint Agent for SAP HANA
<a name="backint-backup-install"></a>

**Topics**
+ [AWS Systems Manager Agent (SSM Agent)](#aws-backint-backup-ssm)
+ [Systems Manager document](#aws-backint-backup-ssm-doc)
+ [Switch to AWS Backup from Amazon S3](#aws-backint-backup-switch)

### AWS Systems Manager Agent (SSM Agent)
<a name="aws-backint-backup-ssm"></a>

To install the with the AWS Systems Manager Agent (SSM Agent) document, you must install the [AWS Systems Manager Agent (SSM Agent)](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) version 2.3.274.0 or later, and your instance must be a managed instance that is configured for AWS Systems Manager. For more information about managed instances, see [AWS Systems Manager Managed Instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html). To update the SSM Agent, see [Update SSM Agent by using Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/rc-console.html#rc-console-agentexample).

**Note**  
The SSM Agent will not work if you do not attach the `AmazonSSMManagedInstanceCore` policy to your Amazon EC2 instance role.

### Systems Manager document
<a name="aws-backint-backup-ssm-doc"></a>

Ensure that your installed SSM Agent is running, and then follow these steps.

1. Go to [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager) > Shared Resources > Documents.

1. Search for the **AWSSAP-InstallBackintForAWSBackup** document.

1. Select **Run command**.

1. Specify the following parameters in **Command parameters**.
   + System ID – Enter a system ID for your SAP HANA database. For instance, `HDB`.
   + Installation Directory Confirmation – yes
   + Modify Global Ini File – modify
   + Confirm Log Backup Post Install – yes
   + Ensure No Backup In Process – yes

   You can retain the other parameters without any manual changes.

1. Under **Target selection**, choose **Choose instances manually**, and search for the Amazon EC2 instance on which your SAP HANA database is running.

   Alternatively, you can select an instance with the `SSMForSAPManaged: True` tag.

1.  **Run** the **AWSSAP-InstallBackintForAWSBackup** SSM document.

The `Run` command takes a few minutes to complete. You can refresh the page to check the status. On successful completion, the *Overall status* and *Detailed status* display Success.

### Switch to AWS Backup from Amazon S3
<a name="aws-backint-backup-switch"></a>

You can switch your storage media to be AWS Backup if you have setup with Amazon S3. Before you do that, ensure the following:
+ Scheduled data backups are disabled – these can fail during switch-over.
+ Scheduled backup from SAP HANA Cockpit, SAP HANA Studio or through SQL to stop log backups to Amazon S3 are disabled – these are re-enabled with AWS Backup.

To make the switch from Amazon S3 to AWS Backup, you must reinstall with Systems Manager document. The **AWSSAP-InstallBackintForAWSBackup** document replaces existing with a newer version that supports AWS Backup. For more details, see the preceding section [Systems Manager document](#aws-backint-backup-ssm-doc).

Once the switch-over is complete, setup AWS Systems Manager for SAP for an automated backup solution. For more information, see [Get started with AWS Systems Manager for SAP](https://docs.aws.amazon.com/ssm-sap/latest/userguide/get-started.html).

## Backup and restore your SAP HANA system with AWS Backup
<a name="backint-backup-restore"></a>

You can now create a backup plan or perform on-demand backups. For more information, see [Backup Operations in the AWS Backup console](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-saphana.html#saphanabackupconsole).

For details about backup and restore of your SAP HANA databases on AWS Backup, see [SAP HANA databases on Amazon EC2 instances backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-saphana.html#saphanabackupconsole).

 AWS Backup supports PrivateLink for SAP HANA on AWS. To create a backup dataplane VPC endpoint, see [Create an AWS Backup VPC endpoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-network.html).