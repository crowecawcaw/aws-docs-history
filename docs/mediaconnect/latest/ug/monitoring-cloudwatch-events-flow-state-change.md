# MediaConnect flow

state change event

This event is published when a flow's state has changed from or to any of the
following states: Standby, Active, Updating, Deleting, Starting, Stopping, or Error.

For information about subscribing to this event, see [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

The following message is an example of this event.

```
{
    "account": "111122223333",
    "detail": {
        "currentStatus": "STARTING",
        "previousStatus": "STANDBY"
    },
    "detail-type": "MediaConnect Flow Status Change",
    "id": "01234567-0123-0123-0123-0123456789ab",
    "region": "us-east-1",
    "resources": ["arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow"],
    "source": "aws.mediaconnect",
    "time": "2022-01-06T00:45:47Z",
    "version": "0"
}

```
