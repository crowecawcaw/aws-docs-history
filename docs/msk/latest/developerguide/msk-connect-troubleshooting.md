# Troubleshoot issues in Amazon MSK Connect

The following information can help you troubleshoot problems that you might have while using MSK Connect. You can also post your issue to the [AWS re:Post](https://repost.aws/ "https://repost.aws/").

###### Connector is unable to access resources hosted on the public internet

See [Enabling internet access for Amazon MSK Connect](msk-connect-internet-access.md "msk-connect-internet-access.md").

###### Connector's number of running tasks is not equal to the number of tasks specified in tasks.max

Here are some reasons a connector may use fewer tasks than the specified tasks.max configuration:

- Some connector implementations limit the number of tasks the can be used. For example, the Debezium connector for MySQL is limited to using a single task.
- When using autoscaled capacity mode, Amazon MSK Connect overrides a connector's
  tasks.max property with a value that is proportional to the number of workers
  running in the connector and the number of MCUs per worker. If you have configured
  the optional `maxAutoscalingTaskCount` parameter, the `tasks.max` value
  will not exceed this limit. For more information, see [Understand maximum autoscaling task count](msk-connect-connectors.md#msk-connect-max-autoscaling-task-count "msk-connect-connectors.md#msk-connect-max-autoscaling-task-count").
- For sink connectors, the level of parallelism (number of tasks) cannot be more than the number of
  topic partitions. While you can set the tasks.max larger than that, a single partition is never processed by more than a single task at a time.
- In Kafka Connect 2.7.x, the default consumer partition assignor is `RangeAssignor`.
  The behavior of this assignor is to give the first partition of every topic to a
  single consumer, the second partition of every topic to a single consumer, etc. This
  means that the maximum number of active tasks for a sink connector using
  `RangeAssignor` is equal to the maximum number of partitions in any
  single topic being consumed. If this doesn't work for your use case, you should [create a Worker Configuration](msk-connect-workers.md#msk-connect-create-custom-worker-config "msk-connect-workers.md#msk-connect-create-custom-worker-config") in which the
  `consumer.partition.assignment.strategy` property is set to a more
  suitable consumer partition assignor. See [Kafka 2.7 Interface ConsumerPartitionAssignor: _All Known Implementing Classes_](https://kafka.apache.org/27/javadoc/org/apache/kafka/clients/consumer/ConsumerPartitionAssignor.html "https://kafka.apache.org/27/javadoc/org/apache/kafka/clients/consumer/ConsumerPartitionAssignor.html").

###### Connector restart operation reaches RESTART\_FAILED state

If a restart operation reaches the `RESTART_FAILED` state, try the following to resolve the issue:

- Check the `errorInfo` field in the `DescribeConnectorOperation` response for details.
- Review connector logs from CloudWatch, Amazon S3, or Firehose for error messages indicating why tasks cannot complete startup.
- Check whether the connector's tasks are blocked by external dependencies (databases, network endpoints, or other systems that the connector interacts with).
- Verify that the connector's Kafka cluster is reachable and healthy.

###### Cannot restart connector — 400 BadRequestException

Here are some reasons why you might not be able to restart a connector:

- The connector is not in the `RUNNING` state (for example, it is `CREATING`, `UPDATING`, or `DELETING`).
- Another lifecycle operation is already in progress on the connector.
- You specified `--only-failed-tasks` on a connector using Amazon MSK version earlier than 3.7 (this feature requires version 3.7 or later).
- The connector was created before the restart capability was available. This feature is currently supported only for newly created connectors.
