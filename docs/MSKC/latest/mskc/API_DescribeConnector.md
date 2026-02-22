# DescribeConnector

Returns summary information about the connector.

## Request Syntax

```
GET /v1/connectors/`connectorArn` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[connectorArn](#API_DescribeConnector_RequestSyntax "#API_DescribeConnector_RequestSyntax")**

The Amazon Resource Name (ARN) of the connector that you want to describe.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "capacity": {
      "autoScaling": {
         "maxAutoscalingTaskCount": ***number***,
         "maxWorkerCount": ***number***,
         "mcuCount": ***number***,
         "minWorkerCount": ***number***,
         "scaleInPolicy": {
            "cpuUtilizationPercentage": ***number***
         },
         "scaleOutPolicy": {
            "cpuUtilizationPercentage": ***number***
         }
      },
      "provisionedCapacity": {
         "mcuCount": ***number***,
         "workerCount": ***number***
      }
   },
   "connectorArn": "***string***",
   "connectorConfiguration": {
      "***string***" : "***string***"
   },
   "connectorDescription": "***string***",
   "connectorName": "***string***",
   "connectorState": "***string***",
   "creationTime": "***string***",
   "currentVersion": "***string***",
   "kafkaCluster": {
      "apacheKafkaCluster": {
         "bootstrapServers": "***string***",
         "vpc": {
            "securityGroups": [ "***string***" ],
            "subnets": [ "***string***" ]
         }
      }
   },
   "kafkaClusterClientAuthentication": {
      "authenticationType": "***string***"
   },
   "kafkaClusterEncryptionInTransit": {
      "encryptionType": "***string***"
   },
   "kafkaConnectVersion": "***string***",
   "logDelivery": {
      "workerLogDelivery": {
         "cloudWatchLogs": {
            "enabled": ***boolean***,
            "logGroup": "***string***"
         },
         "firehose": {
            "deliveryStream": "***string***",
            "enabled": ***boolean***
         },
         "s3": {
            "bucket": "***string***",
            "enabled": ***boolean***,
            "prefix": "***string***"
         }
      }
   },
   "networkType": "***string***",
   "plugins": [
      {
         "customPlugin": {
            "customPluginArn": "***string***",
            "revision": ***number***
         }
      }
   ],
   "serviceExecutionRoleArn": "***string***",
   "stateDescription": {
      "code": "***string***",
      "message": "***string***"
   },
   "workerConfiguration": {
      "revision": ***number***,
      "workerConfigurationArn": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[capacity](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

Information about the capacity of the connector, whether it is auto scaled or
provisioned.

Type: [CapacityDescription](API_CapacityDescription.md "API_CapacityDescription.md") object

**[connectorArn](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

The Amazon Resource Name (ARN) of the connector.

Type: String

**[connectorConfiguration](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

A map of keys to values that represent the configuration for the connector.

Type: String to string map

**[connectorDescription](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

A summary description of the connector.

Type: String

**[connectorName](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

The name of the connector.

Type: String

**[connectorState](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

The state of the connector.

Type: String

Valid Values: `RUNNING | CREATING | UPDATING | DELETING | FAILED`

**[creationTime](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

The time the connector was created.

Type: Timestamp

**[currentVersion](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

The current version of the connector.

Type: String

**[kafkaCluster](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

The Apache Kafka cluster that the connector is connected to.

Type: [KafkaClusterDescription](API_KafkaClusterDescription.md "API_KafkaClusterDescription.md") object

**[kafkaClusterClientAuthentication](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

The type of client authentication used to connect to the Apache Kafka cluster. The value
is NONE when no client authentication is used.

Type: [KafkaClusterClientAuthenticationDescription](API_KafkaClusterClientAuthenticationDescription.md "API_KafkaClusterClientAuthenticationDescription.md") object

**[kafkaClusterEncryptionInTransit](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

Details of encryption in transit to the Apache Kafka cluster.

Type: [KafkaClusterEncryptionInTransitDescription](API_KafkaClusterEncryptionInTransitDescription.md "API_KafkaClusterEncryptionInTransitDescription.md") object

**[kafkaConnectVersion](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

The version of Kafka Connect. It has to be compatible with both the Apache Kafka
cluster's version and the plugins.

Type: String

**[logDelivery](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

Details about delivering logs to Amazon CloudWatch Logs.

Type: [LogDeliveryDescription](API_LogDeliveryDescription.md "API_LogDeliveryDescription.md") object

**[networkType](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

The network type of the connector. It gives connectors connectivity to either IPv4 (IPV4) or IPv4 and IPv6 (DUAL) destinations. Defaults to IPV4.

Type: String

Valid Values: `IPV4 | DUAL`

**[plugins](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

Specifies which plugins were used for this connector.

Type: Array of [PluginDescription](API_PluginDescription.md "API_PluginDescription.md") objects

**[serviceExecutionRoleArn](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon
Web Services resources.

Type: String

**[stateDescription](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

Details about the state of a connector.

Type: [StateDescription](API_StateDescription.md "API_StateDescription.md") object

**[workerConfiguration](#API_DescribeConnector_ResponseSyntax "#API_DescribeConnector_ResponseSyntax")**

Specifies which worker configuration was used for the connector.

Type: [WorkerConfigurationDescription](API_WorkerConfigurationDescription.md "API_WorkerConfigurationDescription.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**BadRequestException**

HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then
retry it.

HTTP Status Code: 400

**ForbiddenException**

HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your
request.

HTTP Status Code: 403

**InternalServerErrorException**

HTTP Status Code 500: Unexpected internal server error. Retrying your request might
resolve the issue.

HTTP Status Code: 500

**NotFoundException**

HTTP Status Code 404: Resource not found due to incorrect input. Correct your request
and then retry it.

HTTP Status Code: 404

**ServiceUnavailableException**

HTTP Status Code 503: Service Unavailable. Retrying your request in some time might
resolve the issue.

HTTP Status Code: 503

**TooManyRequestsException**

HTTP Status Code 429: Limit exceeded. Resource limit reached.

HTTP Status Code: 429

**UnauthorizedException**

HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be
validated.

HTTP Status Code: 401

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kafkaconnect-2021-09-14/DescribeConnector.md "../../../goto/cli2/kafkaconnect-2021-09-14/DescribeConnector.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kafkaconnect-2021-09-14/DescribeConnector.md "../../../goto/DotNetSDKV4/kafkaconnect-2021-09-14/DescribeConnector.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/DescribeConnector.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/DescribeConnector.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/DescribeConnector.md "../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/DescribeConnector.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/DescribeConnector.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/DescribeConnector.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/DescribeConnector.md "../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/DescribeConnector.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/DescribeConnector.md "../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/DescribeConnector.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/DescribeConnector.md "../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/DescribeConnector.md")
- [AWS SDK for Python](../../../goto/boto3/kafkaconnect-2021-09-14/DescribeConnector.md "../../../goto/boto3/kafkaconnect-2021-09-14/DescribeConnector.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/DescribeConnector.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/DescribeConnector.md")
