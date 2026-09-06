

# GetTelemetryPipeline
<a name="API_GetTelemetryPipeline"></a>

Retrieves information about a specific telemetry pipeline, including its configuration, status, and metadata.

## Request Syntax
<a name="API_GetTelemetryPipeline_RequestSyntax"></a>

```
POST /GetTelemetryPipeline HTTP/1.1
Content-type: application/json

{
   "PipelineIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetTelemetryPipeline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTelemetryPipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PipelineIdentifier](#API_GetTelemetryPipeline_RequestSyntax) **   <a name="cwoa-GetTelemetryPipeline-request-PipelineIdentifier"></a>
The identifier (name or ARN) of the telemetry pipeline to retrieve.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: Yes

## Response Syntax
<a name="API_GetTelemetryPipeline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Pipeline": { 
      "Arn": "string",
      "Configuration": { 
         "Body": "string"
      },
      "CreatedTimeStamp": number,
      "LastUpdateTimeStamp": number,
      "Name": "string",
      "Status": "string",
      "StatusReason": { 
         "Description": "string"
      },
      "Tags": { 
         "string" : "string" 
      }
   }
}
```

## Response Elements
<a name="API_GetTelemetryPipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Pipeline](#API_GetTelemetryPipeline_ResponseSyntax) **   <a name="cwoa-GetTelemetryPipeline-response-Pipeline"></a>
The complete telemetry pipeline resource information, including configuration, status, and metadata.  
Type: [TelemetryPipeline](API_TelemetryPipeline.md) object

## Errors
<a name="API_GetTelemetryPipeline_Errors"></a>

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

 ** ResourceNotFoundException **   
 The specified resource (such as a telemetry rule) could not be found.     
 ** ResourceId **   
 The identifier of the resource which could not be found.   
 ** ResourceType **   
 The type of the resource which could not be found. 
HTTP Status Code: 404

 ** TooManyRequestsException **   
 The request throughput limit was exceeded.   
HTTP Status Code: 429

 ** ValidationException **   
 Indicates input validation failed. Check your request parameters and retry the request.     
 ** Errors **   
 The errors in the input which caused the exception. 
HTTP Status Code: 400

## See Also
<a name="API_GetTelemetryPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/GetTelemetryPipeline) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/GetTelemetryPipeline) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/GetTelemetryPipeline) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/GetTelemetryPipeline) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetTelemetryPipeline) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetTelemetryPipeline) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/GetTelemetryPipeline) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetTelemetryPipeline) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/GetTelemetryPipeline) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetTelemetryPipeline) 