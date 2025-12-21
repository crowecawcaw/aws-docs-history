# `AWSSupport-EnableWindowsEC2SerialConsole`

**Description**

The runbook `AWSSupport-EnableWindowsEC2SerialConsole` helps you enable Amazon EC2
Serial Console, Special Admin Console (SAC), and boot menu on your Amazon EC2 Windows instance.
With Amazon Elastic Compute Cloud (Amazon EC2) Serial Console feature, you have access to your Amazon EC2 instance's
serial port to troubleshoot boot, network configuration, and other issues. The runbook
automates the steps required to enable the feature on instances in running state and managed
by AWS Systems Manager, as well as ones in stopped state or not managed by AWS Systems Manager.

**How does it work?**

The `AWSSupport-EnableWindowsEC2SerialConsole` automation runbook helps to
enable SAC and boot menu on Amazon EC2 instances running Microsoft Windows Server. For instances
in running state and managed by AWS Systems Manager, the runbook runs an AWS Systems Manager Run Command
PowerShell script to enable SAC and boot menu. For instances in stopped state or not managed
by AWS Systems Manager, the runbook uses the [AWSSupport-StartEC2RescueWorkflow](automation-awssupport-startec2rescueworkflow.md "automation-awssupport-startec2rescueworkflow.md") to create a temporary Amazon EC2 instance to
perform the required changes offline.

For more information see [Amazon EC2 Serial Console for
Windows instances.](../../../AWSEC2/latest/WindowsGuide/ec2-serial-console.md "../../../AWSEC2/latest/WindowsGuide/ec2-serial-console.md")

###### Important

- If you enable SAC on an instance, the Amazon EC2 services that rely on password
  retrieval will not work from the Amazon EC2 console. For more information, see [Use SAC to
  troubleshoot your Windows instance.](../../../AWSEC2/latest/WindowsGuide/troubleshooting-sac.md "../../../AWSEC2/latest/WindowsGuide/troubleshooting-sac.md")
- To configure access to the serial console, you must grant serial console
  access at the account level and then configure AWS Identity and Access Management (IAM) policies to
  grant access to your users. You must also configure a password-based user on
  every instance so that your users can use the serial console for
  troubleshooting. For more information see [Configure access to the Amazon EC2 Serial Console.](../../../AWSEC2/latest/UserGuide/configure-access-to-serial-console.md "../../../AWSEC2/latest/UserGuide/configure-access-to-serial-console.md")
- To see if the serial console is enabled on your account see [View account access status to the serial console.](../../../AWSEC2/latest/WindowsGuide/configure-access-to-serial-console.md#sc-view-account-access "../../../AWSEC2/latest/WindowsGuide/configure-access-to-serial-console.md#sc-view-account-access")
- Serial console access is only supported on virtualized instances built on the
  [Nitro System.](../../../AWSEC2/latest/UserGuide/instance-types.md#nitro-instance-types "../../../AWSEC2/latest/UserGuide/instance-types.md#nitro-instance-types")
  For more information, see the Amazon EC2 Serial Console [Prerequisites.](../../../AWSEC2/latest/WindowsGuide/ec2-serial-console-prerequisites.md "../../../AWSEC2/latest/WindowsGuide/ec2-serial-console-prerequisites.md")

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

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "autoscaling:DescribeAutoScalingInstances",
 "ec2:GetSerialConsoleAccessStatus",
 "ec2:Describe*",
 "ec2:createTags",
 "ec2:createImage",
 "ssm:DescribeAutomationExecutions",
 "ssm:DescribeInstanceInformation",
 "ssm:GetAutomationExecution",
 "ssm:ListCommandInvocations",
 "ssm:ListCommands"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AttachVolume",
 "ec2:DetachVolume",
 "ec2:ModifyInstanceAttribute",
 "ec2:RebootInstances",
 "ec2:StartInstances",
 "ec2:StopInstances",
 "iam:GetInstanceProfile",
 "ssm:GetParameters",
 "ssm:SendCommand",
 "ssm:StartAutomationExecution"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/`i-02573cafcfEXAMPLE`",
 "arn:aws:ec2:`us-east-1`:`111122223333`:volume/`vol-049df61146EXAMPLE`",
 "arn:aws:iam::`111122223333`:instance-profile/`instance-profile-name`",
 "arn:aws:ssm:`us-east-1`:`111122223333`:parameter/aws/service/*",
 "arn:aws:ssm:`us-east-1`:*:document/AWSSupport-StartEC2RescueWorkflow",
 "arn:aws:ssm:`us-east-1`:*:document/AWS-ConfigureAWSPackage",
 "arn:aws:ssm:`us-east-1`:*:document/AWS-RunPowerShellScript",
 "arn:aws:ssm:`us-east-1`:`111122223333`:automation-execution/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStack"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aws:RequestTag/Name": "AWSSupport-EC2Rescue: *"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": [
 "AWSSupport-EC2Rescue-AutomationExecution",
 "Name"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:DeleteStack",
 "cloudformation:DescribeStackEvents",
 "cloudformation:DescribeStackResource",
 "cloudformation:DescribeStacks",
 "ec2:AttachVolume",
 "ec2:DetachVolume",
 "ec2:RebootInstances",
 "ec2:StopInstances",
 "ec2:TerminateInstances",
 "ssm:SendCommand"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/Name": "AWSSupport-EC2Rescue: *"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateLaunchTemplate",
 "ec2:DeleteLaunchTemplate",
 "ec2:RunInstances"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "cloudformation.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "ssm.amazonaws.com",
 "ec2.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to the `AWSSupport-EnableWindowsEC2SerialConsole` in the
   AWS Systems Manager console.
2. Select Execute automation.
3. For the input parameters, enter the following:
   - **InstanceId: (Required)**

   The ID of the Amazon EC2 instance that you want to enable Amazon EC2 serial console,
   (SAC), and boot menu.
   - **AutomationAssumeRole: (Optional)**

   The Amazon Resource Name (ARN) of the IAM role that allows Systems Manager
   Automation to perform the actions on your behalf. If no role is specified,
   Systems Manager Automation uses the permissions of the user who starts this
   runbook.
   - **HelperInstanceType: (Conditional)**

   The type of Amazon EC2 instance that the runbook provisions to configure Amazon EC2
   serial console for an offline instance.
   - **HelperInstanceProfileName:
     (Conditional)**

   The name of an existing IAM instance profile for the helper instance. If
   you are enabling SAC and boot menu on an instance that is in stopped state
   or not managed by AWS Systems Manager, this is required. If an IAM instance profile
   is not specified, the automation creates one on your behalf.
   - **SubnetId: (Conditional)**

   The subnet ID for a helper instance. By default, it uses the the same
   subnet where the provided instance resides.

   ###### Important

   If you provide a custom subnet, it must be in the same Availability
   Zone as InstanceId, and it must allow access to the Systems Manager endpoints.
   This is only required if the target instance is in stopped state or is
   not managed by AWS Systems Manager.
   - **CreateInstanceBackupBeforeScriptExecution:
     (Optional)**

   Specify True to create an Amazon Machine Images (AMI) backup of the Amazon EC2
   instance before enabling SAC and boot menu. The AMI will persist after the
   automation completes. It is your responsibility to secure access to the AMI
   or delete it.
   - **BackupAmazonMachineImagePrefix:
     (Conditional)**

   A prefix for the Amazon Machine Image (AMI) that is created if the
   `CreateInstanceBackupBeforeScriptExecution` parameter is set
   to `True`.

4. Select Execute.
5. The automation initiates.
6. The document performs the following steps:
   - **CheckIfEc2SerialConsoleAccessEnabled:**

   Checks if Amazon EC2 Serial Console access is enabled at the account level.
   Note: Access to the serial console is not available by default. For more
   information see [Configure access to the Amazon EC2 Serial Console.](../../../AWSEC2/latest/WindowsGuide/configure-access-to-serial-console.md#sc-grant-account-access "../../../AWSEC2/latest/WindowsGuide/configure-access-to-serial-console.md#sc-grant-account-access")
   - **CheckIfEc2InstanceIsWindows:**

   Asserts if the target instance platform is Windows.
   - **GetInstanceType:**

   Retrieves the instance type of the target instance.
   - CheckIfInstanceTypeIsNitro:

   Checks if the instance type hypervisor is Nitro-based. Serial Console
   Access is only supported on virtualized instances built on the Nitro
   System.
   - **CheckIfInstanceIsInAutoScalingGroup:**

   Checks if the Amazon EC2 instance is part of an Amazon EC2 Auto Scaling group by calling the
   `DescribeAutoScalingInstances` API. If the instance is part
   of an Amazon EC2 Auto Scaling group, it ensures that the Porting Assistant for .NET instance is in Standby
   lifecycle state.
   - **WaitForEc2InstanceStateStablized:**

   Waits for the instance to be in running or stopped state.
   - **GetEc2InstanceState:**

   Gets the current state of the instance.
   - **BranchOnEc2InstanceState:**

   Branches based on the instance state retrieved in the previous step. If
   that instance state is running, it goes to the
   `CheckIfEc2InstanceIsManagedBySSM` step and if not, it goes
   to the `CheckIfHelperInstanceProfileIsProvided` step.
   - **CheckIfEc2InstanceIsManagedBySSM:**

   Checks if the instance is managed by AWS Systems Manager. If managed, the runbook
   enables SAC and boot menu using a PowerShell Run Command.
   - **BranchOnPreEC2RescueBackup:**

   Branches based on the
   `CreateInstanceBackupBeforeScriptExecution` input
   parameter.
   - **CreateAmazonMachineImageBackup:**

   Creates an AMI backup of the instance.
   - **EnableSACAndBootMenu:**

   Enables SAC and boot menu by running a PowerShell Run Command
   script.
   - **RebootInstance:**

   Reboots the Amazon EC2 instance to apply the configuration. This is the final
   step if the instance is online and is managed by AWS Systems Manager.
   - **CheckIfHelperInstanceProfileIsProvided:**

   Checks if the `HelperInstanceProfileName` specified exists
   before enabling SAC and boot menu offline using a temporary Amazon EC2
   instance.
   - **RunAutomationToInjectOfflineScriptForEnablingSACAndBootMenu:**

   Runs the `AWSSupport-StartEC2RescueWorkflow` to enable SAC and
   boot menu when the instance is in stopped state or not managed by
   AWS Systems Manager.
   - **GetExecutionDetails:**

   Retrieves Image ID of backup and offline script output.

7. After completed, review the Outputs section for the detailed results of the
   execution:
   - **EnableSACAndBootMenu.Output:**

   Output of the command execution in the `EnableSACAndBootMenu`
   step.
   - **GetExecutionDetails.OfflineScriptOutput:**

   Output of the offline script executed in the
   `RunAutomationToInjectOfflineScriptForEnablingSACAndBootMenu`
   step.
   - **GetExecutionDetails.BackupBeforeScriptExecution:**

   Image ID of the AMI backup taken if
   `CreateInstanceBackupBeforeScriptExecution` input parameter
   is True.

**References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-EnableWindowsEC2SerialConsole "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-EnableWindowsEC2SerialConsole")
- [Run an
  automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an
  Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation
  Workflows landing page](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
