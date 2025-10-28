# StartTelemetryEnrichment

Enables the resource tags for telemetry feature for your account, which enhances
telemetry data with additional resource metadata from AWS Resource Explorer to provide
richer context for monitoring and observability.

## Request Syntax

```
POST /StartTelemetryEnrichment HTTP/1.1

```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 202
Content-type: application/json

{
   "AwsResourceExplorerManagedViewArn": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

**[AwsResourceExplorerManagedViewArn](#API_StartTelemetryEnrichment_ResponseSyntax "#API_StartTelemetryEnrichment_ResponseSyntax")**

The Amazon Resource Name (ARN) of the AWS Resource Explorer managed view created for
resource tags for telemetry.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws([a-z0-9\-]+)?:resource-explorer-2:([a-z0-9\-]+)?:([0-9]{12})?:managed-view/(.+)`

**[Status](#API_StartTelemetryEnrichment_ResponseSyntax "#API_StartTelemetryEnrichment_ResponseSyntax")**

The status of the resource tags for telemetry feature after the start operation
(`Running`, `Stopped`, or `Impaired`).

Type: String

Valid Values: `Running | Stopped | Impaired`

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

HTTP Status Code: 409

**InternalServerException**

Indicates the request has failed to process because of an unknown server error,
exception, or failure.

**amznErrorType**

The name of the exception.

HTTP Status Code: 500

**TooManyRequestsException**

The request throughput limit was exceeded.

HTTP Status Code: 429

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md "../../../goto/cli2/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md "../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md "../../../goto/boto3/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/StartTelemetryEnrichment.md")
