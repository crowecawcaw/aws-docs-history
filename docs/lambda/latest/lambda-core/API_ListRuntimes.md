

# ListRuntimes

Returns a paginated list of runtimes in your account for the current Region.

## Request Syntax
<a name="API_ListRuntimes_RequestSyntax"></a>

```
GET /2026-10-01/runtimes?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRuntimes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListRuntimes_RequestSyntax) **   <a name="lambdacore-ListRuntimes-request-uri-MaxResults"></a>
The maximum number of runtimes to return per page. Valid range: 1 to 100.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListRuntimes_RequestSyntax) **   <a name="lambdacore-ListRuntimes-request-uri-NextToken"></a>
The pagination token from a previous response. Use it to retrieve the next page of results.

## Request Body
<a name="API_ListRuntimes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRuntimes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [ 
      { 
         "Arn": "string",
         "Created": "string",
         "Description": "string",
         "LastModified": "string",
         "LicenseInfo": "string",
         "Name": "string",
         "PendingDeletionAt": "string",
         "ReleaseLifecycle": { 
            "DeprecationDate": "string",
            "FunctionCreateBlockDate": "string",
            "FunctionUpdateBlockDate": "string",
            "ReleaseState": "string"
         },
         "State": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListRuntimes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListRuntimes_ResponseSyntax) **   <a name="lambdacore-ListRuntimes-response-Items"></a>
The list of runtimes for the current page of results.  
Type: Array of [RuntimeInfo](API_RuntimeInfo.md) objects

 ** [NextToken](#API_ListRuntimes_ResponseSyntax) **   <a name="lambdacore-ListRuntimes-response-NextToken"></a>
The pagination token to include in a subsequent request to retrieve the next page of results.  
Type: String

## Errors
<a name="API_ListRuntimes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **   
One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.    
 ** message **   
The error message that describes the exception.  
 ** Type **   
The exception type.
HTTP Status Code: 400

 ** ServiceException **   
An internal service error occurred. Retry the request with exponential backoff.    
 ** Message **   
The error message that describes the exception.  
 ** Type **   
The exception type.
HTTP Status Code: 500

 ** TooManyRequestsException **   
The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.    
 ** message **   
The error message that describes the exception.  
 ** Reason **   
The reason for the throttling.  
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the request.  
 ** Type **   
The exception type.
HTTP Status Code: 429

## See Also
<a name="API_ListRuntimes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-core-2026-04-30/ListRuntimes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-core-2026-04-30/ListRuntimes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/ListRuntimes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-core-2026-04-30/ListRuntimes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/ListRuntimes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-core-2026-04-30/ListRuntimes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-core-2026-04-30/ListRuntimes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-core-2026-04-30/ListRuntimes) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-core-2026-04-30/ListRuntimes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/ListRuntimes) 