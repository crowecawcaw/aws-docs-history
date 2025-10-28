# AWS managed policy:

AWSMSKReplicatorExecutionRole

The
`AWSMSKReplicatorExecutionRole`
policy grants permissions to the Amazon MSK replicator to replicate data between MSK clusters.
The permissions in this policy are grouped as follows:

- `cluster` – Grants the Amazon MSK
  Replicator
  permissions
  to
  connect to the cluster using
  IAM
  authentication.
  Also grants
  permissions
  to describe and alter the cluster.
- `topic` – Grants the Amazon MSK
  Replicator
  permissions
  to describe,
  create,
  and alter a
  topic,
  and to alter the topic's dynamic configuration.
- `consumer group` – Grants the
  Amazon MSK Replicator
  permissions
  to describe and alter consumer groups, to read and write date from an MSK cluster,
  and to delete internal topics created by the replicator.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ClusterPermissions",
 "Effect": "Allow",
 "Action": [
 "kafka-cluster:Connect",
 "kafka-cluster:DescribeCluster",
 "kafka-cluster:AlterCluster",
 "kafka-cluster:DescribeTopic",
 "kafka-cluster:CreateTopic",
 "kafka-cluster:AlterTopic",
 "kafka-cluster:WriteData",
 "kafka-cluster:ReadData",
 "kafka-cluster:AlterGroup",
 "kafka-cluster:DescribeGroup",
 "kafka-cluster:DescribeTopicDynamicConfiguration",
 "kafka-cluster:AlterTopicDynamicConfiguration",
 "kafka-cluster:WriteDataIdempotently"
 ],
 "Resource": [
 "arn:aws:kafka:*:*:cluster/*"
 ]
 },
 {
 "Sid": "TopicPermissions",
 "Effect": "Allow",
 "Action": [
 "kafka-cluster:DescribeTopic",
 "kafka-cluster:CreateTopic",
 "kafka-cluster:AlterTopic",
 "kafka-cluster:WriteData",
 "kafka-cluster:ReadData",
 "kafka-cluster:DescribeTopicDynamicConfiguration",
 "kafka-cluster:AlterTopicDynamicConfiguration",
 "kafka-cluster:AlterCluster"
 ],
 "Resource": [
 "arn:aws:kafka:*:*:topic/*/*"
 ]
 },
 {
 "Sid": "GroupPermissions",
 "Effect": "Allow",
 "Action": [
 "kafka-cluster:AlterGroup",
 "kafka-cluster:DescribeGroup"
 ],
 "Resource": [
 "arn:aws:kafka:*:*:group/*/*"
 ]
 }
 ]
}`

```
