

# UpdateConnector
<a name="API_UpdateConnector"></a>

Updates the specified connector. For request body, specify only one parameter: either `capacity` or `connectorConfiguration`.

## Request Syntax
<a name="API_UpdateConnector_RequestSyntax"></a>

```
PUT /v1/connectors/{{connectorArn}}?currentVersion={{currentVersion}} HTTP/1.1
Content-type: application/json

{
   "capacity": { 
      "autoScaling": { 
         "maxAutoscalingTaskCount": {{number}},
         "maxWorkerCount": {{number}},
         "mcuCount": {{number}},
         "minWorkerCount": {{number}},
         "scaleInPolicy": { 
            "cpuUtilizationPercentage": {{number}}
         },
         "scaleOutPolicy": { 
            "cpuUtilizationPercentage": {{number}}
         }
      },
      "provisionedCapacity": { 
         "mcuCount": {{number}},
         "workerCount": {{number}}
      }
   },
   "connectorConfiguration": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_UpdateConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [connectorArn](#API_UpdateConnector_RequestSyntax) **   <a name="MSKC-UpdateConnector-request-uri-connectorArn"></a>
The Amazon Resource Name (ARN) of the connector that you want to update.  
Required: Yes

 ** [currentVersion](#API_UpdateConnector_RequestSyntax) **   <a name="MSKC-UpdateConnector-request-uri-currentVersion"></a>
The current version of the connector that you want to update.  
Required: Yes

## Request Body
<a name="API_UpdateConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [capacity](#API_UpdateConnector_RequestSyntax) **   <a name="MSKC-UpdateConnector-request-capacity"></a>
The target capacity.  
Type: [CapacityUpdate](API_CapacityUpdate.md) object  
Required: No

 ** [connectorConfiguration](#API_UpdateConnector_RequestSyntax) **   <a name="MSKC-UpdateConnector-request-connectorConfiguration"></a>
A map of keys to values that represent the configuration for the connector.  
Type: String to string map  
Required: No

## Response Syntax
<a name="API_UpdateConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectorArn": "string",
   "connectorOperationArn": "string",
   "connectorState": "string"
}
```

## Response Elements
<a name="API_UpdateConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectorArn](#API_UpdateConnector_ResponseSyntax) **   <a name="MSKC-UpdateConnector-response-connectorArn"></a>
The Amazon Resource Name (ARN) of the connector.  
Type: String

 ** [connectorOperationArn](#API_UpdateConnector_ResponseSyntax) **   <a name="MSKC-UpdateConnector-response-connectorOperationArn"></a>
The Amazon Resource Name (ARN) of the connector operation.  
Type: String

 ** [connectorState](#API_UpdateConnector_ResponseSyntax) **   <a name="MSKC-UpdateConnector-response-connectorState"></a>
The state of the connector.  
Type: String  
Valid Values: `RUNNING | CREATING | UPDATING | DELETING | FAILED` 

## Errors
<a name="API_UpdateConnector_Errors"></a>

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
<a name="API_UpdateConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kafkaconnect-2021-09-14/UpdateConnector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kafkaconnect-2021-09-14/UpdateConnector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/UpdateConnector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kafkaconnect-2021-09-14/UpdateConnector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/UpdateConnector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/UpdateConnector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kafkaconnect-2021-09-14/UpdateConnector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kafkaconnect-2021-09-14/UpdateConnector) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kafkaconnect-2021-09-14/UpdateConnector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/UpdateConnector) 