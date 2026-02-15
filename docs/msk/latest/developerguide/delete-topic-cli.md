# Delete a topic using the AWS CLI

Run the following command, replacing `ClusterArn` with the Amazon Resource Name (ARN) of your cluster and `TopicName` with the name of the topic you want to delete.

```
aws kafka delete-topic --cluster-arn `ClusterArn` --topic-name `TopicName`
```

The output of this command looks like the following JSON example.

```
{
    "topicArn": "arn:aws:kafka:us-east-1:123456789012:topic/MyCluster/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2/MyTopic",
    "topicName": "MyTopic",
    "status": "DELETING"
}
```
