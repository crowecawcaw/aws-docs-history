# MediaConnect flow

maintenance event

This event is published when a flow's maintenance status has changed, either to or
from any of the following states:

- **SCHEDULED** - Maintenance is scheduled for
  the flow.
- **RESCHEDULED** - MediaConnect is unable to perform
  maintenance at the previously scheduled date and time. A new date and time
  has been automatically assigned by MediaConnect for this flow's maintenance.
- **CANCELED** - Maintenance for this flow is
  cancelled by MediaConnect.
- **INPROGRESS** - Maintenance has started and
  is currently in progress for this flow.
- **FINISHED** - Maintenance completed
  successfully for this flow.
- **FAILED** - Maintenance did not complete
  successfully for this flow.

For information about subscribing to this event, see [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

For information about MediaConnect maintenance, see [MediaConnect
flow maintenance](maintenance.md "maintenance.md").

The following message is an example of this EventBridge event.

```
{
    "version": "0",
    "id": "01234567-0123-0123-0123-0123456789ab",
    "detail-type": "MediaConnect Flow Maintenance",
    "source": "aws.mediaconnect",
    "account": "111122223333",
    "time": "2022-02-14T00:45:47Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:ExampleFlow"
    ],
    "detail": {
        "currentStatus": "FINISHED"
    }
}

```
