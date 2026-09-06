

# ListNetworkConnectors
<a name="API_ListNetworkConnectors"></a>

Returns a paginated list of network connectors in your account for the current Region. You can optionally filter results by connector state. Use the `Marker` parameter from a previous response to retrieve the next page of results.

Each item in the response includes the connector ARN, name, ID, type, current state, and last modified timestamp. To retrieve full configuration details for a specific connector, use `GetNetworkConnector`.

## Request Syntax
<a name="API_ListNetworkConnectors_RequestSyntax"></a>

```
GET /2026-04-04/network-connectors?Marker={{Marker}}&MaxItems={{MaxItems}}&State={{State}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNetworkConnectors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListNetworkConnectors_RequestSyntax) **   <a name="lambdacore-ListNetworkConnectors-request-uri-Marker"></a>
The pagination token from a previous `ListNetworkConnectors` response. Use this value to retrieve the next page of results.

 ** [MaxItems](#API_ListNetworkConnectors_RequestSyntax) **   <a name="lambdacore-ListNetworkConnectors-request-uri-MaxItems"></a>
The maximum number of connectors to return per page. Valid range: 1 to 100.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [State](#API_ListNetworkConnectors_RequestSyntax) **   <a name="lambdacore-ListNetworkConnectors-request-uri-State"></a>
Optional filter to return only connectors in the specified state (for example, `ACTIVE` or `FAILED`).  
Valid Values: `PENDING | ACTIVE | INACTIVE | FAILED | DELETING | DELETE_FAILED` 

## Request Body
<a name="API_ListNetworkConnectors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNetworkConnectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NetworkConnectors": [ 
      { 
         "Arn": "string",
         "Id": "string",
         "LastModified": "string",
         "Name": "string",
         "State": "string",
         "Type": "string"
      }
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListNetworkConnectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NetworkConnectors](#API_ListNetworkConnectors_ResponseSyntax) **   <a name="lambdacore-ListNetworkConnectors-response-NetworkConnectors"></a>
A list of network connector summaries for the current page of results.  
Type: Array of [NetworkConnectorSummary](API_NetworkConnectorSummary.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [NextMarker](#API_ListNetworkConnectors_ResponseSyntax) **   <a name="lambdacore-ListNetworkConnectors-response-NextMarker"></a>
The pagination token to include in a subsequent request to retrieve the next page. This value is null when there are no more results.  
Type: String

## Errors
<a name="API_ListNetworkConnectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **   
One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.    
 ** Type **   
The exception type.
HTTP Status Code: 400

 ** ServiceException **   
An internal service error occurred. Retry the request with exponential backoff.    
 ** Type **   
The exception type.
HTTP Status Code: 500

 ** TooManyRequestsException **   
The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.    
 ** Reason **   
The reason for the throttling.  
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the request.  
 ** Type **   
The exception type.
HTTP Status Code: 429

## See Also
<a name="API_ListNetworkConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-core-2026-04-30/ListNetworkConnectors) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-core-2026-04-30/ListNetworkConnectors) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/ListNetworkConnectors) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-core-2026-04-30/ListNetworkConnectors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/ListNetworkConnectors) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-core-2026-04-30/ListNetworkConnectors) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-core-2026-04-30/ListNetworkConnectors) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-core-2026-04-30/ListNetworkConnectors) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-core-2026-04-30/ListNetworkConnectors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/ListNetworkConnectors) 