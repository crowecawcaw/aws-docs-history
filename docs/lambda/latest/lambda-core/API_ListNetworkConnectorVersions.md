

# ListNetworkConnectorVersions
<a name="API_ListNetworkConnectorVersions"></a>

Returns a paginated list of the versions of a network connector. Each configuration update creates a new immutable version; this operation lists those versions for the connector you specify. You can optionally filter results by version state. Use the `Marker` parameter from a previous response to retrieve the next page of results.

Each item in the response includes the version-qualified ARN, version number, current state, and last modified timestamp for that version. To retrieve the current (latest) configuration of the connector, use `GetNetworkConnector`; to inspect a specific version, call `GetNetworkConnector` with a version-qualified identifier.

## Request Syntax
<a name="API_ListNetworkConnectorVersions_RequestSyntax"></a>

```
GET /2026-04-04/network-connectors/{{Identifier}}/versions?Marker={{Marker}}&MaxItems={{MaxItems}}&State={{State}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNetworkConnectorVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_ListNetworkConnectorVersions_RequestSyntax) **   <a name="lambdacore-ListNetworkConnectorVersions-request-uri-Identifier"></a>
The identifier of the network connector whose versions you want to list. You can specify the connector ID, name, or full ARN. Specify an unqualified identifier — this operation lists all versions of the connector, not a specific version.  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Required: Yes

 ** [Marker](#API_ListNetworkConnectorVersions_RequestSyntax) **   <a name="lambdacore-ListNetworkConnectorVersions-request-uri-Marker"></a>
The pagination token from a previous `ListNetworkConnectorVersions` response. Use this value to retrieve the next page of results.

 ** [MaxItems](#API_ListNetworkConnectorVersions_RequestSyntax) **   <a name="lambdacore-ListNetworkConnectorVersions-request-uri-MaxItems"></a>
The maximum number of versions to return per page. Valid range: 1 to 100.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [State](#API_ListNetworkConnectorVersions_RequestSyntax) **   <a name="lambdacore-ListNetworkConnectorVersions-request-uri-State"></a>
Optional filter to return only versions in the specified state (for example, `ACTIVE` or `FAILED`).  
Valid Values: `PENDING | ACTIVE | INACTIVE | FAILED | DELETING | DELETE_FAILED` 

## Request Body
<a name="API_ListNetworkConnectorVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNetworkConnectorVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NetworkConnectorVersions": [ 
      { 
         "Arn": "string",
         "Id": "string",
         "LastModified": "string",
         "Name": "string",
         "State": "string",
         "StateReason": "string",
         "StateReasonCode": "string",
         "Version": number,
         "VersionArn": "string"
      }
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListNetworkConnectorVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NetworkConnectorVersions](#API_ListNetworkConnectorVersions_ResponseSyntax) **   <a name="lambdacore-ListNetworkConnectorVersions-response-NetworkConnectorVersions"></a>
A list of connector version summaries for the current page of results.  
Type: Array of [NetworkConnectorVersionSummary](API_NetworkConnectorVersionSummary.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextMarker](#API_ListNetworkConnectorVersions_ResponseSyntax) **   <a name="lambdacore-ListNetworkConnectorVersions-response-NextMarker"></a>
The pagination token to include in a subsequent request to retrieve the next page. This value is null when there are no more results.  
Type: String

## Errors
<a name="API_ListNetworkConnectorVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **   
One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.    
 ** Type **   
The exception type.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified network connector does not exist. Verify the identifier (ID, name, or ARN) and Region.    
 ** Type **   
The exception type.
HTTP Status Code: 404

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
<a name="API_ListNetworkConnectorVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-core-2026-04-30/ListNetworkConnectorVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-core-2026-04-30/ListNetworkConnectorVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/ListNetworkConnectorVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-core-2026-04-30/ListNetworkConnectorVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/ListNetworkConnectorVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-core-2026-04-30/ListNetworkConnectorVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-core-2026-04-30/ListNetworkConnectorVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-core-2026-04-30/ListNetworkConnectorVersions) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-core-2026-04-30/ListNetworkConnectorVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/ListNetworkConnectorVersions) 