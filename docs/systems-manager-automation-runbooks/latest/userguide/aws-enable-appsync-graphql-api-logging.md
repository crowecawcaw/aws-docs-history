# `AWS-EnableAppSyncGraphQLApiLogging`

**Description**

The `AWS-EnableAppSyncGraphQLApiLogging` runbook enables field-level logging and request-level logging for the AWS AppSync GraphQL API you specify. The runbook will apply changes to the specified GraphQL API even if logging has already been enabled.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableAppSyncGraphQLApiLogging "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableAppSyncGraphQLApiLogging")

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

- ApiId

Type: String

Description: (Required) The ID of the API you want to enable logging for.

- FieldLogLevel

Type: String

Valid Values: ERROR | ALL

Description: (Required) The field logging level.

- CloudWatchLogsRoleArn

Type: String

Description: (Required) The ARN of the service role that AWS AppSync assumes to publish to Amazon CloudWatch Logs.

- ExcludeVerboseContent

Type: Boolean

Default: False

Description: (Optional) Set to `True` to exclude information such as headers, context, and evaluated mapping templates, regardless of logging level.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `appsync:GetGraphqlApi`
- `appsync:UpdateGraphqlApi`
- `iam:PassRole`

**Document Steps**

- aws:executeAwsApi - Gathers the authentication type and configuration information relevant for the primary authentication type.
- aws:branch - Branches based on the authentication type.
- aws:executeAwsApi - Updates the logging configuration for the AWS AppSync GraphQL API based on the values specified for the runbook's input parameters.

**Outputs**

- `EnableApiLoggingWithApiKeyOrAwsIamAuthorization.UpdateGraphQLApiResponse`: Response from the `UpdateGraphqlApi` call.
- `EnableApiLoggingWithLambdaAuthorization.UpdateGraphQLApiResponse`: Response from the `UpdateGraphqlApi` call.
- `EnableApiLoggingWithCognitoAuth.UpdateGraphQLApiResponse`: Response from the `UpdateGraphqlApi` call.
- `EnableApiLoggingWithOpenIdAuthorization.UpdateGraphQLApiResponse`: Response from the `UpdateGraphqlApi` call.
