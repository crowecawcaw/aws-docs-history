

# DeleteWorkerConfiguration
<a name="API_DeleteWorkerConfiguration"></a>

Deletes the specified worker configuration.

## Request Syntax
<a name="API_DeleteWorkerConfiguration_RequestSyntax"></a>

```
DELETE /v1/worker-configurations/{{workerConfigurationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteWorkerConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workerConfigurationArn](#API_DeleteWorkerConfiguration_RequestSyntax) **   <a name="MSKC-DeleteWorkerConfiguration-request-uri-workerConfigurationArn"></a>
The Amazon Resource Name (ARN) of the worker configuration that you want to delete.  
Required: Yes

## Request Body
<a name="API_DeleteWorkerConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteWorkerConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "workerConfigurationArn": "string",
   "workerConfigurationState": "string"
}
```

## Response Elements
<a name="API_DeleteWorkerConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workerConfigurationArn](#API_DeleteWorkerConfiguration_ResponseSyntax) **   <a name="MSKC-DeleteWorkerConfiguration-response-workerConfigurationArn"></a>
The Amazon Resource Name (ARN) of the worker configuration that you requested to delete.  
Type: String

 ** [workerConfigurationState](#API_DeleteWorkerConfiguration_ResponseSyntax) **   <a name="MSKC-DeleteWorkerConfiguration-response-workerConfigurationState"></a>
The state of the worker configuration.  
Type: String  
Valid Values: `ACTIVE | DELETING` 

## Errors
<a name="API_DeleteWorkerConfiguration_Errors"></a>

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
<a name="API_DeleteWorkerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kafkaconnect-2021-09-14/DeleteWorkerConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kafkaconnect-2021-09-14/DeleteWorkerConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/DeleteWorkerConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kafkaconnect-2021-09-14/DeleteWorkerConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/DeleteWorkerConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/DeleteWorkerConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kafkaconnect-2021-09-14/DeleteWorkerConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kafkaconnect-2021-09-14/DeleteWorkerConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kafkaconnect-2021-09-14/DeleteWorkerConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/DeleteWorkerConfiguration) 