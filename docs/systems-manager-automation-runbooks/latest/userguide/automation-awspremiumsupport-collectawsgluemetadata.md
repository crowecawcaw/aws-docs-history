

# `AWSPremiumSupport-CollectAWSGlueMetadata`
<a name="automation-awspremiumsupport-collectawsgluemetadata"></a>

## Description
<a name="automation-awspremiumsupport-collectawsgluemetadata-description"></a>

 The `AWSPremiumSupport-CollectAWSGlueMetadata` runbook gathers configuration metadata for your AWS Glue resources, including databases, crawlers, ETL jobs, development endpoints, triggers, workflows, and security configurations. The runbook writes this metadata to a JSON report in the Amazon S3 bucket that you choose. Your Technical Account Manager (TAM) or Specialist Technical Account Manager (STAM) reviews the report as part of the AWS Glue Operational Review. This review is a proactive assessment of your AWS Glue environment against AWS best practices. 

## How it works
<a name="automation-awspremiumsupport-collectawsgluemetadata-how-it-works"></a>

 A Python application collects the AWS Glue metadata. The application runs on a temporary Amazon EC2 instance. The runbook creates this temporary instance in a new isolated Amazon VPC using an embedded AWS CloudFormation template. The Amazon EC2 instance runs on a private-facing subnet with internet access through a Network Address Translation (NAT) gateway. The runbook accesses AWS services, including AWS Glue, Amazon EC2 Systems Manager, and Amazon S3, through Amazon VPC endpoints in the same Region. The NAT gateway retrieves metadata from Amazon S3 buckets that are associated with your AWS Glue resources in other AWS Regions. 

 When the runbook finishes, it deletes the CloudFormation stack and uploads the report to the Amazon S3 bucket of your choice. The runbook then attaches the report to the AWS Support case for this Operational Review. The JSON file is in the root folder of your Amazon S3 bucket. Contact your TAM or STAM if you have questions about the Operational Review and the collected metadata. 

**Important**  
 The AWS Glue Operational Review requires an AWS Enterprise Support Subscription. Before you run this runbook, contact your TAM or STAM for instructions. For more information about AWS Support plans, see [AWS Support Proactive Services](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html). 

**Important**  
 Make sure you have not reached the limit for Elastic IP (EIP) addresses, Amazon EC2 instances, or Amazon VPCs in your account or Region. If you need an additional EIP or Amazon VPC, complete the [Service Limit Increase request form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase). 

**Important**  
 AWS charges your account for the costs of the Amazon EC2 instance, its Amazon EBS volume, and the data transferred while this runbook runs. The time required depends on the amount and configuration of the AWS Glue resources in your account. By default, this runbook creates a `t2.micro` instance. If you have a large number of AWS Glue resources, increase the temporary instance size. 

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-CollectAWSGlueMetadata) 

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

## Document parameters
<a name="automation-awspremiumsupport-collectawsgluemetadata-parameters"></a>

`AutomationAssumeRole`  
 **Type:** AWS::IAM::Role::Arn   
 **Description:** (Optional) The ARN of the role that allows the Automation runbook to perform the actions on your behalf. If no role is specified, SSM Automation uses your current IAM user permissions context to execute this runbook.   
 **Allowed pattern:** `^$|^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/[\w+=/,.@-]+$` 

`Acknowledge`  
 **Type:** String   
 **Required:** Yes   
 **Description:** Write "Yes" if you acknowledge that this runbook collects metadata about your AWS Glue resources in the Region where you run it. The runbook stores the output file in the Amazon S3 bucket of your choice. For more information, see the Description section.   
 **Allowed pattern:** `^[Yy][Ee][Ss]$` 

`SupportCase`  
 **Type:** String   
 **Description:** (Optional) AWS Support case number provided by your TAM or STAM. The runbook updates the case and attaches the data collected. Contact your TAM or STAM for more information.   
 **Allowed pattern:** `^[0-9]{10}$`   
 **Default:** 0000000000 

`S3BucketName`  
 **Type:** String   
 **Description:** (Optional) The Amazon S3 bucket name in your account where you want to upload the data collected. Make sure the bucket policy does not grant any unnecessary read or write permissions to parties that do not need access to the file.   
 **Allowed pattern:** `^$|^[a-zA-Z0-9\.\-_]{1,255}$` 

`InstanceType`  
 **Type:** String   
 **Description:** (Optional) The size of the temporary Amazon EC2 instance type that runs the AWS Glue metadata gathering application.   
 **Valid values:** t2.micro \| t2.small \| t2.medium \| t2.large   
 **Default:** t2.micro 

`Module`  
 **Type:** String   
 **Description:** (Optional) AWS Glue Operational Review Module (remove any new lines, tabs, or white spaces when you input a new value). Only change this value if requested by your Specialist Technical Account Manager (STAM).   
 **Default:** A JSON configuration string that defines the modules to execute for metadata collection including metadata, catalog, crawler, ETL jobs, development endpoints, triggers, workflows, security configurations, and catalog encryption. 

## Required IAM permissions to collect the AWS Glue metadata
<a name="automation-awspremiumsupport-collectawsgluemetadata-iam-data-collector"></a>

 The AWS Glue data collector application requires the following actions to successfully run this runbook and upload the file to the private Amazon S3 bucket of your choice. An IAM role automatically grants these permissions to the temporary Amazon EC2 instance. 
+  `glue:List*` 
+  `glue:Query*` 
+  `glue:Get*` 
+  `glue:BatchGet*` 
+  `glue:CheckSchemaVersionValidity` 
+  `glue:SearchTables` 
+  `sts:GetCallerIdentity` 
+  `s3:PutObject` 
+  `s3:AbortMultipartUpload` 
+  `s3:ListBucket` 
+  `s3:ListAllMyBuckets` 
+  `s3:GetBucketLocation` 

## Required IAM permissions to run this runbook
<a name="automation-awspremiumsupport-collectawsgluemetadata-iam-runbook"></a>

 To run this runbook, the AutomationAssumeRole or your IAM user requires the following actions. These permissions are required to create a new temporary Amazon VPC and the Amazon EC2 instance using CloudFormation. 
+  `cloudformation:CreateStack` 
+  `cloudformation:DeleteStack` 
+  `cloudformation:DescribeStackEvents` 
+  `cloudformation:DescribeStacks` 
+  `cloudformation:UpdateStack` 
+  `ec2:AllocateAddress` 
+  `ec2:AssociateRouteTable` 
+  `ec2:AttachInternetGateway` 
+  `ec2:AuthorizeSecurityGroupEgress` 
+  `ec2:AuthorizeSecurityGroupIngress` 
+  `ec2:CreateInternetGateway` 
+  `ec2:CreateNatGateway` 
+  `ec2:CreateRoute` 
+  `ec2:CreateRouteTable` 
+  `ec2:CreateSecurityGroup` 
+  `ec2:CreateSubnet` 
+  `ec2:CreateTags` 
+  `ec2:CreateVpc` 
+  `ec2:CreateVpcEndpoint` 
+  `ec2:DeleteInternetGateway` 
+  `ec2:DeleteNatGateway` 
+  `ec2:DeleteRoute` 
+  `ec2:DeleteRouteTable` 
+  `ec2:DeleteSecurityGroup` 
+  `ec2:DeleteSubnet` 
+  `ec2:DeleteTags` 
+  `ec2:DeleteVpc` 
+  `ec2:DeleteVpcEndpoints` 
+  `ec2:DescribeAddresses` 
+  `ec2:DescribeImages` 
+  `ec2:DescribeInstances` 
+  `ec2:DescribeInstanceStatus` 
+  `ec2:DescribeInternetGateways` 
+  `ec2:DescribeNatGateways` 
+  `ec2:DescribeRouteTables` 
+  `ec2:DescribeSecurityGroups` 
+  `ec2:DescribeSubnets` 
+  `ec2:DescribeVpcEndpoints` 
+  `ec2:DescribeVpcs` 
+  `ec2:DetachInternetGateway` 
+  `ec2:DisassociateRouteTable` 
+  `ec2:ModifySubnetAttribute` 
+  `ec2:ModifyVpcAttribute` 
+  `ec2:RebootInstances` 
+  `ec2:ReleaseAddress` 
+  `ec2:RevokeSecurityGroupEgress` 
+  `ec2:RunInstances` 
+  `ec2:TerminateInstances` 
+  `iam:AddRoleToInstanceProfile` 
+  `iam:AttachRolePolicy` 
+  `iam:CreateInstanceProfile` 
+  `iam:CreateRole` 
+  `iam:DeleteInstanceProfile` 
+  `iam:DeleteRole` 
+  `iam:DeleteRolePolicy` 
+  `iam:DetachRolePolicy` 
+  `iam:GetInstanceProfile` 
+  `iam:GetRole` 
+  `iam:GetRolePolicy` 
+  `iam:PassRole` 
+  `iam:PutRolePolicy` 
+  `iam:RemoveRoleFromInstanceProfile` 
+  `s3:GetAccountPublicAccessBlock` 
+  `s3:GetBucketAcl` 
+  `s3:GetBucketPolicyStatus` 
+  `s3:GetBucketPublicAccessBlock` 
+  `s3:ListBucket` 
+  `ssm:DescribeAutomationExecutions` 
+  `ssm:DescribeInstanceInformation` 
+  `ssm:GetDocument` 
+  `ssm:GetParameters` 
+  `ssm:ListCommandInvocations` 
+  `ssm:ListCommands` 
+  `ssm:SendCommand` 
+  `support:AddAttachmentsToSet` 
+  `support:AddCommunicationToCase` 
+  `support:DescribeCases` 

The following example policy shows the least-privilege permissions required for the `AutomationAssumeRole`. Replace `REGION`, `ACCOUNTID`, and `S3_BUCKET_NAME` with your own values:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CloudFormationStackAccess",
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "cloudformation:DescribeStackEvents",
                "cloudformation:DescribeStacks",
                "cloudformation:UpdateStack"
            ],
            "Resource": "arn:aws:cloudformation:{{REGION}}:{{ACCOUNTID}}:stack/AWSPremiumSupport-CollectAWSGlueMetadata-*/*"
        },
        {
            "Sid": "EC2NetworkingAccess",
            "Effect": "Allow",
            "Action": [
                "ec2:AllocateAddress",
                "ec2:AssociateRouteTable",
                "ec2:AttachInternetGateway",
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:CreateInternetGateway",
                "ec2:CreateNatGateway",
                "ec2:CreateRoute",
                "ec2:CreateRouteTable",
                "ec2:CreateSecurityGroup",
                "ec2:CreateSubnet",
                "ec2:CreateTags",
                "ec2:CreateVpc",
                "ec2:CreateVpcEndpoint",
                "ec2:DeleteInternetGateway",
                "ec2:DeleteNatGateway",
                "ec2:DeleteRoute",
                "ec2:DeleteRouteTable",
                "ec2:DeleteSecurityGroup",
                "ec2:DeleteSubnet",
                "ec2:DeleteTags",
                "ec2:DeleteVpc",
                "ec2:DeleteVpcEndpoints",
                "ec2:DescribeAddresses",
                "ec2:DescribeImages",
                "ec2:DescribeInstances",
                "ec2:DescribeInstanceStatus",
                "ec2:DescribeInternetGateways",
                "ec2:DescribeNatGateways",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcEndpoints",
                "ec2:DescribeVpcs",
                "ec2:DetachInternetGateway",
                "ec2:DisassociateRouteTable",
                "ec2:ModifySubnetAttribute",
                "ec2:ModifyVpcAttribute",
                "ec2:RebootInstances",
                "ec2:ReleaseAddress",
                "ec2:RevokeSecurityGroupEgress",
                "ec2:RunInstances",
                "ec2:TerminateInstances"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": "{{REGION}}"
                }
            }
        },
        {
            "Sid": "IAMRoleAccess",
            "Effect": "Allow",
            "Action": [
                "iam:AddRoleToInstanceProfile",
                "iam:AttachRolePolicy",
                "iam:CreateInstanceProfile",
                "iam:CreateRole",
                "iam:DeleteInstanceProfile",
                "iam:DeleteRole",
                "iam:DeleteRolePolicy",
                "iam:DetachRolePolicy",
                "iam:GetInstanceProfile",
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:PutRolePolicy",
                "iam:RemoveRoleFromInstanceProfile"
            ],
            "Resource": [
                "arn:aws:iam::{{ACCOUNTID}}:role/AWSPremiumSupport-CollectAWSGlueMetadata-*",
                "arn:aws:iam::{{ACCOUNTID}}:instance-profile/AWSPremiumSupport-CollectAWSGlueMetadata-*"
            ]
        },
        {
            "Sid": "PassRoleToEC2",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{ACCOUNTID}}:role/AWSPremiumSupport-CollectAWSGlueMetadata-*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ec2.amazonaws.com"
                }
            }
        },
        {
            "Sid": "S3BucketAccess",
            "Effect": "Allow",
            "Action": [
                "s3:GetAccountPublicAccessBlock",
                "s3:GetBucketAcl",
                "s3:GetBucketPolicyStatus",
                "s3:GetBucketPublicAccessBlock",
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::{{S3_BUCKET_NAME}}"
        },
        {
            "Sid": "SSMAutomationAccess",
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeAutomationExecutions",
                "ssm:DescribeInstanceInformation",
                "ssm:GetDocument",
                "ssm:GetParameters",
                "ssm:ListCommandInvocations",
                "ssm:ListCommands",
                "ssm:SendCommand"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": "{{REGION}}"
                }
            }
        },
        {
            "Sid": "SupportCaseAccess",
            "Effect": "Allow",
            "Action": [
                "support:AddAttachmentsToSet",
                "support:AddCommunicationToCase",
                "support:DescribeCases"
            ],
            "Resource": "*"
        }
    ]
}
```

## Document steps
<a name="automation-awspremiumsupport-collectawsgluemetadata-steps"></a>

1.  **aws:branch** - Branches the workflow based on whether you provided an Amazon S3 bucket name or left the parameter empty. 

1.  **aws:assertAwsResourceProperty** - Checks if the Amazon S3 bucket exists. 

1.  **aws:executeScript** - Checks if the Amazon S3 bucket to which the runbook uploads the report allows anonymous read or write access permissions. Make sure that only authorized people have access to the file. 

1.  **aws:branch** - Terminates the automation if the script detects that the Amazon S3 bucket is publicly accessible. Make sure that only authorized people have access to the file. 

1.  **aws:executeScript** - Gets the CloudFormation template content body from the Automation runbook attachment. The CloudFormation template is used to create the temporary Amazon EC2 instance. 

1.  **aws:createStack** - Creates the CloudFormation Stack containing the Amazon VPC, private subnet, route table, Amazon EC2 instance role and profile, and Amazon VPC endpoints. 

1.  **aws:executeAwsApi** - Creates the temporary Amazon EC2 instance in the new Amazon VPC. The Amazon EC2 instance runs on a private-facing subnet with internet access through a NAT gateway. 

1.  **aws:waitForAwsResourceProperty** - Waits until the Amazon EC2 instance created by the CloudFormation template is ready. 

1.  **aws:executeAwsApi** - Gets the temporary Amazon EC2 instance ID. 

1.  **aws:waitForAwsResourceProperty** - Waits until the temporary Amazon EC2 instance passes status checks. 

1.  **aws:waitForAwsResourceProperty** - Waits until the temporary Amazon EC2 instance is managed by SSM. If this step times out or fails, the runbook reboots the instance. 

1.  **aws:executeAwsApi** - Reboots the temporary Amazon EC2 instance if it is not managed by SSM. 

1.  **aws:waitForAwsResourceProperty** - Waits until the temporary Amazon EC2 instance is managed by SSM after reboot. 

1.  **aws:runCommand** - Installs and executes the application to collect the AWS Glue metadata. 

1.  **aws:runCommand** - Uploads the metadata report to the Amazon S3 bucket of your choice. 

1.  **aws:runCommand** - Attaches the metadata report to the AWS Support case. The script compresses and splits the report into 5 MB parts. The script can attach a maximum of 12 files to the AWS Support case. 

1.  **aws:executeAwsApi** - Describes the CloudFormation Stack events if the runbook fails to create or update the CloudFormation Stack. 

1.  **aws:deleteStack** - Deletes the CloudFormation Stack. 