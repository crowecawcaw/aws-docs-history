# Create a topic using the AWS CLI

Run the following command, replacing `ClusterArn` with the Amazon Resource Name (ARN) of your cluster. If you don't have the ARN for your cluster, you can find it by listing all clusters. For more information, see [List Amazon MSK clusters](msk-list-clusters.md "msk-list-clusters.md").

```
aws kafka create-topic --cluster-arn `ClusterArn` --topic-name MyTopic --partition-count 3 --replication-factor 3
```

The output of this command looks like the following JSON example.

```
{
    "topicArn": "arn:aws:kafka:us-east-1:123456789012:topic/MyCluster/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2/MyTopic",
    "topicName": "MyTopic",
    "status": "CREATING"
}
```
