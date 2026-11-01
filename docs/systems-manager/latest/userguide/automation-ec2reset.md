

# Reset passwords and SSH keys on EC2 instances
<a name="automation-ec2reset"></a>

You can use the `AWSSupport-ResetAccess` runbook to automatically re-enable local Administrator password generation on Amazon Elastic Compute Cloud (Amazon EC2) instances for Windows Server and to generate a new SSH key on EC2 instances for Linux. The `AWSSupport-ResetAccess` runbook is designed to perform a combination of AWS Systems Manager actions and AWS CloudFormation actions that automate the steps normally required to reset the local administrator password.

You can use Automation with the `AWSSupport-ResetAccess` runbook to solve the following problems:

**Windows**

*You lost the EC2 key pair*: To resolve this problem, you can use the **AWSSupport-ResetAccess** runbook to create a password-enabled AMI from your current instance, launch a new instance from the AMI, and select a key pair you own.

*You lost the local Administrator password*: To resolve this problem, you can use the `AWSSupport-ResetAccess` runbook to generate a new password that you can decrypt with the current EC2 key pair.

**Linux**

*You lost your EC2 key pair, or you configured SSH access to the instance with a key you lost*: To resolve this problem, you can use the `AWSSupport-ResetAccess` runbook to create a new SSH key for your current instance, which lets you connect to the instance again.

**Note**  
If your EC2 instance for Windows Server is configured for Systems Manager, you can also reset your local Administrator password by using EC2Rescue and AWS Systems Manager Run Command. For more information, see [Using EC2Rescue for Windows Server with Systems Manager Run Command](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2rw-ssm.html) in the *Amazon EC2 User Guide*.

**Related information**  
[Connect to your Linux instance from Windows using PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html) in the *Amazon EC2 User Guide*

## How it works
<a name="automation-ec2reset-how"></a>

Troubleshooting an instance with Automation and the `AWSSupport-ResetAccess` runbook works as follows:
+ You specify the ID of the instance and run the runbook.
+ The system creates a temporary VPC by deploying the EC2Rescue CloudFormation stack.
+ The system identifies a subnet for your temporary VPC in the same Availability Zone as your original instance.
+ The system launches a temporary, SSM-enabled helper instance.
+ The system stops your original instance, and creates a backup. It then attaches the original root volume to the helper instance.
+ The system uses Run Command to run EC2Rescue on the helper instance. On Windows, EC2Rescue enables password generation for the local Administrator by using EC2Config or EC2Launch on the attached, original root volume. On Linux, EC2Rescue generates and injects a new SSH key and saves the private key, encrypted, in Parameter Store. When finished, EC2Rescue reattaches the root volume back to the original instance.
+ The system creates a new Amazon Machine Image (AMI) of your instance, now that password generation is enabled. You can use this AMI to create a new EC2 instance, and associate a new key pair if needed.
+ The system restarts your original instance, and terminates the temporary instance. The system also terminates the temporary VPC and deletes the EC2Rescue CloudFormation stack created at the start of the automation.
+ **Windows**: Your instance generates a new password you can decode from the Amazon EC2 console using the current key pair assigned to the instance.

  **Linux**: You can SSH to the instance by using the SSH key stored in Systems Manager Parameter Store as **/ec2rl/openssh/{{instance ID}}/key**.

## Before you begin
<a name="automation-ec2reset-begin"></a>

Before you run the following Automation, do the following:
+ Copy the instance ID of the instance on which you want to reset the Administrator password. Specify this ID in the procedure.
+ Optionally, collect the ID of a subnet in the same availability zone as your unreachable instance. The EC2Rescue instance will be created in this subnet. If you don’t specify a subnet, then Automation creates a new temporary VPC in your AWS account. Verify that your AWS account has at least one VPC available. By default, you can create five VPCs in a Region. If you already created five VPCs in the Region, the automation fails without making changes to your instance. For more information about Amazon VPC quotas, see [VPC and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-vpcs-subnets) in the *Amazon VPC User Guide*.
+ Optionally, you can create and specify an AWS Identity and Access Management (IAM) role for Automation. If you don't specify this role, then Automation runs in the context of the user who ran the automation.

### Granting AWSSupport-EC2Rescue permissions to perform actions on your instances
<a name="automation-ec2reset-access"></a>

EC2Rescue needs permission to perform a series of actions on your instances during the automation. These actions invoke the IAM, Amazon EC2, and CloudFormation services to safely and securely attempt to remediate issues with your instances. If you have Administrator-level permissions in your AWS account and/or VPC, you might be able to run the automation without configuring permissions, as described in this section. If you don't have Administrator-level permissions, then you or an administrator must configure permissions as described in [Granting permissions by using IAM policies](#automation-ec2reset-access-iam).

#### Granting permissions by using IAM policies
<a name="automation-ec2reset-access-iam"></a>

You can either attach the following IAM policy to your user, group, or role as an inline policy; or, you can create a new IAM managed policy and attach it to your user, group, or role. For more information about adding an inline policy to your user, group, or role see [Working With Inline Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_inline-using.html). For more information about creating a new managed policy, see [Working With Managed Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-using.html).

**Note**  
Attach the **AmazonSSMAutomationRole** managed policy alongside the following policy, whether you add the following policy inline or as a new managed policy. The automation depends on permissions that **AmazonSSMAutomationRole** grants and the following policy doesn't, including the Systems Manager API permissions, `ec2:RunInstances`, and the CloudFormation permissions used to create and delete the temporary EC2Rescue stack.

**Note**  
This policy assumes that you specify an existing instance profile in the `HelperInstanceProfileName` parameter when you run the automation. The IAM role inside that instance profile is a separate identity from the one you attach the following policy to. It must trust `ec2.amazonaws.com` and have the **AmazonSSMManagedInstanceCore** policy attached, so that the EC2Rescue helper instance can register with Systems Manager and receive commands. Don't attach **AmazonSSMAutomationRole** to it, because the helper instance doesn't call those APIs. To reset an SSH key on a Linux instance, that role additionally needs `ssm:PutParameter` on `arn:aws:ssm:*:{{account ID}}:parameter/ec2rl/openssh/*/key`, and `kms:Encrypt` with `kms:GenerateDataKey` so that the parameter can be written as a `SecureString`. If you leave `HelperInstanceProfileName` empty, the automation creates a helper IAM role and instance profile on your behalf, which requires permissions to create and configure IAM resources that this policy doesn't grant.

**IAM Policy for `AWSSupport-ResetAccess`**

Replace {{account ID}}, {{EC2RescueHelperRole}}, and {{EC2RescueAutomationRole}} with your own information.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ReadApprovedHelperProfile",
            "Effect": "Allow",
            "Action": "iam:GetInstanceProfile",
            "Resource": "arn:aws:iam::{{111122223333}}:instance-profile/{{EC2RescueHelperRole}}"
        },
        {
            "Sid": "PassHelperRoleToEc2",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{EC2RescueHelperRole}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ec2.amazonaws.com"
                }
            }
        },
        {
            "Sid": "PassExecutionRoleToNestedAutomation",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{EC2RescueAutomationRole}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ssm.amazonaws.com"
                }
            }
        },
        {
            "Sid": "ReadRescueStackResources",
            "Effect": "Allow",
            "Action": "cloudformation:DescribeStackResource",
            "Resource": "arn:aws:cloudformation:*:{{111122223333}}:stack/AWSSupport-EC2Rescue-*/*"
        },
        {
            "Sid": "MoveRootVolumeAndRebootHelper",
            "Effect": "Allow",
            "Action": [
                "ec2:AttachVolume",
                "ec2:DetachVolume",
                "ec2:ModifyInstanceAttribute",
                "ec2:RebootInstances"
            ],
            "Resource": [
                "arn:aws:ec2:*:{{111122223333}}:instance/*",
                "arn:aws:ec2:*:{{111122223333}}:volume/*"
            ]
        },
        {
            "Sid": "ManageHelperLaunchTemplate",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateLaunchTemplate",
                "ec2:DeleteLaunchTemplate"
            ],
            "Resource": "arn:aws:ec2:*:{{111122223333}}:launch-template/*"
        },
        {
            "Sid": "ManageTemporaryNetwork",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateVpc",
                "ec2:ModifyVpcAttribute",
                "ec2:DeleteVpc",
                "ec2:CreateInternetGateway",
                "ec2:AttachInternetGateway",
                "ec2:DetachInternetGateway",
                "ec2:DeleteInternetGateway",
                "ec2:CreateSubnet",
                "ec2:ModifySubnetAttribute",
                "ec2:DeleteSubnet",
                "ec2:CreateRouteTable",
                "ec2:CreateRoute",
                "ec2:DeleteRoute",
                "ec2:AssociateRouteTable",
                "ec2:DisassociateRouteTable",
                "ec2:DeleteRouteTable"
            ],
            "Resource": [
                "arn:aws:ec2:*:{{111122223333}}:vpc/*",
                "arn:aws:ec2:*:{{111122223333}}:subnet/*",
                "arn:aws:ec2:*:{{111122223333}}:internet-gateway/*",
                "arn:aws:ec2:*:{{111122223333}}:route-table/*"
            ]
        },
        {
            "Sid": "ReadInstanceAndNetworkState",
            "Effect": "Allow",
            "Action": [
                "autoscaling:DescribeAutoScalingInstances",
                "ec2:Describe*"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Running the Automation
<a name="automation-ec2reset-executing"></a>

The following procedure describes how to run the `AWSSupport-ResetAccess` runbook by using the AWS Systems Manager console.

**Important**  
The following automation stops the instance. Stopping the instance can result in lost data on attached instance store volumes (if present). Stopping the instance can also cause the public IP to change, if no Elastic IP is associated. To avoid these configuration changes, use Run Command to reset access. For more information, see [Using EC2Rescue for Windows Server with Systems Manager Run Command](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2rw-ssm.html) in the *Amazon EC2 User Guide*.

**To run the AWSSupport-ResetAccess Automation**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Automation**.

1. Choose **Execute automation**.

1. In the **Automation document** section, choose **Owned by Amazon** from the list.

1. In the runbooks list, choose the button in the card for **AWSSupport-ResetAccess**, and then choose **Next**.

1. In the **Execute automation document** page, choose **Simple execution**.

1. In the **Document details** section, verify that **Document version** is set to the highest default version. For example, **$DEFAULT** or **3 (default)**.

1. In the **Input parameters** section, specify the following parameters: 

   1. For **InstanceId**, specify the ID of the unreachable instance. 

   1. For **SubnetId**, specify a subnet in an existing VPC in the same availability zone as the instance you specified. By default, Systems Manager creates a new VPC, but you can specify a subnet in an existing VPC if you want.
**Note**  
If you don't see the option to specify a subnet ID, verify that you are using the latest **Default** version of the runbook.

   1. For **EC2RescueInstanceType**, specify an instance type for the EC2Rescue instance. The default instance type is `t3.medium`.

   1. For **HelperInstanceProfileName**, specify the name of an existing IAM instance profile for the EC2Rescue helper instance. If you leave this empty, the automation attempts to create a helper IAM role and instance profile on your behalf, which requires additional permissions. For the permissions that instance profile needs, see [Granting permissions by using IAM policies](#automation-ec2reset-access-iam).

   1. For **AutomationAssumeRole**, choose the ARN of the IAM role that you granted the permissions described in [Granting permissions by using IAM policies](#automation-ec2reset-access-iam). If you leave this empty, the automation runs with the permissions of your own user or role, which must then include those same permissions.

1. (Optional) In the **Tags** area, apply one or more tag key name/value pairs to help identify the automation, for example `Key=Purpose,Value=ResetAccess`.

1. Choose **Execute**.

1. To monitor the automation progress, choose the running automation, and then choose the **Steps** tab. When the automation is finished, choose the **Descriptions** tab, and then choose **View output** to view the results. To view the output of individual steps, choose the **Steps** tab, and then choose **View Outputs** next to a step.

The runbook creates a backup AMI and a password-enabled AMI as part of the automation. All other resources created by the automation are automatically deleted, but these AMIs remain in your account. The AMIs are named using the following conventions:
+ Backup AMI: `AWSSupport-EC2Rescue:{{InstanceID}}`
+ Password-enabled AMI: AWSSupport-EC2Rescue: Password-enabled AMI from {{Instance ID}}

You can locate these AMIs by searching on the Automation execution ID.

For Linux, the new SSH private key for your instance is saved, encrypted, in Parameter Store. The parameter name is **/ec2rl/openssh/{{instance ID}}/key**.