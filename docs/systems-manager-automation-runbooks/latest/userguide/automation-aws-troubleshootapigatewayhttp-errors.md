# `AWSSupport-TroubleshootAPIGatewayHttpErrors`

**Description**

The **AWSSupport-TroubleshootAPIGatewayHttpErrors** runbook helps troubleshoot 5XX/4XX errors when invoking a deployed Amazon API Gateway REST API by parsing access and/or execution logs and analyzing errors to provide remediation steps via re:Post articles and AWS documentation.

###### Important

This runbook has the following limitations:

- Logging must be enabled. See [Set up Amazon CloudWatch API logging using the API Gateway console](../../../apigateway/latest/developerguide/set-up-logging.md#set-up-access-logging-using-console "../../../apigateway/latest/developerguide/set-up-logging.md#set-up-access-logging-using-console").
- Logs must have been enabled prior to the error(s) occurring. Log capturing and analysis cannot be done retrospectively.
- Errors covered: 500, 502, 503, 504, 401, 403, 429.
- Only REST APIs are supported. WebSocket and HTTP (v2) are not covered by this runbook.

###### Important

Using this runbook might incur extra charges against your AWS account for the Amazon CloudWatch Logs captured by your REST API, and CloudWatch Logs Insights used in the analysis. See [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/") for more details on the charges that may be incurred. If the `aws:deletestack` step fails, go to the CloudFormation console to manually delete the stack. The stack name created by this runbook begins with `AWSSupport-TroubleshootAPIGatewayHttpErrors`. For information about deleting CloudFormation stacks, see [Deleting a stack](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md") in the AWS CloudFormation User Guide.

**How does it work?**

The runbook performs the following validation and analysis steps:

- Validates that the specified REST API exists and you have the necessary permissions.
- Validates that the specified stage exists in the API.
- Validates that the specified resource path exists in the API.
- Validates that the specified HTTP method exists for the resource.
- Analyzes CloudWatch Logs for the specified parameters and time range to identify errors and provide remediation recommendations.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootAPIGatewayHttpErrors "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootAPIGatewayHttpErrors")

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
- `logs:CreateLogGroup`
- `logs:CreateLogStream`
- `logs:DescribeLogGroups`
- `logs:DescribeLogStreams`
- `logs:PutLogEvents`
- `logs:StartQuery`
- `logs:GetQueryResults`
  Example IAM policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "apigateway:GET",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:PutLogEvents",
                "logs:StartQuery",
                "logs:GetQueryResults"
            ],
            "Resource": "*"
        }
    ]
}

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-TroubleshootAPIGatewayHttpErrors`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayHttpErrors/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayHttpErrors/description") in Systems Manager under Documents.
2. Select **Execute automation.**
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
       (IAM) role that allows SSM Automation to perform the actions on
       your behalf. If no role is specified, SSM Automation uses
       the permissions of the user who starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **RestApiId (Required):**
     - Description: (Required) The API ID for the API that requires troubleshooting. Must be a 10-character alphanumeric string.
     - Type: `String`
     - Allowed Pattern:
       `^[a-zA-Z0-9]{10}$`

   - **StageName (Required):**
     - Description: (Required) The name of the deployed stage. Must be 1-128 characters containing letters, numbers, underscores, or hyphens.
     - Type: `String`
     - Allowed Pattern:
       `^[a-zA-Z0-9_\\-]{1,128}$`

   - **ResourcePath (Optional):**
     - Description: (Optional) The resource path for which method is configured. Examples: `/`, `/store/items`, `/{resource}`.
     - Type: `String`
     - Default: `/`

   - **HttpMethod (Optional):**
     - Description: (Optional) The method for the configured resource path.
     - Type: `String`
     - Allowed Values:
       `[ANY, DELETE, HEAD, OPTIONS, GET, POST, PUT, PATCH]`
     - Default: `GET`

   - **StartTime (Optional):**
     - Description: (Optional) The start date and time for querying the CloudWatch Logs. Format: `yyyy-MM-ddTHH:mm:ss` in UTC timezone. If not specified, defaults to 3 days before current time.
     - Type: `String`
     - Allowed Pattern:
       `^$|^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T(2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]$`
     - Default: `""`

   - **EndTime (Optional):**
     - Description: (Optional) The end date and time for querying the CloudWatch Logs. Format: `yyyy-MM-ddTHH:mm:ss` in UTC timezone. If not specified, defaults to current time.
     - Type: `String`
     - Allowed Pattern:
       `^$|^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T(2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]$`
     - Default: `""`

   - **AccessLogs (Optional):**
     - Description: (Optional) Whether access logs should be analyzed.
     - Type: `Boolean`
     - Allowed Values:
       `[true, false]`
     - Default: `false`

   - **RequestId (Optional):**
     - Description: (Optional) The request ID for request where error was observed. Must be a valid UUID format.
     - Type: `String`
     - Allowed Pattern:
       `^$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
     - Default: `""`

4. Select **Execute.**
5. The automation initiates.
6. The document performs the following steps:
   - **CheckApiExists**:

   Validates that the provided REST API exists and you have the necessary permissions to access it.
   - **CheckStageExists**:

   Validates that the provided stage name exists in the given API and retrieves access log group information.
   - **CheckResourceExists**:

   Validates that the provided resource path exists in the API and retrieves the resource ID.
   - **CheckMethodExists**:

   Validates that the provided HTTP method exists for the specified resource.
   - **AnalyseLogs**:

   Searches for logs using the provided parameters and returns recommendations based on any errors found. This step analyzes both execution and access logs (if enabled) to identify 4XX and 5XX errors and provides specific remediation guidance.

7. After completion, review the **Outputs** section for the detailed results of the execution, including error analysis and remediation recommendations.
   **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayHttpErrors/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAPIGatewayHttpErrors/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
