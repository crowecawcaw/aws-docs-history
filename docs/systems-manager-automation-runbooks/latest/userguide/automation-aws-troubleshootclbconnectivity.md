# `AWSSupport-TroubleshootCLBConnectivity`

**Description**

The `AWSSupport-TroubleshootCLBConnectivity` runbook help you
troubleshoot connectivity issues between a Classic Load Balancer (CLB) and Amazon Elastic Compute Cloud (Amazon EC2)
instances. Also, connectivity issues between a client and the CLB are reviewed. This
runbook also reviews health checks for the CLB, verifies that best practices are
being followed, and creates a troubleshooting dashboard for you. Optionally, you can
upload the automation output to an Amazon Simple Storage Service (Amazon S3) bucket. However, this runbook
does not support uploading output to S3 buckets that are publicly accessible. We
recommend creating a temporary S3 bucket for this automation.

###### Important

Using this runbook might incur charges for the dashboard that is created. For
more information, see [Amazon CloudWatch
Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/")

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootCLBConnectivity "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootCLBConnectivity")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- InvestigationType

Type: String

Valid values: Best Practices | Connectivity Issues | Troubleshooting
Dashboard

Description: (Required) The operations you want the runbook to perform.

- LoadBalancerName

Type: String

Description: (Required) The name of the CLB.

- S3Location

Type: String

Description: (Optional) The name of the S3 bucket you want to send the
automation results to. Publicly accessible buckets are not supported. If
your S3 bucket uses server-side encryption, the user or role running this
automation must have `kms:GenerateDataKey` permissions for the
AWS KMS key.

- S3LocationPrefix

Type: String

Description: (Optional) The Amazon S3 key prefix (subfolder) you want to upload
the automation output to. The format output is stored in the following
format:
amzn-s3-demo-bucket/`S3LocationPrefix`/{{`InvestigationType`}}\_{{automation:`EXECUTION_ID`}}.txt.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:DescribeInstances`
- `ec2:DescribeNetworkAcls`
- `ec2:DescribeNetworkInterfaces`
- `ec2:DescribeRouteTables`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeVpcAttribute`
- `ec2:DescribeVpcs`
- `ec2:DescribeSubnets`
- `elasticloadbalancing:DescribeLoadBalancers`
- `elasticloadbalancing:DescribeLoadBalancerPolicies`
- `elasticloadbalancing:DescribeInstanceHealth`
- `elasticloadbalancing:DescribeLoadBalancerAttributes`
- `iam:ListRoles`
- `cloudwatch:PutDashboard`
- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `ssm:DescribeAutomationExecutions`
- `ssm:DescribeAutomationStepExecutions`
- `ssm:DescribeInstanceInformation`
- `ssm:DescribeInstanceProperties`
- `ssm:GetDocument`
- `ssm:ListCommands`
- `ssm:ListCommandInvocations`
- `ssm:ListDocuments`
- `ssm:SendCommand`
- `s3:GetBucketAcl`
- `s3:GetBucketPolicyStatus`
- `s3:GetPublicAccessBlock`
- `s3:PutObject`

**Document Steps**

- `aws:executeScript` - Verifies that the CLB you specify in the
  `LoadBalancerName` parameter exists.
- `aws:branch` - Branches based on the value specified for the
  `InvestigationType` parameter.
- `aws:executeScript` - Performs connectivity checks to the CLB.
- `aws:executeScript` - Verifies that the CLB configuration adheres
  to Elastic Load Balancing best practices.
- `aws:executeScript` - Creates an Amazon CloudWatch dashboard for your CLB.
- `aws:executeScript` - Creates a text file with the results of the
  automation and uploads it to the Amazon S3 bucket you specify in the
  `S3Location` parameter.

**Outputs**

RunBestPractices.Summary

RunConnectivityChecks.Summary

CreateTroubleshootingDashboard.Output

UploadOutputToS3.Output
