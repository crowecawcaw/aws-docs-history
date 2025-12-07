# DeleteTelemetryPipeline

Deletes a telemetry pipeline and its associated resources. This operation stops data
processing and removes the pipeline configuration.

## Request Syntax

```
POST /DeleteTelemetryPipeline HTTP/1.1
Content-type: application/json

{
   "PipelineIdentifier": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[PipelineIdentifier](#API_DeleteTelemetryPipeline_RequestSyntax "#API_DeleteTelemetryPipeline_RequestSyntax")**

The ARN of the telemetry pipeline to delete.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 512.

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md "../../../goto/cli2/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md "../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md "../../../goto/boto3/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/DeleteTelemetryPipeline.md")
