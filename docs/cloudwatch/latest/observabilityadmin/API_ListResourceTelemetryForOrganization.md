# ListResourceTelemetryForOrganization

Returns a list of telemetry configurations for AWS resources supported by telemetry
config in the organization.

## Request Syntax

```
POST /ListResourceTelemetryForOrganization HTTP/1.1
Content-type: application/json

{
   "AccountIdentifiers": [ "`string`" ],
   "MaxResults": `number`,
   "NextToken": "`string`",
   "ResourceIdentifierPrefix": "`string`",
   "ResourceTags": {
      "`string`" : "`string`"
   },
   "ResourceTypes": [ "`string`" ],
   "TelemetryConfigurationState": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[AccountIdentifiers](#API_ListResourceTelemetryForOrganization_RequestSyntax "#API_ListResourceTelemetryForOrganization_RequestSyntax")**

A list of AWS accounts used to filter the resources to those associated with the
specified accounts.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 10 items.

Length Constraints: Fixed length of 12.

Pattern: `[0-9]{12}`

Required: No

**[MaxResults](#API_ListResourceTelemetryForOrganization_RequestSyntax "#API_ListResourceTelemetryForOrganization_RequestSyntax")**

A number field used to limit the number of results within the returned list.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 50.

Required: No

**[NextToken](#API_ListResourceTelemetryForOrganization_RequestSyntax "#API_ListResourceTelemetryForOrganization_RequestSyntax")**

The token for the next set of items to return. A previous call provides this token.

Type: String

Required: No

**[ResourceIdentifierPrefix](#API_ListResourceTelemetryForOrganization_RequestSyntax "#API_ListResourceTelemetryForOrganization_RequestSyntax")**

A string used to filter resources in the organization which have a
`ResourceIdentifier` starting with the `ResourceIdentifierPrefix`.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 768.

Required: No

**[ResourceTags](#API_ListResourceTelemetryForOrganization_RequestSyntax "#API_ListResourceTelemetryForOrganization_RequestSyntax")**

A key-value pair to filter resources in the organization based on tags associated with
the resource. Fore more information about tags, see [What are tags?](../../../whitepapers/latest/tagging-best-practices/what-are-tags.md "../../../whitepapers/latest/tagging-best-practices/what-are-tags.md")

Type: String to string map

Map Entries: Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

Required: No

**[ResourceTypes](#API_ListResourceTelemetryForOrganization_RequestSyntax "#API_ListResourceTelemetryForOrganization_RequestSyntax")**

A list of resource types used to filter resources in the organization. If this parameter
is provided, the resources will be returned in the same order used in the request.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 9 items.

Valid Values: `AWS::EC2::Instance | AWS::EC2::VPC | AWS::Lambda::Function | AWS::CloudTrail | AWS::EKS::Cluster | AWS::WAFv2::WebACL | AWS::ElasticLoadBalancingV2::LoadBalancer | AWS::Route53Resolver::ResolverEndpoint | AWS::BedrockAgentCore::Runtime | AWS::BedrockAgentCore::Browser | AWS::BedrockAgentCore::CodeInterpreter`

Required: No

**[TelemetryConfigurationState](#API_ListResourceTelemetryForOrganization_RequestSyntax "#API_ListResourceTelemetryForOrganization_RequestSyntax")**

A key-value pair to filter resources in the organization based on the telemetry type and
the state of the telemetry configuration. The key is the telemetry type and the value is the
state.

Type: String to string map

Valid Keys: `Logs | Metrics | Traces`

Valid Values: `Enabled | Disabled | NotApplicable`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "TelemetryConfigurations": [
      {
         "AccountIdentifier": "***string***",
         "LastUpdateTimeStamp": ***number***,
         "ResourceIdentifier": "***string***",
         "ResourceTags": {
            "***string***" : "***string***"
         },
         "ResourceType": "***string***",
         "TelemetryConfigurationState": {
            "***string***" : "***string***"
         }
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListResourceTelemetryForOrganization_ResponseSyntax "#API_ListResourceTelemetryForOrganization_ResponseSyntax")**

The token for the next set of items to return. A previous call provides this token.

Type: String

**[TelemetryConfigurations](#API_ListResourceTelemetryForOrganization_ResponseSyntax "#API_ListResourceTelemetryForOrganization_ResponseSyntax")**

A list of telemetry configurations for AWS resources supported by telemetry config in
the organization.

Type: Array of [TelemetryConfiguration](API_TelemetryConfiguration.md "API_TelemetryConfiguration.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md "../../../goto/cli2/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md "../../../goto/DotNetSDKV4/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md "../../../goto/boto3/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/ListResourceTelemetryForOrganization.md")
