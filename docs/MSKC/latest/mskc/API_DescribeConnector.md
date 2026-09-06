

# DescribeConnector
<a name="API_DescribeConnector"></a>

Returns summary information about the connector.

## Request Syntax
<a name="API_DescribeConnector_RequestSyntax"></a>

```
GET /v1/connectors/{{connectorArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [connectorArn](#API_DescribeConnector_RequestSyntax) **   <a name="MSKC-DescribeConnector-request-uri-connectorArn"></a>
The Amazon Resource Name (ARN) of the connector that you want to describe.  
Required: Yes

## Request Body
<a name="API_DescribeConnector_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
   "connectorConfiguration": { 
      "string" : "string" 
   },
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
   "stateDescription": { 
      "code": "string",
      "message": "string"
   },
   "workerConfiguration": { 
      "revision": number,
      "workerConfigurationArn": "string"
   }
}
```

## Response Elements
<a name="API_DescribeConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capacity](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-capacity"></a>
Information about the capacity of the connector, whether it is auto scaled or provisioned.  
Type: [CapacityDescription](API_CapacityDescription.md) object

 ** [connectorArn](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-connectorArn"></a>
The Amazon Resource Name (ARN) of the connector.  
Type: String

 ** [connectorConfiguration](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-connectorConfiguration"></a>
A map of keys to values that represent the configuration for the connector.  
Type: String to string map

 ** [connectorDescription](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-connectorDescription"></a>
A summary description of the connector.  
Type: String

 ** [connectorName](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-connectorName"></a>
The name of the connector.  
Type: String

 ** [connectorState](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-connectorState"></a>
The state of the connector.  
Type: String  
Valid Values: `RUNNING | CREATING | UPDATING | DELETING | FAILED` 

 ** [creationTime](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-creationTime"></a>
The time the connector was created.  
Type: Timestamp

 ** [currentVersion](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-currentVersion"></a>
The current version of the connector.  
Type: String

 ** [kafkaCluster](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-kafkaCluster"></a>
The Apache Kafka cluster that the connector is connected to.  
Type: [KafkaClusterDescription](API_KafkaClusterDescription.md) object

 ** [kafkaClusterClientAuthentication](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-kafkaClusterClientAuthentication"></a>
The type of client authentication used to connect to the Apache Kafka cluster. The value is NONE when no client authentication is used.  
Type: [KafkaClusterClientAuthenticationDescription](API_KafkaClusterClientAuthenticationDescription.md) object

 ** [kafkaClusterEncryptionInTransit](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-kafkaClusterEncryptionInTransit"></a>
Details of encryption in transit to the Apache Kafka cluster.  
Type: [KafkaClusterEncryptionInTransitDescription](API_KafkaClusterEncryptionInTransitDescription.md) object

 ** [kafkaConnectVersion](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-kafkaConnectVersion"></a>
The version of Kafka Connect. It has to be compatible with both the Apache Kafka cluster's version and the plugins.  
Type: String

 ** [logDelivery](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-logDelivery"></a>
Details about delivering logs to Amazon CloudWatch Logs.  
Type: [LogDeliveryDescription](API_LogDeliveryDescription.md) object

 ** [networkType](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-networkType"></a>
The network type of the connector. It gives connectors connectivity to either IPv4 (IPV4) or IPv4 and IPv6 (DUAL) destinations. Defaults to IPV4.  
Type: String  
Valid Values: `IPV4 | DUAL` 

 ** [plugins](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-plugins"></a>
Specifies which plugins were used for this connector.  
Type: Array of [PluginDescription](API_PluginDescription.md) objects

 ** [serviceExecutionRoleArn](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-serviceExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.  
Type: String

 ** [stateDescription](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-stateDescription"></a>
Details about the state of a connector.  
Type: [StateDescription](API_StateDescription.md) object

 ** [workerConfiguration](#API_DescribeConnector_ResponseSyntax) **   <a name="MSKC-DescribeConnector-response-workerConfiguration"></a>
Specifies which worker configuration was used for the connector.  
Type: [WorkerConfigurationDescription](API_WorkerConfigurationDescription.md) object

## Errors
<a name="API_DescribeConnector_Errors"></a>

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
<a name="API_DescribeConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kafkaconnect-2021-09-14/DescribeConnector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kafkaconnect-2021-09-14/DescribeConnector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/DescribeConnector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kafkaconnect-2021-09-14/DescribeConnector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/DescribeConnector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/DescribeConnector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kafkaconnect-2021-09-14/DescribeConnector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kafkaconnect-2021-09-14/DescribeConnector) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kafkaconnect-2021-09-14/DescribeConnector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/DescribeConnector) 