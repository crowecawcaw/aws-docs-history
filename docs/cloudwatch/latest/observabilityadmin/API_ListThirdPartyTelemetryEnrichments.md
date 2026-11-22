

# ListThirdPartyTelemetryEnrichments

Returns a summary of each third-party telemetry enrichment in your account and Region. To get the full configuration of an enrichment, use `GetThirdPartyTelemetryEnrichment`. The results are paginated. To get the next page of results, use `NextToken`.

## Request Syntax
<a name="API_ListThirdPartyTelemetryEnrichments_RequestSyntax"></a>

```
POST /ListThirdPartyTelemetryEnrichments HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Status": "{{string}}",
   "TelemetrySource": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListThirdPartyTelemetryEnrichments_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListThirdPartyTelemetryEnrichments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListThirdPartyTelemetryEnrichments_RequestSyntax) **   <a name="cwoa-ListThirdPartyTelemetryEnrichments-request-MaxResults"></a>
The maximum number of results to return in a single call. If you omit this parameter, the operation returns up to 100 results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListThirdPartyTelemetryEnrichments_RequestSyntax) **   <a name="cwoa-ListThirdPartyTelemetryEnrichments-request-NextToken"></a>
The token for the next set of results. A previous call generates this token. If you omit this parameter, the operation returns the first page of results.  
Type: String  
Required: No

 ** [Status](#API_ListThirdPartyTelemetryEnrichments_RequestSyntax) **   <a name="cwoa-ListThirdPartyTelemetryEnrichments-request-Status"></a>
Returns only the enrichments that have this status. Valid values:  
+  `Initializing` - CloudWatch is setting up the enrichment. Some telemetry can be enriched before setup completes.
+  `Running` - The enrichment is active.
+  `Stopped` - The enrichment is stopped.
+  `Impaired` - The enrichment has a problem. `StatusReason` describes the problem.
Type: String  
Valid Values: `Initializing | Running | Stopped | Impaired`   
Required: No

 ** [TelemetrySource](#API_ListThirdPartyTelemetryEnrichments_RequestSyntax) **   <a name="cwoa-ListThirdPartyTelemetryEnrichments-request-TelemetrySource"></a>
Returns only the enrichments for this third-party telemetry source.  
Type: String  
Valid Values: `Azure`   
Required: No

## Response Syntax
<a name="API_ListThirdPartyTelemetryEnrichments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "TelemetryEnrichments": [ 
      { 
         "Name": "string",
         "Status": "string",
         "TelemetrySource": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListThirdPartyTelemetryEnrichments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListThirdPartyTelemetryEnrichments_ResponseSyntax) **   <a name="cwoa-ListThirdPartyTelemetryEnrichments-response-NextToken"></a>
A token to resume pagination of results.  
Type: String

 ** [TelemetryEnrichments](#API_ListThirdPartyTelemetryEnrichments_ResponseSyntax) **   <a name="cwoa-ListThirdPartyTelemetryEnrichments-response-TelemetryEnrichments"></a>
The enrichments in your account and Region.  
Type: Array of [ThirdPartyTelemetryEnrichmentSummary](API_ThirdPartyTelemetryEnrichmentSummary.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListThirdPartyTelemetryEnrichments_Errors"></a>

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

## See Also
<a name="API_ListThirdPartyTelemetryEnrichments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/ListThirdPartyTelemetryEnrichments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/ListThirdPartyTelemetryEnrichments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/ListThirdPartyTelemetryEnrichments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/ListThirdPartyTelemetryEnrichments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/ListThirdPartyTelemetryEnrichments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/ListThirdPartyTelemetryEnrichments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/ListThirdPartyTelemetryEnrichments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/ListThirdPartyTelemetryEnrichments) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/ListThirdPartyTelemetryEnrichments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/ListThirdPartyTelemetryEnrichments) 