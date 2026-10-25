

# Pause and resume a connector
<a name="mkc-pause-resume-connector"></a>

You can pause a running connector to stop it from processing records, and resume it later. A paused connector keeps its configuration, its capacity settings, and its committed offsets. When you resume the connector, its tasks continue processing from the offsets that they last committed.

Pausing a connector is useful when you want to stop data flow temporarily without deleting the connector. For example, you can pause a connector while you perform maintenance on a source database or on a sink target.

Both Pause and Resume operations are asynchronous. When you submit a pause or resume request for a specific connector, you receive a connector operation ARN that you can use to track the operation's progress.

Before you pause or resume a connector, make sure that the following prerequisites are met:
+ To pause a connector, the connector must be in the `RUNNING` state.
+ To resume a connector, the connector must be in the `PAUSED` state.
+ No other lifecycle operation can be in progress on the connector.

**Pausing or resuming a connector using the AWS Management Console**

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. In the left pane, under **MSK Connect**, choose **Connectors**.

1. Select the connector that you want to pause or resume.

1. Choose **Actions**, then choose **Pause** or **Resume**. The console enables only the action that the connector's current state allows. For example, a connector in the `RUNNING` state offers **Pause**, and a connector in the `PAUSED` state offers **Resume**. Neither action is available while another operation is in progress.

1. You can then monitor the current state of the operation in the **Operations** tab of the connector.

## Pausing or resuming a connector using the AWS CLI
<a name="mkc-pause-resume-connector-cli"></a>

To pause a connector and all of its tasks, run the `pause-connector` command with the connector's ARN:

```
aws kafkaconnect pause-connector \
   --connector-arn <connector_arn>
```

To resume a paused connector, run the `resume-connector` command with the connector's ARN:

```
aws kafkaconnect resume-connector \
   --connector-arn <connector_arn>
```

Both commands return the connector ARN and a connector operation ARN. To track the operation, use the returned `connectorOperationArn` with the `describe-connector-operation` command:

```
aws kafkaconnect describe-connector-operation \
   --connector-operation-arn <operation_arn>
```

A connector reports its own state separately from the operation state. While a pause operation runs, the connector is in the `PAUSING` state, and it moves to `PAUSED` when the operation completes. While a resume operation runs, the connector is in the `RESUMING` state, and it moves to `RUNNING` when the operation completes.

A pause operation can be in one of the following states.

`PAUSE_IN_PROGRESS`  
The pause operation has been accepted and is executing.

`PAUSE_COMPLETE`  
The connector and all of its running tasks are paused, and have stopped processing records. Tasks that were already in a failed state stay failed. They are not paused, and they do not prevent the operation from completing.

`PAUSE_FAILED`  
The pause operation did not complete, and the connector might be left in an intermediate state. To determine the connector's current state and the steps to recover, see [If a pause or resume operation fails](#mkc-pause-resume-connector-failures).

A resume operation can be in one of the following states.

`RESUME_IN_PROGRESS`  
The resume operation has been accepted and is executing.

`RESUME_COMPLETE`  
The connector and all of its paused tasks have resumed processing records. Tasks that were already in a failed state stay failed. They are not resumed, and they do not prevent the operation from completing.

`RESUME_FAILED`  
The resume operation did not complete, and the connector might be left in an intermediate state. To determine the connector's current state and the steps to recover, see [If a pause or resume operation fails](#mkc-pause-resume-connector-failures).

**Note**  
A resume operation can take longer than a pause operation. If the connector uses autoscaled capacity, the resume operation scales the workers back up from the minimum worker count before the tasks start processing records.

## If a pause or resume operation fails
<a name="mkc-pause-resume-connector-failures"></a>

The state of the connector depends on how far the operation got before it failed. Check the connector's state with `DescribeConnector`, and the `errorInfo` field with `DescribeConnectorOperation`, before you retry.

The connector is in the state that it started in  
The change never reached the connector, so the connector is still `RUNNING` after a failed pause, or `PAUSED` after a failed resume. You can retry the operation.

The connector is in the state that you asked for  
The connector accepted the change, but some of its tasks did not reach the target state in time. The connector is `PAUSED` after a failed pause, or `RUNNING` after a failed resume, and `errorInfo` reports `KafkaConnect.ConnectorNotReachedTargetState`. Review your connector logs to find out why the tasks did not reach the target state.

The connector is still `PAUSING` or `RESUMING`  
Amazon MSK Connect could not confirm whether the connector accepted the change. Because the connector is not in the state that the operation requires, you cannot retry the operation. Contact AWS Support to recover the connector.

## Considerations
<a name="mkc-pause-resume-connector-considerations"></a>
+ When you pause a connector, Amazon MSK Connect does not delete any connector resources. The connector keeps its configuration, its capacity settings, and its committed offsets.
+ You continue to incur charges for a paused connector. A connector that uses provisioned capacity is billed at its full capacity. A connector that uses autoscaled capacity scales toward its minimum worker count, and is billed for the workers that remain.
+ A paused connector stops processing records. For a sink connector, records that producers write to the source topics while the connector is paused are processed after you resume it. Records that fall outside the retention period of those topics are not processed.
+ While a pause or resume operation is in progress, you cannot perform other lifecycle operations on the connector, such as update or delete.
+ To update a paused connector with the `UpdateConnector` API, you must set `skipHealthValidation` to `true` in the update request, because Amazon MSK Connect cannot validate the health of a connector that is not processing records.
+ You can restart a paused connector with the `RestartConnector` API. The connector returns to the `PAUSED` state after the restart completes. Restart is not available for connectors that were created before Amazon MSK Connect supported the operation.
+ Use `DescribeConnectorOperation` with the returned `connectorOperationArn` to track whether the operation is in progress, complete, or failed.

For more information about using the MSK Connect API to pause or resume a connector, see [PauseConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_PauseConnector.html) and [ResumeConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ResumeConnector.html).