

# AWS IoT TwinMaker events
<a name="events-ref-iottwinmaker"></a>

AWS IoT TwinMaker sends service events to EventBridge via AWS CloudTrail.

## AWS IoT TwinMaker events delivered via AWS CloudTrail
<a name="event-ref-iottwinmaker-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS IoT TwinMaker to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.iottwinmaker
+ `eventSource`: iottwinmaker.amazonaws.com

```
{
  "source": ["aws.iottwinmaker"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["iottwinmaker.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.iottwinmaker"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["iottwinmaker.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```