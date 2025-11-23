# `AWSSupport-StartEC2RescueWorkflow`

**Description**

The `AWSSupport-StartEC2RescueWorkflow` runbook runs the provided base64
encoded script (Bash or Powershell) on a helper instance created to rescue your instance.
The root volume of your instance is attached and mounted to the helper instance, also known
as the EC2Rescue instance. If your instance is Windows, provide a Powershell script.
Otherwise, use Bash. The runbook sets some environment variables which you can use in your
script. The environment variables contain information about the input you provided, as well
as information about the offline root volume. The offline volume is already mounted and
ready to use. For example, you can save a Desired State Configuration file to an offline
Windows root volume, or chroot to an offline Linux root volume and perform an offline
remediation.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-StartEC2RescueWorkflow "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-StartEC2RescueWorkflow")

###### Important

Amazon EC2 instances created from Marketplace Amazon Machine Images (AMIs) are not
supported by this automation.

**Additional Information**

To base64 encode a script, you can use either Powershell or Bash. Powershell:

```
[System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes([System.IO.File]::ReadAllText('PATH_TO_FILE')))
```

Bash:

```
base64 PATH_TO_FILE
```

Here is a list of environment variables you can use in your offline scripts, depending on
the target OS

Windows:

| Variable                                     | Description                                      | Example value                        |
| -------------------------------------------- | ------------------------------------------------ | ------------------------------------ |
| $env:EC2RESCUE_ACCOUNT_ID                    | {{ global:ACCOUNT\_ID }}                         | 123456789012                         |
| $env:EC2RESCUE_DATE                          | {{ global:DATE }}                                | 2018-09-07                           |
| $env:EC2RESCUE_DATE_TIME                     | {{ global:DATE\_TIME }}                          | 2018-09-07_18.09.59                  |
| $env:EC2RESCUE_EC2RW_DIR                     | EC2Rescue for Windows installation path          | C:\Program Files\Amazon\EC2Rescue    |
| $env:EC2RESCUE_EC2RW_DIR                     | EC2Rescue for Windows installation path          | C:\Program Files\Amazon\EC2Rescue    |
| $env:EC2RESCUE_EXECUTION_ID                  | {{ automation:EXECUTION\_ID }}                   | 7ef8008e-219b-4aca-8bb5-65e2e898e20b |
| $env:EC2RESCUE_OFFLINE_CURRENT_CONTROL_SET   | Offline Windows Current Control Set path         | `HKLM:\AWSTempSystem\ControlSet001`  |
| $env:EC2RESCUE_OFFLINE_DRIVE                 | Offline Windows drive letter                     | D:\                                  |
| $env:EC2RESCUE_OFFLINE_EBS_DEVICE            | Offline root volume EBS device                   | xvdf                                 |
| $env:EC2RESCUE_OFFLINE_KERNEL_VER            | Offline Windows Kernel version                   | 6.1.7601.24214                       |
| $env:EC2RESCUE_OFFLINE_OS_ARCHITECTURE       | Offline Windows architecture                     | AMD64                                |
| $env:EC2RESCUE_OFFLINE_OS_CAPTION            | Offline Windows caption                          | Windows Server 2008 R2 Datacenter    |
| $env:EC2RESCUE_OFFLINE_OS_TYPE               | Offline Windows OS type                          | Server                               |
| $env:EC2RESCUE_OFFLINE_PROGRAM_FILES_DIR     | Offline Windows Program files directory path     | D:\Program Files                     |
| $env:EC2RESCUE_OFFLINE_PROGRAM_FILES_X86_DIR | Offline Windows Program files x86 directory path | D:\Program Files (x86)               |
| $env:EC2RESCUE_OFFLINE_REGISTRY_DIR          | Offline Windows registry directory path          | D:\Windows\System32\config           |
| $env:EC2RESCUE_OFFLINE_SYSTEM_ROOT           | Offline Windows system root directory path       | D:\Windows                           |
| $env:EC2RESCUE_REGION                        | {{ global:REGION }}                              | us-west-1                            |
| $env:EC2RESCUE_S3_BUCKET                     | {{ S3BucketName }}                               | amzn-s3-demo-bucket                  |
| $env:EC2RESCUE_S3_PREFIX                     | {{ S3Prefix }}                                   | myprefix/                            |
| $env:EC2RESCUE_SOURCE_INSTANCE               | {{ InstanceId }}                                 | i-abcdefgh123456789                  |
| $script:EC2RESCUE_OFFLINE_WINDOWS_INSTALL    | Offline Windows Installation metadata            | Customer Powershell Object           |

Linux:

| Variable                      | Description                           | Example value                        |
| ----------------------------- | ------------------------------------- | ------------------------------------ |
| EC2RESCUE_ACCOUNT_ID          | {{ global:ACCOUNT\_ID }}              | 123456789012                         |
| EC2RESCUE_DATE                | {{ global:DATE }}                     | 2018-09-07                           |
| EC2RESCUE_DATE_TIME           | {{ global:DATE\_TIME }}               | 2018-09-07_18.09.59                  |
| EC2RESCUE_EC2RL_DIR           | EC2Rescue for Linux installation path | /usr/local/ec2rl-1.1.3               |
| EC2RESCUE_EXECUTION_ID        | {{ automation:EXECUTION\_ID }}        | 7ef8008e-219b-4aca-8bb5-65e2e898e20b |
| EC2RESCUE_OFFLINE_DEVICE      | Offline device name                   | /dev/xvdf1                           |
| EC2RESCUE_OFFLINE_EBS_DEVICE  | Offline root volume EBS device        | /dev/sdf                             |
| EC2RESCUE_OFFLINE_SYSTEM_ROOT | Offline root volume mount point       | /mnt/mount                           |
| EC2RESCUE_PYTHON              | Python version                        | python2.7                            |
| EC2RESCUE_REGION              | {{ global:REGION }}                   | us-west-1                            |
| EC2RESCUE_S3_BUCKET           | {{ S3BucketName }}                    | amzn-s3-demo-bucket                  |
| EC2RESCUE_S3_PREFIX           | {{ S3Prefix }}                        | myprefix/                            |
| EC2RESCUE_SOURCE_INSTANCE     | {{ InstanceId }}                      | i-abcdefgh123456789                  |

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AMIPrefix

Type: String

Default: `AWSSupport-EC2Rescue`

Description: (Optional) A prefix for the backup AMI name.

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- CreatePostEC2RescueBackup

Type: String

Valid values: true | false

Default: false

Description: (Optional) Set it to `true` to create an AMI of InstanceId
after running the script, before starting it. The AMI will persist after the
automation completes. It is your responsibility to secure access to the AMI, or to
delete it.

- CreatePreEC2RescueBackup

Type: String

Valid values: true | false

Default: false

Description: (Optional) Set it to `true` to create an AMI of InstanceId
before running the script. The AMI will persist after the automation completes. It
is your responsibility to secure access to the AMI, or to delete it.

- EC2RescueInstanceType

Type: String

Valid values: t2.small | t2.medium | t2.large | t3.small | t3.medium | t3.large |
i3.large

Default: t3.medium

Description: (Optional) The EC2 instance type for the EC2Rescue instance.

- InstanceId

Type: String

Description: (Required) ID of your EC2 instance. IMPORTANT: AWS Systems Manager Automation
stops this instance. Data stored in instance store volumes will be lost. The public
IP address will change if you are not using an Elastic IP.

- OfflineScript

Type: String

Description: (Required) Base64 encoded script to run against the helper instance.
Use Bash if your source instance is Linux, and PowerShell if it is Windows.

- S3BucketName

Type: String

Description: (Optional) S3 bucket name in your account where you want to upload
the troubleshooting logs. Make sure the bucket policy does not grant unnecessary
read/write permissions to parties that do not need access to the collected
logs.

- S3Prefix

Type: String

Default: `AWSSupport-EC2Rescue`

Description: (Optional) A prefix for the S3 logs.

- SubnetId

Type: String

Default: SelectedInstanceSubnet

Description: (Optional) The subnet ID for the EC2Rescue instance. By default, the
same subnet where the provided instance resides is used. IMPORTANT: If you provide a
custom subnet, it must be in the same Availability Zone as InstanceId, and it must
allow access to the SSM endpoints.

- UniqueId

Type: String

Default: {{ automation:EXECUTION\_ID }}

Description: (Optional) A unique identifier for the automation.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

It is recommended the user who runs the automation have the
**AmazonSSMAutomationRole** IAM managed policy attached. In addition to
that policy, the user must have:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "lambda:InvokeFunction",
 "lambda:DeleteFunction",
 "lambda:GetFunction"
 ],
 "Resource": "arn:aws:lambda:*:`111122223333`:function:AWSSupport-EC2Rescue-*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::awssupport-ssm.*/*.template",
 "arn:aws:s3:::awssupport-ssm.*/*.zip"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "iam:CreateRole",
 "iam:CreateInstanceProfile",
 "iam:GetRole",
 "iam:GetInstanceProfile",
 "iam:PutRolePolicy",
 "iam:DetachRolePolicy",
 "iam:AttachRolePolicy",
 "iam:PassRole",
 "iam:AddRoleToInstanceProfile",
 "iam:RemoveRoleFromInstanceProfile",
 "iam:DeleteRole",
 "iam:DeleteRolePolicy",
 "iam:DeleteInstanceProfile"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/AWSSupport-EC2Rescue-*",
 "arn:aws:iam::`111122223333`:instance-profile/AWSSupport-EC2Rescue-*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "lambda:CreateFunction",
 "ec2:CreateVpc",
 "ec2:ModifyVpcAttribute",
 "ec2:DeleteVpc",
 "ec2:CreateInternetGateway",
 "ec2:AttachInternetGateway",
 "ec2:DetachInternetGateway",
 "ec2:DeleteInternetGateway",
 "ec2:CreateSubnet",
 "ec2:DeleteSubnet",
 "ec2:CreateRoute",
 "ec2:DeleteRoute",
 "ec2:CreateRouteTable",
 "ec2:AssociateRouteTable",
 "ec2:DisassociateRouteTable",
 "ec2:DeleteRouteTable",
 "ec2:CreateVpcEndpoint",
 "ec2:DeleteVpcEndpoints",
 "ec2:ModifyVpcEndpoint",
 "ec2:Describe*"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```

**Document Steps**

1. `aws:executeAwsApi` - Describe the provided instance
2. `aws:executeAwsApi` - Describe the provided instance's root
   volume
3. `aws:assertAwsResourceProperty` - Check the root volume device type is
   EBS
4. `aws:assertAwsResourceProperty` - Check the root volume is not
   encrypted
5. `aws:assertAwsResourceProperty` - Check the provide subnet ID
   1. (Use current instance subnet) - If \*SubnetId = SelectedInstanceSubnet\*
      then run `aws:createStack` to deploy the EC2Rescue CloudFormation
      stack
   2. (Create new VPC) - If \*SubnetId = CreateNewVPC\* then run
      `aws:createStack` to deploy the EC2Rescue CloudFormation stack
   3. (Use custom subnet) - In all other cases:

   `aws:assertAwsResourceProperty` - Check the provided subnet is
   in the same Availability Zone as the provided instance

   `aws:createStack` - Deploy the EC2Rescue CloudFormation stack

6. `aws:invokeLambdaFunction` - Perform additional input validation
7. `aws:executeAwsApi` - Update the EC2Rescue CloudFormation stack to create the
   EC2Rescue helper instance
8. `aws:waitForAwsResourceProperty` - Wait for the EC2Rescue CloudFormation stack
   update to complete
9. `aws:executeAwsApi` - Describe the EC2Rescue CloudFormation stack
   output to obtain the EC2Rescue helper instance ID
10. `aws:waitForAwsResourceProperty` - Wait for the EC2Rescue helper
    instance to become a managed instance
11. `aws:changeInstanceState` - Stop the provided instance
12. `aws:changeInstanceState` - Stop the provided instance
13. `aws:changeInstanceState` - Force stop the provided instance
14. `aws:assertAwsResourceProperty` - Check the CreatePreEC2RescueBackup
    input value
    1. (Create pre-EC2Rescue backup) - If \*CreatePreEC2RescueBackup =
       true\*
    2. `aws:executeAwsApi` - Create an AMI backup of the provided
       instance
    3. `aws:createTags` - Tag the AMI backup

15. `aws:runCommand` - Install EC2Rescue on the EC2Rescue helper
    instance
16. `aws:executeAwsApi` - Detach the root volume from the provided
    instance
17. `aws:assertAwsResourceProperty` - Check the provided instance
    platform
    1. (Instance is Windows):

    `aws:executeAwsApi` - Attach the root volume to the EC2Rescue
    helper instance as \*xvdf\*

    `aws:sleep` - Sleep 10 seconds

    `aws:runCommand` - Run the provided offline script in
    Powershell 2. (Instance is Linux):

    `aws:executeAwsApi` - Attach the root volume to the EC2Rescue
    helper instance as \*/dev/sdf\*

    `aws:sleep` - Sleep 10 seconds

    `aws:runCommand` - Run the provided offline script in
    Bash

18. `aws:changeInstanceState` - Stop the EC2Rescue helper instance
19. `aws:changeInstanceState` - Force stop the EC2Rescue helper
    instance
20. `aws:executeAwsApi` - Detach the root volume from the EC2Rescue helper
    instance
21. `aws:executeAwsApi` - Attach the root volume back to the provided
    instance
22. `aws:assertAwsResourceProperty` - Check the CreatePostEC2RescueBackup
    input value
    1. (Create post-EC2Rescue backup) - If \*CreatePostEC2RescueBackup =
       true\*
    2. `aws:executeAwsApi` - Create an AMI backup of the provided
       instance
    3. `aws:createTags` - Tag the AMI backup

23. `aws:executeAwsApi` - Restore the initial delete on termination state
    for the root volume of the provided instance
24. `aws:changeInstanceState` - Restore the initial state of the provided
    instance (running/stopped)
25. `aws:deleteStack` - Delete the EC2Rescue CloudFormation stack

**Outputs**

runScriptForLinux.Output

runScriptForWindows.Output

preScriptBackup.ImageId

postScriptBackup.ImageId
