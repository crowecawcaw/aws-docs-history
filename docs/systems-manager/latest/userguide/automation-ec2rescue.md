

# Run the EC2Rescue tool on unreachable instances
<a name="automation-ec2rescue"></a>

EC2Rescue can help you diagnose and troubleshoot problems on Amazon Elastic Compute Cloud (Amazon EC2) instances for Linux and Windows Server. You can run the tool manually, as described in [Using EC2Rescue for Linux Server](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Linux-Server-EC2Rescue.html) and [Using EC2Rescue for Windows Server](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/Windows-Server-EC2Rescue.html). Or, you can run the tool automatically by using Systems Manager Automation and the **`AWSSupport-ExecuteEC2Rescue`** runbook. Automation is a tool in AWS Systems Manager. The **`AWSSupport-ExecuteEC2Rescue`** runbook is designed to perform a combination of Systems Manager actions and CloudFormation actions that automate the steps normally required to use EC2Rescue. 

You can use the **`AWSSupport-ExecuteEC2Rescue`** runbook to troubleshoot and potentially remediate different types of operating system (OS) issues. Instances with encypted root volumes are not supported. See the following topics for a complete list:

**Windows**: See *Rescue Action* in [Using EC2Rescue for Windows Server with the Command Line](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2rw-cli.html#ec2rw-rescue).

**Linux** and **macOS**: Some EC2Rescue for Linux modules detect and attempt to remediate issues. For more information, see the [`aws-ec2rescue-linux`](https://github.com/awslabs/aws-ec2rescue-linux/tree/master/docs) documentation for each module on GitHub.

## How it works
<a name="automation-ec2rescue-how"></a>

Troubleshooting an instance with Automation and the **`AWSSupport-ExecuteEC2Rescue`** runbook works as follows:
+ You specify the ID of the unreachable instance and start the runbook.
+ The system creates a temporary VPC by deploying the EC2Rescue CloudFormation stack.
+ The system identifies a subnet for your temporary VPC in the same Availability Zone as your original instance.
+ The system launches a temporary, SSM-enabled helper instance.
+ The system stops your original instance, and creates a backup. It then attaches the original root volume to the helper instance.
+ The system uses Run Command to run EC2Rescue on the helper instance. EC2Rescue identifies and attempts to fix issues on the attached, original root volume. When finished, EC2Rescue reattaches the root volume back to the original instance.
+ The system restarts your original instance, and terminates the temporary instance. The system also terminates the temporary VPC and deletes the EC2Rescue CloudFormation stack created at the start of the automation.

## Before you begin
<a name="automation-ec2rescue-begin"></a>

Before you run the following Automation, do the following:
+ Copy the instance ID of the unreachable instance. Specify this ID in the procedure.
+ Optionally, collect the ID of a subnet in the same availability zone as your unreachable instance. The EC2Rescue instance will be created in this subnet. If you don’t specify a subnet, then Automation creates a new temporary VPC in your AWS account. Verify that your AWS account has at least one VPC available. By default, you can create five VPCs in a Region. If you already created five VPCs in the Region, the automation fails without making changes to your instance. For more information about Amazon VPC quotas, see [VPC and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-vpcs-subnets) in the *Amazon VPC User Guide*.
+ Optionally, you can create and specify an AWS Identity and Access Management (IAM) role for Automation. If you don't specify this role, then Automation runs in the context of the user who ran the automation.

### Granting `AWSSupport-EC2Rescue` permissions to perform actions on your instances
<a name="automation-ec2rescue-access"></a>

EC2Rescue needs permission to perform a series of actions on your instances during the automation. These actions invoke the IAM, Amazon EC2, and CloudFormation services to safely and securely attempt to remediate issues with your instances. If you have Administrator-level permissions in your AWS account and/or VPC, you might be able to run the automation without configuring permissions, as described in this section. If you don't have Administrator-level permissions, then you or an administrator must configure permissions as described in [Granting permissions by using IAM policies](#automation-ec2rescue-access-iam).

#### Granting permissions by using IAM policies
<a name="automation-ec2rescue-access-iam"></a>

You can either attach the following IAM policy to your user, group, or role as an inline policy; or, you can create a new IAM managed policy and attach it to your user, group, or role. For more information about adding an inline policy to your user, group, or role see [Working With Inline Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_inline-using.html). For more information about creating a new managed policy, see [Working With Managed Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-using.html).

**Note**  
Attach the **AmazonSSMAutomationRole** managed policy alongside the following policy, whether you add the following policy inline or as a new managed policy. The automation depends on permissions that **AmazonSSMAutomationRole** grants and the following policy doesn't, including the Systems Manager API permissions, `ec2:RunInstances`, and the CloudFormation permissions used to create and delete the temporary EC2Rescue stack.

**Note**  
This policy assumes that you specify an existing instance profile in the `HelperInstanceProfileName` parameter when you run the automation. The IAM role inside that instance profile is a separate identity from the one you attach the following policy to. It must trust `ec2.amazonaws.com` and have the **AmazonSSMManagedInstanceCore** policy attached, so that the EC2Rescue helper instance can register with Systems Manager and receive commands. Don't attach **AmazonSSMAutomationRole** to it, because the helper instance doesn't call those APIs. If you set `LogDestination`, that role additionally needs `s3:ListBucket` on the bucket, and `s3:PutObject` with `s3:AbortMultipartUpload` on the `AWSSupport-ExecuteEC2Rescue` prefix within it. If you leave `HelperInstanceProfileName` empty, the automation creates a helper IAM role and instance profile on your behalf, which requires permissions to create and configure IAM resources that this policy doesn't grant.

**IAM Policy for AWSSupport-EC2Rescue**

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
<a name="automation-ec2rescue-executing"></a>

**Important**  
The following automation stops the unreachable instance. Stopping the instance can result in lost data on attached instance store volumes (if present). Stopping the instance can also cause the public IP to change, if no Elastic IP is associated.

**To run the `AWSSupport-ExecuteEC2Rescue` Automation**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Automation**.

1. Choose **Execute automation**.

1. In the **Automation document** section, choose **Owned by Amazon** from the list.

1. In the runbooks list, choose the button in the card for `AWSSupport-ExecuteEC2Rescue`, and then choose **Next**.

1. In the **Execute automation document** page, choose **Simple execution**.

1. In the **Document details** section, verify that **Document version** is set to the highest default version. For example, **$DEFAULT** or **3 (default)**.

1. In the **Input parameters** section, specify the following parameters: 

   1. For **UnreachableInstanceId**, specify the ID of the unreachable instance. 

   1. (Optional) For **EC2RescueInstanceType**, specify an instance type for the EC2Rescue instance. The default instance type is `t2.medium`.

   1. For **AutomationAssumeRole**, choose the ARN of the IAM role that you granted the permissions described in [Granting permissions by using IAM policies](#automation-ec2rescue-access-iam). If you leave this empty, the automation runs with the permissions of your own user or role, which must then include those same permissions.

   1. For **HelperInstanceProfileName**, enter the name of the instance profile that you prepared for the EC2Rescue helper instance.

   1. (Optional) For **LogDestination**, specify an S3 bucket if you want to collect operating system-level logs while troubleshooting your instance. Logs are automatically uploaded to the specified bucket.

   1. For **SubnetId**, specify a subnet in an existing VPC in the same availability zone as the unreachable instance. By default, Systems Manager creates a new VPC, but you can specify a subnet in an existing VPC if you want.
**Note**  
If you don't see the option to specify a bucket or a subnet ID, verify that you are using the latest **Default** version of the runbook.

1. (Optional) In the **Tags** area, apply one or more tag key name/value pairs to help identify the automation, for example `Key=Purpose,Value=EC2Rescue`.

1. Choose **Execute**.

The runbook creates a backup AMI as part of the automation. All other resources created by the automation are automatically deleted, but this AMI remains in your account. The AMI is named using the following convention:

Backup AMI: AWSSupport-EC2Rescue:{{UnreachableInstanceId}}

You can locate this AMI in the Amazon EC2 console by searching on the Automation execution ID.