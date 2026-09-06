

# ListConnectors
<a name="API_ListConnectors"></a>

Returns a list of all the connectors in this account and Region. The list is limited to connectors whose name starts with the specified prefix. The response also includes a description of each of the listed connectors.

## Request Syntax
<a name="API_ListConnectors_RequestSyntax"></a>

```
GET /v1/connectors?connectorNamePrefix={{connectorNamePrefix}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListConnectors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [connectorNamePrefix](#API_ListConnectors_RequestSyntax) **   <a name="MSKC-ListConnectors-request-uri-connectorNamePrefix"></a>
The name prefix that you want to use to search for and list connectors.

 ** [maxResults](#API_ListConnectors_RequestSyntax) **   <a name="MSKC-ListConnectors-request-uri-maxResults"></a>
The maximum number of connectors to list in one response.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListConnectors_RequestSyntax) **   <a name="MSKC-ListConnectors-request-uri-nextToken"></a>
If the response of a ListConnectors operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where the previous operation left off.

## Request Body
<a name="API_ListConnectors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListConnectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectors": [ 
      { 
         "capacity": { 
            "autoScaling": { 
               "maxAutoscalingTaskCount": number,
               "maxWorkerCount": number,
               "mcuCount": number,
               "minWorkerCount": number,
               "scaleInPolicy": { 
                  "cpuUtilizationPercentage": number
               },
               "scaleOutPolicy": { 
                  "cpuUtilizationPercentage": number
               }
            },
            "provisionedCapacity": { 
               "mcuCount": number,
               "workerCount": number
            }
         },
         "connectorArn": "string",
         "connectorDescription": "string",
         "connectorName": "string",
         "connectorState": "string",
         "creationTime": "string",
         "currentVersion": "string",
         "kafkaCluster": { 
            "apacheKafkaCluster": { 
               "bootstrapServers": "string",
               "vpc": { 
                  "securityGroups": [ "string" ],
                  "subnets": [ "string" ]
               }
            }
         },
         "kafkaClusterClientAuthentication": { 
            "authenticationType": "string"
         },
         "kafkaClusterEncryptionInTransit": { 
            "encryptionType": "string"
         },
         "kafkaConnectVersion": "string",
         "logDelivery": { 
            "workerLogDelivery": { 
               "cloudWatchLogs": { 
                  "enabled": boolean,
                  "logGroup": "string"
               },
               "firehose": { 
                  "deliveryStream": "string",
                  "enabled": boolean
               },
               "s3": { 
                  "bucket": "string",
                  "enabled": boolean,
                  "prefix": "string"
               }
            }
         },
         "networkType": "string",
         "plugins": [ 
            { 
               "customPlugin": { 
                  "customPluginArn": "string",
                  "revision": number
               }
            }
         ],
         "serviceExecutionRoleArn": "string",
         "workerConfiguration": { 
            "revision": number,
            "workerConfigurationArn": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListConnectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectors](#API_ListConnectors_ResponseSyntax) **   <a name="MSKC-ListConnectors-response-connectors"></a>
An array of connector descriptions.  
Type: Array of [ConnectorSummary](API_ConnectorSummary.md) objects

 ** [nextToken](#API_ListConnectors_ResponseSyntax) **   <a name="MSKC-ListConnectors-response-nextToken"></a>
If the response of a ListConnectors operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where it left off.  
Type: String

## Errors
<a name="API_ListConnectors_Errors"></a>

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
<a name="API_ListConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kafkaconnect-2021-09-14/ListConnectors) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kafkaconnect-2021-09-14/ListConnectors) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/ListConnectors) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kafkaconnect-2021-09-14/ListConnectors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/ListConnectors) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/ListConnectors) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kafkaconnect-2021-09-14/ListConnectors) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kafkaconnect-2021-09-14/ListConnectors) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kafkaconnect-2021-09-14/ListConnectors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/ListConnectors) 