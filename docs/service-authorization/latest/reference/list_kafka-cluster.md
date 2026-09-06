

# Actions, resources, and condition keys for Apache Kafka APIs for Amazon MSK clusters
<a name="list_kafka-cluster"></a>

Apache Kafka APIs for Amazon MSK clusters (service prefix: `kafka-cluster`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/kafka-cluster/kafka-cluster.json) for this service.

**Topics**
+ [Actions defined by Apache Kafka APIs for Amazon MSK clusters](#list_kafka-cluster-actions-as-permissions)
+ [Resource types defined by Apache Kafka APIs for Amazon MSK clusters](#list_kafka-cluster-resources-for-iam-policies)
+ [Condition keys for Apache Kafka APIs for Amazon MSK clusters](#list_kafka-cluster-policy-keys)

## Actions defined by Apache Kafka APIs for Amazon MSK clusters
<a name="list_kafka-cluster-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AlterCluster](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to alter various aspects of the cluster, equivalent to Apache Kafka's ALTER CLUSTER ACL
  - **Resource types (\*required):** [cluster\*](#list_kafka-cluster-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-cluster-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AlterClusterDynamicConfiguration](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to alter the dynamic configuration of a cluster, equivalent to Apache Kafka's ALTER\_CONFIGS CLUSTER ACL
  - **Resource types (\*required):** [cluster\*](#list_kafka-cluster-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-cluster-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AlterGroup](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to join groups on a cluster, equivalent to Apache Kafka's READ GROUP ACL
  - **Resource types (\*required):** [group\*](#list_kafka-cluster-resource-group)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AlterTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to alter topics on a cluster, equivalent to Apache Kafka's ALTER TOPIC ACL
  - **Resource types (\*required):** [topic\*](#list_kafka-cluster-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AlterTopicDynamicConfiguration](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to alter the dynamic configuration of topics on a cluster, equivalent to Apache Kafka's ALTER\_CONFIGS TOPIC ACL
  - **Resource types (\*required):** [topic\*](#list_kafka-cluster-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AlterTransactionalId](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to alter transactional IDs on a cluster, equivalent to Apache Kafka's WRITE TRANSACTIONAL\_ID ACL
  - **Resource types (\*required):** [transactional-id\*](#list_kafka-cluster-resource-transactional-id)
  - **Condition keys:**  
  - **Access level:** Write

- **   [Connect](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to connect and authenticate to the cluster
  - **Resource types (\*required):** [cluster\*](#list_kafka-cluster-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-cluster-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to create topics on a cluster, equivalent to Apache Kafka's CREATE CLUSTER/TOPIC ACL
  - **Resource types (\*required):** [topic\*](#list_kafka-cluster-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGroup](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to delete groups on a cluster, equivalent to Apache Kafka's DELETE GROUP ACL
  - **Resource types (\*required):** [group\*](#list_kafka-cluster-resource-group)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to delete topics on a cluster, equivalent to Apache Kafka's DELETE TOPIC ACL
  - **Resource types (\*required):** [topic\*](#list_kafka-cluster-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeCluster](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to describe various aspects of the cluster, equivalent to Apache Kafka's DESCRIBE CLUSTER ACL
  - **Resource types (\*required):** [cluster\*](#list_kafka-cluster-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-cluster-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeClusterDynamicConfiguration](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to describe the dynamic configuration of a cluster, equivalent to Apache Kafka's DESCRIBE\_CONFIGS CLUSTER ACL
  - **Resource types (\*required):** [cluster\*](#list_kafka-cluster-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-cluster-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeGroup](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to describe groups on a cluster, equivalent to Apache Kafka's DESCRIBE GROUP ACL
  - **Resource types (\*required):** [group\*](#list_kafka-cluster-resource-group)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeTopic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to describe topics on a cluster, equivalent to Apache Kafka's DESCRIBE TOPIC ACL
  - **Resource types (\*required):** [topic\*](#list_kafka-cluster-resource-topic)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeTopicDynamicConfiguration](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to describe the dynamic configuration of topics on a cluster, equivalent to Apache Kafka's DESCRIBE\_CONFIGS TOPIC ACL
  - **Resource types (\*required):** [topic\*](#list_kafka-cluster-resource-topic)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeTransactionalId](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to describe transactional IDs on a cluster, equivalent to Apache Kafka's DESCRIBE TRANSACTIONAL\_ID ACL
  - **Resource types (\*required):** [transactional-id\*](#list_kafka-cluster-resource-transactional-id)
  - **Condition keys:**  
  - **Access level:** List

- **   [ReadData](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to read data from topics on a cluster, equivalent to Apache Kafka's READ TOPIC ACL
  - **Resource types (\*required):** [topic\*](#list_kafka-cluster-resource-topic)
  - **Condition keys:**  
  - **Access level:** Read

- **   [WriteData](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to write data to topics on a cluster, equivalent to Apache Kafka's WRITE TOPIC ACL
  - **Resource types (\*required):** [topic\*](#list_kafka-cluster-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write

- **   [WriteDataIdempotently](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#actions)  **
  - **Description:** Grants permission to write data idempotently on a cluster, equivalent to Apache Kafka's IDEMPOTENT\_WRITE CLUSTER ACL
  - **Resource types (\*required):** [cluster\*](#list_kafka-cluster-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafka-cluster-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Apache Kafka APIs for Amazon MSK clusters
<a name="list_kafka-cluster-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cluster](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources)  | arn:${Partition}:kafka:${Region}:${Account}:cluster/${ClusterName}/${ClusterUuid} | [aws:ResourceTag/${TagKey}](#list_kafka-cluster-aws_ResourceTag___TagKey_) | 
|  [group](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources)  | arn:${Partition}:kafka:${Region}:${Account}:group/${ClusterName}/${ClusterUuid}/${GroupName} |   | 
|  [topic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources)  | arn:${Partition}:kafka:${Region}:${Account}:topic/${ClusterName}/${ClusterUuid}/${TopicName} |   | 
|  [transactional-id](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources)  | arn:${Partition}:kafka:${Region}:${Account}:transactional-id/${ClusterName}/${ClusterUuid}/${TransactionalId} |   | 

## Condition keys for Apache Kafka APIs for Amazon MSK clusters
<a name="list_kafka-cluster-policy-keys"></a>

Apache Kafka APIs for Amazon MSK clusters defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag key-value pairs attached to the resource. The resource tag context key will only apply to the cluster resource, not topics, groups and transactional IDs | String | 