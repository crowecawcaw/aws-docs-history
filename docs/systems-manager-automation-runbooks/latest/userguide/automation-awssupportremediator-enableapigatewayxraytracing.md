

# `AWSSupportRemediator-EnableApiGatewayXRayTracing`

**Description**

Enables active tracing with AWS X-Ray for the specified Amazon API Gateway stage.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [API Gateway REST API stages should have AWS X-Ray tracing enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-3).

If the `AWSServiceRoleForAPIGateway` service-linked role does not exist in the account, API Gateway creates it automatically when active tracing is enabled. For more information about service-linked roles for API Gateway, see [Using Service-Linked Roles for API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/using-service-linked-roles.html).

If the API Gateway stage does not exist or active tracing with X-Ray is already enabled, the automation completes successfully without making changes.

Enabling active tracing might incur additional X-Ray charges. For more information about pricing, see [X-Ray pricing](https://aws.amazon.com/xray/pricing/).

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ RestApiId

  Type: String

  Description: (Required) The identifier of the API Gateway REST API that contains the stage.
+ StageName

  Type: String

  Description: (Required) The name of the API Gateway stage on which to enable X-Ray tracing.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `apigateway:GET`
+ `apigateway:PATCH`

**Document Steps**

1. **validateApiGateway** - Validates whether the API Gateway stage exists and whether active tracing with X-Ray is already enabled.

1. **branchOnChangeRequired** - Branches on whether the API Gateway stage requires modification.

1. **enableTracing** - Enables active tracing with X-Ray for the API Gateway stage by patching the `tracingEnabled` property to `true`.

**Outputs**
+ validateApiGateway.ChangeRequired: Whether the API Gateway stage requires a change.
+ validateApiGateway.InitialTracingEnabledSetting: The value of the stage's `tracingEnabled` property before execution.
+ validateApiGateway.ValidationMessage: A message describing the validation result.