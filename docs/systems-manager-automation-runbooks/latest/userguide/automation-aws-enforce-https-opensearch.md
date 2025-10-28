# `AWSConfigRemediation-EnforceHTTPSOnOpenSearchDomain`

**Description**

The `AWSConfigRemediation-EnforceHTTPSOnOpenSearchDomain` runbook
enables `EnforceHTTPS` on a given Amazon OpenSearch Service domain using the [UpdateDomainConfig](../../../opensearch-service/latest/developerguide/configuration-api.md#configuration-api-actions-updatedomainconfig "../../../opensearch-service/latest/developerguide/configuration-api.md#configuration-api-actions-updatedomainconfig") API.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnforceHTTPSOnOpenSearchDomain "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnforceHTTPSOnOpenSearchDomain")

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
use to enforce HTTPS.

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

- `aws:executeScript` - Enables the `EnforceHTTPS`
  endpoint option on the Amazon OpenSearch Service domain you specify in the
  `DomainName` parameter.
