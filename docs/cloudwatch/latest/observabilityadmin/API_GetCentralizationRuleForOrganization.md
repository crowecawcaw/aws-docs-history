# GetCentralizationRuleForOrganization

Retrieves the details of a specific organization centralization rule. This operation can
only be called by the organization's management account or a delegated administrator
account.

## Request Syntax

```
POST /GetCentralizationRuleForOrganization HTTP/1.1
Content-type: application/json

{
   "RuleIdentifier": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[RuleIdentifier](#API_GetCentralizationRuleForOrganization_RequestSyntax "#API_GetCentralizationRuleForOrganization_RequestSyntax")**

The identifier (name or ARN) of the organization centralization rule to retrieve.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CentralizationRule": {
      "Destination": {
         "Account": "***string***",
         "DestinationLogsConfiguration": {
            "BackupConfiguration": {
               "KmsKeyArn": "***string***",
               "Region": "***string***"
            },
            "LogsEncryptionConfiguration": {
               "EncryptionConflictResolutionStrategy": "***string***",
               "EncryptionStrategy": "***string***",
               "KmsKeyArn": "***string***"
            }
         },
         "Region": "***string***"
      },
      "Source": {
         "Regions": [ "***string***" ],
         "Scope": "***string***",
         "SourceLogsConfiguration": {
            "EncryptedLogGroupStrategy": "***string***",
            "LogGroupSelectionCriteria": "***string***"
         }
      }
   },
   "CreatedRegion": "***string***",
   "CreatedTimeStamp": ***number***,
   "CreatorAccountId": "***string***",
   "FailureReason": "***string***",
   "LastUpdateTimeStamp": ***number***,
   "RuleArn": "***string***",
   "RuleHealth": "***string***",
   "RuleName": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CentralizationRule](#API_GetCentralizationRuleForOrganization_ResponseSyntax "#API_GetCentralizationRuleForOrganization_ResponseSyntax")**

The configuration details for the organization centralization rule.

Type: [CentralizationRule](API_CentralizationRule.md "API_CentralizationRule.md") object

**[CreatedRegion](#API_GetCentralizationRuleForOrganization_ResponseSyntax "#API_GetCentralizationRuleForOrganization_ResponseSyntax")**

The AWS region where the organization centralization rule was created.

Type: String

Length Constraints: Minimum length of 1.

**[CreatedTimeStamp](#API_GetCentralizationRuleForOrganization_ResponseSyntax "#API_GetCentralizationRuleForOrganization_ResponseSyntax")**

The timestamp when the organization centralization rule was created.

Type: Long

**[CreatorAccountId](#API_GetCentralizationRuleForOrganization_ResponseSyntax "#API_GetCentralizationRuleForOrganization_ResponseSyntax")**

The AWS Account that created the organization centralization rule.

Type: String

**[FailureReason](#API_GetCentralizationRuleForOrganization_ResponseSyntax "#API_GetCentralizationRuleForOrganization_ResponseSyntax")**

The reason why an organization centralization rule is marked UNHEALTHY.

Type: String

Valid Values: `TRUSTED_ACCESS_NOT_ENABLED | DESTINATION_ACCOUNT_NOT_IN_ORGANIZATION | INTERNAL_SERVER_ERROR`

**[LastUpdateTimeStamp](#API_GetCentralizationRuleForOrganization_ResponseSyntax "#API_GetCentralizationRuleForOrganization_ResponseSyntax")**

The timestamp when the organization centralization rule was last updated.

Type: Long

**[RuleArn](#API_GetCentralizationRuleForOrganization_ResponseSyntax "#API_GetCentralizationRuleForOrganization_ResponseSyntax")**

The Amazon Resource Name (ARN) of the organization centralization rule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

**[RuleHealth](#API_GetCentralizationRuleForOrganization_ResponseSyntax "#API_GetCentralizationRuleForOrganization_ResponseSyntax")**

The health status of the organization centralization rule.

Type: String

Valid Values: `Healthy | Unhealthy | Provisioning`

**[RuleName](#API_GetCentralizationRuleForOrganization_ResponseSyntax "#API_GetCentralizationRuleForOrganization_ResponseSyntax")**

The name of the organization centralization rule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[0-9A-Za-z-_.#/]+`

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

**InternalServerException**

Indicates the request has failed to process because of an unknown server error,
exception, or failure.

**amznErrorType**

The name of the exception.

**retryAfterSeconds**

The number of seconds to wait before retrying the request.

HTTP Status Code: 500

**ResourceNotFoundException**

The specified resource (such as a telemetry rule) could not be found.

**ResourceId**

The identifier of the resource which could not be found.

**ResourceType**

The type of the resource which could not be found.

HTTP Status Code: 404

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

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md "../../../goto/cli2/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md "../../../goto/DotNetSDKV4/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md "../../../goto/boto3/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization.md")
