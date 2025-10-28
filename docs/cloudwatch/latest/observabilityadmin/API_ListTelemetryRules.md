# ListTelemetryRules

Lists all telemetry rules in your account. You can filter the results by specifying a
rule name prefix.

## Request Syntax

```
POST /ListTelemetryRules HTTP/1.1
Content-type: application/json

{
   "MaxResults": `number`,
   "NextToken": "`string`",
   "RuleNamePrefix": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[MaxResults](#API_ListTelemetryRules_RequestSyntax "#API_ListTelemetryRules_RequestSyntax")**

The maximum number of telemetry rules to return in a single call.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[NextToken](#API_ListTelemetryRules_RequestSyntax "#API_ListTelemetryRules_RequestSyntax")**

The token for the next set of results. A previous call generates this token.

Type: String

Required: No

**[RuleNamePrefix](#API_ListTelemetryRules_RequestSyntax "#API_ListTelemetryRules_RequestSyntax")**

A string to filter telemetry rules whose names begin with the specified prefix.

Type: String

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "TelemetryRuleSummaries": [
      {
         "CreatedTimeStamp": ***number***,
         "LastUpdateTimeStamp": ***number***,
         "ResourceType": "***string***",
         "RuleArn": "***string***",
         "RuleName": "***string***",
         "TelemetryType": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListTelemetryRules_ResponseSyntax "#API_ListTelemetryRules_ResponseSyntax")**

A token to resume pagination of results.

Type: String

**[TelemetryRuleSummaries](#API_ListTelemetryRules_ResponseSyntax "#API_ListTelemetryRules_ResponseSyntax")**

A list of telemetry rule summaries.

Type: Array of [TelemetryRuleSummary](API_TelemetryRuleSummary.md "API_TelemetryRuleSummary.md") objects

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

HTTP Status Code: 500

**TooManyRequestsException**

The request throughput limit was exceeded.

HTTP Status Code: 429

**ValidationException**

Indicates input validation failed. Check your request parameters and retry the request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/ListTelemetryRules.md "../../../goto/cli2/observabilityadmin-2018-05-10/ListTelemetryRules.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/ListTelemetryRules.md "../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/ListTelemetryRules.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/ListTelemetryRules.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/ListTelemetryRules.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/ListTelemetryRules.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/ListTelemetryRules.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/ListTelemetryRules.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/ListTelemetryRules.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/ListTelemetryRules.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/ListTelemetryRules.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/ListTelemetryRules.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/ListTelemetryRules.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/ListTelemetryRules.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/ListTelemetryRules.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/ListTelemetryRules.md "../../../goto/boto3/observabilityadmin-2018-05-10/ListTelemetryRules.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/ListTelemetryRules.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/ListTelemetryRules.md")
