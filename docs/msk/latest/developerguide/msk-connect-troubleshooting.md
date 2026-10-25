

# Troubleshoot issues in Amazon MSK Connect
<a name="msk-connect-troubleshooting"></a>

The following information can help you troubleshoot problems that you might have while using MSK Connect. You can also post your issue to the [AWS re:Post](https://repost.aws/).

**Connector is unable to access resources hosted on the public internet**  
See [Enabling internet access for Amazon MSK Connect](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-internet-access.html).

**Connector's number of running tasks is not equal to the number of tasks specified in tasks.max**  
Here are some reasons a connector may use fewer tasks than the specified tasks.max configuration:
+ Some connector implementations limit the number of tasks the can be used. For example, the Debezium connector for MySQL is limited to using a single task.
+ When using autoscaled capacity mode, Amazon MSK Connect overrides a connector's tasks.max property with a value that is proportional to the number of workers running in the connector and the number of MCUs per worker. If you have configured the optional `maxAutoscalingTaskCount` parameter, the `tasks.max` value will not exceed this limit. For more information, see [Understand maximum autoscaling task count](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-connectors.html#msk-connect-max-autoscaling-task-count).
+ For sink connectors, the level of parallelism (number of tasks) cannot be more than the number of topic partitions. While you can set the tasks.max larger than that, a single partition is never processed by more than a single task at a time.
+ In Kafka Connect 2.7.x, the default consumer partition assignor is `RangeAssignor`. The behavior of this assignor is to give the first partition of every topic to a single consumer, the second partition of every topic to a single consumer, etc. This means that the maximum number of active tasks for a sink connector using `RangeAssignor` is equal to the maximum number of partitions in any single topic being consumed. If this doesn't work for your use case, you should [create a Worker Configuration](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-workers.html#msk-connect-create-custom-worker-config) in which the `consumer.partition.assignment.strategy` property is set to a more suitable consumer partition assignor. See [Kafka 2.7 Interface ConsumerPartitionAssignor: *All Known Implementing Classes*](https://kafka.apache.org/27/javadoc/org/apache/kafka/clients/consumer/ConsumerPartitionAssignor.html).

**Connector restart operation reaches RESTART\_FAILED state**  
If a restart operation reaches the `RESTART_FAILED` state, try the following to resolve the issue:
+ Check the `errorInfo` field in the `DescribeConnectorOperation` response for details.
+ Review connector logs from CloudWatch, Amazon S3, or Firehose for error messages indicating why tasks cannot complete startup.
+ Check whether the connector's tasks are blocked by external dependencies (databases, network endpoints, or other systems that the connector interacts with).
+ Verify that the connector's Kafka cluster is reachable and healthy.

**Cannot restart connector — 400 BadRequestException**  
Here are some reasons why you might not be able to restart a connector:
+ The connector is not in the `RUNNING` state (for example, it is `CREATING`, `UPDATING`, or `DELETING`).
+ Another lifecycle operation is already in progress on the connector.
+ You specified `--only-failed-tasks` on a connector using Amazon MSK version earlier than 3.7 (this feature requires version 3.7 or later).
+ The connector was created before the restart capability was available. This feature is currently supported only for newly created connectors.

**Connector pause or resume operation reaches a failed state**  
A pause operation that reaches the `PAUSE_FAILED` state, or a resume operation that reaches the `RESUME_FAILED` state, does not always leave your connector unusable, and only some failures can be retried. Diagnose the failure as follows:

1. Call `DescribeConnectorOperation` with the `connectorOperationArn` that your pause or resume request returned, and read the `errorInfo` field to find out why the operation failed.

1. Call `DescribeConnector` and note the connector's current state. The state determines what you can do next.

1. Review your connector logs in CloudWatch, Amazon S3, or Firehose for the period when the operation ran. Look for errors that stop the connector from applying the change, such as an unreachable Kafka cluster, a failed broker authentication, or a task that is blocked on an external dependency such as a source database or a sink target.

Then take the action for the state that your connector is in.

`RUNNING` after a failed pause, or `PAUSED` after a failed resume  
The change never reached your connector, so the connector is still in the state that it started in, and the operation is safe to retry. Fix the cause that `errorInfo` and your connector logs point to. For example, update the connector to correct a configuration value, or restore network access to your Kafka cluster. Then call `PauseConnector` or `ResumeConnector` again.

`PAUSED` after a failed pause, or `RUNNING` after a failed resume  
Your connector reached the state that you asked for, but some of its tasks did not, and `errorInfo` reports `KafkaConnect.ConnectorNotReachedTargetState`. Do not retry the operation. The connector is already in the target state, so the request is rejected with a 400 `BadRequestException`. Instead, compare the `PausedTaskCount`, `RunningTaskCount`, and `ErroredTaskCount` metrics against the number of tasks that you expect, and use your connector logs to find why the remaining tasks did not converge.  
To bring the remaining tasks into the state that you asked for, first fix the cause that your connector logs report. Then update the connector with `skipHealthValidation` set to `true`. The update restarts the connector's tasks, and they then apply the pause or resume.  
After a failed resume, you can also restart the connector to restart the tasks that did not start, because the connector is in the `RUNNING` state that a restart requires.

`PAUSING` or `RESUMING`  
First confirm that the operation has actually failed: call `DescribeConnectorOperation` and check the operation state, because a connector stays in `PAUSING` or `RESUMING` while the operation is still in progress too. If the operation state is `PAUSE_FAILED` or `RESUME_FAILED` and the connector is still `PAUSING` or `RESUMING`, Amazon MSK Connect could not confirm whether your connector accepted the change. You cannot retry the operation, and you cannot run any other lifecycle operation, because the connector is not in a state that any of them accept. Contact AWS Support to recover the connector.

The `errorInfo` field reports one of the following Kafka Connect error codes.

`KafkaConnect.ConnectorNotReachedTargetState`  
Your connector accepted the change, but some of its tasks did not reach the target state in time. The connector is in the state that you asked for, so work through the task counts and the connector logs rather than retrying the operation.

`KafkaConnect.NotFound`  
Your connector is no longer registered on its Kafka Connect workers. This can happen for several reasons, for example if the Kafka Connect internal topics that store connector configurations are deleted. To recreate the connector, update its configuration. Updating the connector does not always bring it back in the state that you wanted, so check the connector's state and its task-count metrics before you run another operation on it.

`KafkaConnect.BrokerAuthenticationFailure`  
Amazon MSK Connect could not authenticate to your Kafka cluster. Verify the authentication type that your connector uses, and verify that the permissions that this type requires are still in place. Then retry the operation.

`KafkaConnect.BrokerUnreachable`  
Amazon MSK Connect could not reach your Kafka cluster. Verify that the cluster is healthy, that its bootstrap servers match your connector's configuration, and that the subnets and security groups that your connector uses still allow traffic to the cluster. Then retry the operation.

For more information about where a failed operation leaves your connector, see [If a pause or resume operation fails](mkc-pause-resume-connector.md#mkc-pause-resume-connector-failures).

**Connector pause or resume operation stays in progress**  
An operation can stay in the `PAUSE_IN_PROGRESS` or `RESUME_IN_PROGRESS` state for a long time. If Amazon MSK Connect cannot reach your connector's Kafka Connect API, or cannot confirm that your connector applied the change, it retries the operation, so an operation that is still in progress can still reach `PAUSE_COMPLETE` or `RESUME_COMPLETE` on a later attempt. An operation that has not reached a terminal state has not failed.

A connector is left in the `PAUSING` or `RESUMING` state both by an operation that is still in progress and by one that failed, so call `DescribeConnectorOperation` to tell the two apart before you act. While the operation state is `PAUSE_IN_PROGRESS` or `RESUME_IN_PROGRESS`, the operation is still running, and:
+ Your connector stays in the `PAUSING` or `RESUMING` state.
+ You cannot perform other lifecycle operations on your connector, such as update or delete.
+ You cannot retry the pause or resume request, because your connector is not in the state that the operation requires.

Because you cannot retry, remove whatever is stopping your connector from applying the change so that the next retry succeeds. Check your connector logs in CloudWatch, Amazon S3, or Firehose for an unreachable Kafka cluster, a failed broker authentication, or a task that is blocked on an external dependency, and fix what you find. Keep polling `DescribeConnectorOperation`. If the operation does not reach a terminal state, contact AWS Support to recover the connector.

**Cannot pause or resume a connector: 400 BadRequestException**  
Here are some reasons why you might not be able to pause or resume a connector:
+ You called `PauseConnector` on a connector that is not in the `RUNNING` state. A connector that is already `PAUSED` or `PAUSING` cannot be paused again. Call `DescribeConnector` to confirm the connector's state, and pause it only from `RUNNING`.
+ You called `ResumeConnector` on a connector that is not in the `PAUSED` state. A connector that is already `RESUMING` is being resumed, so wait for that operation to complete instead of calling `ResumeConnector` again.
+ Another lifecycle operation is already in progress on your connector. Track that operation with `DescribeConnectorOperation`, wait for it to reach a terminal state, and then submit your request.

**Cannot update a paused connector**  
To update a connector that is in the `PAUSED` state, set `skipHealthValidation` to `true` in the update request, because Amazon MSK Connect cannot validate the health of a connector that is not processing records.