# `AWSSupport-TroubleshootAPIGatewayLambdaInvocation`

###### Description

The `AWSSupport-TroubleshootAPIGatewayLambdaInvocation` runbook helps you troubleshoot Amazon API Gateway integrations with AWS Lambda functions in HTTP and REST APIs. The runbook supports Lambda functions used as an integration or as an authorizer, and covers the following use cases:

- **Insufficient or missing permissions:** Identifies missing permissions in Lambda resource policies or IAM roles.
- **Lambda function throttling:** Detects throttling caused by concurrency limits and provides recommendations.
- **Lambda integration timeout:** Analyzes timeout issues and suggests optimization strategies.
- **Lambda function errors:** Identifies function errors and guides you to log analysis.
- **Lambda malformed response:** Detects response format issues for Lambda integrations and authorizers.
- **Invalid configuration:** Validates API Gateway and Lambda configuration.

###### Limitations

This runbook has the following limitations:

- The runbook doesn't support cross-account Lambda scenarios.
- The runbook doesn't analyze API Gateway mapping templates, regex patterns, or integration responses.
- The runbook supports only Lambda authorizers. It doesn't support IAM authorizers or Amazon Cognito authorizers.
- The runbook doesn't cover client-side throttling on API Gateway.

###### Additional costs

Using this runbook queries metrics from Amazon CloudWatch. Standard CloudWatch charges might apply to your AWS account for the metrics queried during the analysis. For more information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### How it works

The runbook performs the following validation and analysis steps:

- Validates that the specified API Gateway API, stage, and route or resource exist, and confirms that a Lambda integration or authorizer is configured.
- Checks whether API Gateway has sufficient permissions to invoke the Lambda function by evaluating the Lambda resource policy and the IAM role using IAM policy simulation.
- Fetches API Gateway metrics (`4xxError`, `5xxError`, `Count`, `Latency`, and `IntegrationLatency`) from CloudWatch to detect API-level errors.
- Fetches Lambda metrics (`Invocations`, `Throttles`, `Errors`, `Duration`, and `ConcurrentExecutions`) from CloudWatch and correlates them with the API Gateway errors.
- Analyzes Lambda authorizer and integration response formats when API errors persist but no Lambda errors are detected.
- Compiles a summary report with findings, recommendations, and relevant references.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootAPIGatewayLambdaInvocation "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootAPIGatewayLambdaInvocation")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `apigateway:GET`
- `apigatewayv2:GetApi`
- `apigatewayv2:GetRoute`
- `apigatewayv2:GetStage`
- `apigatewayv2:GetAuthorizer`
- `apigatewayv2:GetIntegration`
- `lambda:GetFunction`
- `lambda:GetAccountSettings`
- `lambda:GetPolicy`
- `lambda:GetProvisionedConcurrencyConfig`
- `lambda:GetFunctionConcurrency`
- `iam:GetRole`
- `iam:GetContextKeysForPrincipalPolicy`
- `iam:GetContextKeysForCustomPolicy`
- `iam:SimulatePrincipalPolicy`
- `iam:SimulateCustomPolicy`
- `cloudwatch:GetMetricData`
  Example IAM policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "APIGatewayReadAccess",
            "Effect": "Allow",
            "Action": [
                "apigateway:GET",
                "apigatewayv2:GetApi",
                "apigatewayv2:GetRoute",
                "apigatewayv2:GetStage",
                "apigatewayv2:GetAuthorizer",
                "apigatewayv2:GetIntegration"
            ],
            "Resource": [
                "arn:aws:apigateway:*::/restapis/*",
                "arn:aws:apigateway:*::/apis/*"
            ]
        },
        {
            "Sid": "LambdaReadAccess",
            "Effect": "Allow",
            "Action": [
                "lambda:GetFunction",
                "lambda:GetPolicy",
                "lambda:GetProvisionedConcurrencyConfig",
                "lambda:GetFunctionConcurrency",
                "lambda:GetAccountSettings"
            ],
            "Resource": "*"
        },
        {
            "Sid": "IAMReadAndSimulate",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:GetContextKeysForPrincipalPolicy",
                "iam:GetContextKeysForCustomPolicy",
                "iam:SimulatePrincipalPolicy",
                "iam:SimulateCustomPolicy"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CloudWatchMetricsRead",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:GetMetricData"
            ],
            "Resource": "*"
        }
    ]
}

```

###### Note

The IAM user or role that starts the runbook requires the following actions:

- `iam:ListRoles`
- `iam:PassRole`
- `ssm:DescribeAutomationExecutions`
- `ssm:DescribeAutomationStepExecutions`
- `ssm:DescribeDocument`
- `ssm:GetAutomationExecution`
- `ssm:GetDocument`
- `ssm:ListDocuments`
- `ssm:StartAutomationExecution`

###### Instructions

Follow these steps to configure the automation:

1. Open [AWSSupport-TroubleshootAPIGatewayLambdaInvocation](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayLambdaInvocation/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayLambdaInvocation/description") in Systems Manager under Documents.
2. Choose Execute automation.
3. For the input parameters, enter the following:

   - **AutomationAssumeRole (Optional):**

   The Amazon Resource Name (ARN) of the IAM role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your permissions.
   - **ApiId (Required):**

   The API ID of the API Gateway API that requires troubleshooting.
   - **HttpMethod (Required):**

   The HTTP method for the resource or route that requires troubleshooting. Allowed values: `ANY`, `DELETE`, `HEAD`, `OPTIONS`, `GET`, `POST`, `PUT`, `PATCH`, `$default`.
   - **RouteIdOrResourceId (Required):**

   The Route ID (HTTP API) or Resource ID (REST API) with a Lambda integration or authorizer that requires troubleshooting. For example, `dsyrv84` for an HTTP API route or `jklob2` for a REST API resource.
   - **StageName (Required):**

   The stage that the API is deployed to.
   - **StartTime (Optional):**

   Start time in UTC to identify the timeframe to query. The format must be `yyyy-MM-ddTHH:mm:ss` (for example, `1970-01-01T00:00:00`). The start time must not be more than 30 days in the past. If this input is missing or invalid, the runbook defaults to 2 days before the end time. If no end time is specified, the runbook defaults to 2 days before the current time.
   - **EndTime (Optional):**

   End time in UTC to identify the timeframe to query. The format must be `yyyy-MM-ddTHH:mm:ss` (for example, `1970-01-01T00:00:00`). The end time must not be more than 2 days after the start time. If this input is missing or invalid, the runbook defaults to the current time.

4. Choose Execute.
5. The automation initiates.
6. The document performs the following steps:

   - **`ValidateResourcesAndInputs`**:

   Verifies that the API Gateway API, stage, and route or resource exist, and confirms that a Lambda integration or authorizer is configured. Validates the time range inputs and extracts Lambda function and API details.
   - **`CheckAPIGatewayLambdaInvokePermissions`**:

   Simulates the IAM role permissions and evaluates the Lambda resource policy to determine whether API Gateway is authorized to invoke the Lambda function. Generates example policies when permissions are insufficient.
   - **`GetAPIMetrics`**:

   Retrieves API Gateway metrics (`4xxError`, `5xxError`, `Count`, `Latency`, and `IntegrationLatency`) from CloudWatch for the specified time range and identifies API-level error patterns.
   - **`GetLambdaMetrics`**:

   Retrieves Lambda metrics (`Invocations`, `Throttles`, `Errors`, `Duration`, and `ConcurrentExecutions`) from CloudWatch and correlates them with the API Gateway error timestamps.
   - **`CompareAPIGatewayAndLambdaMetrics`**:

   Analyzes and correlates the API Gateway and Lambda metrics to identify throttling patterns, timeout scenarios, and unhandled Lambda function errors. Determines the root cause of the invocation issue.
   - **`AuthorizerAndIntegrationTroubleshooting`**:

   When API errors persist but no Lambda errors are detected, analyzes the Lambda authorizer and integration response format, and provides recommendations for proper Lambda function output formatting.
   - **`CompileResults`**:

   Compiles a summary report of the findings, validation issues, permission problems, and troubleshooting recommendations with actionable guidance and relevant references.

7. After completion, review the Outputs section for the detailed results of the execution.

###### References

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayLambdaInvocation/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayLambdaInvocation/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
