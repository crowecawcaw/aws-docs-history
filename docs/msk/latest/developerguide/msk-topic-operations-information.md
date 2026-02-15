# Topic Operations

You can use Amazon MSK APIs to manage topics in your MSK Provisioned cluster without the need to set up and maintain Kafka admin clients. With these APIs, you can define or read topic properties such as replication factor and partition count, along with configuration settings like retention and cleanup policies. You can programmatically manage Kafka topics using your familiar interfaces including AWS CLI, AWS SDKs, and AWS CloudFormation. These APIs are also integrated into the Amazon MSK console, bringing all topic operations to one place. You can now create or update topics with just a few clicks using guided defaults while gaining comprehensive visibility into topic configurations, partition-level information, and metrics.

###### Important

These topic API responses reflect data that updates approximately every minute. For the most current topic state after making changes, allow approximately one minute before querying.

## Requirements for using topic APIs

- Your cluster must be an MSK Provisioned cluster. These APIs are not available for MSK Serverless clusters.
- Your cluster must be running Apache Kafka version 3.6.0 or later. For more information about supported versions, see [Supported Apache Kafka versions](supported-kafka-versions.md "supported-kafka-versions.md").
- Your cluster must be in the `ACTIVE` state. For more information about cluster states, see [Understand MSK Provisioned cluster states](msk-cluster-states.md "msk-cluster-states.md").
- You must have the appropriate IAM permissions. For more information, see [IAM permissions for topic operations APIs](#topic-operations-permissions "#topic-operations-permissions").

## IAM permissions for topic operations APIs

To call these APIs, you must have the appropriate IAM permissions. The following table lists the required permissions for each API.

| Required permissions for topic operations APIs | API                                                                                                                                      | Required Permissions   | Resource |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | -------- |
| ListTopics                                     | `kafka-cluster:Connect`<br>`kafka-cluster:DescribeTopic`                                                                                 | Cluster ARN, Topic ARN |
| DescribeTopic                                  | `kafka-cluster:Connect`<br>`kafka-cluster:DescribeTopic`<br>`kafka-cluster:DescribeTopicDynamicConfiguration`                            | Cluster ARN, Topic ARN |
| DescribeTopicPartitions                        | `kafka-cluster:Connect`<br>`kafka-cluster:DescribeTopic`<br>`kafka-cluster:DescribeTopicDynamicConfiguration`                            | Cluster ARN, Topic ARN |
| CreateTopic                                    | `kafka-cluster:Connect`<br>`kafka-cluster:CreateTopic`                                                                                   | Cluster ARN, Topic ARN |
| DeleteTopic                                    | `kafka-cluster:Connect`<br>`kafka-cluster:DescribeTopic`<br>`kafka-cluster:DeleteTopic`                                                  | Cluster ARN, Topic ARN |
| UpdateTopic                                    | `kafka-cluster:Connect`<br>`kafka-cluster:DescribeTopic`<br>`kafka-cluster:AlterTopic`<br>`kafka-cluster:AlterTopicDynamicConfiguration` | Cluster ARN, Topic ARN |

###### Note

For `kafka-cluster:Connect`, specify the cluster ARN in your IAM policy. For all other actions, specify the topic ARN in your IAM policy.

###### Note

For `ListTopics`, you can use a wildcard (\*) to match all topics on a cluster. For example: `arn:aws:kafka:us-east-1:123456789012:topic/my-cluster/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2/*`.

For more information about IAM access control for Amazon MSK, see [IAM access control](iam-access-control.md "iam-access-control.md").

###### Topics

- [List topics in an Amazon MSK cluster](msk-list-topics.md "msk-list-topics.md")
- [Get detailed information about a topic](msk-describe-topic.md "msk-describe-topic.md")
- [View partition information for a topic](msk-describe-topic-partitions.md "msk-describe-topic-partitions.md")
- [Create topics in an Amazon MSK cluster](msk-create-topic.md "msk-create-topic.md")
- [Update a topic in an Amazon MSK cluster](msk-update-topic.md "msk-update-topic.md")
- [Delete a topic in an Amazon MSK cluster](msk-delete-topic.md "msk-delete-topic.md")
