

# StopThirdPartyTelemetryEnrichment

Stops a third-party telemetry enrichment. CloudWatch stops adding resource metadata from the third-party telemetry source to your telemetry.

To use this operation, you must have the `config:DeleteServiceLinkedConfigurationRecorder` permission.

## Request Syntax
<a name="API_StopThirdPartyTelemetryEnrichment_RequestSyntax"></a>

```
POST /StopThirdPartyTelemetryEnrichment HTTP/1.1
Content-type: application/json

{
   "TelemetryEnrichmentIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopThirdPartyTelemetryEnrichment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StopThirdPartyTelemetryEnrichment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TelemetryEnrichmentIdentifier](#API_StopThirdPartyTelemetryEnrichment_RequestSyntax) **   <a name="cwoa-StopThirdPartyTelemetryEnrichment-request-TelemetryEnrichmentIdentifier"></a>
The identifier of the enrichment to stop. You can specify one of the following:  
+ The name of the enrichment.
+ The Amazon Resource Name (ARN) of the enrichment.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

## Response Syntax
<a name="API_StopThirdPartyTelemetryEnrichment_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "Name": "string",
   "Status": "string",
   "StatusReason": "string",
   "TelemetrySource": "string"
}
```

## Response Elements
<a name="API_StopThirdPartyTelemetryEnrichment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_StopThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-StopThirdPartyTelemetryEnrichment-response-Name"></a>
The name of the enrichment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*` 

 ** [Status](#API_StopThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-StopThirdPartyTelemetryEnrichment-response-Status"></a>
The status of the enrichment after the stop operation. Valid values:  
+  `Initializing` - CloudWatch is setting up the enrichment. Some telemetry can be enriched before setup completes.
+  `Running` - The enrichment is active.
+  `Stopped` - The enrichment is stopped.
+  `Impaired` - The enrichment has a problem. `StatusReason` describes the problem.
Type: String  
Valid Values: `Initializing | Running | Stopped | Impaired` 

 ** [StatusReason](#API_StopThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-StopThirdPartyTelemetryEnrichment-response-StatusReason"></a>
The reason for the current status. This field is present when the status is `Impaired`.  
Type: String

 ** [TelemetrySource](#API_StopThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-StopThirdPartyTelemetryEnrichment-response-TelemetrySource"></a>
The third-party telemetry source of the enrichment.  
Type: String  
Valid Values: `Azure` 

## Errors
<a name="API_StopThirdPartyTelemetryEnrichment_Errors"></a>

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
<a name="API_StopThirdPartyTelemetryEnrichment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/StopThirdPartyTelemetryEnrichment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/StopThirdPartyTelemetryEnrichment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/StopThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/StopThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/StopThirdPartyTelemetryEnrichment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/StopThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/StopThirdPartyTelemetryEnrichment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/StopThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/StopThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/StopThirdPartyTelemetryEnrichment) 