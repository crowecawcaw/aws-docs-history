# CreateCentralizationRuleForOrganization

Creates a centralization rule that applies across an AWS Organization. This operation
can only be called by the organization's management account or a delegated administrator
account.

## Request Syntax

```
POST /CreateCentralizationRuleForOrganization HTTP/1.1
Content-type: application/json

{
   "Rule": {
      "Destination": {
         "Account": "`string`",
         "DestinationLogsConfiguration": {
            "BackupConfiguration": {
               "KmsKeyArn": "`string`",
               "Region": "`string`"
            },
            "LogsEncryptionConfiguration": {
               "EncryptionConflictResolutionStrategy": "`string`",
               "EncryptionStrategy": "`string`",
               "KmsKeyArn": "`string`"
            }
         },
         "Region": "`string`"
      },
      "Source": {
         "Regions": [ "`string`" ],
         "Scope": "`string`",
         "SourceLogsConfiguration": {
            "EncryptedLogGroupStrategy": "`string`",
            "LogGroupSelectionCriteria": "`string`"
         }
      }
   },
   "RuleName": "`string`",
   "Tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[Rule](#API_CreateCentralizationRuleForOrganization_RequestSyntax "#API_CreateCentralizationRuleForOrganization_RequestSyntax")**

The configuration details for the organization-wide centralization rule, including the
source configuration and the destination configuration to centralize telemetry data across the
organization.

Type: [CentralizationRule](API_CentralizationRule.md "API_CentralizationRule.md") object

Required: Yes

**[RuleName](#API_CreateCentralizationRuleForOrganization_RequestSyntax "#API_CreateCentralizationRuleForOrganization_RequestSyntax")**

A unique name for the organization-wide centralization rule being created.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[0-9A-Za-z-_.#/]+`

Required: Yes

**[Tags](#API_CreateCentralizationRuleForOrganization_RequestSyntax "#API_CreateCentralizationRuleForOrganization_RequestSyntax")**

The key-value pairs to associate with the organization telemetry rule resource for
categorization and management purposes.

Type: String to string map

Map Entries: Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "RuleArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[RuleArn](#API_CreateCentralizationRuleForOrganization_ResponseSyntax "#API_CreateCentralizationRuleForOrganization_ResponseSyntax")**

The Amazon Resource Name (ARN) of the created organization centralization rule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

Indicates you don't have permissions to perform the requested operation. The user or role
that is making the request must have at least one IAM permissions policy attached that grants
the required permissions. For more information, see [Access management for AWS resources](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the
IAM user guide.

**amznErrorType**

The name of the exception.

HTTP Status Code: 400

**ConflictException**

The requested operation conflicts with the current state of the specified resource or
with another request.

**ResourceId**

The identifier of the resource which is in conflict with the requested operation.

**ResourceType**

The type of the resource which is in conflict with the requested operation.

HTTP Status Code: 409

**InternalServerException**

Indicates the request has failed to process because of an unknown server error,
exception, or failure.

**amznErrorType**

The name of the exception.

**retryAfterSeconds**

The number of seconds to wait before retrying the request.

HTTP Status Code: 500

**ServiceQuotaExceededException**

The requested operation would exceed the allowed quota for the specified resource type.

**amznErrorType**

The name of the exception.

**QuotaCode**

The code for the exceeded service quota.

**ResourceId**

The identifier of the resource which exceeds the service quota.

**ResourceType**

The type of the resource which exceeds the service quota.

**ServiceCode**

The code for the service of the exceeded quota.

HTTP Status Code: 402

**TooManyRequestsException**

The request throughput limit was exceeded.

HTTP Status Code: 429

**ValidationException**

Indicates input validation failed. Check your request parameters and retry the request.

**Errors**

The errors in the input which caused the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md "../../../goto/cli2/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md "../../../goto/DotNetSDKV4/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md "../../../goto/boto3/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/CreateCentralizationRuleForOrganization.md")
