# `AWSSupport-TroubleshootCFNCustomResource`

**Description**

The
`AWSSupport-TroubleshootCFNCustomResource`
runbook helps diagnose why an
AWS CloudFormation stack failed in creating, updating, or deleting a custom resource. The runbook checks the service token used for the custom resource and the error message that was returned. After reviewing the details for the custom resource, the runbook output provides an explanation of the stack behavior and troubleshooting steps for the custom resource.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootCFNCustomResource "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootCFNCustomResource")

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

- StackName

Type: String

Description: (Required) The name of the AWS CloudFormation stack where the custom resource failed.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `cloudformation:DescribeStacks`
- `cloudformation:DescribeStackEvents`
- `cloudformation:ListStackResources`
- `ec2:DescribeRouteTables`
- `ec2:DescribeNatGateways`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeVpcs`
- `ec2:DescribeVpcEndpoints`
- `ec2:DescribeSubnets`
- `logs:FilterLogEvents`

**Document Steps**

- `validateCloudFormationStack`

* Verifies that the AWS CloudFormation stack exists in the same AWS account and AWS Region.

- `checkCustomResource`

* Analyzes the AWS CloudFormation stack, checks the failed custom resource, and outputs information about how to troubleshoot the failed custom resource.
