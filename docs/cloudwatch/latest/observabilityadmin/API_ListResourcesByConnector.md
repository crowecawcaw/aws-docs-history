

# ListResourcesByConnector

Lists resources in your cloud provider that the connector can access, such as management groups, subscriptions, resource types, Regions, resources, and Event Hubs. Use the results to build a telemetry manifest. This operation returns results in pages. To get the next page, pass the returned `NextToken` in the next call. We recommend that you use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListResourcesByConnector_RequestSyntax"></a>

```
POST /ListResourcesByConnector HTTP/1.1
Content-type: application/json

{
   "ConnectorIdentifier": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Selector": { ... }
}
```

## URI Request Parameters
<a name="API_ListResourcesByConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListResourcesByConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConnectorIdentifier](#API_ListResourcesByConnector_RequestSyntax) **   <a name="cwoa-ListResourcesByConnector-request-ConnectorIdentifier"></a>
The connector to use for the query. Specify one of the following:  
+ The Amazon Resource Name (ARN) of the connector
+ The ID of the connector
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `([a-z0-9]+|arn:aws[a-z0-9\-]*:observabilityadmin:[a-z0-9-]+:[0-9]{12}:connector/(azure/)?[a-z0-9]+)`   
Required: Yes

 ** [MaxResults](#API_ListResourcesByConnector_RequestSyntax) **   <a name="cwoa-ListResourcesByConnector-request-MaxResults"></a>
The maximum number of results to return in one call. For an `EventHubs` query, a page can contain more results than this value.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [NextToken](#API_ListResourcesByConnector_RequestSyntax) **   <a name="cwoa-ListResourcesByConnector-request-NextToken"></a>
The token for the next page of results, returned by a previous call.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Pattern: `[A-Za-z0-9+/=_-]+`   
Required: No

 ** [Selector](#API_ListResourcesByConnector_RequestSyntax) **   <a name="cwoa-ListResourcesByConnector-request-Selector"></a>
What to list: one cloud provider, and one type of resource in that provider.  
Type: [ConnectorQuery](API_ConnectorQuery.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_ListResourcesByConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Results": { ... }
}
```

## Response Elements
<a name="API_ListResourcesByConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourcesByConnector_ResponseSyntax) **   <a name="cwoa-ListResourcesByConnector-response-NextToken"></a>
The token to use in the next call to get the next page of results. Absent when there are no more results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Pattern: `[A-Za-z0-9+/=_-]+` 

 ** [Results](#API_ListResourcesByConnector_ResponseSyntax) **   <a name="cwoa-ListResourcesByConnector-response-Results"></a>
The results, in the same shape as the `Selector` that you specified.  
Type: [ConnectorQueryResults](API_ConnectorQueryResults.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_ListResourcesByConnector_Errors"></a>

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
<a name="API_ListResourcesByConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/ListResourcesByConnector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/ListResourcesByConnector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/ListResourcesByConnector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/ListResourcesByConnector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/ListResourcesByConnector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/ListResourcesByConnector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/ListResourcesByConnector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/ListResourcesByConnector) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/ListResourcesByConnector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/ListResourcesByConnector) 