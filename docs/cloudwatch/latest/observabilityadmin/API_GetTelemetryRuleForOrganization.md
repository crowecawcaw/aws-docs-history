# GetTelemetryRuleForOrganization

Retrieves the details of a specific organization telemetry rule. This operation can only
be called by the organization's management account or a delegated administrator account.

## Request Syntax

```
POST /GetTelemetryRuleForOrganization HTTP/1.1
Content-type: application/json

{
   "RuleIdentifier": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[RuleIdentifier](#API_GetTelemetryRuleForOrganization_RequestSyntax "#API_GetTelemetryRuleForOrganization_RequestSyntax")**

The identifier (name or ARN) of the organization telemetry rule to retrieve.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedTimeStamp": ***number***,
   "LastUpdateTimeStamp": ***number***,
   "RuleArn": "***string***",
   "RuleName": "***string***",
   "TelemetryRule": {
      "DestinationConfiguration": {
         "CloudtrailParameters": {
            "AdvancedEventSelectors": [
               {
                  "FieldSelectors": [
                     {
                        "EndsWith": [ "***string***" ],
                        "Equals": [ "***string***" ],
                        "Field": "***string***",
                        "NotEndsWith": [ "***string***" ],
                        "NotEquals": [ "***string***" ],
                        "NotStartsWith": [ "***string***" ],
                        "StartsWith": [ "***string***" ]
                     }
                  ],
                  "Name": "***string***"
               }
            ]
         },
         "DestinationPattern": "***string***",
         "DestinationType": "***string***",
         "ELBLoadBalancerLoggingParameters": {
            "FieldDelimiter": "***string***",
            "OutputFormat": "***string***"
         },
         "LogDeliveryParameters": {
            "LogTypes": [ "***string***" ]
         },
         "RetentionInDays": ***number***,
         "VPCFlowLogParameters": {
            "LogFormat": "***string***",
            "MaxAggregationInterval": ***number***,
            "TrafficType": "***string***"
         },
         "WAFLoggingParameters": {
            "LoggingFilter": {
               "DefaultBehavior": "***string***",
               "Filters": [
                  {
                     "Behavior": "***string***",
                     "Conditions": [
                        {
                           "ActionCondition": {
                              "Action": "***string***"
                           },
                           "LabelNameCondition": {
                              "LabelName": "***string***"
                           }
                        }
                     ],
                     "Requirement": "***string***"
                  }
               ]
            },
            "LogType": "***string***",
            "RedactedFields": [
               {
                  "Method": "***string***",
                  "QueryString": "***string***",
                  "SingleHeader": {
                     "Name": "***string***"
                  },
                  "UriPath": "***string***"
               }
            ]
         }
      },
      "ResourceType": "***string***",
      "Scope": "***string***",
      "SelectionCriteria": "***string***",
      "TelemetrySourceTypes": [ "***string***" ],
      "TelemetryType": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreatedTimeStamp](#API_GetTelemetryRuleForOrganization_ResponseSyntax "#API_GetTelemetryRuleForOrganization_ResponseSyntax")**

The timestamp when the organization telemetry rule was created.

Type: Long

**[LastUpdateTimeStamp](#API_GetTelemetryRuleForOrganization_ResponseSyntax "#API_GetTelemetryRuleForOrganization_ResponseSyntax")**

The timestamp when the organization telemetry rule was last updated.

Type: Long

**[RuleArn](#API_GetTelemetryRuleForOrganization_ResponseSyntax "#API_GetTelemetryRuleForOrganization_ResponseSyntax")**

The Amazon Resource Name (ARN) of the organization telemetry rule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

**[RuleName](#API_GetTelemetryRuleForOrganization_ResponseSyntax "#API_GetTelemetryRuleForOrganization_ResponseSyntax")**

The name of the organization telemetry rule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[0-9A-Za-z-_.#/]+`

**[TelemetryRule](#API_GetTelemetryRuleForOrganization_ResponseSyntax "#API_GetTelemetryRuleForOrganization_ResponseSyntax")**

The configuration details of the organization telemetry rule.

Type: [TelemetryRule](API_TelemetryRule.md "API_TelemetryRule.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md "../../../goto/cli2/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md "../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md "../../../goto/boto3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization.md")
