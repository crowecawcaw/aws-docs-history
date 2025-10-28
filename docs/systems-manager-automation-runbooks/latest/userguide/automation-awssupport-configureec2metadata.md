# `AWSSupport-ConfigureEC2Metadata`

**Description**

This runbook helps you configure instance metadata service (IMDS) options for
Amazon Elastic Compute Cloud (Amazon EC2) instances. Using this runbook, you can configure the
following:

- Enforce the use of IMDSv2 for instance metadata.
- Configure the `HttpPutResponseHopLimit` value.
- Allow or deny instance metadata access.
  For more information about instance metadata, see [Configuring the
  Instance Metadata Service](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md") in the _Amazon EC2 User Guide_.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ConfigureEC2Metadata "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ConfigureEC2Metadata")

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

- EnforceIMDSv2

Type: String

Valid values: required | optional

Default: optional

Description: (Optional) Enforce IMDSv2. If you choose
`required`, the Amazon EC2 instance will only use IMDSv2. If you
choose `optional`, you can choose between IMDSv1 and IMDSv2 for
metadata access.

###### Important

If you enforce IMDSv2, applications that use IMDSv1 might not function
correctly. Before enforcing IMDSv2, make sure your applications that use
IMDS are upgraded to a version that support IMDSv2. For information
about Instance Metadata Service Version 2 (IMDSv2), see [Configuring the Instance Metadata Service](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md") in the
_Amazon EC2 User Guide_.

- HttpPutResponseHopLimit

Type: Integer

Valid values: 0-64

Default: 0

Description: (Optional) The desired HTTP PUT response hop limit value
(1-64) for instance metadata requests. This value controls the number of
hops that the PUT response can traverse. To prevent the response from
traveling outside of the instance, specify `1` for the parameter
value.

- InstanceId

Type: String

Description: (Required) The ID of the Amazon EC2 instance whose metadata
settings you want to configure.

- MetadataAccess

Type: String

Valid values: enabled | disabled

Default: enabled

Description: (Optional) Allow or deny instance metadata access in the
Amazon EC2 instance. If you specify `disabled`, all other parameters
will be ignored and the metadata access will be denied for the instance.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:DescribeInstances`
- `ec2:ModifyInstanceMetadataOptions`
- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`

**Document Steps**

1. branchOnMetadataAccess - Branches automation based on the value of
   `MetadataAccess` parameter.
2. disableMetadataAccess - Calls the ModifyInstanceMetadataOptions API action
   to disable metadata endpoint access.
3. branchOnHttpPutResponseHopLimit - Branches automation based on the value
   of `HttpPutResponseHopLimit` parameter.
4. maintainHopLimitAndConfigureImdsVersion - If
   `HttpPutResponseHopLimit` is 0, maintains current hop limit
   and changes other metadata options.
5. waitBeforeAssertingIMDSv2State - Waits 30 seconds before asserting IMDSv2
   status.
6. setHopLimitAndConfigureImdsVersion - If
   `HttpPutResponseHopLimit` is greater than 0, configures the
   metadata options using the given input parameters.
7. waitBeforeAssertingHopLimit - Waits 30 seconds before asserting metadata
   options.
8. assertHopLimit - Asserts the `HttpPutResponseHopLimit` property
   is set to the value you specified.
9. branchVerificationOnIMDSv2Option - Branches verification based on the
   value of `EnforceIMDSv2` parameter.
10. assertIMDSv2IsOptional - Asserts `HttpTokens` value set to
    `optional`.
11. assertIMDSv2IsEnforced - Asserts `HttpTokens` value set to
    `required`.
12. waitBeforeAssertingMetadataState - Waits 30 seconds before asserting the
    metadata state is disabled.
13. assertMetadataIsDisabled - Asserts metadata is
    `disabled`.
14. describeMetadataOptions - Gets the metadata options after the changes
    you've specified have been applied.

**Outputs**

describeMetadataOptions.State

describeMetadataOptions.MetadataAccess

describeMetadataOptions.IMDSv2

describeMetadataOptions.HttpPutResponseHopLimit
