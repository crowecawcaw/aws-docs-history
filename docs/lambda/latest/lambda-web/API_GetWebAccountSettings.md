

# GetWebAccountSettings
<a name="API_GetWebAccountSettings"></a>

Retrieves details about your AWS Lambda Web Functions account settings for the current AWS Region, including the quotas that apply to web functions and your current usage.

## Request Syntax
<a name="API_GetWebAccountSettings_RequestSyntax"></a>

```
GET /2025-03-07/web-account-settings HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWebAccountSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetWebAccountSettings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWebAccountSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accountQuotas": { 
      "maxEndpointsPerFunction": number,
      "maxRevisionsPerFunction": number,
      "maxTotalArmVCpus": number,
      "maxTotalRateLimit": number
   },
   "accountUsage": { 
      "functionCount": number
   }
}
```

## Response Elements
<a name="API_GetWebAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountQuotas](#API_GetWebAccountSettings_ResponseSyntax) **   <a name="lambdaweb-GetWebAccountSettings-response-accountQuotas"></a>
The quotas that apply to web functions in your account in the current AWS Region.  
Type: [AccountQuotas](API_AccountQuotas.md) object

 ** [accountUsage](#API_GetWebAccountSettings_ResponseSyntax) **   <a name="lambdaweb-GetWebAccountSettings-response-accountUsage"></a>
The current web function usage for your account in the current AWS Region.  
Type: [AccountUsage](API_AccountUsage.md) object

## Errors
<a name="API_GetWebAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.    
 ** message **   
A message describing the access denied error.
HTTP Status Code: 403

 ** InternalServerException **   
The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.    
 ** message **   
A message describing the internal error.
HTTP Status Code: 500

 ** ThrottlingException **   
The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.    
 ** message **   
A message describing the throttling error.  
 ** quotaCode **   
The quota code that was exceeded, if applicable.  
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the request.  
 ** serviceCode **   
The service code of the throttled service.
HTTP Status Code: 429

## See Also
<a name="API_GetWebAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-web-2025-03-07/GetWebAccountSettings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-web-2025-03-07/GetWebAccountSettings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/GetWebAccountSettings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-web-2025-03-07/GetWebAccountSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/GetWebAccountSettings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-web-2025-03-07/GetWebAccountSettings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-web-2025-03-07/GetWebAccountSettings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-web-2025-03-07/GetWebAccountSettings) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-web-2025-03-07/GetWebAccountSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/GetWebAccountSettings) 