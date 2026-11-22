

# StartThirdPartyTelemetryEnrichment

Starts a third-party telemetry enrichment. An enrichment adds resource metadata, such as tags, from a third-party telemetry source to the telemetry that CloudWatch receives from the resources of that source.

You specify an AWS Config connector for your third-party environment, such as a Microsoft Azure tenant. You can use each connector for only one enrichment.

To use this operation, you must have the `config:PutThirdPartyServiceLinkedConfigurationRecorder` permission. If the AWS Config service-linked role does not exist in your account, you must also have the `iam:CreateServiceLinkedRole` permission.

## Request Syntax
<a name="API_StartThirdPartyTelemetryEnrichment_RequestSyntax"></a>

```
POST /StartThirdPartyTelemetryEnrichment HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}",
   "Tags": { 
      "{{string}}" : "{{string}}" 
   },
   "TelemetrySourceConfiguration": { ... }
}
```

## URI Request Parameters
<a name="API_StartThirdPartyTelemetryEnrichment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartThirdPartyTelemetryEnrichment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_StartThirdPartyTelemetryEnrichment_RequestSyntax) **   <a name="cwoa-StartThirdPartyTelemetryEnrichment-request-Name"></a>
A name for the enrichment. The name must be unique in your account and Region. You can use the name instead of the ARN to identify the enrichment in other operations.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`   
Required: Yes

 ** [Tags](#API_StartThirdPartyTelemetryEnrichment_RequestSyntax) **   <a name="cwoa-StartThirdPartyTelemetryEnrichment-request-Tags"></a>
The tags to associate with the enrichment resource.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

 ** [TelemetrySourceConfiguration](#API_StartThirdPartyTelemetryEnrichment_RequestSyntax) **   <a name="cwoa-StartThirdPartyTelemetryEnrichment-request-TelemetrySourceConfiguration"></a>
The third-party telemetry source to collect resource metadata from. Specify exactly one telemetry source.  
Type: [TelemetrySourceConfigurationInput](API_TelemetrySourceConfigurationInput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_StartThirdPartyTelemetryEnrichment_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "Arn": "string",
   "Name": "string",
   "Status": "string",
   "StatusReason": "string",
   "Tags": { 
      "string" : "string" 
   },
   "TelemetrySourceConfiguration": { ... }
}
```

## Response Elements
<a name="API_StartThirdPartyTelemetryEnrichment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_StartThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-StartThirdPartyTelemetryEnrichment-response-Arn"></a>
The Amazon Resource Name (ARN) of the enrichment.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[a-z]+)*:observabilityadmin:[a-z0-9\-]+:[0-9]{12}:telemetry-enrichments/[a-z][a-z0-9]{9,63}` 

 ** [Name](#API_StartThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-StartThirdPartyTelemetryEnrichment-response-Name"></a>
The name of the enrichment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*` 

 ** [Status](#API_StartThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-StartThirdPartyTelemetryEnrichment-response-Status"></a>
The status of the enrichment after the start operation. Valid values:  
+  `Initializing` - CloudWatch is setting up the enrichment. Some telemetry can be enriched before setup completes.
+  `Running` - The enrichment is active.
+  `Stopped` - The enrichment is stopped.
+  `Impaired` - The enrichment has a problem. `StatusReason` describes the problem.
Type: String  
Valid Values: `Initializing | Running | Stopped | Impaired` 

 ** [StatusReason](#API_StartThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-StartThirdPartyTelemetryEnrichment-response-StatusReason"></a>
The reason for the current status. This field is present when the status is `Impaired`.  
Type: String

 ** [Tags](#API_StartThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-StartThirdPartyTelemetryEnrichment-response-Tags"></a>
The tags associated with the enrichment.  
Type: String to string map

 ** [TelemetrySourceConfiguration](#API_StartThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-StartThirdPartyTelemetryEnrichment-response-TelemetrySourceConfiguration"></a>
The source configuration of the enrichment.  
Type: [TelemetrySourceConfigurationOutput](API_TelemetrySourceConfigurationOutput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_StartThirdPartyTelemetryEnrichment_Errors"></a>

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

 ** ServiceQuotaExceededException **   
 The requested operation would exceed the allowed quota for the specified resource type.     
 ** amznErrorType **   
 The name of the exception.   
 ** QuotaCode **   
 The code for the exceeded service quota.   
 ** ResourceId **   
 The identifier of the resource which exceeds the service quota.   
 ** ResourceType **   
 The type of the resource which exceeds the service quota.   
 ** ServiceCode **   
 The code for the service of the exceeded quota. 
HTTP Status Code: 402

 ** TooManyRequestsException **   
 The request throughput limit was exceeded.   
HTTP Status Code: 429

 ** ValidationException **   
 Indicates input validation failed. Check your request parameters and retry the request.     
 ** Errors **   
 The errors in the input which caused the exception. 
HTTP Status Code: 400

## See Also
<a name="API_StartThirdPartyTelemetryEnrichment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/StartThirdPartyTelemetryEnrichment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/StartThirdPartyTelemetryEnrichment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/StartThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/StartThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/StartThirdPartyTelemetryEnrichment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/StartThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/StartThirdPartyTelemetryEnrichment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/StartThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/StartThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/StartThirdPartyTelemetryEnrichment) 