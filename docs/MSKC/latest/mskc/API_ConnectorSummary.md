# ConnectorSummary

Summary of a connector.

## Contents

**capacity**

The connector's compute capacity settings.

Type: [CapacityDescription](API_CapacityDescription.md "API_CapacityDescription.md") object

Required: No

**connectorArn**

The Amazon Resource Name (ARN) of the connector.

Type: String

Required: No

**connectorDescription**

The description of the connector.

Type: String

Required: No

**connectorName**

The name of the connector.

Type: String

Required: No

**connectorState**

The state of the connector.

Type: String

Valid Values: `RUNNING | CREATING | UPDATING | DELETING | FAILED`

Required: No

**creationTime**

The time that the connector was created.

Type: Timestamp

Required: No

**currentVersion**

The current version of the connector.

Type: String

Required: No

**kafkaCluster**

The details of the Apache Kafka cluster to which the connector is connected.

Type: [KafkaClusterDescription](API_KafkaClusterDescription.md "API_KafkaClusterDescription.md") object

Required: No

**kafkaClusterClientAuthentication**

The type of client authentication used to connect to the Apache Kafka cluster. The value
is NONE when no client authentication is used.

Type: [KafkaClusterClientAuthenticationDescription](API_KafkaClusterClientAuthenticationDescription.md "API_KafkaClusterClientAuthenticationDescription.md") object

Required: No

**kafkaClusterEncryptionInTransit**

Details of encryption in transit to the Apache Kafka cluster.

Type: [KafkaClusterEncryptionInTransitDescription](API_KafkaClusterEncryptionInTransitDescription.md "API_KafkaClusterEncryptionInTransitDescription.md") object

Required: No

**kafkaConnectVersion**

The version of Kafka Connect. It has to be compatible with both the Apache Kafka
cluster's version and the plugins.

Type: String

Required: No

**logDelivery**

The settings for delivering connector logs to Amazon CloudWatch Logs.

Type: [LogDeliveryDescription](API_LogDeliveryDescription.md "API_LogDeliveryDescription.md") object

Required: No

**plugins**

Specifies which plugins were used for this connector.

Type: Array of [PluginDescription](API_PluginDescription.md "API_PluginDescription.md") objects

Required: No

**serviceExecutionRoleArn**

The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon
Web Services resources.

Type: String

Required: No

**workerConfiguration**

The worker configurations that are in use with the connector.

Type: [WorkerConfigurationDescription](API_WorkerConfigurationDescription.md "API_WorkerConfigurationDescription.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/ConnectorSummary.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/ConnectorSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/ConnectorSummary.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/ConnectorSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/ConnectorSummary.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/ConnectorSummary.md")
