# List topics in an Amazon MSK cluster

You can list all topics in your MSK Provisioned cluster to view basic metadata such as partition counts and replication factors. This is useful for monitoring your cluster's topics, performing inventory checks, or identifying topics for further investigation.

###### Note

The `ListTopics` API provides basic topic metadata. To get detailed information about a specific topic, including its current status and configuration, use the `DescribeTopic` API. For more information, see [Get detailed information about a topic](msk-describe-topic.md "msk-describe-topic.md").

###### Note

This API response reflects data that updates approximately every minute. For the most current topic state after making changes, allow approximately one minute before querying.

###### Topics

- [List topics using the AWS Management Console](list-topics-console.md "list-topics-console.md")
- [List topics using the AWS CLI](list-topics-cli.md "list-topics-cli.md")
- [List topics using the API](list-topics-api.md "list-topics-api.md")
