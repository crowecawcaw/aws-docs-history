

# GetThirdPartyTelemetryEnrichment

Returns the details of a third-party telemetry enrichment, including its status and source configuration.

## Request Syntax
<a name="API_GetThirdPartyTelemetryEnrichment_RequestSyntax"></a>

```
POST /GetThirdPartyTelemetryEnrichment HTTP/1.1
Content-type: application/json

{
   "TelemetryEnrichmentIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetThirdPartyTelemetryEnrichment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetThirdPartyTelemetryEnrichment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TelemetryEnrichmentIdentifier](#API_GetThirdPartyTelemetryEnrichment_RequestSyntax) **   <a name="cwoa-GetThirdPartyTelemetryEnrichment-request-TelemetryEnrichmentIdentifier"></a>
The identifier of the enrichment to return. You can specify one of the following:  
+ The name of the enrichment.
+ The Amazon Resource Name (ARN) of the enrichment.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

## Response Syntax
<a name="API_GetThirdPartyTelemetryEnrichment_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetThirdPartyTelemetryEnrichment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-GetThirdPartyTelemetryEnrichment-response-Arn"></a>
The Amazon Resource Name (ARN) of the enrichment.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[a-z]+)*:observabilityadmin:[a-z0-9\-]+:[0-9]{12}:telemetry-enrichments/[a-z][a-z0-9]{9,63}` 

 ** [Name](#API_GetThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-GetThirdPartyTelemetryEnrichment-response-Name"></a>
The name of the enrichment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*` 

 ** [Status](#API_GetThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-GetThirdPartyTelemetryEnrichment-response-Status"></a>
The current status of the enrichment. Valid values:  
+  `Initializing` - CloudWatch is setting up the enrichment. Some telemetry can be enriched before setup completes.
+  `Running` - The enrichment is active.
+  `Stopped` - The enrichment is stopped.
+  `Impaired` - The enrichment has a problem. `StatusReason` describes the problem.
Type: String  
Valid Values: `Initializing | Running | Stopped | Impaired` 

 ** [StatusReason](#API_GetThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-GetThirdPartyTelemetryEnrichment-response-StatusReason"></a>
The reason for the current status. This field is present when the status is `Impaired`.  
Type: String

 ** [Tags](#API_GetThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-GetThirdPartyTelemetryEnrichment-response-Tags"></a>
The tags associated with the enrichment.  
Type: String to string map

 ** [TelemetrySourceConfiguration](#API_GetThirdPartyTelemetryEnrichment_ResponseSyntax) **   <a name="cwoa-GetThirdPartyTelemetryEnrichment-response-TelemetrySourceConfiguration"></a>
The source configuration of the enrichment.  
Type: [TelemetrySourceConfigurationOutput](API_TelemetrySourceConfigurationOutput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_GetThirdPartyTelemetryEnrichment_Errors"></a>

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
<a name="API_GetThirdPartyTelemetryEnrichment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/GetThirdPartyTelemetryEnrichment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/GetThirdPartyTelemetryEnrichment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/GetThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/GetThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetThirdPartyTelemetryEnrichment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/GetThirdPartyTelemetryEnrichment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/GetThirdPartyTelemetryEnrichment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetThirdPartyTelemetryEnrichment) 