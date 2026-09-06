

# UpdateNetworkConnector
<a name="API_UpdateNetworkConnector"></a>

Updates the VPC configuration or operator role of an existing network connector. You can modify the subnet IDs, security group IDs, network protocol, or operator role. The connector must be in `ACTIVE` state to accept updates.

This operation is asynchronous. The connector remains in `ACTIVE` state during the update — existing workloads that reference this connector are not disrupted. Use `GetNetworkConnector` to monitor the `LastUpdateStatus` field, which transitions through `InProgress` to `Successful` or `Failed`. If the update fails, the `LastUpdateStatusReasonCode` field provides a specific error code for troubleshooting. This operation is idempotent when you provide a `ClientToken`.

## Request Syntax
<a name="API_UpdateNetworkConnector_RequestSyntax"></a>

```
PUT /2026-04-04/network-connectors/{{Identifier}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Configuration": { ... },
   "OperatorRole": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateNetworkConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_UpdateNetworkConnector_RequestSyntax) **   <a name="lambdacore-UpdateNetworkConnector-request-uri-Identifier"></a>
The identifier of the network connector to update. You can specify the connector ID, name, or full ARN.  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Required: Yes

## Request Body
<a name="API_UpdateNetworkConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateNetworkConnector_RequestSyntax) **   <a name="lambdacore-UpdateNetworkConnector-request-ClientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the update request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** [Configuration](#API_UpdateNetworkConnector_RequestSyntax) **   <a name="lambdacore-UpdateNetworkConnector-request-Configuration"></a>
The updated network configuration for the connector. Provide the full `VpcEgressConfiguration` including all subnet IDs and security group IDs — this replaces the existing configuration.  
Type: [NetworkConnectorConfiguration](API_NetworkConnectorConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [OperatorRole](#API_UpdateNetworkConnector_RequestSyntax) **   <a name="lambdacore-UpdateNetworkConnector-request-OperatorRole"></a>
The updated ARN of the IAM role that Lambda assumes to manage ENIs. Use this to change the operator role without recreating the connector.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10000.  
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`   
Required: No

## Response Syntax
<a name="API_UpdateNetworkConnector_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "Id": "string"
}
```

## Response Elements
<a name="API_UpdateNetworkConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [Id](#API_UpdateNetworkConnector_ResponseSyntax) **   <a name="lambdacore-UpdateNetworkConnector-response-Id"></a>
The unique identifier of the network connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 140.

## Errors
<a name="API_UpdateNetworkConnector_Errors"></a>

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
<a name="API_UpdateNetworkConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-core-2026-04-30/UpdateNetworkConnector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-core-2026-04-30/UpdateNetworkConnector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/UpdateNetworkConnector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-core-2026-04-30/UpdateNetworkConnector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/UpdateNetworkConnector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-core-2026-04-30/UpdateNetworkConnector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-core-2026-04-30/UpdateNetworkConnector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-core-2026-04-30/UpdateNetworkConnector) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-core-2026-04-30/UpdateNetworkConnector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/UpdateNetworkConnector) 