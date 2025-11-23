# `AWSSupport-ResetLinuxUserPassword`

**Description**

The `AWSSupport-ResetLinuxUserPassword` runbook helps you reset the password of
a local operating system (OS) user. This runbook is especially helpful for users who need to
access their Amazon Elastic Compute Cloud (Amazon EC2) instances using the serial console. The runbook creates a
temporary Amazon EC2 instance in your AWS account with either an automatically generated
AWS Identity and Access Management (IAM) role or a custom IAM instance profile you specify. The custom (IAM)
instance profile must have permissions to retrieve the AWS Secrets Manager secret value containing the
password.

The runbook stops your target Amazon EC2 instance, detaches the root Amazon Elastic Block Store (Amazon EBS) volume,
and attaches it to the temporary Amazon EC2 instance. Using Run Command, a script runs on the
temporary instance to set the password of the OS user that you specify. Then, the root Amazon EBS
volume is reattached to your target instance. The runbook also provides an option to create
a snapshot of the root volume at the beginning of the automation.

**Before you begin**

Create an Secrets Manager secret with the value of the password that you want to assign to your OS
user. The value must be in plaintext. For more information, see [Create an AWS Secrets Manager
secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_.

**Considerations**

- We recommend backing up your instance before using this runbook. Consider setting
  the value of the `CreateSnapshot` parameter as
  `Yes`.
- Changing the local user password requires the runbook to stop your instance. When
  an instance is stopped, any data stored in memory or on instance store volumes is
  lost. Also, any automatically assigned public IPv4 addresses are released. For more
  information about what happens when you stop an instance, see [Stop and start your instance](../../../AWSEC2/latest/UserGuide/Stop_Start.md "../../../AWSEC2/latest/UserGuide/Stop_Start.md") in the
  _Amazon EC2 User Guide_.
- If the Amazon EBS volumes attached to your target Amazon EC2 instance are encrypted with a
  customer managed AWS Key Management Service (AWS KMS) key, make sure the AWS KMS key is not
  `deleted` or `disabled` or your instance will fail to
  start.
- Using a custom IAM instance profile requires the
  `AutomationAssumeRole` to have IAM `GetInstanceProfile`
  permission for validation, and the custom instance profile itself must include
  Systems Manager and Secrets Manager access permissions. The runbook validates instance profile
  existence upfront but will fail during helper instance operations if the instance
  profile lacks required access.
  [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ResetLinuxUserPassword "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ResetLinuxUserPassword")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- InstanceId

Type: String

Description: (Required) The ID of the Amazon EC2 Linux instance that contains the OS
user password that you want to reset.

- LinuxUserName

Type: String

Default: ec2-user

Description: (Optional) The OS user account whose password you want to
reset.

- SecretArn

Type: String

Description: (Required) The ARN of your Secrets Manager secret containing the new
password.

- SecurityGroupId

Type: String

Description: (Optional) The ID of the security group to attach to the temporary
Amazon EC2 instance. If you don't provide a value for this parameter, the default
Amazon Virtual Private Cloud (Amazon VPC) security group is used.

- SubnetId

Type: String

Description: (Optional) The ID of the subnet that you want to launch the Amazon EC2
temporary instance in to. By default, the automation chooses the same subnet as your
target instance. If you choose to provide a different subnet, it must be in the same
Availability Zone as the target instance and have access to Systems Manager endpoints.

- CreateSnapshot

Type: String

Valid values: Yes | No

Default: Yes

Description: (Optional) Determines whether a snapshot of the root volume of your
target Amazon EC2 instance is created before the automation runs.

- StopConsent

Type: String

Valid values: Yes | No

Default: No

Description: Enter `Yes` to acknowledge that your target
Amazon EC2 instance will be stopped during this automation. When the Amazon EC2 instance is
stopped, any data stored in memory or instance store volumes is lost, and the
automatic public IPv4 address is released. For more information, see [Stop and start your instance](../../../AWSEC2/latest/UserGuide/Stop_Start.md "../../../AWSEC2/latest/UserGuide/Stop_Start.md") in the
_Amazon EC2 User Guide_.

- InstanceProfileName

Type: String

Description: (Optional) The name of the IAM instance profile to attach to the
helper Amazon EC2 instance. If not provided, a temporary instance profile with the required
permissions will be created automatically. The custom instance profile must have
permissions to access the specified Secrets Manager secret and Systems Manager.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:DescribeInstanceInformation`
- `ssm:ListTagsForResource`
- `ssm:SendCommand`
- `ec2:AttachVolume`
- `ec2:CreateSnapshot`
- `ec2:CreateSnapshots`
- `ec2:CreateVolume`
- `ec2:DescribeImages`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceStatus`
- `ec2:DescribeSnapshotAttribute`
- `ec2:DescribeSnapshots`
- `ec2:DescribeSnapshotTierStatus`
- `ec2:DescribeVolumes`
- `ec2:DescribeVolumeStatus`
- `ec2:DetachVolume`
- `ec2:RunInstances`
- `ec2:StartInstances`
- `ec2:StopInstances`
- `ec2:TerminateInstances`
- `cloudformation:CreateStack`
- `cloudformation:DeleteStack`
- `cloudformation:DescribeStackResource`
- `cloudformation:DescribeStacks`
- `cloudformation:ListStacks`
- `logs:CreateLogDelivery`
- `logs:CreateLogGroup`
- `logs:DeleteLogDelivery`
- `logs:DeleteLogGroup`
- `logs:DescribeLogGroups`
- `logs:DescribeLogStreams`
- `logs:PutLogEvents`
- `iam:GetInstanceProfile`

**Document Steps**

1. `aws:branch` – Branches based on whether you have provided
   consent to stopping the target Amazon EC2 instance.
2. `aws:assertAwsResourceProperty` – Ensures the Amazon EC2 instance
   status is in a `running` or `stopped` state. Otherwise, the
   automation ends.
3. `aws:executeAwsApi` – Gets the Amazon EC2 instance properties.
4. `aws:executeAwsApi` – Gets the root volume properties.
5. `aws:branch` – Branches the automation depending on whether a
   subnet ID for the temporary Amazon EC2 instance was provided.
6. `aws:assertAwsResourceProperty` – Ensures the subnet that you
   specify in `SubnetId` parameter is in the same Availability Zone as the
   target Amazon EC2 instance.
7. `aws:assertAwsResourceProperty`– Ensures the target Amazon EC2
   instance root volume is an Amazon EBS volume.
8. `aws:assertAwsResourceProperty` – Ensures the Amazon EC2 instance
   architecture is `arm64` or `x86_64`.
9. `aws:assertAwsResourceProperty` – Ensures the Amazon EC2 instance
   shutdown behavior is `stop` and not `terminate`.
10. `aws:branch` – Ensures the Amazon EC2 instance is not a Spot
    Instance. Otherwise, the automation ends.
11. `aws:executeScript` – Ensures the Amazon EC2 instance is not part of
    an auto scaling group. If the instance is part of an auto scaling group, the
    automation confirms the Amazon EC2 instance is in a `Standby` lifecycle
    state.
12. `aws:branch` – Branches the automation depending on whether a
    custom IAM instance profile name was provided or not
13. `aws:assertAwsResourceProperty` – Ensures the custom IAM
    instance profile exists and validates its name matches the input parameter.
14. `aws:createStack` – Creates a temporary Amazon EC2 instance that is
    used to reset the password for the OS user that you specify.
15. `aws:waitForAwsResourceProperty` – Waits until the newly
    launched temporary Amazon EC2 instance is running.
16. `aws:executeAwsApi` – Gets the ID of the temporary Amazon EC2
    instance.
17. `aws:waitForAwsResourceProperty` – Waits for the temporary Amazon EC2
    instance to report as managed by Systems Manager.
18. `aws:changeInstanceState`– Stops the target Amazon EC2
    instance.
19. `aws:changeInstanceState` – Forces the target Amazon EC2 instance to
    stop in case it gets stuck in a stopping state.
20. `aws:branch` – Branches the automation depending on whether a
    snapshot of the root volume of the target Amazon EC2 instance was requested.
21. `aws:executeAwsApi` – Creates a snapshot of the target Amazon EC2
    instance root Amazon EBS volume.
22. `aws:waitForAwsResourceProperty` – Waits for the snapshot to be
    in a `completed` state.
23. `aws:executeAwsApi` – Detaches the Amazon EBS root volume from the
    target Amazon EC2 instance.
24. `aws:waitForAwsResourceProperty` – Waits for the Amazon EBS root
    volume to be detached from the target Amazon EC2 instance.
25. `aws:executeAwsApi` – Attaches the root Amazon EBS volume to the
    temporary Amazon EC2 instance.
26. `aws:waitForAwsResourceProperty` – Waits for the Amazon EBS root
    volume to be attached to the temporary Amazon EC2 instance.
27. `aws:runCommand` – Resets the target user password by running a
    shell script using Run Command on the temporary Amazon EC2 instance.
28. `aws:executeAwsApi` – Detaches the Amazon EBS root volume from the
    temporary Amazon EC2 instance.
29. `aws:waitForAwsResourceProperty` – Waits for the Amazon EBS root
    volume to be detached from the temporary Amazon EC2 instance.
30. `aws:executeAwsApi` – Detaches the Amazon EBS root volume from the
    temporary Amazon EC2 instance after an error.
31. `aws:waitForAwsResourceProperty` – Waits for the Amazon EBS root
    volume to be detached from the temporary Amazon EC2 instance after an error.
32. `aws:branch` – Branches the automation depending on whether a
    snapshot of the root volume was requested to determine the recovery path in case of
    an error.
33. `aws:executeAwsApi` – Reattaches the root Amazon EBS volume to the
    target Amazon EC2 instance.
34. `aws:waitForAwsResourceProperty` – Waits for the Amazon EBS root
    volume to be attached to the Amazon EC2 instance.
35. `aws:executeAwsApi` – Creates a new Amazon EBS volume from the target
    Amazon EC2 instance root volume snapshot.
36. `aws:waitForAwsResourceProperty` – Waits until the new Amazon EBS
    volume is in an `available` state.
37. `aws:executeAwsApi` – Attaches the new Amazon EBS volume to the
    target instance as the root volume.
38. `aws:waitForAwsResourceProperty` – Waits for the Amazon EBS volume to
    be in an `attached` state.
39. `aws:executeAwsApi` – Describes the CloudFormation stack events if the
    runbooks fails to create or update the CloudFormation stack.
40. `aws:branch` – Branches the automation depending on the previous
    Amazon EC2 instance state. If the state was `running`, the instance is
    started. If it was in a `stopped` state, the automation continues.
41. `aws:changeInstanceState` – Starts the Amazon EC2 instance if
    needed.
42. `aws:waitForAwsResourceProperty` – Waits until the CloudFormation stack
    is in a terminal status before deleting.
43. `aws:executeAwsApi` – Deletes the CloudFormation stack including the
    temporary Amazon EC2 instance.
