

# Monitoring AWS Elemental Inference events in Amazon EventBridge
<a name="monitoring-events"></a>

Elemental Inference automatically turns information about event clipping metadata into events in EventBridge. You can use Amazon EventBridge to manage these events. For example, you can create event rules and deliver the events in emails or SMS messages. You can deliver events to a number of destinations. 

For information about the specific events in Elemental Inference that are sent to EventBridge, see the sections that follow.

For information about working with AWS Elemental Inference events in EventBridge, see [Amazon EventBridge user guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

**Topics**
+ [Clip Metadata Generated event](#eventName)

## Clip Metadata Generated event
<a name="eventName"></a>

This event is published when Elemental Inference detects an interesting event in a stream that you are pushing to Elemental Inference. The event includes the following information:
+ `resource`: The ARN of the Elemental Inference feed that this clipping event belongs to.
+ `timescale`
+ `startPts` and `endPts`: The start and end presentation time stamp in the source video. This range identifies the start and end of the interesting event.
+ `description`: The field is optional.
+ `tags`

The following message is an example of this event.

```
{
    "version": "0",
    "id": "12345678-1234-1234-1234-123456789012",
    "detail-type": "Clip Metadata Generated",
    "source": "aws.elemental-inference",
    "account": "111122223333",
    "time": "2026-03-09T08:41:11Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:elemental-inference:us-west-2:feed/vbphju6m7nohlpcs3sd"
    ],
    "detail": {
        "timescale": 90000,
        "startPts": 159574109479500,
        "endPts": 159574109560500,
        "description": "",
        "tags": [
            "goal"
        ]
    }
}
```