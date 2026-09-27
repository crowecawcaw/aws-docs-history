

# RestartConnector
<a name="API_RestartConnector"></a>

Restarts the specified connector. By default, this operation restarts the connector and all of its tasks. This operation is asynchronous and returns a connector operation ARN that you can pass to `DescribeConnectorOperation` to track the state of the restart.

## Request Syntax
<a name="API_RestartConnector_RequestSyntax"></a>

```
POST /v1/connectors/{{connectorArn}}/restart?onlyFailedTasks={{onlyFailedTasks}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RestartConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [connectorArn](#API_RestartConnector_RequestSyntax) **   <a name="MSKC-RestartConnector-request-uri-connectorArn"></a>
The Amazon Resource Name (ARN) of the connector that you want to restart.  
Required: Yes

 ** [onlyFailedTasks](#API_RestartConnector_RequestSyntax) **   <a name="MSKC-RestartConnector-request-uri-onlyFailedTasks"></a>
Specifies whether to restart only the connector's failed tasks. If `true`, the operation restarts only the tasks that are currently in a failed state, and healthy tasks continue running. If `false` or not specified, the operation restarts the connector and all of its tasks.

## Request Body
<a name="API_RestartConnector_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RestartConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectorArn": "string",
   "connectorOperationArn": "string"
}
```

## Response Elements
<a name="API_RestartConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectorArn](#API_RestartConnector_ResponseSyntax) **   <a name="MSKC-RestartConnector-response-connectorArn"></a>
The Amazon Resource Name (ARN) of the connector.  
Type: String

 ** [connectorOperationArn](#API_RestartConnector_ResponseSyntax) **   <a name="MSKC-RestartConnector-response-connectorOperationArn"></a>
The Amazon Resource Name (ARN) of the connector operation created to perform the restart.  
Type: String

## Errors
<a name="API_RestartConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.  
HTTP Status Code: 400

 ** ForbiddenException **   
HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.  
HTTP Status Code: 403

 ** InternalServerErrorException **   
HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.  
HTTP Status Code: 500

 ** NotFoundException **   
HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.  
HTTP Status Code: 404

 ** ServiceUnavailableException **   
HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.  
HTTP Status Code: 503

 ** TooManyRequestsException **   
HTTP Status Code 429: Limit exceeded. Resource limit reached.  
HTTP Status Code: 429

 ** UnauthorizedException **   
HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.  
HTTP Status Code: 401

## See Also
<a name="API_RestartConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kafkaconnect-2021-09-14/RestartConnector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kafkaconnect-2021-09-14/RestartConnector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/RestartConnector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kafkaconnect-2021-09-14/RestartConnector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/RestartConnector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/RestartConnector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kafkaconnect-2021-09-14/RestartConnector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kafkaconnect-2021-09-14/RestartConnector) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kafkaconnect-2021-09-14/RestartConnector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/RestartConnector) 