# `AWSConfigRemediation-DeleteOpenSearchDomain`

**Description**

The `AWSConfigRemediation-DeleteOpenSearchDomain` runbook deletes the
given Amazon OpenSearch Service domain using the [DeleteDomain](../../../opensearch-service/latest/developerguide/configuration-api.md#configuration-api-actions-deletedomain "../../../opensearch-service/latest/developerguide/configuration-api.md#configuration-api-actions-deletedomain") API.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteOpenSearchDomain "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteOpenSearchDomain")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- DomainName

Type: String

Allowed values: (\d{12}/)?[a-z]{1}[a-z0-9-]{2,28}

Description: (Required) The name of the Amazon OpenSearch Service domain that you want to
delete.

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
- `es:DeleteDomain`
- `es:DescribeDomain`

**Document Steps**

- `aws:executeScript` - Accepts the Amazon OpenSearch Service domain name as input,
  deletes it, and verifies the deletion.
