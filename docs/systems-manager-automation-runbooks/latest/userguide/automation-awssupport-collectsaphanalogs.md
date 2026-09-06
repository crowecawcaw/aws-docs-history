

# `AWSSupport-CollectSAPHANALogs`
<a name="automation-awssupport-collectsaphanalogs"></a>

 **Description** 

The `AWSSupport-CollectSAPHANALogs` runbook collects system logs from SAP HANA on an Amazon Elastic Compute Cloud (Amazon EC2) instance that is part of an SAP on AWS deployment. The Amazon EC2 instance must be managed by AWS Systems Manager (Systems Manager). The runbook checks for required packages and installs them if missing, runs the appropriate log collection tool for the detected operating system, and optionally uploads the collected logs to an Amazon Simple Storage Service (Amazon S3) bucket.

**Important**  
This runbook requires at least 200 MB of available disk space on the `/var/log` partition. Running this runbook may install additional packages on the target Amazon EC2 instance. You must acknowledge this by setting the `Acknowledgement` parameter to `Yes`. Storing logs in Amazon S3 incurs standard Amazon S3 storage and request charges.

 **Supported operating systems** 
+ Red Hat Enterprise Linux 8.4 and later
+ SUSE Linux Enterprise Server 12 SP5
+ SUSE Linux Enterprise Server 15 SP3 and later

 **Packages installed if missing** 

SUSE Linux Enterprise Server:
+ `supportutils`
+ `yast2-support`
+ `supportutils-plugin-suse-public-cloud`
+ `supportutils-plugin-ha-sap`
+ `crmsh`
+ `unzip`
+ `curl`
+ `aws-cli` (optional, installed if `InstallAWSCLI` is set to `Yes`)

Red Hat Enterprise Linux:
+ `sos`
+ `crm_report`
+ `unzip`
+ `curl`
+ `aws-cli` (optional, installed if `InstallAWSCLI` is set to `Yes`)

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CollectSAPHANALogs)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ InstanceID

  Type: AWS::EC2::Instance::Id

  Description: (Required) The ID of the Amazon EC2 instance running the SAP workload from which logs should be collected.
+ Acknowledgement

  Type: String

  Valid values: Yes

  Description: (Required) I acknowledge that this runbook may install additional packages in the target Amazon EC2 instance for log collection.
+ S3LogDestination

  Type: AWS::S3::Bucket::Name

  Description: (Optional) The name of the Amazon S3 bucket to which logs are uploaded. The bucket must not be public and must belong to the same AWS account. If not provided, logs are stored in instance local storage.
+ S3Prefix

  Type: String

  Default: AWSSupport-CollectSAPHANALogs

  Allowed pattern: `^$|^[a-zA-Z0-9][-./a-zA-Z0-9]{0,255}$`

  Description: (Optional) The Amazon S3 bucket prefix where logs are stored. If not provided, defaults to `AWSSupport-CollectSAPHANALogs`.
+ InstallAWSCLI

  Type: String

  Valid values: Yes \| No

  Default: No

  Description: (Optional) Whether to install the AWS CLI on the instance. If `Yes`, the runbook installs the AWS CLI if not already present.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ssm:DescribeInstanceInformation`
+ `ssm:SendCommand`
+ `ssm:GetCommandInvocation`
+ `s3:GetBucketPublicAccessBlock`
+ `s3:GetBucketAcl`
+ `s3:GetBucketLocation`
+ `s3:GetBucketOwnershipControls`
+ `s3:GetEncryptionConfiguration`
+ `s3:PutObject`

 **Document Steps** 

1. `AssertInstanceIsSSMManaged` - Verifies that the target Amazon EC2 instance is managed by Systems Manager and has a `PingStatus` of `Online`. The runbook cancels if the instance is not managed.

1. `GetInstanceInformation` - Retrieves information about the specified Amazon EC2 instance, including the platform name, which is used to determine the appropriate log collection method.

1. `CollectLogs` - Runs a shell script on the instance to collect logs. For SUSE Linux Enterprise Server instances, the script uses `supportconfig`. For Red Hat Enterprise Linux instances, it uses `sos report`. For HA clusters, the script also collects additional HA logs from the last 7 days using the `crm report` command. Required packages are installed if missing.

1. `BranchOnS3BucketProvided` - Branches the execution based on whether an Amazon S3 bucket was provided in `S3LogDestination`. If no bucket was provided, the runbook skips to `GenerateReport`. Otherwise, it proceeds to `CheckS3BucketPublicStatus`.

1. `CheckS3BucketPublicStatus` - Checks if the Amazon S3 bucket specified in `S3LogDestination` is configured with server-side encryption (SSE), and if it allows anonymous or public read or write access permissions. Also verifies that the actual bucket owner is the same as the expected bucket owner. If this step fails, the runbook continues to `GenerateReport` without uploading.

1. `UploadLogsToS3` - Uploads the collected logs to the specified Amazon S3 bucket. If `InstallAWSCLI` is set to `Yes` and the AWS CLI is not installed, the script installs AWS CLI before uploading.

1. `GenerateReport` - Generates a report of the log collection process. If an Amazon S3 bucket was provided, it includes the Amazon S3 bucket name and prefix where logs were uploaded. If not, it indicates that logs were stored locally on the instance. It also reports why any previous steps failed.

 **Outputs** 

`GenerateReport.Summary` - A summary of the log collection result.

`GenerateReport.LogLocation` - The location where logs were stored, either a local path on the instance or an Amazon S3 URI.

`GenerateReport.Status` - The overall status of the log collection execution.

 **Instructions** 

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-CollectSAPHANALogs`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-CollectSAPHANALogs/description) in Systems Manager under Documents.

1. Select Execute automation.

1. For the input parameters, enter the following:
   + **AutomationAssumeRole (Optional):**

     The ARN of the IAM role that allows Systems Manager Automation to perform actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user who starts this runbook.
   + **InstanceID (Required):**

     The ID of the Amazon EC2 instance running the SAP workload.
   + **Acknowledgement (Required):**

     Enter `Yes` to acknowledge that the runbook may install additional packages on the target Amazon EC2 instance.
   + **S3LogDestination (Optional):**

     The name of the Amazon S3 bucket to upload logs to. If not provided, logs are stored locally on the instance.
   + **S3Prefix (Optional):**

     The Amazon S3 bucket prefix for stored logs. Defaults to `AWSSupport-CollectSAPHANALogs`.
   + **InstallAWSCLI (Optional):**

     Select `Yes` to automatically install the AWS CLI if it is not present on the instance. Defaults to `No`.

1. Select Execute.

1. The automation initiates.

1. The document performs the following steps:
   + **`AssertInstanceIsSSMManaged`**

     Verifies that the target Amazon EC2 instance is managed by Systems Manager and has a `PingStatus` of `Online`.
   + **`GetInstanceInformation`**

     Retrieves information about the specified Amazon EC2 instance, including the platform name.
   + **`CollectLogs`**

     Runs a shell script to collect logs using `supportconfig` for SLES or `sos report` for RHEL. For HA clusters, also collects HA logs from the last 7 days using `crm report`.
   + **`BranchOnS3BucketProvided`**

     Skips to `GenerateReport` if no Amazon S3 bucket was provided, otherwise proceeds to `CheckS3BucketPublicStatus`.
   + **`CheckS3BucketPublicStatus`**

     Verifies the Amazon S3 bucket has SSE enabled, does not allow public access, and is owned by the same AWS account.
   + **`UploadLogsToS3`**

     Uploads the collected logs to the specified Amazon S3 bucket. Installs the AWS CLI if `InstallAWSCLI` is `Yes` and it is not already present.
   + **`GenerateReport`**

     Generates a summary of the log collection result, including the log location and any step failures.

1. After completion, review the Outputs section for the detailed results of the execution.

 **References** 

Systems Manager Automation
+ [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-CollectSAPHANALogs/description)
+ [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)
+ [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
+ [Support Automation Workflows landing page](https://aws.amazon.com/premiumsupport/technology/saw/)