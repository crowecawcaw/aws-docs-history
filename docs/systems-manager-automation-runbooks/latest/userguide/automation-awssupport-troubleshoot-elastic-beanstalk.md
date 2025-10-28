# `AWSSupport-TroubleshootElasticBeanstalk`

**Description**

The `AWSSupport-TroubleshootElasticBeanstalk` runbook helps you
troubleshoot the potential reasons why your AWS Elastic Beanstalk environment is in a
`Degraded` or `Severe` state. This automation checks the
following AWS resources associated with your Elastic Beanstalk environment:

- Configuration details for a load balancer, AWS CloudFormation stack, Amazon EC2 Auto Scaling
  group, Amazon Elastic Compute Cloud (Amazon EC2) instances, and virtual private cloud (VPC).
- Network configuration issues with the associated security group rules,
  route tables, and network access control lists (ACLs) associated with your
  subnets.
- Verifies connectivity to the Elastic Beanstalk endpoints and public internet
  access.
- Verifies the status of the load balancer.
- Verifies the status of the Amazon EC2 instances.
- Retrieves a log bundle from your Elastic Beanstalk environment, and optionally uploads
  the files to Support.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootElasticBeanstalk "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootElasticBeanstalk")

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

- ApplicationName

Type: String

Description: (Required) The name of your Elastic Beanstalk application.

- EnvironmentName

Type: String

Description: (Required) The name of your Elastic Beanstalk environment.

- AWSS3UploaderLink

Type: String

Description: (Optional) A URL provided to you by Support to upload the log
bundle from your Elastic Beanstalk environment to. This option is only available to
customers who have purchased an Support plan, and have opened a Support
case.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `autoscaling:Describe*`
- `cloudformation:Describe*`
- `cloudformation:Estimate*`
- `cloudformation:Get*`
- `cloudformation:List*`
- `cloudformation:Validate*`
- `cloudwatch:Describe*`
- `cloudwatch:Get*`
- `cloudwatch:List*`
- `ec2:Describe*`
- `elasticbeanstalk:Check*`
- `elasticbeanstalk:Describe*`
- `elasticbeanstalk:List*`
- `elasticbeanstalk:RetrieveEnvironmentInfo*`
- `elasticbeanstalk:RequestEnvironmentInfo*`
- `elasticloadbalancing:Describe*`
- `rds:Describe*`
- `s3:Get*`
- `s3:List*`
- `sns:Get*`
- `sns:List*`

**Document Steps**

- `aws:executeScript` - Verifies the AWS Identity and Access Management (IAM) principal
  who started the automation has the requisite permissions to perform all of
  the actions defined in the runbook.
- `aws:branch` - Branches the workflow based on the results of
  the previous step.
- `aws:executeScript` - Collects information about the Elastic Beanstalk
  environment including the load balancer, AWS CloudFormation stack, Auto Scaling group, Amazon EC2
  instances, and VPC configuration.
- `aws:executeScript` - Checks for network connectivity issues
  with the route tables and ACLs associated with the subnets in your
  VPC.
- `aws:executeScript` - Checks for network connectivity issues
  with the security group rules associated with your Amazon EC2 instances.
- `aws:executeScript` - Verifies the status checks for the Amazon EC2
  instances.
- `aws:executeScript` - Generates a link for a log bundle of your
  Elastic Beanstalk environment.
- `aws:executeScript` - Uploads log bundle to Support.
- `aws:executeScript` - Outputs a report of action items to help
  you troubleshoot issues that might be affecting the status of your Elastic Beanstalk
  environment.
