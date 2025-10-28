# Monitor Amazon EBS snapshot lock

You can monitor actions related to Amazon EBS snapshot lock using the following tools:

###### Topics

- [Monitor using CloudTrail](#snapshot-lock-ct "#snapshot-lock-ct")
- [Monitor using EventBridge](#snapshot-lock-ev "#snapshot-lock-ev")

## Monitor Amazon EBS snapshot locks using AWS CloudTrail

You can monitor API calls for snapshot locks as events, including calls from the console
and from code calls to the APIs. Using the information collected by CloudTrail, you can determine
the request that was made, the IP address from which the request was made, who made the
request, when it was made, and additional details.

For more information, see [Log API calls using AWS CloudTrail](../../../AWSEC2/latest/UserGuide/monitor-with-cloudtrail.md "../../../AWSEC2/latest/UserGuide/monitor-with-cloudtrail.md").

## Monitor Amazon EBS snapshot locks using Amazon EventBridge

Amazon EBS emits events related to snapshot lock actions. You can use AWS Lambda and
Amazon EventBridge to handle event notifications programmatically. Events are emitted on a
best effort basis. For more information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

The following events are emitted:

- Successfully locked snapshot in governance or compliance mode.

```
{
  "version": "0",
  "id": "`01234567-01234-0123-0123-012345678901`",
  "detail-type": "EBS Snapshot Notification",
  "source": "aws.ec2",
  "account": "`012345678901`",
  "time": "`yyyy-mm-ddThh:mm:ssZ`",
  "region": "`us-east-1`",
  "resources": [
    "`arn:aws:ec2::us-west-2:snapshot/snap-01234567890abcdef`"
  ],
  "detail": {
    "event": "lockSnapshot",
    "result": "succeeded",
    "snapshot_id": "`arn:aws:ec2::us-west-2:snapshot/snap-01234567890abcdef`",
    "source": `012345678901`,
    "lockState": "`compliance-cooloff`",
    "lockCreatedOn": "`yyyy-mm-ddThh:mm:ssZ`",
    "lockExpiresOn": "`yyyy-mm-ddThh:mm:ssZ`",
    "lockDuration": `123`,
    "lockStartDurationTime": "`yyyy-mm-ddThh:mm:ssZ`",
    "cooOffPeriod": `24`,
    "coolOffPeriodExpiresOn": "`yyyy-mm-ddThh:mm:ssZ`"
  }
}
```

- Failed lock event when a snapshot is locked while it is in the `pending`
  state, and it fails to reach the `completed` state.

```
{
  "version": "0",
  "id": "`01234567-01234-0123-0123-012345678901`",
  "detail-type": "EBS Snapshot Notification",
  "source": "aws.ec2",
  "account": "`012345678901`",
  "time": "`yyyy-mm-ddThh:mm:ssZ`",
  "region": "`us-east-1`",
  "resources": [
    "`arn:aws:ec2::us-west-2:snapshot/snap-01234567890abcdef`"
  ],
  "detail": {
    "event": "lockSnapshot",
    "result": "failed",
    "cause": "snapshot failed",
    "snapshot_id": "`arn:aws:ec2::us-west-2:snapshot/snap-01234567890abcdef`",
    "lockState": "pending-compliance",
    "lockCreatedOn": "`yyyy-mm-ddThh:mm:ssZ`",
    "lockDuration": `123`,
    "lockStartDurationTime": "`yyyy-mm-ddThh:mm:ssZ`",
    "cooOffPeriod": `24`,
    "coolOffPeriodExpiresOn": "`yyyy-mm-ddThh:mm:ssZ`"
  }
}
```

- Lock expired

```
{
  "version": "0",
  "id": "`01234567-01234-0123-0123-012345678901`",
  "detail-type": "EBS Snapshot Notification",
  "source": "aws.ec2",
  "account": "`012345678901`",
  "time": "`yyyy-mm-ddThh:mm:ssZ`",
  "region": "`us-east-1`",
  "resources": [
    "`arn:aws:ec2::us-west-2:snapshot/snap-01234567890abcdef`"
  ],
  "detail": {
    "event": "lockDurationExpiry",
    "result": "succeeded",
    "snapshot_id": "`arn:aws:ec2::us-west-2:snapshot/snap-01234567890abcdef`",
    "lockState": "`expired`",
    "lockCreatedOn": "`yyyy-mm-ddThh:mm:ssZ`",
    "lockExpiresOn": "`yyyy-mm-ddThh:mm:ssZ`",
    "lockDuration": `123`
  }
}
```

- Cooling-off period expired after being locked in compliance mode.

```
{
  "version": "0",
  "id": "`01234567-01234-0123-0123-012345678901`",
  "detail-type": "EBS Snapshot Notification",
  "source": "aws.ec2",
  "account": "`012345678901`",
  "time": "`yyyy-mm-ddThh:mm:ssZ`",
  "region": "`us-east-1`",
  "resources": [
    "`arn:aws:ec2::us-west-2:snapshot/snap-01234567890abcdef`"
  ],
  "detail": {
    "event": "cooloffperiodExpiry",
    "result": "succeeded",
    "snapshot_id": "`arn:aws:ec2::us-west-2:snapshot/snap-01234567890abcdef`",
    "lockState": "`compliance`",
    "lockCreatedOn": "`yyyy-mm-ddThh:mm:ssZ`",
    "lockExpiresOn": "`yyyy-mm-ddThh:mm:ssZ`",
    "lockDuration": `123`,
    "lockStartDurationTime": "`yyyy-mm-ddThh:mm:ssZ`",
    "cooOffPeriod": `24`,
    "coolOffPeriodExpiresOn": "`yyyy-mm-ddThh:mm:ssZ`"
  }
}
```
