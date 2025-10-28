# `AWSSupport-CollectECSInstanceLogs`

**Description**

The `AWSSupport-CollectECSInstanceLogs` runbook collects operating
system and Amazon Elastic Container Service (Amazon ECS) related log files from an Amazon Elastic Compute Cloud (Amazon EC2) instance to
help you troubleshoot common Amazon ECS issues. While the automation is collecting the
associated log files, changes are made to the file system. These changes include the
creation of temporary directories and a log directory, the copying of log files to
these directories, and compressing the log files into an archive.

If you specify a value for the `LogDestination` parameter, the target
instance must have the AWS Command Line Interface (AWS CLI) for Linux instances
or AWS Tools for Windows PowerShell for Windows instances installed. The
automation evaluates the policy status of the Amazon Simple Storage Service (Amazon S3) bucket you specify. To
help with the security of the logs gathered from your Amazon EC2 instance, if the policy
status `isPublic` is set to `true` , or if the access control
list (ACL) grants `READ|WRITE` permissions to the `All Users`
Amazon S3 predefined group, the logs are not uploaded. Additionaly, if the provided
bucket is not available in your account, the logs are not uploaded. For more
information about Amazon S3 predefined g roups, see [Amazon S3
predefined groups](../../../AmazonS3/latest/userguide/acl-overview.md#specifying-grantee-predefined-groups "../../../AmazonS3/latest/userguide/acl-overview.md#specifying-grantee-predefined-groups") in the _Amazon Simple Storage Service User Guide_ .

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CollectECSInstanceLogs "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CollectECSInstanceLogs")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- ECSInstanceId

Type: String

Description: (Required) The ID of the instance you want to collect logs
from. The instance you specify must be managed by Systems Manager.

- LogDestination

Type: String

Description: (Optional) The Amazon S3 bucket in your AWS account to upload
the archived logs to.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:ListCommandInvocations`
- `ssm:ListCommands`
- `ssm:SendCommand`
- `ssm:DescribeInstanceInformation`
  We recommend that the Amazon EC2 instance you specify in the
  `ECSInstanceId` parameter has an IAM role with the
  `AmazonSSMManagedInstanceCore` Amazon managed policy attached. To
  upload the log archive to the Amazon S3 bucket you specify in the
  `LogDestination` parameter, you must add following permissions:

- `s3:PutObject`
- `s3:ListBucket`
- `s3:GetBucketPolicyStatus`
- `s3:GetBucketAcl`

**Document Steps**

- `assertInstanceIsManaged` - Verifies whether the instance you
  specify in the `ECSInstanceId` parameter is managed by Systems Manager.
- `getInstancePlatform` - Gets information about the operating
  system (OS) platform of the instance specified in the
  `ECSInstanceId` parameter.
- `verifyInstancePlatform` - Branches the automation based on the
  OS platform.
- `runLogCollectionScriptOnLinux` - Gathers operating system and
  Amazon ECS related log files on Linux instances and creates an archive file in
  the `/var/log/collectECSlogs` directory.
- `runLogCollectionScriptOnWindows` - Gathers operating system and
  Amazon ECS related log files on Windows instances and creates an archive file in
  the `C:\ProgramData\collectECSlogs` directory.
- `verifyIfS3BucketProvided` - Verifies whether a value was
  specified for the `LogDestination` parameter.
- `runUploadScript` - Branches the automation step based on the OS
  platform.
- `runUploadScriptOnLinux` - Uploads the log archive to the Amazon S3
  bucket specified in the `LogDestination` parameter and deletes
  the archived log file from OS.
- `runUploadScriptOnWindows` - Uploads the log archive to the Amazon S3
  bucket specified in the `LogDestination` parameter and deletes
  the archived log file from OS.
