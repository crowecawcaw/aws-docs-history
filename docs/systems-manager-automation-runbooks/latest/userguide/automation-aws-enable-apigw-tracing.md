# `AWSConfigRemediation-EnableAPIGatewayTracing`

**Description**

The
`AWSConfigRemediation-EnableAPIGatewayTracing`
runbook enables
tracing on an Amazon API Gateway (API Gateway) stage. AWS Config must be enabled in the AWS Region
where you run this automation.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableAPIGatewayTracing "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableAPIGatewayTracing")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf.

- StageArn

Type: String

Description: (Required) The Amazon Resource Name (ARN) of the API Gateway stage
you want to enable tracing on.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `config:GetResourceConfigHistory`
- `apigateway:GET`
- `apigateway:PATCH`

**Document Steps**

- `aws:executeScript`

* Enables tracing on the API Gateway stage
  specified in the
  `StageArn`
  parameter.
