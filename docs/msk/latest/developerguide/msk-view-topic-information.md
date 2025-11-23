# Topic Operations

You can use Amazon MSK APIs to view information about topics in your MSK Provisioned cluster. These APIs provide read-only access to topic metadata, including partition counts, replication factors, configurations, and partition details. This information is useful for monitoring, troubleshooting, and understanding the structure of your Kafka topics.

###### Important

The `ListTopics`, `DescribeTopic`, and `DescribeTopicPartitions` APIs responses reflect data that updates approximately every minute. For the most current topic state after making changes, allow approximately one minute before querying.

###### Note

These APIs provide read-only access to topic metadata. To create or modify topics, use Apache Kafka tools or the Kafka AdminClient. For more information, see [Step 4: Create a topic in the Amazon MSK cluster](create-topic.md "create-topic.md").

## Requirements for viewing topic information

- Your cluster must be an MSK Provisioned cluster. These APIs are not available for MSK Serverless clusters.
- Your cluster must be running Apache Kafka version 3.6.0 or later. For more information about supported versions, see [Supported Apache Kafka versions](supported-kafka-versions.md "supported-kafka-versions.md").
- Your cluster must be in the `ACTIVE` state. For more information about cluster states, see [Understand MSK Provisioned cluster states](msk-cluster-states.md "msk-cluster-states.md").
- You must have the appropriate IAM permissions. For more information, see [IAM permissions for viewing topic information](#view-topic-information-permissions "#view-topic-information-permissions").

## IAM permissions for viewing topic information

To call these APIs, you must have the appropriate IAM permissions. The following table lists the required permissions for each API.

| Required permissions for viewing topic information | API                                                                                                           | Required Permissions | Resource |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------- | -------- |
| ListTopics                                         | `kafka-cluster:Connect`<br>`kafka-cluster:DescribeTopic`                                                      | Cluster ARN          |
| DescribeTopic                                      | `kafka-cluster:Connect`<br>`kafka-cluster:DescribeTopic`<br>`kafka-cluster:DescribeTopicDynamicConfiguration` | Topic ARN            |
| DescribeTopicPartitions                            | `kafka-cluster:Connect`<br>`kafka-cluster:DescribeTopic`<br>`kafka-cluster:DescribeTopicDynamicConfiguration` | Topic ARN            |

###### Note

For `ListTopics`, specify the cluster ARN in your IAM policy. For `DescribeTopic` and `DescribeTopicPartitions`, specify the topic ARN in your IAM policy.

For more information about IAM access control for Amazon MSK, see [IAM access control](iam-access-control.md "iam-access-control.md").

###### Topics

- [List topics in an Amazon MSK cluster](msk-list-topics.md "msk-list-topics.md")
- [Get detailed information about a topic](msk-describe-topic.md "msk-describe-topic.md")
- [View partition information for a topic](msk-describe-topic-partitions.md "msk-describe-topic-partitions.md")
