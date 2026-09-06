

# ConnectorSummary
<a name="API_ConnectorSummary"></a>

Summary of a connector.

## Contents
<a name="API_ConnectorSummary_Contents"></a>

 ** capacity **   <a name="MSKC-Type-ConnectorSummary-capacity"></a>
The connector's compute capacity settings.  
Type: [CapacityDescription](API_CapacityDescription.md) object  
Required: No

 ** connectorArn **   <a name="MSKC-Type-ConnectorSummary-connectorArn"></a>
The Amazon Resource Name (ARN) of the connector.  
Type: String  
Required: No

 ** connectorDescription **   <a name="MSKC-Type-ConnectorSummary-connectorDescription"></a>
The description of the connector.  
Type: String  
Required: No

 ** connectorName **   <a name="MSKC-Type-ConnectorSummary-connectorName"></a>
The name of the connector.  
Type: String  
Required: No

 ** connectorState **   <a name="MSKC-Type-ConnectorSummary-connectorState"></a>
The state of the connector.  
Type: String  
Valid Values: `RUNNING | CREATING | UPDATING | DELETING | FAILED`   
Required: No

 ** creationTime **   <a name="MSKC-Type-ConnectorSummary-creationTime"></a>
The time that the connector was created.  
Type: Timestamp  
Required: No

 ** currentVersion **   <a name="MSKC-Type-ConnectorSummary-currentVersion"></a>
The current version of the connector.  
Type: String  
Required: No

 ** kafkaCluster **   <a name="MSKC-Type-ConnectorSummary-kafkaCluster"></a>
The details of the Apache Kafka cluster to which the connector is connected.  
Type: [KafkaClusterDescription](API_KafkaClusterDescription.md) object  
Required: No

 ** kafkaClusterClientAuthentication **   <a name="MSKC-Type-ConnectorSummary-kafkaClusterClientAuthentication"></a>
The type of client authentication used to connect to the Apache Kafka cluster. The value is NONE when no client authentication is used.  
Type: [KafkaClusterClientAuthenticationDescription](API_KafkaClusterClientAuthenticationDescription.md) object  
Required: No

 ** kafkaClusterEncryptionInTransit **   <a name="MSKC-Type-ConnectorSummary-kafkaClusterEncryptionInTransit"></a>
Details of encryption in transit to the Apache Kafka cluster.  
Type: [KafkaClusterEncryptionInTransitDescription](API_KafkaClusterEncryptionInTransitDescription.md) object  
Required: No

 ** kafkaConnectVersion **   <a name="MSKC-Type-ConnectorSummary-kafkaConnectVersion"></a>
The version of Kafka Connect. It has to be compatible with both the Apache Kafka cluster's version and the plugins.  
Type: String  
Required: No

 ** logDelivery **   <a name="MSKC-Type-ConnectorSummary-logDelivery"></a>
The settings for delivering connector logs to Amazon CloudWatch Logs.  
Type: [LogDeliveryDescription](API_LogDeliveryDescription.md) object  
Required: No

 ** networkType **   <a name="MSKC-Type-ConnectorSummary-networkType"></a>
The network type of the connector. It gives connectors connectivity to either IPv4 (IPV4) or IPv4 and IPv6 (DUAL) destinations. Defaults to IPV4.  
Type: String  
Valid Values: `IPV4 | DUAL`   
Required: No

 ** plugins **   <a name="MSKC-Type-ConnectorSummary-plugins"></a>
Specifies which plugins were used for this connector.  
Type: Array of [PluginDescription](API_PluginDescription.md) objects  
Required: No

 ** serviceExecutionRoleArn **   <a name="MSKC-Type-ConnectorSummary-serviceExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.  
Type: String  
Required: No

 ** workerConfiguration **   <a name="MSKC-Type-ConnectorSummary-workerConfiguration"></a>
The worker configurations that are in use with the connector.  
Type: [WorkerConfigurationDescription](API_WorkerConfigurationDescription.md) object  
Required: No

## See Also
<a name="API_ConnectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/ConnectorSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/ConnectorSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/ConnectorSummary) 