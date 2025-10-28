# `AWSSupport-TroubleshootActiveDirectoryReplication`

**Description**

The **AWSSupport-TroubleshootActiveDirectoryReplication** runbook helps troubleshoot Microsoft Active Directory (AD) domain controller replication failures by checking common settings on a target domain controller instance. This runbook runs a series of PowerShell commands against the provided domain controller instance to check the current replication status and report errors that can potentially cause domain replication issues. The runbook can optionally start replication critical services (`Netlogon`, `RPCSS`, `W32Time`, and `KDC`) if they are stopped and synchronize the system time by running `w32tm /resync /force` on the target instance.

###### Important

AWS Managed Microsoft AD is not in the scope of this runbook.

###### Important

While the automation is running commands on the target instance, changes are made to the target instance file system. These changes include the creation of the log directory (`$env:ProgramData\TroubleshootActiveDirectoryReplication`) and report files.

**How does it work?**

The runbook performs the following checks and actions:

- Verifies the target instance is running Windows and is managed by Systems Manager.
- Runs PowerShell scripts to check Active Directory replication configuration and status.
- Checks security group and network ACL settings for replication partner connectivity.
- Troubleshoots time synchronization and critical services status.
- Uploads log files to the specified Amazon S3 bucket for analysis.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootActiveDirectoryReplication "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootActiveDirectoryReplication")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Windows

**Parameters**

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:DescribeInstances`
- `secretsmanager:GetSecretValu`e
- `ssm:DescribeInstanceInformation`
- `ssm:SendCommand`
- `ssm:GetCommandInvocation`
- `s3:GetBucketAcl`
- `s3:GetBucketPolicy`
- `s3:GetBucketPolicyStatus`
- `s3:GetBucketPublicAccessBlock`
- `s3:PutObject`
  Example Policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "secretsmanager:GetSecretValue"
                "ssm:DescribeInstanceInformation",
                "ssm:SendCommand",
                "ssm:GetCommandInvocation",
                "s3:GetBucketAcl",
                "s3:GetBucketPolicy",
                "s3:GetBucketPolicyStatus",
                "s3:GetBucketPublicAccessBlock",
                "s3:PutObject"
            ],
            "Resource": "*"
        }
    ]
}

```

**AWS Secrets Manager setup**

The check replication PowerShell script connects to the target Microsoft Active Directory domain controller by retrieving the username and password with a runtime call to AWS Secrets Manager. Follow the steps in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") to create a new AWS Secrets Manager secret. Make sure that the username and password are stored using a key/value pair in the format `{"username":"EXAMPLE-USER","password":"EXAMPLE-PASSWORD"}`. After creating the AWS Secrets Manager secret, make sure you grant the `secretsmanager:GetSecretValue` permission on the secret ARN to your target domain controller IAM instance profile role.

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-TroubleshootActiveDirectoryReplication`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootActiveDirectoryReplication/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootActiveDirectoryReplication/description") in Systems Manager under Documents.
2. Select **Execute automation**.
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **InstanceId (Required):**
     - Description: (Required) The ID of the Amazon EC2 domain controller instance that you want to troubleshoot Active Directory replication issues. Note that the provided instance has to be a domain controller.
     - Type: `AWS::EC2::Instance::Id`

   - **SecretsManagerArn (Required):**
     - Description: (Required) The ARN of your AWS Secrets Manager secret containing an Active Directory username and password with Enterprise Admin or equivalent permissions to access your Active Directory domain and forest configuration. Make sure that the username and password are stored using a key/value pair in the format `{"username":"EXAMPLE-USER","password":"EXAMPLE-PASSWORD"}`. Make sure to attach the `secretsmanager:GetSecretValue` permission on the secret ARN to your target domain controller IAM instance profile role.
     - Type: `String`
     - Allowed Pattern:
       `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):secretsmanager:[a-z0-9-]{2,20}:[0-9]{12}:secret:[a-zA-Z0-9]{1}[a-zA-Z0-9\\/_+=.@-]{1,256}$`

   - **TimeSync (Optional):**
     - Description: (Optional) Select `Check` or `Sync`. If you select `Check`, the runbook prints out the current system time sync status. If `Sync` is selected, the runbook will attempt a force time resync by running `w32tm /resync /force` on the target instance.
     - Type: `String`
     - Allowed Values:
       `[Check, Sync]`
     - Default: `Check`

   - **ServiceAction (Optional):**
     - Description: (Optional) Select `Check` or `Fix`. If you select `Check`, the runbook prints out the current status of the `Netlogon`, `Windows Time service (W32Time)`, `Remote Procedure Call (RPC) Service`, and `Key Distribution Center (KDC)` services. If `Fix` is selected the runbook will attempt to start these services if any is stopped.
     - Type: `String`
     - Allowed Values:
       `[Check, Fix]`
     - Default: `Check`

   - **LogDestination (Required):**
     - Description: (Required) The Amazon Amazon S3 bucket in your AWS account to upload the command outputs.
     - Type: `String`

4. Select **Execute**.
5. The automation initiates.
6. The document performs the following steps:
   - **assertIfOperatingSystemIsWindows**:

   Checks if the operating system of the provided target Amazon EC2 instance is Windows.
   - **assertifInstanceIsSsmManaged**:

   Ensures the Amazon EC2 instance is managed by Systems Manager, otherwise the automation ends.
   - **checkReplication**:

   Runs a PowerShell script on the specified domain controller instance to get the Active Directory domain replication configuration and status.
   - **checkInstanceSgAndNacl**:

   Checks whether traffic to the replication partners are allowed by the security group and network ACL associated to the target domain controller instance.
   - **troubleshootReplication**:

   Runs a PowerShell script to troubleshoot time synchronization and critical services status.
   - **verifyS3BucketPublicStatus**:

   Checks if the Amazon S3 bucket specified in `LogDestination` allows anonymous, or public read or write access permissions.
   - **`runUploadScript`**:

   Runs a PowerShell script to upload the log archive to the AAmazon S3 bucket specified in the `LogDestination` parameter and deletes the archived log file from OS. The log files can be used for troubleshooting or to be shared with AWS Support when troubleshooting replication issues.

7. After completion, review the **Outputs** section for the detailed results of the execution.
   **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootActiveDirectoryReplication/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootActiveDirectoryReplication/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
