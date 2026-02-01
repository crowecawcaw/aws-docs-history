• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Run the EC2Rescue tool on unreachable

instances

EC2Rescue can help you diagnose and troubleshoot problems on Amazon Elastic Compute Cloud (Amazon EC2)
instances for Linux and Windows Server. You can run the tool manually, as described in
[Using EC2Rescue
for Linux Server](../../../AWSEC2/latest/UserGuide/Linux-Server-EC2Rescue.md "../../../AWSEC2/latest/UserGuide/Linux-Server-EC2Rescue.md") and [Using
EC2Rescue for Windows Server](../../../AWSEC2/latest/WindowsGuide/Windows-Server-EC2Rescue.md "../../../AWSEC2/latest/WindowsGuide/Windows-Server-EC2Rescue.md"). Or, you can run the tool automatically
by using Systems Manager Automation and the **`AWSSupport-ExecuteEC2Rescue`** runbook. Automation
is a tool in AWS Systems Manager. The **`AWSSupport-ExecuteEC2Rescue`** runbook is designed
to perform a combination of Systems Manager actions, CloudFormation actions, and Lambda functions
that automate the steps normally required to use EC2Rescue.

You can use the **`AWSSupport-ExecuteEC2Rescue`** runbook to troubleshoot
and potentially remediate different types of operating system (OS) issues.
Instances with encypted root volumes are not supported. See the following topics
for a complete list:

**Windows**: See _Rescue
Action_ in [Using EC2Rescue
for Windows Server with the Command Line](../../../AWSEC2/latest/WindowsGuide/ec2rw-cli.md#ec2rw-rescue "../../../AWSEC2/latest/WindowsGuide/ec2rw-cli.md#ec2rw-rescue").

**Linux** and **macOS**: Some EC2Rescue for Linux modules detect and attempt to
remediate issues. For more information, see the [`aws-ec2rescue-linux`](https://github.com/awslabs/aws-ec2rescue-linux/tree/master/docs "https://github.com/awslabs/aws-ec2rescue-linux/tree/master/docs") documentation for each module
on GitHub.

## How it works

Troubleshooting an instance with Automation and the **`AWSSupport-ExecuteEC2Rescue`** runbook works
as follows:

- You specify the ID of the unreachable instance and start the
  runbook.
- The system creates a temporary VPC, and then runs a series of
  Lambda functions to configure the VPC.
- The system identifies a subnet for your temporary VPC in the same
  Availability Zone as your original instance.
- The system launches a temporary, SSM-enabled helper
  instance.
- The system stops your original instance, and creates a backup. It
  then attaches the original root volume to the helper
  instance.
- The system uses Run Command to run EC2Rescue on the helper instance.
  EC2Rescue identifies and attempts to fix issues on the attached,
  original root volume. When finished, EC2Rescue reattaches the root
  volume back to the original instance.
- The system restarts your original instance, and terminates the
  temporary instance. The system also terminates the temporary VPC and
  the Lambda functions created at the start of the automation.

## Before you begin

Before you run the following Automation, do the following:

- Copy the instance ID of the unreachable instance. You will specify
  this ID in the procedure.
- Optionally, collect the ID of a subnet in the same availability
  zone as your unreachable instance. The EC2Rescue instance will be
  created in this subnet. If you don’t specify a subnet, then
  Automation creates a new temporary VPC in your AWS account. Verify
  that your AWS account has at least one VPC available. By default,
  you can create five VPCs in a Region. If you already created five
  VPCs in the Region, the automation fails without making changes to
  your instance. For more information about Amazon VPC quotas, see [VPC and Subnets](../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-vpcs-subnets "../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-vpcs-subnets") in the
  _Amazon VPC User Guide_.
- Optionally, you can create and specify an AWS Identity and Access Management (IAM) role
  for Automation. If you don't specify this role, then Automation runs
  in the context of the user who ran the automation.

### Granting

`AWSSupport-EC2Rescue` permissions to perform actions
on your instances

EC2Rescue needs permission to perform a series of actions on your
instances during the automation. These actions invoke the AWS Lambda,
IAM, and Amazon EC2 services to safely and securely attempt to remediate
issues with your instances. If you have Administrator-level permissions
in your AWS account and/or VPC, you might be able to run the
automation without configuring permissions, as described in this
section. If you don't have Administrator-level permissions, then you or
an administrator must configure permissions by using one of the
following options.

- [Granting
  permissions by using IAM policies](#automation-ec2rescue-access-iam "#automation-ec2rescue-access-iam")
- [Granting
  permissions by using an CloudFormation template](#automation-ec2rescue-access-cfn "#automation-ec2rescue-access-cfn")

#### Granting

permissions by using IAM policies

You can either attach the following IAM policy to your user,
group, or role as an inline policy; or, you can create a new IAM
managed policy and attach it to your user, group, or role. For more
information about adding an inline policy to your user, group, or
role see [Working With Inline Policies](../../../IAM/latest/UserGuide/access_policies_inline-using.md "../../../IAM/latest/UserGuide/access_policies_inline-using.md"). For more information
about creating a new managed policy, see [Working With Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-using.md "../../../IAM/latest/UserGuide/access_policies_managed-using.md").

###### Note

If you create a new IAM managed policy, you must also attach
the **AmazonSSMAutomationRole**
managed policy to it so that your instances can communicate with
the Systems Manager API.

**IAM Policy for
AWSSupport-EC2Rescue**

Replace `account ID` with your own
information.

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
 "ec2:Describe*",
 "autoscaling:DescribeAutoScalingInstances"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```

#### Granting

permissions by using an CloudFormation template

CloudFormation automates the process of creating IAM roles and policies
by using a preconfigured template. Use the following procedure to
create the required IAM roles and policies for the EC2Rescue
Automation by using CloudFormation.

###### To create the required IAM roles and policies for

EC2Rescue

1. Download [`AWSSupport-EC2RescueRole.zip`](samples/AWSSupport-EC2RescueRole.md "samples/AWSSupport-EC2RescueRole.md")
   and extract the
   `AWSSupport-EC2RescueRole.json` file
   to a directory on your local machine.
2. If your AWS account is in a special partition, edit the
   template to change the ARN values to those for your
   partition.

For example, for the China Regions, change all cases of
`arn:aws` to `arn:aws-cn`. 3. Sign in to the AWS Management Console and open the CloudFormation console at
[https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/"). 4. Choose **Create stack**, **With
new resources (standard)**. 5. On the **Create stack** page, for
**Prerequisite - Prepare template**,
choose **Template is ready**. 6. For **Specify template**, choose
**Upload a template file**. 7. Choose **Choose file**, and then browse
to and select the
`AWSSupport-EC2RescueRole.json` file
from the directory where you extracted it. 8. Choose **Next**. 9. On the **Specify stack details** page,
for **Stack name** field, enter a name to
identify this stack, and then choose
**Next**. 10. (Optional) In the **Tags** area, apply
one or more tag key name/value pairs to the stack.

Tags are optional metadata that you assign to a resource.
Tags enable you to categorize a resource in different ways,
such as by purpose, owner, or environment. For example, you
might want to tag a stack to identify the type of tasks it
runs, the types of targets or other resources involved, and
the environment it runs in. 11. Choose **Next** 12. On the **Review** page, review the stack
details, and then scroll down and choose the **I
acknowledge that CloudFormation might create IAM
resources** option. 13. Choose **Create stack**.

CloudFormation shows the **CREATE_IN_PROGRESS**
status for a few minutes. The status changes to
**CREATE_COMPLETE** after the stack has
been created. You can also choose the refresh icon to check
the status of the create process. 14. In the **Stacks** list, choose the option
button the stack you just created, and then choose the
**Outputs** tab. 15. Note the **Value**. The is the ARN of the
AssumeRole. You specify this ARN when you run the Automation
in the next procedure, [Running the
Automation](#automation-ec2rescue-executing "#automation-ec2rescue-executing").

## Running the

Automation

###### Important

The following automation stops the unreachable instance. Stopping the
instance can result in lost data on attached instance store volumes (if
present). Stopping the instance can also cause the public IP to change,
if no Elastic IP is associated.

###### To run the `AWSSupport-ExecuteEC2Rescue`

Automation

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Automation**.
3. Choose **Execute automation**.
4. In the **Automation document** section, choose
   **Owned by Amazon** from the list.
5. In the runbooks list, choose the button in the card for
   `**AWSSupport-ExecuteEC2Rescue**`,
   and then choose **Next**.
6. In the **Execute automation document** page,
   choose **Simple execution**.
7. In the **Document details** section, verify that
   **Document version** is set to the highest
   default version. For example, **$DEFAULT** or
   **3 (default)**.
8. In the **Input parameters** section, specify the
   following parameters:
   1. For **UnreachableInstanceId**, specify
      the ID of the unreachable instance.
   2. (Optional) For **EC2RescueInstanceType**,
      specify an instance type for the EC2Rescue instance. The
      default instance type is `t2.medium`.
   3. For **AutomationAssumeRole**, if you
      created roles for this Automation by using the CloudFormation
      procedure described earlier in this topic, then choose the
      ARN of the AssumeRole that you created in the CloudFormation
      console.
   4. (Optional) For **LogDestination**,
      specify an S3 bucket if you want to collect operating
      system-level logs while troubleshooting your instance. Logs
      are automatically uploaded to the specified bucket.
   5. For **SubnetId**, specify a subnet in an
      existing VPC in the same availability zone as the
      unreachable instance. By default, Systems Manager creates a new VPC,
      but you can specify a subnet in an existing VPC if you
      want.

   ###### Note

   If you don't see the option to specify a bucket or a
   subnet ID, verify that you are using the latest
   **Default** version of the
   runbook.

9. (Optional) In the **Tags** area, apply one or
   more tag key name/value pairs to help identify the automation, for
   example `Key=Purpose,Value=EC2Rescue`.
10. Choose **Execute**.

The runbook creates a backup AMI as part of the automation. All other
resources created by the automation are automatically deleted, but this AMI
remains in your account. The AMI is named using the following
convention:

Backup AMI:
AWSSupport-EC2Rescue:`UnreachableInstanceId`

You can locate this AMI in the Amazon EC2 console by searching on the
Automation execution ID.
