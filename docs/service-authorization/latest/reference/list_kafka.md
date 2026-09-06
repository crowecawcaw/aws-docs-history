

# Actions, resources, and condition keys for Amazon Managed Streaming for Apache Kafka
<a name="list_kafka"></a>

Amazon Managed Streaming for Apache Kafka (service prefix: `kafka`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/msk/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/msk/1.0/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/msk/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/kafka/kafka.json) for this service.

**Topics**
+ [API operations defined by Amazon Managed Streaming for Apache Kafka](#list_kafka-operations)
+ [Actions defined by Amazon Managed Streaming for Apache Kafka](#list_kafka-actions-as-permissions)
+ [Resource types defined by Amazon Managed Streaming for Apache Kafka](#list_kafka-resources-for-iam-policies)
+ [Condition keys for Amazon Managed Streaming for Apache Kafka](#list_kafka-policy-keys)

## API operations defined by Amazon Managed Streaming for Apache Kafka
<a name="list_kafka-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_kafka-actions-as-permissions).




- **   BatchAssociateScramSecret  **
  - **IAM action:**  [kafka:BatchAssociateScramSecret](#list_kafka-action-BatchAssociateScramSecret) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDisassociateScramSecret  **
  - **IAM action:**  [kafka:BatchDisassociateScramSecret](#list_kafka-action-BatchDisassociateScramSecret) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateChannel  **
  - **IAM action:**  [kafka:CreateChannel](#list_kafka-action-CreateChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka:TagResource](#list_kafka-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kafka.amazonaws.com / **Access level:** Write

- **   CreateCluster  **
  - **IAM action:**  [kafka:CreateCluster](#list_kafka-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka:TagResource](#list_kafka-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateClusterV2  **
  - **IAM action:**  [kafka:CreateClusterV2](#list_kafka-action-CreateClusterV2)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka:TagResource](#list_kafka-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConfiguration  **
  - **IAM action:**  [kafka:CreateConfiguration](#list_kafka-action-CreateConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateReplicator  **
  - **IAM action:**  [kafka:CreateReplicator](#list_kafka-action-CreateReplicator)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka:DescribeClusterV2](#list_kafka-action-DescribeClusterV2)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [kafka:GetBootstrapBrokers](#list_kafka-action-GetBootstrapBrokers)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [kafka:TagResource](#list_kafka-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kafka.amazonaws.com / **Access level:** Write

- **   CreateTopic  **
  - **IAM action:**  [kafka-cluster:Connect](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka-cluster:CreateTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateVpcConnection  **
  - **IAM action:**  [kafka:CreateVpcConnection](#list_kafka-action-CreateVpcConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka:TagResource](#list_kafka-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteChannel  **
  - **IAM action:**  [kafka:DeleteChannel](#list_kafka-action-DeleteChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCluster  **
  - **IAM action:**  [kafka:DeleteCluster](#list_kafka-action-DeleteCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteClusterPolicy  **
  - **IAM action:**  [kafka:DeleteClusterPolicy](#list_kafka-action-DeleteClusterPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfiguration  **
  - **IAM action:**  [kafka:DeleteConfiguration](#list_kafka-action-DeleteConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReplicator  **
  - **IAM action:**  [kafka:DeleteReplicator](#list_kafka-action-DeleteReplicator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTopic  **
  - **IAM action:**  [kafka-cluster:Connect](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka-cluster:DeleteTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka-cluster:DescribeTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DeleteVpcConnection  **
  - **IAM action:**  [kafka:DeleteVpcConnection](#list_kafka-action-DeleteVpcConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeChannel  **
  - **IAM action:**  [kafka:DescribeChannel](#list_kafka-action-DescribeChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCluster  **
  - **IAM action:**  [kafka:DescribeCluster](#list_kafka-action-DescribeCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterOperation  **
  - **IAM action:**  [kafka:DescribeClusterOperation](#list_kafka-action-DescribeClusterOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterOperationV2  **
  - **IAM action:**  [kafka:DescribeClusterOperationV2](#list_kafka-action-DescribeClusterOperationV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterV2  **
  - **IAM action:**  [kafka:DescribeClusterV2](#list_kafka-action-DescribeClusterV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConfiguration  **
  - **IAM action:**  [kafka:DescribeConfiguration](#list_kafka-action-DescribeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConfigurationRevision  **
  - **IAM action:**  [kafka:DescribeConfigurationRevision](#list_kafka-action-DescribeConfigurationRevision) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplicator  **
  - **IAM action:**  [kafka:DescribeReplicator](#list_kafka-action-DescribeReplicator)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [kafka:ListTagsForResource](#list_kafka-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeTopic  **
  - **IAM action:**  [kafka-cluster:Connect](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka-cluster:DescribeTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [kafka-cluster:DescribeTopicDynamicConfiguration](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeTopicPartitions  **
  - **IAM action:**  [kafka-cluster:Connect](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka-cluster:DescribeTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [kafka-cluster:DescribeTopicDynamicConfiguration](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeVpcConnection  **
  - **IAM action:**  [kafka:DescribeVpcConnection](#list_kafka-action-DescribeVpcConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBootstrapBrokers  **
  - **IAM action:**  [kafka:GetBootstrapBrokers](#list_kafka-action-GetBootstrapBrokers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetClusterPolicy  **
  - **IAM action:**  [kafka:GetClusterPolicy](#list_kafka-action-GetClusterPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCompatibleKafkaVersions  **
  - **IAM action:**  [kafka:GetCompatibleKafkaVersions](#list_kafka-action-GetCompatibleKafkaVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListChannels  **
  - **IAM action:**  [kafka:ListChannels](#list_kafka-action-ListChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClientVpcConnections  **
  - **IAM action:**  [kafka:ListClientVpcConnections](#list_kafka-action-ListClientVpcConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusterOperations  **
  - **IAM action:**  [kafka:ListClusterOperations](#list_kafka-action-ListClusterOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusterOperationsV2  **
  - **IAM action:**  [kafka:ListClusterOperationsV2](#list_kafka-action-ListClusterOperationsV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusters  **
  - **IAM action:**  [kafka:ListClusters](#list_kafka-action-ListClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClustersV2  **
  - **IAM action:**  [kafka:ListClustersV2](#list_kafka-action-ListClustersV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurationRevisions  **
  - **IAM action:**  [kafka:ListConfigurationRevisions](#list_kafka-action-ListConfigurationRevisions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurations  **
  - **IAM action:**  [kafka:ListConfigurations](#list_kafka-action-ListConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKafkaVersions  **
  - **IAM action:**  [kafka:ListKafkaVersions](#list_kafka-action-ListKafkaVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNodes  **
  - **IAM action:**  [kafka:ListNodes](#list_kafka-action-ListNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReplicators  **
  - **IAM action:**  [kafka:ListReplicators](#list_kafka-action-ListReplicators) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListScramSecrets  **
  - **IAM action:**  [kafka:ListScramSecrets](#list_kafka-action-ListScramSecrets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [kafka:ListTagsForResource](#list_kafka-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTopics  **
  - **IAM action:**  [kafka-cluster:Connect](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka-cluster:DescribeTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListVpcConnections  **
  - **IAM action:**  [kafka:ListVpcConnections](#list_kafka-action-ListVpcConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutClusterPolicy  **
  - **IAM action:**  [kafka:PutClusterPolicy](#list_kafka-action-PutClusterPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RebootBroker  **
  - **IAM action:**  [kafka:RebootBroker](#list_kafka-action-RebootBroker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectClientVpcConnection  **
  - **IAM action:**  [kafka:RejectClientVpcConnection](#list_kafka-action-RejectClientVpcConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [kafka:TagResource](#list_kafka-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [kafka:UntagResource](#list_kafka-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateBrokerCount  **
  - **IAM action:**  [kafka:UpdateBrokerCount](#list_kafka-action-UpdateBrokerCount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBrokerStorage  **
  - **IAM action:**  [kafka:UpdateBrokerStorage](#list_kafka-action-UpdateBrokerStorage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBrokerType  **
  - **IAM action:**  [kafka:UpdateBrokerType](#list_kafka-action-UpdateBrokerType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateChannel  **
  - **IAM action:**  [kafka:UpdateChannel](#list_kafka-action-UpdateChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateClusterConfiguration  **
  - **IAM action:**  [kafka:UpdateClusterConfiguration](#list_kafka-action-UpdateClusterConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateClusterKafkaVersion  **
  - **IAM action:**  [kafka:UpdateClusterKafkaVersion](#list_kafka-action-UpdateClusterKafkaVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfiguration  **
  - **IAM action:**  [kafka:UpdateConfiguration](#list_kafka-action-UpdateConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnectivity  **
  - **IAM action:**  [kafka:UpdateConnectivity](#list_kafka-action-UpdateConnectivity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMonitoring  **
  - **IAM action:**  [kafka:UpdateMonitoring](#list_kafka-action-UpdateMonitoring) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRebalancing  **
  - **IAM action:**  [kafka:UpdateRebalancing](#list_kafka-action-UpdateRebalancing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReplicationInfo  **
  - **IAM action:**  [kafka:UpdateReplicationInfo](#list_kafka-action-UpdateReplicationInfo) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSecurity  **
  - **IAM action:**  [kafka:UpdateSecurity](#list_kafka-action-UpdateSecurity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStorage  **
  - **IAM action:**  [kafka:UpdateStorage](#list_kafka-action-UpdateStorage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTopic  **
  - **IAM action:**  [kafka-cluster:AlterTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka-cluster:AlterTopicDynamicConfiguration](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka-cluster:Connect](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafka-cluster:DescribeTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List



## Actions defined by Amazon Managed Streaming for Apache Kafka
<a name="list_kafka-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchAssociateScramSecret](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-scram-secrets.html#BatchAssociateScramSecret)  **
  - **Description:** Grants permission to associate one or more Scram Secrets with an Amazon MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDisassociateScramSecret](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-scram-secrets.html#BatchDisassociateScramSecret)  **
  - **Description:** Grants permission to disassociate one or more Scram Secrets from an Amazon MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateChannel](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-channels.html#CreateChannel)  **
  - **Description:** Grants permission to create an MSK Data Channel for an MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kafka-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafka-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#CreateCluster)  **
  - **Description:** Grants permission to create an MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kafka-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafka-aws_TagKeys)
  - **Access level:** Write

- **   [CreateClusterV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters.html#CreateClusterV2)  **
  - **Description:** Grants permission to create an MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kafka-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafka-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConfiguration](https://docs.aws.amazon.com/msk/1.0/apireference/configurations.html#CreateConfiguration)  **
  - **Description:** Grants permission to create an MSK configuration
  - **Resource types (\*required):** [configuration\*](#list_kafka-resource-configuration)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateReplicator](https://docs.aws.amazon.com/msk/latest/developerguide/v1-replicators.html#CreateReplicator)  **
  - **Description:** Grants permission to create a MSK replicator
  - **Resource types (\*required):** [replicator\*](#list_kafka-resource-replicator)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kafka-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafka-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTopic](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topics.html)  **
  - **Description:** Grants permission to create a Kafka topic in an MSK cluster
  - **Resource types (\*required):** [topic\*](#list_kafka-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateVpcConnection](https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connection.html#CreateVpcConnection)  **
  - **Description:** Grants permission to create a MSK VPC connection
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kafka-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafka-aws_TagKeys)
  - **Resource types (\*required):** [vpc-connection\*](#list_kafka-resource-vpc-connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kafka-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafka-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteChannel](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-channels-channelarn.html#DeleteChannel)  **
  - **Description:** Grants permission to delete an MSK Data Channel
  - **Resource types (\*required):** [channel\*](#list_kafka-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DeleteCluster)  **
  - **Description:** Grants permission to delete an MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteClusterPolicy](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-policy.html#DeleteClusterPolicy)  **
  - **Description:** Grants permission to delete a cluster resource-based policy
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfiguration](https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn.html#DeleteConfiguration)  **
  - **Description:** Grants permission to delete the specified MSK configuration
  - **Resource types (\*required):** [configuration\*](#list_kafka-resource-configuration)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteReplicator](https://docs.aws.amazon.com/msk/latest/developerguide/v1-replicators.html#DeleteReplicator)  **
  - **Description:** Grants permission to delete a MSK replicator
  - **Resource types (\*required):** [replicator\*](#list_kafka-resource-replicator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTopic](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topics-topicname.html)  **
  - **Description:** Grants permission to delete a Kafka topic from an MSK cluster
  - **Resource types (\*required):** [topic\*](#list_kafka-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVpcConnection](https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connection-arn.html#DeleteVpcConnection)  **
  - **Description:** Grants permission to delete a MSK VPC connection
  - **Resource types (\*required):** [vpc-connection\*](#list_kafka-resource-vpc-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeChannel](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-channels-channelarn.html#DescribeChannel)  **
  - **Description:** Grants permission to describe an MSK Data Channel
  - **Resource types (\*required):** [channel\*](#list_kafka-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster)  **
  - **Description:** Grants permission to describe an MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeClusterOperation](https://docs.aws.amazon.com/msk/1.0/apireference/operations-clusteroperationarn.html#DescribeClusterOperation)  **
  - **Description:** Grants permission to describe the cluster operation that is specified by the given ARN
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeClusterOperationV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-operations-clusteroperationarn.html#DescribeClusterOperationV2)  **
  - **Description:** Grants permission to describe the cluster operation that is specified by the given ARN
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeClusterV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters-clusterarn.html#DescribeClusterV2)  **
  - **Description:** Grants permission to describe an MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeConfiguration](https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn.html#DescribeConfiguration)  **
  - **Description:** Grants permission to describe an MSK configuration
  - **Resource types (\*required):** [configuration\*](#list_kafka-resource-configuration)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConfigurationRevision](https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn-revisions-revision.html#DescribeConfigurationRevision)  **
  - **Description:** Grants permission to describe an MSK configuration revision
  - **Resource types (\*required):** [configuration\*](#list_kafka-resource-configuration)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReplicator](https://docs.aws.amazon.com/msk/latest/developerguide/v1-replicators.html#DescribeReplicator)  **
  - **Description:** Grants permission to describe a MSK replicator
  - **Resource types (\*required):** [replicator\*](#list_kafka-resource-replicator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTopic](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topics-topicname.html)  **
  - **Description:** Grants permission to return metadata details about a specific Kafka topic
  - **Resource types (\*required):** [topic\*](#list_kafka-resource-topic)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTopicPartitions](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topics-topicname-partitions.html)  **
  - **Description:** Grants permission to list all partitions of a specific topic
  - **Resource types (\*required):** [topic\*](#list_kafka-resource-topic)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeVpcConnection](https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connection-arn.html#DescribeVpcConnection)  **
  - **Description:** Grants permission to describe a MSK VPC connection
  - **Resource types (\*required):** [vpc-connection\*](#list_kafka-resource-vpc-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBootstrapBrokers](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.html#GetBootstrapBrokers)  **
  - **Description:** Grants permission to get connection details for the brokers in an MSK cluster
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetClusterPolicy](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-policy.html#GetClusterPolicy)  **
  - **Description:** Grants permission to describe a cluster resource-based policy
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCompatibleKafkaVersions](https://docs.aws.amazon.com/msk/1.0/apireference/compatible-kafka-versions.html#GetCompatibleKafkaVersions)  **
  - **Description:** Grants permission to get a list of the Apache Kafka versions to which you can update an MSK cluster
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListChannels](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-channels.html#ListChannels)  **
  - **Description:** Grants permission to list all MSK Data Channels for a specified MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListClientVpcConnections](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-client-vpc-connections.html#ListClientVpcConnections)  **
  - **Description:** Grants permission to list all MSK VPC connections created for a cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListClusterOperations](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-operations.html#ListClusterOperations)  **
  - **Description:** Grants permission to return a list of all the operations that have been performed on the specified MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListClusterOperationsV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters-clusterarn-operations.html#ListClusterOperationsV2)  **
  - **Description:** Grants permission to return a list of all the operations that have been performed on the specified MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListClusters](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#ListClusters)  **
  - **Description:** Grants permission to list all MSK clusters in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListClustersV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters.html#ListClustersV2)  **
  - **Description:** Grants permission to list all MSK clusters in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConfigurationRevisions](https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn-revisions.html#ListConfigurationRevisions)  **
  - **Description:** Grants permission to list all revisions for an MSK configuration in this account
  - **Resource types (\*required):** [configuration\*](#list_kafka-resource-configuration)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConfigurations](https://docs.aws.amazon.com/msk/1.0/apireference/configurations.html#ListConfigurations)  **
  - **Description:** Grants permission to list all MSK configurations in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListKafkaVersions](https://docs.aws.amazon.com/msk/1.0/apireference/kafka-versions.html#ListKafkaVersions)  **
  - **Description:** Grants permission to list all Apache Kafka versions supported by Amazon MSK
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNodes](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes.html#ListNodes)  **
  - **Description:** Grants permission to list brokers in an MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReplicators](https://docs.aws.amazon.com/msk/latest/developerguide/v1-replicators.html#ListReplicators)  **
  - **Description:** Grants permission to list all MSK replicators in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListScramSecrets](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-scram-secrets.html#ListScramSecrets)  **
  - **Description:** Grants permission to list the Scram Secrets associated with an Amazon MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/msk/1.0/apireference/tags-resourcearn.html#ListTagsForResource)  **
  - **Description:** Grants permission to list tags of an MSK resource
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTopics](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topics.html)  **
  - **Description:** Grants permission to list all Kafka topics for a specified MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVpcConnections](https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connections.html#ListVpcConnections)  **
  - **Description:** Grants permission to list all MSK VPC connections that this account uses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutClusterPolicy](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-policy.html#PutClusterPolicy)  **
  - **Description:** Grants permission to create or update the resource-based policy for a cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RebootBroker](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-reboot-broker.html#RebootBroker)  **
  - **Description:** Grants permission to reboot broker
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RejectClientVpcConnection](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-client-vpc-connection.html#RejectClientVpcConnection)  **
  - **Description:** Grants permission to reject a MSK VPC connection
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [vpc-connection\*](#list_kafka-resource-vpc-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/msk/1.0/apireference/tags-resourcearn.html#TagResource)  **
  - **Description:** Grants permission to tag an MSK resource
  - **Resource types (\*required):** [cluster](#list_kafka-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kafka-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafka-aws_TagKeys)
  - **Resource types (\*required):** [vpc-connection](#list_kafka-resource-vpc-connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kafka-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafka-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/msk/1.0/apireference/tags-resourcearn.html#UntagResource)  **
  - **Description:** Grants permission to remove tags from an MSK resource
  - **Resource types (\*required):** [cluster](#list_kafka-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafka-aws_TagKeys)
  - **Resource types (\*required):** [vpc-connection](#list_kafka-resource-vpc-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafka-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateBrokerCount](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes-count.html#UpdateBrokerCount)  **
  - **Description:** Grants permission to update the number of brokers of the MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBrokerStorage](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes-storage.html#UpdateBrokerStorage)  **
  - **Description:** Grants permission to update the storage size of the brokers of the MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBrokerType](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes-type.html#UpdateBrokerType)  **
  - **Description:** Grants permission to update the broker type of an Amazon MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateChannel](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-channels-channelarn.html#UpdateChannel)  **
  - **Description:** Grants permission to update the configuration of an MSK Data Channel
  - **Resource types (\*required):** [channel\*](#list_kafka-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateClusterConfiguration](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-configuration.html#UpdateClusterConfiguration)  **
  - **Description:** Grants permission to update the configuration of the MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuration\*](#list_kafka-resource-configuration) / **Condition keys:**  
  - **Access level:** Write

- **   [UpdateClusterKafkaVersion](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-version.html#UpdateClusterKafkaVersion)  **
  - **Description:** Grants permission to update the MSK cluster to the specified Apache Kafka version
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfiguration](https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn.html#UpdateConfiguration)  **
  - **Description:** Grants permission to create a new revision of the MSK configuration
  - **Resource types (\*required):** [configuration\*](#list_kafka-resource-configuration)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConnectivity](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-connectivity.html#UpdateConnectivity)  **
  - **Description:** Grants permission to update the connectivity settings for the MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)<br />[kafka:publicAccessEnabled](#list_kafka-kafka_publicAccessEnabled)
  - **Access level:** Write

- **   [UpdateMonitoring](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-monitoring.html#UpdateMonitoring)  **
  - **Description:** Grants permission to update the monitoring settings for the MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRebalancing](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-rebalancing.html)  **
  - **Description:** Grants permission to update the intelligent rebalancing status of the MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateReplicationInfo](https://docs.aws.amazon.com/msk/latest/developerguide/v1-replicators.html#UpdateReplicationInfo)  **
  - **Description:** Grants permission to update the replication info of the MSK replicator
  - **Resource types (\*required):** [replicator\*](#list_kafka-resource-replicator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSecurity](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-security.html#UpdateSecurity)  **
  - **Description:** Grants permission to update the security settings for the MSK cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStorage](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-storage.html#UpdateStorage)  **
  - **Description:** Grants permission to update the EBS storage (size or provisioned throughput) associated with MSK brokers or set cluster storage mode to TIERED
  - **Resource types (\*required):** [cluster\*](#list_kafka-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTopic](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topics-topicname.html)  **
  - **Description:** Grants permission to update the configuration of a Kafka topic in an MSK cluster
  - **Resource types (\*required):** [topic\*](#list_kafka-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon Managed Streaming for Apache Kafka
<a name="list_kafka-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [channel](https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-channel.html)  | arn:${Partition}:kafka:${Region}:${Account}:channel/${ClusterName}/${ClusterUuid}/${ChannelName}/${Uuid} | [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_) | 
|  [cluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html)  | arn:${Partition}:kafka:${Region}:${Account}:cluster/${ClusterName}/${Uuid} | [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_) | 
|  [configuration](https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn.html)  | arn:${Partition}:kafka:${Region}:${Account}:configuration/${ConfigurationName}/${Uuid} |   | 
|  [group](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources)  | arn:${Partition}:kafka:${Region}:${Account}:group/${ClusterName}/${ClusterUuid}/${GroupName} |   | 
|  [replicator](https://docs.aws.amazon.com/msk/latest/developerguide/v1-replicators.html)  | arn:${Partition}:kafka:${Region}:${Account}:replicator/${ReplicatorName}/${Uuid} | [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_) | 
|  [topic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources)  | arn:${Partition}:kafka:${Region}:${Account}:topic/${ClusterName}/${ClusterUuid}/${TopicName} |   | 
|  [transactional-id](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources)  | arn:${Partition}:kafka:${Region}:${Account}:transactional-id/${ClusterName}/${ClusterUuid}/${TransactionalId} |   | 
|  [vpc-connection](https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connections-arn.html)  | arn:${Partition}:kafka:${Region}:${VpcOwnerAccount}:vpc-connection/${ClusterOwnerAccount}/${ClusterName}/${Uuid} | [aws:ResourceTag/${TagKey}](#list_kafka-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Managed Streaming for Apache Kafka
<a name="list_kafka-policy-keys"></a>

Amazon Managed Streaming for Apache Kafka defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [kafka:publicAccessEnabled](https://docs.aws.amazon.com/service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.html#apachekafkaapisforamazonmskclusters-policy-keys)  | Filters access by the presence of public access enabled in the request | Bool | 