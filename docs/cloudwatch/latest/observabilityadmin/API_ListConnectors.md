

# ListConnectors

Lists the connectors in the account and Region. This operation returns results in pages. To get the next page, pass the returned `NextToken` in the next call. We recommend that you use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListConnectors_RequestSyntax"></a>

```
POST /ListConnectors HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListConnectors_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConnectors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListConnectors_RequestSyntax) **   <a name="cwoa-ListConnectors-request-MaxResults"></a>
The maximum number of connectors to return in one call. The default is 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListConnectors_RequestSyntax) **   <a name="cwoa-ListConnectors-request-NextToken"></a>
The token for the next page of results, returned by a previous call.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Pattern: `[A-Za-z0-9+/=_-]+`   
Required: No

## Response Syntax
<a name="API_ListConnectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectorSummaries": [ 
      { 
         "Arn": "string",
         "CreatedTimeStamp": number,
         "Name": "string",
         "Provider": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConnectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectorSummaries](#API_ListConnectors_ResponseSyntax) **   <a name="cwoa-ListConnectors-response-ConnectorSummaries"></a>
The connectors in the account and Region.  
Type: Array of [ConnectorSummary](API_ConnectorSummary.md) objects

 ** [NextToken](#API_ListConnectors_ResponseSyntax) **   <a name="cwoa-ListConnectors-response-NextToken"></a>
The token to use in the next call to get the next page of results. Absent when there are no more results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Pattern: `[A-Za-z0-9+/=_-]+` 

## Errors
<a name="API_ListConnectors_Errors"></a>

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
<a name="API_ListConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/ListConnectors) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/ListConnectors) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/ListConnectors) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/ListConnectors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/ListConnectors) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/ListConnectors) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/ListConnectors) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/ListConnectors) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/ListConnectors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/ListConnectors) 