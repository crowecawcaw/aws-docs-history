

# Data retrieval APIs for Amazon Managed Streaming for Apache Kafka
<a name="amazonmanagedstreamingforapachekafka"></a>

Amazon Managed Streaming for Apache Kafka provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="kafka-DescribeChannel"></a>[DescribeChannel](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-channels-channelarn.html#DescribeChannel) | Describe an MSK Data Channel | Read | 
| <a name="kafka-DescribeCluster"></a>[DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) | Describe an MSK cluster | Read | 
| <a name="kafka-DescribeClusterOperation"></a>[DescribeClusterOperation](https://docs.aws.amazon.com/msk/1.0/apireference/operations-clusteroperationarn.html#DescribeClusterOperation) | Describe the cluster operation that is specified by the given ARN | Read | 
| <a name="kafka-DescribeClusterOperationV2"></a>[DescribeClusterOperationV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-operations-clusteroperationarn.html#DescribeClusterOperationV2) | Describe the cluster operation that is specified by the given ARN | Read | 
| <a name="kafka-DescribeClusterV2"></a>[DescribeClusterV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters-clusterarn.html#DescribeClusterV2) | Describe an MSK cluster | Read | 
| <a name="kafka-DescribeConfiguration"></a>[DescribeConfiguration](https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn.html#DescribeConfiguration) | Describe an MSK configuration | Read | 
| <a name="kafka-DescribeConfigurationRevision"></a>[DescribeConfigurationRevision](https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn-revisions-revision.html#DescribeConfigurationRevision) | Describe an MSK configuration revision | Read | 
| <a name="kafka-DescribeReplicator"></a>[DescribeReplicator](https://docs.aws.amazon.com/msk/latest/developerguide/v1-replicators.html#DescribeReplicator) | Describe a MSK replicator | Read | 
| <a name="kafka-DescribeTopic"></a>[DescribeTopic](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topics-topicname.html) | Return metadata details about a specific Kafka topic | Read | 
| <a name="kafka-DescribeTopicPartitions"></a>[DescribeTopicPartitions](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topics-topicname-partitions.html) | List all partitions of a specific topic | Read | 
| <a name="kafka-DescribeVpcConnection"></a>[DescribeVpcConnection](https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connection-arn.html#DescribeVpcConnection) | Describe a MSK VPC connection | Read | 
| <a name="kafka-GetBootstrapBrokers"></a>[GetBootstrapBrokers](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.html#GetBootstrapBrokers) | Get connection details for the brokers in an MSK cluster | Read | 
| <a name="kafka-GetClusterPolicy"></a>[GetClusterPolicy](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-policy.html#GetClusterPolicy) | Describe a cluster resource-based policy | Read | 
| <a name="kafka-GetCompatibleKafkaVersions"></a>[GetCompatibleKafkaVersions](https://docs.aws.amazon.com/msk/1.0/apireference/compatible-kafka-versions.html#GetCompatibleKafkaVersions) | Get a list of the Apache Kafka versions to which you can update an MSK cluster | List | 
| <a name="kafka-ListChannels"></a>[ListChannels](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-channels.html#ListChannels) | List all MSK Data Channels for a specified MSK cluster | List | 
| <a name="kafka-ListClientVpcConnections"></a>[ListClientVpcConnections](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-client-vpc-connections.html#ListClientVpcConnections) | List all MSK VPC connections created for a cluster | List | 
| <a name="kafka-ListClusterOperations"></a>[ListClusterOperations](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-operations.html#ListClusterOperations) | Return a list of all the operations that have been performed on the specified MSK cluster | List | 
| <a name="kafka-ListClusterOperationsV2"></a>[ListClusterOperationsV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters-clusterarn-operations.html#ListClusterOperationsV2) | Return a list of all the operations that have been performed on the specified MSK cluster | List | 
| <a name="kafka-ListClusters"></a>[ListClusters](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#ListClusters) | List all MSK clusters in this account | List | 
| <a name="kafka-ListClustersV2"></a>[ListClustersV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters.html#ListClustersV2) | List all MSK clusters in this account | List | 
| <a name="kafka-ListConfigurationRevisions"></a>[ListConfigurationRevisions](https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn-revisions.html#ListConfigurationRevisions) | List all revisions for an MSK configuration in this account | List | 
| <a name="kafka-ListConfigurations"></a>[ListConfigurations](https://docs.aws.amazon.com/msk/1.0/apireference/configurations.html#ListConfigurations) | List all MSK configurations in this account | List | 
| <a name="kafka-ListKafkaVersions"></a>[ListKafkaVersions](https://docs.aws.amazon.com/msk/1.0/apireference/kafka-versions.html#ListKafkaVersions) | List all Apache Kafka versions supported by Amazon MSK | List | 
| <a name="kafka-ListNodes"></a>[ListNodes](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes.html#ListNodes) | List brokers in an MSK cluster | List | 
| <a name="kafka-ListReplicators"></a>[ListReplicators](https://docs.aws.amazon.com/msk/latest/developerguide/v1-replicators.html#ListReplicators) | List all MSK replicators in this account | List | 
| <a name="kafka-ListScramSecrets"></a>[ListScramSecrets](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-scram-secrets.html#ListScramSecrets) | List the Scram Secrets associated with an Amazon MSK cluster | List | 
| <a name="kafka-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/msk/1.0/apireference/tags-resourcearn.html#ListTagsForResource) | List tags of an MSK resource | Read | 
| <a name="kafka-ListTopics"></a>[ListTopics](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-topics.html) | List all Kafka topics for a specified MSK cluster | List | 
| <a name="kafka-ListVpcConnections"></a>[ListVpcConnections](https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connections.html#ListVpcConnections) | List all MSK VPC connections that this account uses | List | 