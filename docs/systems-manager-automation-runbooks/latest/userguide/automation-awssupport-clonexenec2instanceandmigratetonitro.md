# `AWSSupport-CloneXenEC2InstanceAndMigrateToNitro`

**Description**

The **AWSSupport-CloneXenEC2InstanceAndMigrateToNitro**runbook clones, prepares and migrates the cloned Amazon Elastic Compute Cloud (Amazon EC2) Linux instance, currently running on Amazon EC2 Xen platform, to run on [Amazon EC2 Nitro platform](../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances "../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances"). This automation is divided into three different branches:

- **Preliminary Checks**: Evaluates all prerequisites to proceed with the migration including checking if the target Amazon EC2 instance is already running on Nitro platform, determining lifecycle status, validating operating system, and verifying Systems Manager connectivity.
- **Test**: Creates a test AMI from the target Amazon EC2 instance and launches a test Amazon EC2 instance to validate the migration process before proceeding.
- **CloneAndMigrate**: Creates a clone of the target Amazon EC2 instance, installs necessary drivers, configures the system for Nitro platform, and changes the instance type to the desired Nitro type.

###### Important

Before providing approval to stop the target Amazon EC2 instance, ensure that all applications running on the instance are gracefully closed. If the Amazon EC2 instance does not have an Elastic IP address associated, the automatic public IPv4 address will change once the instance is stopped and started.

###### Important

**Disclaimer**: Executing this runbook may incur extra charges to your account for the Amazon EC2 instance, Amazon EBS Volumes & AMIs. Please refer to the [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/") & [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/") for more details.

###### Important

**Prerequisites**

The target Amazon EC2 instance requires outbound access to the repositories to install drivers and dependencies such as `kernel-devel`, `gcc`, `patch`, `rpm-build`, `wget`, `dracut`, `make`, `linux-headers`, and `unzip` using package manager if needed.

**Supported Operating Systems**

- Red Hat Enterprise Linux (RHEL) 8 and 9
- Amazon Linux 2 and AL2023
- Ubuntu Server 18.04 LTS, 20.04 and 22.04
- Debian 11 and 12 (AWS partition only)
- SUSE12SP5 and SUSE15SP(5,6)

**How does it work?**

The runbook performs the following high-level steps:

- Validates prerequisites and checks if the instance is suitable for migration.
- Creates and tests an AMI to ensure the migration will be successful.
- Enables Enhanced networking (ENA) attribute and installs the latest ENA drivers.
- Verifies and configures NVMe module in initramfs.
- Analyzes and modifies /etc/fstab to replace device names with UUIDs.
- Disables predictable interface naming and removes persistent network rules.
- Changes the cloned instance type to the desired Nitro type.
- Creates a final AMI that can be used as a Golden Image for launching Nitro instances.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CloneXenEC2InstanceAndMigrateToNitro "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CloneXenEC2InstanceAndMigrateToNitro")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux

**Parameters**

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `autoscaling:DescribeAutoScalingInstances`
- `ec2:CreateImage`
- `ec2:CreateTags`
- `ec2:DescribeImages`
- `ec2:DescribeInstanceAttribute`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceStatus`
- `ec2:DescribeInstanceTypeOfferings`
- `ec2:DescribeInstanceTypes`
- `ec2:DeregisterImage`
- `ec2:ModifyInstanceAttribute`
- `ec2:RunInstances`
- `ec2:StartInstances`
- `ec2:StopInstances`
- `ec2:TerminateInstances`
- `iam:PassRole`
- `sns:Publish`
- `ssm:DescribeAutomationExecutions`
- `ssm:DescribeInstanceInformation`
- `ssm:SendCommand`
  Example IAM policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "autoscaling:DescribeAutoScalingInstances",
                "ec2:CreateImage",
                "ec2:CreateTags",
                "ec2:DescribeImages",
                :ec2:DescribeInstanceAttribute:,
                "ec2:DescribeInstances",
                "ec2:DescribeInstanceStatus",
                "ec2:DescribeInstanceTypes",
                "ec2:DeregisterImage",
                "ec2:ModifyInstanceAttribute",
                "ec2:RunInstances",
                "ec2:StartInstances",
                "ec2:StopInstances",
                "ec2:TerminateInstances",
                "iam:PassRole",
                "ssm:DescribeAutomationExecutions",
                "ssm:DescribeInstanceInformation",
                "ssm:SendCommand"
            ],
            "Resource": "*"
        }
    ]
}

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-CloneXenEC2InstanceAndMigrateToNitro`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-CloneXenEC2InstanceAndMigrateToNitro/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-CloneXenEC2InstanceAndMigrateToNitro/description") in Systems Manager under Documents.
2. Select **`Execute automation`**.
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Description: (Optional) The ARN of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **TargetInstanceId (Required):**
     - Description: (Required) Instance ID of the target Amazon EC2 instance you want to migrate to Nitro platform.
     - Type: `AWS::EC2::Instance::Id`

   - **NitroInstanceType (Optional):**
     - Description: (Optional) Enter the destination Nitro instance type. Only Nitro M5, M6, C5, C6, R5, R6 and T3 instances are supported (e.g. t3.small). Default: m5.xlarge.
     - Type: `String`
     - Allowed Pattern:
       `^(m5a?z?d?n?|c5a?d?n?|r5a?d?n?b?|(c|m|r)6(a|i)?d?)\\.(2|4|8|12|16|24|32)?xlarge$|^t3a?\\.((x|2x)?large|nano|micro|small|medium)$`
     - Default: m5.xlarge

   - **SNSTopicArn (Required):**
     - Description: (Required) Provide the ARN of the Amazon SNS Topic for approval notification. This Amazon SNS topic is used to send approval notifications during the automation execution.
     - Type: `String`
     - Allowed Pattern:
       `^arn:(aws|aws-cn|aws-us-gov|aws-iso(-[a-z])?):sns:(us(-gov|-isob?)?|ap|ca|af|me|cn|eu|sa)-(central|(north|south)?(east|west)?)-\\d:\\d{12}:[a-zA-Z0-9_.-]{1,256}$`

   - **ApproverIAM (Required):**
     - Description: (Required) Provide a list of AWS authenticated principals who are able to either approve or reject the action. The maximum number of approvers is 10.
     - Type: `StringList`
     - Allowed Pattern:
       `^[a-zA-Z0-9_+=,.@\\-\/]{1,128}$|^arn:(aws|aws-cn|aws-us-gov|aws-iso(-[a-z])?):(sts|iam)::[0-9]{12}:[a-zA-Z0-9_+=,.@\\-\/]{1,256}$`

   - **MinimumRequiredApprovals (Optional):**
     - Description: (Optional) The minimum number of approvals required to resume the automation. Default: 1.
     - Type: Integer
     - Default: 1

   - **DeleteResourcesOnFailure (Optional):**
     - Description: (Optional) Whether to terminate the cloned Amazon EC2 instance and AMI if the automation fails.
     - Type: `Boolean`
     - Allowed Values:
       `[true, false]`
     - Default: `true`

   - **Acknowledgement (Required):**
     - Description: (Required) Please read the complete details of the actions performed by this automation runbook and write 'Yes, I understand and acknowledge' if you acknowledge the steps.
     - Type: `String`
     - Allowed Pattern:
       `^Yes, I understand and acknowledge$`

   - **AllowInstanceStoreInstances (Optional):**
     - Description: (Optional) If you specify `yes`, the runbook runs on instances that have instance store volumes attached. **Warning:** data in the instance store volumes is lost when the instance is stopped. This parameter helps avoid accidental data loss.
     - Type: `Boolean`
     - Allowed Values:
       `[yes, no]`
     - Default: `no`

4. Select **Execute**.
5. The automation initiates.
6. The document performs the following steps:
   - **`checkConcurrency`**:

   Ensures there is only one execution of this runbook targeting the current Amazon EC2 instance.
   - **`getTargetInstanceProperties`**:

   Fetches the details of the target Amazon EC2 instance.
   - **`checkIfNitroInstanceTypeIsSupportedInAZ`**:

   Determines if the target Nitro instance type is supported in the same Availability Zone as the target Amazon EC2 instance.
   - **`createTestImage`**:

   Creates a test AMI from the provided instance.
   - **`launchTestInstanceInSameSubnet`**:

   Launches a test Amazon EC2 instance from the test AMI using the same configuration as target Amazon EC2 instance.
   - **`approvalToStopTargetInstance`**:

   Waits for designated principals approval to stop the target instance.
   - **`createBackupImage`**:

   Creates an AMI from the provided instance for backup.
   - **`launchInstanceInSameSubnet`**:

   Launches a new Amazon EC2 instance from the backup AMI using the same configuration as source Amazon EC2 instance.
   - **`checkAndInstallENADrivers`**:

   Determines the availability of Enhanced Networking Adapter (ENA) drivers on the Amazon EC2 instance and installs, if missing.
   - **`checkAndAddNVMEDrivers`**:

   Determines the availability of NVMe drivers on the cloned Amazon EC2 instance and installs, if missing.
   - **`checkAndModifyFSTABEntries`**:

   Determines if the device name are used in `/etc/fstab` and replaces them with their UUIDs, if found.
   - **`setNitroInstanceTypeForClonedInstance`**:

   Sets the provided target Amazon EC2 instance type for the cloned Amazon EC2 instance.
   - **`approvalForCreatingImageAfterDriversInstallation`**:

   Waits for user approval if the cloned Amazon EC2 instance successfully boots on Nitro platform.
   - **`createImageAfterDriversInstallation`**:

   Creates an Image from the new Amazon EC2 instance only if the new Amazon EC2 instance successfully boots on Nitro Platform.

7. After completed, review the **Outputs** section for the detailed results of the execution.
   **References**

AWS Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-CloneXenEC2InstanceAndMigrateToNitro/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-CloneXenEC2InstanceAndMigrateToNitro/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
