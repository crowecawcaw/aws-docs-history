

# `AWSPremiumSupport-ExtendVolumesOnLinux`
<a name="automation-awspremiumsupport-extendvolumesonlinux"></a>

 **Description** 

The `AWSPremiumSupport-ExtendVolumesOnLinux` runbook extends the Amazon Elastic Block Store (Amazon EBS) volumes, their partitions, and filesystems on a target Amazon Elastic Compute Cloud (Amazon EC2) instance.

**Important considerations**  
**Operation Impact and Volume States**: Amazon EBS volume modifications occur in three phases: `modifying`, `optimizing`, and `completed`. This automation proceeds with filesystem extension when the volume reaches the `optimizing` state. During the `optimizing` state you might experience temporary performance impact and potential filesystem-level disruptions during partition resizing. You can [Monitor the progress of Amazon EBS volume modifications](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-modifications.html).
**Cost and Limitations**: Increasing an Amazon EBS volume size will result in higher monthly storage costs. For more information, see the [Amazon EBS Pricing](https://aws.amazon.com/ebs/pricing). The backup AMI and associated snapshots created by this runbook will incur additional charges based on their size and the length of time that you keep them. For some volume types, if you need to maintain the same IOPS per GB ratio after expansion, you may need to modify the provisioned IOPS. RAID devices and LVM volumes are not supported.
**Backup and Recovery**: The runbook creates a backup AMI before making any changes to the volumes. The AMI and associated snapshots are not automatically removed from your account. You should manually remove these backups if they are no longer required. In case of failure, volumes can be recovered from the snapshots of the associated AMI as described in [Replace an Amazon EBS volume using a snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-restoring-volume.html).

 **How does it work?** 

This runbook performs the following operations:
+ Verifies that the target instance is managed by Systems Manager and is running Linux
+ Ensures there is only one execution of this runbook targeting the current Amazon EC2 instance
+ Creates a backup Amazon Machine Image (AMI) from the target instance
+ Extends the Amazon EBS volumes that were specified for expansion
+ Extends the filesystems on the target instance using shell script commands

**Important**  
Access to `AWSPremiumSupport-*` runbooks requires a Business \+ Support, Enterprise Support or Unified Operations Subscription. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/).

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-ExtendVolumesOnLinux) 

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux

**Parameters**

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DescribeInstances`
+ `ec2:CreateImage`
+ `ec2:DescribeImages`
+ `ec2:DescribeVolumes`
+ `ec2:DescribeVolumesModifications`
+ `ec2:ModifyVolume`
+ `ssm:SendCommand`
+ `ssm:ListCommandInvocations`
+ `ssm:DescribeInstanceInformation`
+ `ssm:DescribeAutomationExecutions`
+ `ssm:GetAutomationExecution`

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
                 "ec2:DescribeVolumesModifications",
                 "ec2:ModifyVolume",
                 "ssm:SendCommand",
                 "ssm:ListCommandInvocations",
                 "ssm:DescribeInstanceInformation",
                 "ssm:DescribeAutomationExecutions",
                 "ssm:GetAutomationExecution"
             ],
             "Resource": "*"
         }
     ]
 }
```

 **Instructions** 

Follow these steps to configure the automation:

1. Open [AWSPremiumSupport-ExtendVolumesOnLinux](https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-ExtendVolumesOnLinux/description) in Systems Manager under Documents.

1. Choose **Execute automation.**

1. For the input parameters, enter the following:
   + **AutomationAssumeRole (Optional):**
     + Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
     + Type: `AWS::IAM::Role::Arn`
   + **InstanceId (Required):**
     + Description: (Required) The ID of the Amazon EC2 instance.
     + Type: `String`
     + Allow Pattern: `^i-[a-z0-9]{8,17}$`
   + **VolumeExpansionCapSize (Required):**
     + Description: (Required) Maximum size (in GiB) that the Amazon EBS volumes will be increased to.
     + Type: `String`
     + Allow Pattern: `^[0-9]{1,4}$`
   + **DiagnosticResults (Required):**
     + Description: (Required) The results of the prechecks script from the `DiagnoseDiskUsage` document, formatted as a one-line CSV. The string starts with `EXTEND;` followed by comma-separated volume information for each volume, with volumes separated by semicolons. Each volume's information includes: Volume ID, Partition, Extend flag (1 to extend, 0 to skip), New size in GB, AWS region, and Reason/Action.
     + Type: `String`
     + Allow Pattern: `^EXTEND;[0-9a-zA-Z\\.;_%:\\-\/,\\s]{7,5400}$`

1. Choose **Execute**.

1. The automation initiates.

1. The runbook performs the following steps:
   + **AssertInstanceIsManagedInstance**:

     Verifies that the target instance is managed by Systems Manager.
   + **DescribeInstance**:

     Retrieves the `Platform` information of the target Amazon EC2 instance.
   + **BranchOnPlatform**:

     Confirms that the target Amazon EC2 instance platform is Linux.
   + **CheckConcurrency**:

     Ensures there is only one execution of this runbook targeting the current Amazon EC2 instance.
   + **CreateImage**:

     Creates a backup Amazon Machine Image (AMI) from the target instance.
   + **WaitUntilImageReady**:

     Waits for the Amazon Machine Image (AMI) to complete creation and reach the `available` state.
   + **ExtendEBSVolume**:

     Extends the Amazon EBS volumes of the target instance that were specified for expansion.
   + **DescribeVolumes**:

     Describes the Amazon EBS volumes attached to the target instance.
   + **ExtendFilesystem**:

     Extends the filesystems of the target instance using shell script commands.

1. After completion, review the **Outputs** section for the detailed results of the execution.

**References**

Systems Manager Automation
+ [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSPremiumSupport-ExtendVolumesOnLinux/description)
+ [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)
+ [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
+ [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/)
+ [Request Amazon EBS volume modifications](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.html)