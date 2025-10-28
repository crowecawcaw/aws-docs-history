# `AWS-DeregisterAMIs`

**Description**

The `AWS-DeregisterAMIs` runbook helps you deregister Amazon Machine Images
(AMIs) by specifying the tag that you've applied to your AMIs.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DeregisterAMIs "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DeregisterAMIs")

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

- DryRun

Type: String

Valid values: Yes | No

Description: (Required) Checks whether you have the required permissions
for the action, without actually making the request, and provides an error
response.

- RetainNumber

Type: String

Description: (Optional) The number of AMIs that you want to retain.
Don't specify a value for this parameter if you specify a value for
`Age`.

- Age

Type: String

Description: (Optional) The number of previous days of AMIs that you
want to retain. Don't specify a value for this parameter if you specify a
value for `RetainNumber`.

- TagKey

Type: String

Description: (Required) The key of the tag assigned to the AMIs that
you want to deregister.

- TagValue

Type: String

Description: (Required) The value of the tag assigned to the AMIs that
you want to deregister.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:DeregisterImage`
- `ec2:DescribeImages`

**Document Steps**

- `aws:executeAwsApi` - Validates the values that you specify for
  the runbook input parameters.
- `aws:executeAwsApi` - Deregisters AMIs using the tag that you
  specify using the `TagKey` and `TagValue` parameters.
