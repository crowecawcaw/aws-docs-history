# `AWSPremiumSupport-ExtendVolumesOnWindows`

**Description**

The `AWSPremiumSupport-ExtendVolumesOnWindows` runbook extends the Amazon Elastic Block Store (Amazon EBS) volumes, their partitions, and filesystems on a target Amazon Elastic Compute Cloud (Amazon EC2) instance.

###### Important considerations

- **Operation Impact and Volume States**: Amazon EBS volume modifications occur in three phases: `modifying`, `optimizing`, and `completed`. This automation proceeds with filesystem extension when the volume reaches the `optimizing` state. During the `optimizing` state you might experience temporary performance impact and potential filesystem-level disruptions during partition resizing. You can [Monitor the progress of Amazon EBS volume modifications](../../../ebs/latest/userguide/monitoring-volume-modifications.md "../../../ebs/latest/userguide/monitoring-volume-modifications.md").
- **Cost and Limitations**: Increasing an Amazon EBS volume size will result in higher monthly storage costs. For more information, see the [Amazon EBS Pricing](https://aws.amazon.com/ebs/pricing "https://aws.amazon.com/ebs/pricing"). The backup AMI and associated snapshots created by this runbook will incur additional charges based on their size and the length of time that you keep them. For some volume types, if you need to maintain the same IOPS per GB ratio after expansion, you may need to modify the provisioned IOPS.
- **Backup and Recovery**: The runbook creates a backup AMI before making any changes to the volumes. The AMI and associated snapshots are not automatically removed from your account. You should manually remove these backups if no longer required. In case of failure, volumes can be recovered from the snapshots of the associated AMI as described in [Replace an Amazon EBS volume using a snapshot](../../../AWSEC2/latest/UserGuide/ebs-restoring-volume.md "../../../AWSEC2/latest/UserGuide/ebs-restoring-volume.md").

**How does it work?**

This runbook performs the following operations:

- Verifies that the target instance is managed by Systems Manager and is running Windows Server
- Ensures there is only one execution of this runbook targeting the current Amazon EC2 instance
- Creates a backup Amazon Machine Image (AMI) from the target instance
- Extends the Amazon EBS volumes that were specified for expansion
- Extends the filesystems on the target instance using PowerShell commands

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-ExtendVolumesOnWindows "https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-ExtendVolumesOnWindows")

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:DescribeInstances`
- `ec2:CreateImage`
- `ec2:DescribeImages`
- `ec2:DescribeVolumes`
- `ec2:ModifyVolume`
- `ssm:SendCommand`
- `ssm:ListCommandInvocations`
- `ssm:DescribeInstanceInformation`
  Example IAM policy:

```

 {
     "Version": "2012-10-17",
     "Statement": [
         {
             "Effect": "Allow",
             "Action": [
                 "ec2:DescribeInstances",
                 "ec2:CreateImage",
                 "ec2:DescribeImages",
                 "ec2:DescribeVolumes",
                 "ec2:ModifyVolume",
                 "ssm:SendCommand",
                 "ssm:DescribeInstanceInformation",
                 "ssm:ListCommandInvocations"
             ],
             "Resource": "*"
         }
     ]
 }

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSPremiumSupport-ExtendVolumesOnWindows`](https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-ExtendVolumesOnWindows/description "https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-ExtendVolumesOnWindows/description") in Systems Manager under Documents.
2. Select **Execute automation.**
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Description: (Optional) The Amazon Resource Name (ARN) of the IAM role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **InstanceId (Required):**
     - Description: (Required) The ID of the Amazon EC2 instance.
     - Type: `String`
     - Allow Pattern: `^i-[0-9a-f]{8,17}$`

   - **VolumeExpansionCapSize (Required):**
     - Description: (Required) Maximum size (in GiB) that the Amazon EBS volumes will be increased.
     - Type: `String`
     - Allow Pattern: `^[0-9]{1,4}$`

   - **DiagnosticResults (Required):**
     - Description: (Required) The results of the prechecks script from the `DiagnoseDiskUsage` document, formatted as a one-line CSV. The string starts with `EXTEND;` followed by comma-separated volume information for each volume, with volumes separated by semicolons. Each volume's information includes: Volume ID, Drive letter, Extend flag (1 to extend, 0 to skip), New size in GB, AWS region, and Reason/Action.
     - Type: `String`
     - Allow Pattern: `^EXTEND;[0-9a-zA-Z\\.;_%:\\-\/,\\s]{7,5400}$`

4. Select **Execute**.
5. The automation initiates.
6. The document performs the following steps:
   - **AssertInstanceIsManagedInstance**:

   Verifies that the target instance is managed by Systems Manager.
   - **DescribeInstance**:

   Retrieves the Platform information of the target Amazon EC2 instance.
   - **BranchOnPlatform**:

   Confirms that the target Amazon EC2 instance platform is Windows Server.
   - **CheckConcurrency**:

   Ensures there is only one execution of this runbook targeting the current Amazon EC2 instance.
   - **CreateImage**:

   Creates a backup Amazon Machine Image (AMI) from the target instance.
   - **WaitUntilImageReady**:

   Waits for the Amazon Machine Image (AMI) to complete creation and reach the `available` state.
   - **ExtendEBSVolume**:

   Extends the Amazon EBS volumes of the target instance that were specified for expansion.
   - **DescribeVolumes**:

   Describes the Amazon EBS volumes of the target instance that were specified for expansion.
   - **ExtendFilesystem**:

   Extends the filesystems of the target instance using PowerShell commands.

7. After completion, review the **Outputs** section for the detailed results of the execution.
   **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-ExtendVolumesOnWindows/description "https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-ExtendVolumesOnWindows/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
- [Request Amazon EBS volume modifications](../../../AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.md "../../../AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.md")
