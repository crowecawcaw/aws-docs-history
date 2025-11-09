# `AWSSupport-RunEC2RescueForWindowsTool`

**Description**

The **AWSSupport-RunEC2RescueForWindowsTool** runbook runs the Amazon EC2 Rescue for Windows Server troubleshooting tool on the target Amazon Elastic Compute Cloud (Amazon EC2) Windows managed instance to help troubleshoot common issues. This runbook supports three main actions:

- **ResetAccess**: Resets the local Administrator password. The password is randomly generated and securely stored in AWS Systems Manager Parameter Store as `/EC2Rescue/Password/<instance_id>`. If you provide no parameters, the password is encrypted with the default AWS Key Management Service (AWS KMS) key `alias/aws/ssm`. Optionally, you can specify a AWS KMS key ID to encrypt the password with your own key.
- **CollectLogs**: Collects logs and configuration files from the operating system and uploads them to an Amazon Simple Storage Service (Amazon S3) bucket in your account by running Amazon EC2 Rescue with the `/collect:all` option.
- **FixAll**: Attempts to detect and address issues on an offline Windows root volume attached to the current instance by running Amazon EC2 Rescue with the `/rescue:all` option.

###### Important

This runbook requires that the target instance is a Windows managed instance with the AWS Tools for Windows PowerShell installed. The runbook installs the Amazon EC2 Rescue for Windows Server tool using the Systems Manager Distributor package `AWSSupport-EC2Rescue`.

**How does it work?**

The runbook performs the following steps:

- Installs the Amazon EC2 Rescue for Windows Server troubleshooting tool using the Systems Manager Distributor package.
- Executes the specified action (`ResetAccess`, `CollectLogs`, or `FixAll`) with the provided parameters.
- For `ResetAccess`: Generates a secure password and stores it in Parameter Store.
- For `CollectLogs`: Collects system logs and uploads them to the specified Amazon S3 bucket.
- For `FixAll`: Attempts to fix issues on the specified offline volume.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-RunEC2RescueForWindowsTool "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-RunEC2RescueForWindowsTool")

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

- `ssm:SendCommand`
- `ssm:ListCommandInvocations`
- `ssm:DescribeInstanceInformation`
- `ssm:GetCommandInvocation`
- `ssm:PutParameter` (for ResetAccess action)
- `kms:Encrypt` (for ResetAccess action with custom AWS KMS key)
- `s3:PutObject` (for CollectLogs action)
- `s3:GetBucketAcl` (for CollectLogs action)
- `s3:GetBucketPolicy` (for CollectLogs action)
- `s3:GetBucketPolicyStatus` (for CollectLogs action)
  Example Policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:SendCommand",
                "ssm:ListCommandInvocations",
                "ssm:DescribeInstanceInformation",
                "ssm:GetCommandInvocation",
                "ssm:PutParameter",
                "kms:Encrypt",
                "s3:PutObject",
                "s3:GetBucketAcl",
                "s3:GetBucketPolicy",
                "s3:GetBucketPolicyStatus"
            ],
            "Resource": "*"
        }
    ]
}

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-RunEC2RescueForWindowsTool`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-RunEC2RescueForWindowsTool/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-RunEC2RescueForWindowsTool/description") in Systems Manager under Documents.
2. Select **Execute automation.**
3. For the input parameters, enter the following:
   - **Command (Required):**
     - Description: (Required) The action to perform.
     - Type: `String`
     - Allow Values: `[ResetAccess, CollectLogs, FixAll]`
     - Default: `ResetAccess`

   - **Parameters (Required):**
     - Description: (Required) Parameters for the command:
       - For `ResetAccess`: The AWS AWS KMS key ID or alias (default: `alias/aws/ssm`)
       - For `CollectLogs`: The Amazon S3 bucket name to upload the logs to
       - For `FixAll`: The device name for the offline remediation (for example, `xvdf`)

     - Type: `String`
     - Allow Pattern: `^[0-9a-z][a-z0-9-.]{3,63}$|^(dev\/[a-z0-9]{2,10}|xv[a-z0-9]{1,10})$|^(alias\\aws\\ssm|[a-zA-Z0-9-/_]{1,32})$`

4. Select **Execute**.
5. The automation initiates.
6. The document performs the following steps:
   - **installEC2Rescue**:

   Installs the Amazon EC2 Rescue for Windows Server troubleshooting tool using the Systems Manager Distributor package `AWSSupport-EC2Rescue`.
   - **runEC2RescueForWindows**:

   Runs the PowerShell script with the action specified in the Command parameter to perform the requested operation.

7. After completion, review the **Outputs** section for the detailed results of the execution.
   **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-RunEC2RescueForWindowsTool/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-RunEC2RescueForWindowsTool/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
- [Use Amazon EC2 Rescue for Windows Server with Systems Manager Run Command](../../../AWSEC2/latest/WindowsGuide/ec2rw-ssm.md "../../../AWSEC2/latest/WindowsGuide/ec2rw-ssm.md")
