# `AWSConfigRemediation-UpdateOpenSearchDomainSecurityGroups`

**Description**

The `AWSConfigRemediation-UpdateOpenSearchDomainSecurityGroups`
runbook updates the security group configuration on a given Amazon OpenSearch Service domain using
the [UpdateDomainConfig](../../../opensearch-service/latest/developerguide/configuration-api.md#configuration-api-actions-updatedomainconfig "../../../opensearch-service/latest/developerguide/configuration-api.md#configuration-api-actions-updatedomainconfig") API.

###### Note

AWS Security groups can only be applied to Amazon OpenSearch Service domains configured for
Amazon Virtual Private Cloud (VPC) Access, and not to Amazon OpenSearch Service domains
configured for Public Access.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-UpdateOpenSearchDomainSecurityGroups "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-UpdateOpenSearchDomainSecurityGroups")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- DomainName

Type: String

Description: (Required) The name of the Amazon OpenSearch Service domain that you want to
use to update security groups.

- SecurityGroupList

Type: StringList

Description: (Required) The security group IDs that you want to assign to
the Amazon OpenSearch Service domain.

- AutomationAssumeRole

Type: String

Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `es:DescribeDomain`
- `es:UpdateDomainConfig`

**Document Steps**

- `aws:executeScript` - Updates the security group configuration on
  the Amazon OpenSearch Service domain you specify in the `DomainName` parameter.
