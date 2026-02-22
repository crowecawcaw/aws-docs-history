# CreateConnector

Creates a connector using the specified properties.

## Request Syntax

```
POST /v1/connectors HTTP/1.1
Content-type: application/json

{
   "capacity": {
      "autoScaling": {
         "maxAutoscalingTaskCount": `number`,
         "maxWorkerCount": `number`,
         "mcuCount": `number`,
         "minWorkerCount": `number`,
         "scaleInPolicy": {
            "cpuUtilizationPercentage": `number`
         },
         "scaleOutPolicy": {
            "cpuUtilizationPercentage": `number`
         }
      },
      "provisionedCapacity": {
         "mcuCount": `number`,
         "workerCount": `number`
      }
   },
   "connectorConfiguration": {
      "`string`" : "`string`"
   },
   "connectorDescription": "`string`",
   "connectorName": "`string`",
   "kafkaCluster": {
      "apacheKafkaCluster": {
         "bootstrapServers": "`string`",
         "vpc": {
            "securityGroups": [ "`string`" ],
            "subnets": [ "`string`" ]
         }
      }
   },
   "kafkaClusterClientAuthentication": {
      "authenticationType": "`string`"
   },
   "kafkaClusterEncryptionInTransit": {
      "encryptionType": "`string`"
   },
   "kafkaConnectVersion": "`string`",
   "logDelivery": {
      "workerLogDelivery": {
         "cloudWatchLogs": {
            "enabled": `boolean`,
            "logGroup": "`string`"
         },
         "firehose": {
            "deliveryStream": "`string`",
            "enabled": `boolean`
         },
         "s3": {
            "bucket": "`string`",
            "enabled": `boolean`,
            "prefix": "`string`"
         }
      }
   },
   "networkType": "`string`",
   "plugins": [
      {
         "customPlugin": {
            "customPluginArn": "`string`",
            "revision": `number`
         }
      }
   ],
   "serviceExecutionRoleArn": "`string`",
   "tags": {
      "`string`" : "`string`"
   },
   "workerConfiguration": {
      "revision": `number`,
      "workerConfigurationArn": "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[capacity](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

Information about the capacity allocated to the connector. Exactly one of the two
properties must be specified.

Type: [Capacity](API_Capacity.md "API_Capacity.md") object

Required: Yes

**[connectorConfiguration](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

A map of keys to values that represent the configuration for the connector.

Type: String to string map

Required: Yes

**[connectorDescription](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

A summary description of the connector.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Required: No

**[connectorName](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

The name of the connector.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: Yes

**[kafkaCluster](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

Specifies which Apache Kafka cluster to connect to.

Type: [KafkaCluster](API_KafkaCluster.md "API_KafkaCluster.md") object

Required: Yes

**[kafkaClusterClientAuthentication](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

Details of the client authentication used by the Apache Kafka cluster.

Type: [KafkaClusterClientAuthentication](API_KafkaClusterClientAuthentication.md "API_KafkaClusterClientAuthentication.md") object

Required: Yes

**[kafkaClusterEncryptionInTransit](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

Details of encryption in transit to the Apache Kafka cluster.

Type: [KafkaClusterEncryptionInTransit](API_KafkaClusterEncryptionInTransit.md "API_KafkaClusterEncryptionInTransit.md") object

Required: Yes

**[kafkaConnectVersion](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

The version of Kafka Connect. It has to be compatible with both the Apache Kafka
cluster's version and the plugins.

Type: String

Required: Yes

**[logDelivery](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

Details about log delivery.

Type: [LogDelivery](API_LogDelivery.md "API_LogDelivery.md") object

Required: No

**[networkType](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

The network type of the connector. It gives connectors connectivity to either IPv4 (IPV4) or IPv4 and IPv6 (DUAL) destinations. Defaults to IPV4.

Type: String

Valid Values: `IPV4 | DUAL`

Required: No

**[plugins](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

###### Important

Amazon MSK Connect does not currently support specifying multiple plugins as a list. To use more than one plugin for your connector, you can create a single custom plugin using a ZIP file that bundles multiple plugins together.

Specifies which plugin to use for the connector. You must specify a single-element list containing one `customPlugin` object.

Type: Array of [Plugin](API_Plugin.md "API_Plugin.md") objects

Required: Yes

**[serviceExecutionRoleArn](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

The Amazon Resource Name (ARN) of the IAM role used by the connector to access the
Amazon Web Services resources that it needs. The types of resources depends on the logic of
the connector. For example, a connector that has Amazon S3 as a destination must have
permissions that allow it to write to the S3 destination bucket.

Type: String

Required: Yes

**[tags](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

The tags you want to attach to the connector.

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Required: No

**[workerConfiguration](#API_CreateConnector_RequestSyntax "#API_CreateConnector_RequestSyntax")**

Specifies which worker configuration to use with the connector.

Type: [WorkerConfiguration](API_WorkerConfiguration.md "API_WorkerConfiguration.md") object

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "connectorArn": "***string***",
   "connectorName": "***string***",
   "connectorState": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[connectorArn](#API_CreateConnector_ResponseSyntax "#API_CreateConnector_ResponseSyntax")**

The Amazon Resource Name (ARN) that Amazon assigned to the connector.

Type: String

**[connectorName](#API_CreateConnector_ResponseSyntax "#API_CreateConnector_ResponseSyntax")**

The name of the connector.

Type: String

**[connectorState](#API_CreateConnector_ResponseSyntax "#API_CreateConnector_ResponseSyntax")**

The state of the connector.

Type: String

Valid Values: `RUNNING | CREATING | UPDATING | DELETING | FAILED`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**BadRequestException**

HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then
retry it.

HTTP Status Code: 400

**ConflictException**

HTTP Status Code 409: Conflict. A resource with this name already exists. Retry your
request with another name.

HTTP Status Code: 409

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

- [AWS Command Line Interface V2](../../../goto/cli2/kafkaconnect-2021-09-14/CreateConnector.md "../../../goto/cli2/kafkaconnect-2021-09-14/CreateConnector.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kafkaconnect-2021-09-14/CreateConnector.md "../../../goto/DotNetSDKV4/kafkaconnect-2021-09-14/CreateConnector.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/CreateConnector.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/CreateConnector.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/CreateConnector.md "../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/CreateConnector.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/CreateConnector.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/CreateConnector.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/CreateConnector.md "../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/CreateConnector.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/CreateConnector.md "../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/CreateConnector.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/CreateConnector.md "../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/CreateConnector.md")
- [AWS SDK for Python](../../../goto/boto3/kafkaconnect-2021-09-14/CreateConnector.md "../../../goto/boto3/kafkaconnect-2021-09-14/CreateConnector.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/CreateConnector.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/CreateConnector.md")
