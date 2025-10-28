# StopTelemetryEnrichment

Disables the resource tags for telemetry feature for your account, stopping the
enhancement of telemetry data with additional resource metadata.

## Request Syntax

```
POST /StopTelemetryEnrichment HTTP/1.1

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
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

**[Status](#API_StopTelemetryEnrichment_ResponseSyntax "#API_StopTelemetryEnrichment_ResponseSyntax")**

The status of the resource tags for telemetry feature after the stop operation
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

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md "../../../goto/cli2/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md "../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md "../../../goto/boto3/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/StopTelemetryEnrichment.md")
