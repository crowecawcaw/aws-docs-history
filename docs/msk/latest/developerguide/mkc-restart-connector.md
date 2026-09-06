# Restart a connector

You can restart a newly created connector and all of its tasks, or selectively
restart only the failed tasks, while preserving configuration and committed offsets.
This is useful when a connector has failed because of problems such as misconfigured
parameters or temporary network connectivity issues. You can also restart connectors that have no
failed tasks to recover from transient issues or to pick up changes in external systems
or dependencies.

The restart operation is asynchronous. When you submit a restart request, the service
returns a connector operation ARN that you can use to track the operation's
progress.

Before you restart a connector, make sure that the following prerequisites are
met:

- The connector must be in the `RUNNING` state.
- No other lifecycle operation can be in progress on the connector.

###### Restarting a connector using the AWS Management Console

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/ "https://console.aws.amazon.com/msk/").
2. In the left pane, under **MSK Connect**, choose **Connectors**.
3. Select the connector that you want to restart.
4. Choose **Actions**, then choose **Restart connector**.
5. (Optional) Select **Restart only failed tasks** to restart
   only the tasks that are in a `FAILED` state. This option is available
   only for connectors using Apache Kafka Connect version 3.7 or later.
6. Choose **Restart**.
7. You can then monitor the current state of the operation in the
   **Operations** tab of the connector.

## Restarting a connector using the AWS CLI

To restart a connector and all of its tasks, run the
`restart-connector` command with the connector's ARN:

```
aws kafkaconnect restart-connector \
   --connector-arn <connector_arn>
```

To restart only the tasks that are in a `FAILED` state and leave healthy
tasks running, add the `--only-failed-tasks` option:

```
aws kafkaconnect restart-connector \
   --connector-arn <connector_arn> \
   --only-failed-tasks
```

The preceding commands return the connector ARN and a connector operation ARN. To
track the restart operation, use the returned `connectorOperationArn` with
the `describe-connector-operation` command to check the operation
status:

```
aws kafkaconnect describe-connector-operation \
   --connector-operation-arn <operation_arn>
```

A restart operation can be in one of the following states.

| State                 | Description                                               |
| --------------------- | --------------------------------------------------------- |
| `RESTART_IN_PROGRESS` | The restart operation has been accepted and is executing. |
| `RESTART_COMPLETE`    | All affected tasks have been successfully restarted.      |
| `RESTART_FAILED`      | The operation was terminated before completion.           |

###### Note

A restart operation can complete successfully (`RESTART_COMPLETE`)
even if a task transitions to a `FAILED` state after restarting. The
operation state reflects whether the restart was executed, not whether the task
is healthy after the restart. Use the connector's state and the following CloudWatch
metrics to monitor post-restart task health: `RunningTaskCount`,
`ErroredTaskCount`, `TaskStartupSuccessPercentage`,
`SinkRecordReadRate` (sink) or `SourceRecordPollRate`
(source), and `RebalanceTimeSinceLast`.

## Considerations

- Restart behavior depends on the connector's Apache Kafka Connect
  version. On Apache Kafka Connect 3.7 and later, restart operations apply to
  the connector and its tasks by default. To restart only the tasks that are in
  a `FAILED` state, use the `--only-failed-tasks` option.
  You cannot select specific individual tasks to restart. On Apache Kafka
  Connect 2.7.1, restart operations only restart the connector instance and not
  its tasks. If you specify `--only-failed-tasks`, the request is
  rejected with a 400 error.
- The restart preserves all connector configuration and committed offsets.
- While a restart is in progress, you cannot perform other lifecycle
  operations (update, delete) on the connector.
- Use `DescribeConnectorOperation` with the returned
  `connectorOperationArn` to track whether the operation is in
  progress, complete, or failed.

To use the MSK Connect API to restart a connector, see [RestartConnector](../../../MSKC/latest/mskc/API_RestartConnector.md "../../../MSKC/latest/mskc/API_RestartConnector.md").
