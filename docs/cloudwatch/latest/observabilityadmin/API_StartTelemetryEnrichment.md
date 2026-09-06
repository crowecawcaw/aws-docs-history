

# StartTelemetryEnrichment
<a name="API_StartTelemetryEnrichment"></a>

 Enables the resource tags for telemetry feature for your account, which enhances telemetry data with additional resource metadata from AWS Resource Explorer to provide richer context for monitoring and observability. 

## Request Syntax
<a name="API_StartTelemetryEnrichment_RequestSyntax"></a>

```
POST /StartTelemetryEnrichment HTTP/1.1
```

## URI Request Parameters
<a name="API_StartTelemetryEnrichment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartTelemetryEnrichment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StartTelemetryEnrichment_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "AwsResourceExplorerManagedViewArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_StartTelemetryEnrichment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [AwsResourceExplorerManagedViewArn](#API_StartTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-StartTelemetryEnrichment-response-AwsResourceExplorerManagedViewArn"></a>
 The Amazon Resource Name (ARN) of the AWS Resource Explorer managed view created for resource tags for telemetry.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws([a-z0-9\-]+)?:resource-explorer-2:([a-z0-9\-]+)?:([0-9]{12})?:managed-view/(.+)` 

 ** [Status](#API_StartTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-StartTelemetryEnrichment-response-Status"></a>
 The status of the resource tags for telemetry feature after the start operation (`Running`, `Stopped`, or `Impaired`).   
Type: String  
Valid Values: `Running | Stopped | Impaired` 

## Errors
<a name="API_StartTelemetryEnrichment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
 Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access management for AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the IAM user guide.     
 ** amznErrorType **   
 The name of the exception. 
HTTP Status Code: 400

 ** ConflictException **   
 The requested operation conflicts with the current state of the specified resource or with another request.     
 ** ResourceId **   
 The identifier of the resource which is in conflict with the requested operation.   
 ** ResourceType **   
 The type of the resource which is in conflict with the requested operation. 
HTTP Status Code: 409

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

## See Also
<a name="API_StartTelemetryEnrichment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/StartTelemetryEnrichment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/StartTelemetryEnrichment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/StartTelemetryEnrichment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/StartTelemetryEnrichment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/StartTelemetryEnrichment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/StartTelemetryEnrichment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/StartTelemetryEnrichment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/StartTelemetryEnrichment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/StartTelemetryEnrichment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/StartTelemetryEnrichment) 