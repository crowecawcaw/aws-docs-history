# `AWSSupport-TroubleshootSUSERegistration`

**Description**

The `AWSSupport-TroubleshootSUSERegistration` runbook helps you to
identify why registering an Amazon Elastic Compute Cloud (Amazon EC2) SUSE Linux Enterprise Server instance with SUSE Update
Infrastructure failed. The automation output provides steps to resolve, or helps you
troubleshoot, the issue. If the instance passes all checks during the automation,
the instance is registered with SUSE Update Infrastructure.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootSUSERegistration "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootSUSERegistration")

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

Description: (Required) The ID of the Amazon EC2 instance you want to
troubleshoot.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:DescribeInstanceProperties`
- `ssm:DescribeInstanceInformation`
- `ssm:ListCommandInvocations`
- `ssm:SendCommand`
- `ssm:ListCommands`
  **Document Steps**

- `aws:assertAwsResourceProperty` - Checks if the Amazon EC2 instance
  is managed by AWS Systems Manager.
- `aws:runCommand` - Checks if the Amazon EC2 instance platform is
  SLES.
- `aws:runCommand` - Checks if the package
  `cloud-regionsrv-client` version is greater than or equal to
  the required version 9.0.10.
- `aws:runCommand` - Checks if the symbolic link for base product
  is broken, and fixes the link it it is broken.
- `aws:runCommand` - Checks if the hosts file
  (`/etc/hosts`) contains records for
  `smt-ec2-suscloud.net`. The automation removes any duplicate
  entries.
- `aws:runCommand` - Checks if the `curl` command is
  installed.
- `aws:runCommand` - Checks if the Amazon EC2 instance can access the
  Instance Metadata Service (IMDS) address 169.254.169.254.
- `aws:runCommand` - Checks if the Amazon EC2 instance has a billing
  code or AWS Marketplace product code.
- `aws:runCommand` - Checks if the Amazon EC2 instance can reach at
  least 1 regional server over HTTPS.
- `aws:runCommand` - Checks if the Amazon EC2 instance can reach the
  Subscription Management Tool (SMT) servers over HTTP.
- `aws:runCommand` - Checks if the Amazon EC2 instance can reach the
  Subscription Management Tool (SMT) servers over HTTPS.
- `aws:runCommand` - Checks if the Amazon EC2 instance can reach the
  `smt-ec2.susecloud.net` address over HTTPS.
- `aws:runCommand` - Registers the Amazon EC2 instance with SUSE
  Update Infrastructure.
- `aws:executeScript` - Gathers and outputs the output of all the
  previous steps.
