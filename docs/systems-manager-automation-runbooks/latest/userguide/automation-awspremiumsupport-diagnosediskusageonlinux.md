# `AWSPremiumSupport-DiagnoseDiskUsageOnLinux`

**Description**

The **AWSPremiumSupport-DiagnoseDiskUsageOnLinux** runbook analyzes the target Amazon Elastic Compute Cloud (Amazon EC2) instance's Amazon Elastic Block Store (Amazon EBS) volumes to determine if they require expansion. It checks each volume's usage, file system type, and expansion history against the thresholds defined in the runbook input parameters. The script considers factors such as recent modifications, supported file systems, and AWS volume limits. It then outputs the volumes, if any, that are candidates for expansion, along with relevant details for each volume.

**How does it work?**

This runbook performs the following operations:

- Verifies that the target instance is managed by Systems Manager and is not running Windows
- Retrieves instance details including platform and root device type
- Fetches the volumes used by the Amazon EC2 instance
- Runs prechecks on Linux to analyze disk usage and determine expansion candidates
- Outputs volumes that are candidates for expansion with relevant details

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-DiagnoseDiskUsageOnLinux "https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-DiagnoseDiskUsageOnLinux")

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- ssm:DescribeInstanceInformation
- ec2:DescribeInstances
- ec2:DescribeVolumes
- ssm:SendCommand
- ssm:ListCommandInvocations
  Example Policy:

```

 {
     "Version": "2012-10-17",
     "Statement": [
         {
             "Effect": "Allow",
             "Action": [
                 "ssm:DescribeInstanceInformation",
                 "ec2:DescribeInstances",
                 "ec2:DescribeVolumes",
                 "ssm:SendCommand",
                 "ssm:ListCommandInvocations"
             ],
             "Resource": "*"
         }
     ]
 }

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSPremiumSupport-DiagnoseDiskUsageOnLinux`](https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-DiagnoseDiskUsageOnLinux/description "https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-DiagnoseDiskUsageOnLinux/description") in Systems Manager under Documents.
2. Select **Execute automation.**
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Description: (Optional) The Amazon Resource Name (ARN) of the IAM role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **InstanceId (Required):**
     - Description: (Required) ID of your Amazon EC2 instance.
     - Type: `String`
     - Allow Pattern: `^i-[0-9a-f]{8,17}$`

   - **VolumeExpansionUsageTrigger (Required):**
     - Description: (Required) Minimum usage of partition space required to trigger extension (in percentage).
     - Type: `String`
     - Allow Pattern: `^[0-9]{1,2}$`

   - **VolumeExpansionCapSize (Required):**
     - Description: (Required) Maximum size that the Amazon EBS Volume will be increased to (in GiB).
     - Type: `String`
     - Allow Pattern: `^[0-9]{1,4}$`

   - **VolumeExpansionGibIncrease (Required):**
     - Description: (Required) Increase in GiB of the volume. The biggest net increase between `VolumeExpansionGibIncrease` and `VolumeExpansionPercentageIncrease` will be used.
     - Type: `String`
     - Allow Pattern: `^[0-9]{1,4}$`

   - **VolumeExpansionPercentageIncrease (Required):**
     - Description: (Required) Increase in percentage of the volume. The biggest net increase between `VolumeExpansionGibIncrease` and `VolumeExpansionPercentageIncrease` will be used.
     - Type: `String`
     - Allow Pattern: `^[0-9]{1,2}$`

4. Select **Execute**.
5. The automation initiates.
6. The document performs the following steps:
   - **AssertInstanceIsManagedInstance**:

   Checks if the target instance is managed by Systems Manager.
   - **DescribeInstance**:

   Describes the target Amazon EC2 instance and retrieves the instance details including `Platform`, and `RootDeviceType`.
   - **BranchOnPlatform**:

   Branches on the type of platform and proceeds the execution if it's different than Windows.
   - **DescribeVolumes**:

   Fetches the volumes used by the Amazon EC2 Instance.
   - **RunPreChecksOnLinux**:

   Run the checks against the volumes gathered in the previous step.

7. After completed, review the **Outputs** section for the detailed results of the execution.
   **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-DiagnoseDiskUsageOnLinux/description "https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-DiagnoseDiskUsageOnLinux/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
