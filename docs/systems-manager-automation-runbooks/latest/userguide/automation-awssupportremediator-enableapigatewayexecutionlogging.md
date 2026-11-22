

# `AWSSupportRemediator-EnableApiGateWayExecutionLogging`

**Description**

Enables execution logging for the specified stage of an Amazon API Gateway REST or WebSocket API by setting the logging level at the stage and method or route level.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon API Gateway Not Logging Execution Logs](https://docs.aws.amazon.com/awssupport/latest/user/operational-excellence-checks.html#api-gw-execution-logging-enabled).

If the API Gateway stage does not exist or execution logging is already enabled, the automation completes successfully without making changes.

This runbook only modifies the stage's `loggingLevel` (REST) or `LoggingLevel` (WebSocket). It does not change `dataTraceEnabled` / `DataTraceEnabled`, nor any other method or route settings such as caching, metrics, or throttling — the runbook preserves these as-is.

Before running this automation, configure an account-level Amazon CloudWatch Logs role for API Gateway so that API Gateway can write logs on your behalf. The role must meet all of the following requirements:
+ The role must exist and have a trust policy that allows `apigateway.amazonaws.com` to assume it.
+ The role must have permissions to write to CloudWatch Logs. The AWS-managed `AmazonAPIGatewayPushToCloudWatchLogs` policy provides the required permissions.

API Gateway uses the same account-level role for both REST and WebSocket APIs. For more information, see [Set up CloudWatch logging for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html). When you run this automation, API Gateway automatically creates a CloudWatch Logs log group for the stage.

This automation verifies the presence of an account-level CloudWatch Logs role ARN, but it does not validate the role's existence, trust policy, or attached permissions. If any of these are missing or incorrect, the automation completes successfully but API Gateway does not write logs.

Updating the stage redeploys the API configuration, which can briefly affect availability for high-traffic APIs. Schedule this automation during a low-traffic window when possible.

To revert the change, set the stage logging level to `OFF` by using the API Gateway console or the `UpdateStage` API. This automation does not disable execution logging. Reverting the logging level does not delete the CloudWatch Logs log group that API Gateway created; delete it manually to stop retaining log data and incurring storage charges.

Enabling execution logging might increase your CloudWatch Logs costs because every API request writes log events that incur ingestion and storage charges. For more information about pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

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
+ ApiStageArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the API Gateway stage.
+ LogLevel

  Type: String

  Description: (Required) The logging level for execution logging. `ERROR` logs errors only. `INFO` logs all events.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `apigateway:GET`
+ `apigateway:PATCH`

**Document Steps**

1. **validateApiGateway** - Validates that the API Gateway stage exists and determines whether execution logging needs to be enabled at the stage, method, or route level. When a change is required, also verifies that an account-level Amazon CloudWatch Logs role ARN is configured for API Gateway.

1. **branchOnChangeRequired** - Branches on whether execution logging needs to be enabled and on the API Gateway type (REST or WebSocket).

1. **updateRestApi** - Enables execution logging for the specified REST API Gateway stage by applying the patch operations computed in `validateApiGateway`. The patch operations set the logging level at the stage default (`/*/*`) when missing and override any method-level setting that is not `INFO` or `ERROR`.

1. **updateWebSocketApi** - Enables execution logging for the specified WebSocket API Gateway stage by applying the default route settings and per-route settings computed in `validateApiGateway`.

**Outputs**
+ validateApiGateway.ChangeRequired: Whether execution logging needs to be enabled.
+ validateApiGateway.ValidationMessage: A message describing the validation result.
+ validateApiGateway.ApiGatewayType: The API Gateway type (`restapis` or `apis`).
+ validateApiGateway.ApiId: The API Gateway API identifier.
+ validateApiGateway.StageName: The API Gateway stage name.
+ validateApiGateway.InitialConfiguration: The initial logging configuration of the API Gateway stage.