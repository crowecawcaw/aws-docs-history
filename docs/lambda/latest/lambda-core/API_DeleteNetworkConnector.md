

# DeleteNetworkConnector
<a name="API_DeleteNetworkConnector"></a>

Initiates deletion of a network connector. The connector transitions to `DELETING` state while elastic network interfaces are cleaned up asynchronously. After deletion completes, subsequent calls to `GetNetworkConnector` return `ResourceNotFoundException`.

This operation is idempotent — calling delete on a connector that is already deleting or has been deleted succeeds without error. You can delete connectors in `ACTIVE` or `FAILED` states. Before deleting a connector, ensure that no Lambda MicroVMs are using it, as they will lose VPC egress connectivity immediately.

## Request Syntax
<a name="API_DeleteNetworkConnector_RequestSyntax"></a>

```
DELETE /2026-04-04/network-connectors/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteNetworkConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_DeleteNetworkConnector_RequestSyntax) **   <a name="lambdacore-DeleteNetworkConnector-request-uri-Identifier"></a>
The identifier of the network connector to delete. You can specify the connector ID, name, or full ARN.  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Required: Yes

## Request Body
<a name="API_DeleteNetworkConnector_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteNetworkConnector_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "Arn": "string",
   "Configuration": { ... },
   "Id": "string",
   "Name": "string",
   "OperatorRole": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_DeleteNetworkConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DeleteNetworkConnector_ResponseSyntax) **   <a name="lambdacore-DeleteNetworkConnector-response-Arn"></a>
The Amazon Resource Name (ARN) of the network connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9]|[1-9][0-9]+)?)` 

 ** [Configuration](#API_DeleteNetworkConnector_ResponseSyntax) **   <a name="lambdacore-DeleteNetworkConnector-response-Configuration"></a>
The network configuration of the connector, including VPC subnets and security groups.  
Type: [NetworkConnectorConfiguration](API_NetworkConnectorConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [Id](#API_DeleteNetworkConnector_ResponseSyntax) **   <a name="lambdacore-DeleteNetworkConnector-response-Id"></a>
The unique identifier of the network connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 140.

 ** [Name](#API_DeleteNetworkConnector_ResponseSyntax) **   <a name="lambdacore-DeleteNetworkConnector-response-Name"></a>
The name of the network connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9]|[1-9][0-9]+)?)|[a-zA-Z0-9_-]{1,64}` 

 ** [OperatorRole](#API_DeleteNetworkConnector_ResponseSyntax) **   <a name="lambdacore-DeleteNetworkConnector-response-OperatorRole"></a>
The ARN of the IAM role that Lambda uses to manage the underlying ENI resources for this connector.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10000.  
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+` 

 ** [State](#API_DeleteNetworkConnector_ResponseSyntax) **   <a name="lambdacore-DeleteNetworkConnector-response-State"></a>
The current state of the network connector. The State field is typically `DELETING` after this call.  
Type: String  
Valid Values: `PENDING | ACTIVE | INACTIVE | FAILED | DELETING | DELETE_FAILED` 

## Errors
<a name="API_DeleteNetworkConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **   
One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.    
 ** Type **   
The exception type.
HTTP Status Code: 400

 ** ResourceConflictException **   
The request could not be completed due to a conflict with the current state of the resource. For example, attempting to update a connector that is not in `ACTIVE` state.    
 ** Type **   
The exception type.
HTTP Status Code: 409

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
<a name="API_DeleteNetworkConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-core-2026-04-30/DeleteNetworkConnector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-core-2026-04-30/DeleteNetworkConnector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/DeleteNetworkConnector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-core-2026-04-30/DeleteNetworkConnector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/DeleteNetworkConnector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-core-2026-04-30/DeleteNetworkConnector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-core-2026-04-30/DeleteNetworkConnector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-core-2026-04-30/DeleteNetworkConnector) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-core-2026-04-30/DeleteNetworkConnector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/DeleteNetworkConnector) 