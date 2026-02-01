# CreateTelemetryPipeline

Creates a telemetry pipeline for processing and transforming telemetry data. The pipeline
defines how data flows from sources through processors to destinations, enabling data
transformation and delivering capabilities.

## Request Syntax

```
POST /CreateTelemetryPipeline HTTP/1.1
Content-type: application/json

{
   "Configuration": {
      "Body": "`string`"
   },
   "Name": "`string`",
   "Tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[Configuration](#API_CreateTelemetryPipeline_RequestSyntax "#API_CreateTelemetryPipeline_RequestSyntax")**

The configuration that defines how the telemetry pipeline processes data, including
sources, processors, and destinations. For more information about pipeline components, see the
[Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/pipeline-components-reference.md "../../../AmazonCloudWatch/latest/monitoring/pipeline-components-reference.md")

Type: [TelemetryPipelineConfiguration](API_TelemetryPipelineConfiguration.md "API_TelemetryPipelineConfiguration.md") object

Required: Yes

**[Name](#API_CreateTelemetryPipeline_RequestSyntax "#API_CreateTelemetryPipeline_RequestSyntax")**

The name of the telemetry pipeline to create. The name must be unique within your
account.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 28.

Pattern: `.*[a-z][a-z0-9\-]+.*`

Required: Yes

**[Tags](#API_CreateTelemetryPipeline_RequestSyntax "#API_CreateTelemetryPipeline_RequestSyntax")**

The key-value pairs to associate with the telemetry pipeline resource for categorization
and management purposes.

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
   "Arn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Arn](#API_CreateTelemetryPipeline_ResponseSyntax "#API_CreateTelemetryPipeline_ResponseSyntax")**

The Amazon Resource Name (ARN) of the created telemetry pipeline.

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

## Examples

### Using CloudWatch as a pipeline source

The following is an example of a `Body` property value for the `Configuration` object.

```
pipeline:
  source:
    cloudwatch_logs:
      log_event_metadata:
        data_source_name: "my_data_source"
        data_source_type: "default"
      aws:
        sts_role_arn: "arn:aws:iam::123456789012:role/MyPipelineAccessRole"
  processor:
    - parse_json: {}
  sink:
    - cloudwatch_logs:
        log_group: "@original"
```

### Using Amazon S3 as a pipeline source

The following is an example of a `Body` property value for the `Configuration` object.

```
pipeline:
  source:
    s3:
      sqs:
        visibility_timeout: "PT60S"
        visibility_duplication_protection: true
        maximum_messages: 10
        queue_url: "https://sqs.us-east-1.amazonaws.com/123456789012/my-sqs-queue"
      notification_type: "sqs"
      codec:
        ndjson: {}
      aws:
        region: "us-east-1"
        sts_role_arn: "arn:aws:iam::123456789012:role/MyAccessRole"
      data_source_name: "crowdstrike_falcon"
  processor:
    - ocsf:
        version: "1.5"
        mapping_version: "1.5.0"
        schema:
          crowdstrike_falcon:
  sink:
    - cloudwatch_logs:
        log_group: "my-log-group"
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md "../../../goto/cli2/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md "../../../goto/DotNetSDKV4/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md "../../../goto/boto3/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/CreateTelemetryPipeline.md")
