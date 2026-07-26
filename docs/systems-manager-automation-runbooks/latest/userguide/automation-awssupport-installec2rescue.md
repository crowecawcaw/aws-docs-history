# `AWSSupport-InstallEC2Rescue`

###### Description

The `AWSSupport-InstallEC2Rescue` runbook installs and runs the
[Amazon EC2 Rescue for
Linux](../../../AWSEC2/latest/UserGuide/Linux-Server-EC2Rescue.md "../../../AWSEC2/latest/UserGuide/Linux-Server-EC2Rescue.md") or
[Amazon EC2
Rescue for Windows Server](../../../AWSEC2/latest/WindowsGuide/Windows-Server-EC2Rescue.md "../../../AWSEC2/latest/WindowsGuide/Windows-Server-EC2Rescue.md") tool on the target Amazon Elastic Compute Cloud (Amazon EC2) instance.

###### Prerequisites

- For Linux instances, Amazon EC2 Rescue for Linux requires Python
  2.7.9, 3.2, or a later version installed on the target instance.
- For Windows instances, Amazon EC2 Rescue for Windows requires .NET Framework
  3.5 SP1 or later and the AWS Tools for PowerShell installed on the target
  instance.

###### How it works

The runbook performs the following operations:

- Installs the `AWSSupport-EC2Rescue` distributor package on the target
  instance using `AWS-ConfigureAWSPackage`.
- Describes the instance to determine the operating system platform (Linux or
  Windows).
- Runs the appropriate EC2 Rescue tool based on the instance platform.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-InstallEC2Rescue "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-InstallEC2Rescue")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:DescribeInstances`
- `ssm:GetCommandInvocation`
- `ssm:ListCommandInvocations`
- `ssm:ListCommands`
- `ssm:SendCommand`
  Example IAM policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EC2Describe",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances"
            ],
            "Resource": "*"
        },
        {
            "Sid": "SSMRunCommand",
            "Effect": "Allow",
            "Action": [
                "ssm:GetCommandInvocation",
                "ssm:ListCommandInvocations",
                "ssm:ListCommands",
                "ssm:SendCommand"
            ],
            "Resource": "*"
        }
    ]
}

```

###### Outputs

`installEC2Rescue.Output` - The output of the EC2 Rescue package
installation.

###### Instructions

Follow these steps to configure the automation:

1. Open [AWSSupport-InstallEC2Rescue](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-InstallEC2Rescue/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-InstallEC2Rescue/description") in Systems Manager under Documents.
2. Choose Execute automation.
3. For the input parameters, enter the following:

   - **InstanceId (Required):**

   The ID of your Amazon EC2 instance.
   - **AutomationAssumeRole (Optional):**

   The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager
   Automation to perform the actions on your behalf. If no role is specified,
   Systems Manager Automation uses the permissions of the user that starts this
   runbook.
   - **Version (Optional):**

   The EC2 Rescue version to install. Only applies to EC2 Rescue for
   Windows.

   Default: `latest`

4. Choose Execute.
5. The automation initiates.
6. The document performs the following steps:

   - **`installEC2Rescue`**:

   Installs the `AWSSupport-EC2Rescue` distributor package on the
   target instance.
   - **`describeInstance`**:

   Describes the target instance to determine its operating system
   platform.
   - **`branchOnInstancePlatform`**:

   Branches execution based on the instance platform (Linux or
   Windows).
   - **`runScriptForLinux`**:

   Runs the Amazon EC2 Rescue for Linux tool on the target
   instance.
   - **`runScriptForWindows`**:

   Runs the Amazon EC2 Rescue for Windows Server tool on the target
   instance.

7. After completion, review the Outputs section for the detailed results of the
   execution.

###### References

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-InstallEC2Rescue/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-InstallEC2Rescue/description")
- [Run an
  automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an
  Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation
  Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
