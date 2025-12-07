# TestTelemetryPipeline

Tests a pipeline configuration with sample records to validate data processing before
deployment. This operation helps ensure your pipeline configuration works as expected.

## Request Syntax

```
POST /TestTelemetryPipeline HTTP/1.1
Content-type: application/json

{
   "Configuration": {
      "Body": "`string`"
   },
   "Records": [
      {
         "Data": "`string`",
         "Type": "`string`"
      }
   ]
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[Configuration](#API_TestTelemetryPipeline_RequestSyntax "#API_TestTelemetryPipeline_RequestSyntax")**

The pipeline configuration to test with the provided sample records.

Type: [TelemetryPipelineConfiguration](API_TelemetryPipelineConfiguration.md "API_TelemetryPipelineConfiguration.md") object

Required: Yes

**[Records](#API_TestTelemetryPipeline_RequestSyntax "#API_TestTelemetryPipeline_RequestSyntax")**

The sample records to process through the pipeline configuration for testing
purposes.

Type: Array of [Record](API_Record.md "API_Record.md") objects

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Results": [
      {
         "Error": {
            "Message": "***string***"
         },
         "Record": {
            "Data": "***string***",
            "Type": "***string***"
         }
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Results](#API_TestTelemetryPipeline_ResponseSyntax "#API_TestTelemetryPipeline_ResponseSyntax")**

The results of processing the test records through the pipeline configuration, including
any outputs or errors.

Type: Array of [PipelineOutput](API_PipelineOutput.md "API_PipelineOutput.md") objects

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

## Examples

### Example

When calling `TestTelemetryPipeline`, the `Body` of the `Configuration` object should only
contain a pipeline with the processor definitions. For example:

```
pipeline:
  processor:
    - lowercase_string:
        with_keys:
          - method
    - uppercase_string:
        with_keys:
          - level
```

### Example

The `Records` value should contain the sample input data you want to process. For example:

```
"Records": [
    {
        "Data": "{ \"method\": \"get\", \"level\": \"INFO\" }",
        "Type": "JSON"
    }
]
```

### Example

The response will contain the result of applying the processor configuration to the input. For the previously shown inputs, the output is:

```
{
    "Results": [
         {
             "Record": {
                 "Data": "{ \"method\": \"GET\", \"level\": \"info\" }"
                 "Type" : "JSON"
             }
         }
    ]
}
```

### Example

Here's another example. Given the following processor configuration:

```
pipeline:
  processor:
    - csv: {}
```

### Example

and this input:

```
"Records": [
    {
        "Data": "red,green",
        "Type": "STRING"
    }
]
```

### Example

the output is:

```
{
    "Results": [
         {
             "Record": {
                 "Data": "{ \"column_1\": \"red\", \"column_2\": \"green\" }"
                 "Type" : "JSON"
             }
         }
    ]
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/TestTelemetryPipeline.md "../../../goto/cli2/observabilityadmin-2018-05-10/TestTelemetryPipeline.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/TestTelemetryPipeline.md "../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/TestTelemetryPipeline.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TestTelemetryPipeline.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TestTelemetryPipeline.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/TestTelemetryPipeline.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/TestTelemetryPipeline.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TestTelemetryPipeline.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TestTelemetryPipeline.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/TestTelemetryPipeline.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/TestTelemetryPipeline.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/TestTelemetryPipeline.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/TestTelemetryPipeline.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/TestTelemetryPipeline.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/TestTelemetryPipeline.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/TestTelemetryPipeline.md "../../../goto/boto3/observabilityadmin-2018-05-10/TestTelemetryPipeline.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TestTelemetryPipeline.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TestTelemetryPipeline.md")
