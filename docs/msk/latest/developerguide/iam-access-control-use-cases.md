# Common use cases for client authorization policy

The first column in the following table shows some common use cases. To authorize a
client to carry out a given use case, include the required actions for that use case in
the client's authorization policy, and set `Effect` to
`Allow`.

For information about all the actions that are part of IAM access control for Amazon MSK,
see [Semantics of IAM authorization policy actions and resources](kafka-actions.md "kafka-actions.md").

###### Note

Actions are denied by default. You must explicitly allow every action that you
want to authorize the client to perform.

| Use case                                | Required actions                                                                                                                                             |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Admin                                   | `kafka-cluster:*`                                                                                                                                            |
| Create a topic                          | `kafka-cluster:Connect` `kafka-cluster:CreateTopic`                                                                                                          |
| Produce data                            | `kafka-cluster:Connect` `kafka-cluster:DescribeTopic` `kafka-cluster:WriteData`                                                                              |
| Consume data                            | `kafka-cluster:Connect` `kafka-cluster:DescribeTopic` `kafka-cluster:DescribeGroup` `kafka-cluster:AlterGroup` `kafka-cluster:ReadData`                      |
| Produce data idempotently               | `kafka-cluster:Connect` `kafka-cluster:DescribeTopic` `kafka-cluster:WriteData` `kafka-cluster:WriteDataIdempotently`                                        |
| Produce data transactionally            | `kafka-cluster:Connect` `kafka-cluster:DescribeTopic` `kafka-cluster:WriteData` `kafka-cluster:DescribeTransactionalId` `kafka-cluster:AlterTransactionalId` |
| Describe the configuration of a cluster | `kafka-cluster:Connect` `kafka-cluster:DescribeClusterDynamicConfiguration`                                                                                  |
| Update the configuration of a cluster   | `kafka-cluster:Connect` `kafka-cluster:DescribeClusterDynamicConfiguration` `kafka-cluster:AlterClusterDynamicConfiguration`                                 |
| Describe the configuration of a topic   | `kafka-cluster:Connect` `kafka-cluster:DescribeTopicDynamicConfiguration`                                                                                    |
| Update the configuration of a topic     | `kafka-cluster:Connect` `kafka-cluster:DescribeTopicDynamicConfiguration` `kafka-cluster:AlterTopicDynamicConfiguration`                                     |
| Alter a topic                           | `kafka-cluster:Connect` `kafka-cluster:DescribeTopic` `kafka-cluster:AlterTopic`                                                                             |
