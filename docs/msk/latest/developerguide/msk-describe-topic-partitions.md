# View partition information for a topic

You can retrieve detailed information about the partitions of a specific topic in your MSK Provisioned cluster. This information includes the partition number, leader broker, replica brokers, and in-sync replicas (ISR). This is useful for monitoring partition distribution, identifying under-replicated partitions, or troubleshooting replication issues.

###### Note

This API response reflects data that updates approximately every minute. For the most current topic state after making changes, allow approximately one minute before querying.

###### Topics

- [View partition information using the AWS Management Console](describe-topic-partitions-console.md "describe-topic-partitions-console.md")
- [View partition information using the AWS CLI](describe-topic-partitions-cli.md "describe-topic-partitions-cli.md")
- [View partition information using the API](describe-topic-partitions-api.md "describe-topic-partitions-api.md")
