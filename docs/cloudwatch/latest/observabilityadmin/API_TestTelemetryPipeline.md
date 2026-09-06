

# TestTelemetryPipeline
<a name="API_TestTelemetryPipeline"></a>

Tests a pipeline configuration with sample records to validate data processing before deployment. This operation helps ensure your pipeline configuration works as expected. 

## Request Syntax
<a name="API_TestTelemetryPipeline_RequestSyntax"></a>

```
POST /TestTelemetryPipeline HTTP/1.1
Content-type: application/json

{
   "Configuration": { 
      "Body": "{{string}}"
   },
   "Records": [ 
      { 
         "Data": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "SignalType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_TestTelemetryPipeline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TestTelemetryPipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Configuration](#API_TestTelemetryPipeline_RequestSyntax) **   <a name="cwoa-TestTelemetryPipeline-request-Configuration"></a>
The pipeline configuration to test with the provided sample records.  
Type: [TelemetryPipelineConfiguration](API_TelemetryPipelineConfiguration.md) object  
Required: Yes

 ** [Records](#API_TestTelemetryPipeline_RequestSyntax) **   <a name="cwoa-TestTelemetryPipeline-request-Records"></a>
The sample records to process through the pipeline configuration for testing purposes.  
Type: Array of [Record](API_Record.md) objects  
Required: Yes

 ** [SignalType](#API_TestTelemetryPipeline_RequestSyntax) **   <a name="cwoa-TestTelemetryPipeline-request-SignalType"></a>
The type of telemetry signal to test. If not specified, defaults to log processing.  
Type: String  
Valid Values: `LOG | METRIC`   
Required: No

## Response Syntax
<a name="API_TestTelemetryPipeline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Results": [ 
      { 
         "Error": { 
            "Message": "string"
         },
         "Record": { 
            "Data": "string",
            "Type": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_TestTelemetryPipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Results](#API_TestTelemetryPipeline_ResponseSyntax) **   <a name="cwoa-TestTelemetryPipeline-response-Results"></a>
The results of processing the test records through the pipeline configuration, including any outputs or errors.  
Type: Array of [PipelineOutput](API_PipelineOutput.md) objects

## Errors
<a name="API_TestTelemetryPipeline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
 Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access management for AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the IAM user guide.     
 ** amznErrorType **   
 The name of the exception. 
HTTP Status Code: 400

 ** InternalServerException **   
 Indicates the request has failed to process because of an unknown server error, exception, or failure.     
 ** amznErrorType **   
 The name of the exception.   
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** TooManyRequestsException **   
 The request throughput limit was exceeded.   
HTTP Status Code: 429

 ** ValidationException **   
 Indicates input validation failed. Check your request parameters and retry the request.     
 ** Errors **   
 The errors in the input which caused the exception. 
HTTP Status Code: 400

## Examples
<a name="API_TestTelemetryPipeline_Examples"></a>

### Example
<a name="API_TestTelemetryPipeline_Example_1"></a>

When calling `TestTelemetryPipeline`, the `Body` of the `Configuration` object should only contain a pipeline with the processor definitions. For example:

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
<a name="API_TestTelemetryPipeline_Example_2"></a>

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
<a name="API_TestTelemetryPipeline_Example_3"></a>

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
<a name="API_TestTelemetryPipeline_Example_4"></a>

Here's another example. Given the following processor configuration:

```
pipeline:
  processor:
    - csv: {}
```

### Example
<a name="API_TestTelemetryPipeline_Example_5"></a>

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
<a name="API_TestTelemetryPipeline_Example_6"></a>

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
<a name="API_TestTelemetryPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/TestTelemetryPipeline) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/TestTelemetryPipeline) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/TestTelemetryPipeline) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/TestTelemetryPipeline) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/TestTelemetryPipeline) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/TestTelemetryPipeline) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/TestTelemetryPipeline) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/TestTelemetryPipeline) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/TestTelemetryPipeline) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/TestTelemetryPipeline) 