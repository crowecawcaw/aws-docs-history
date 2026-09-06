

# Amazon Connect Participant Service events
<a name="events-ref-participant-connect"></a>

Amazon Connect Participant Service sends service events to EventBridge via AWS CloudTrail.

## Amazon Connect Participant Service events delivered via AWS CloudTrail
<a name="event-ref-participant-connect-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Connect Participant Service to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.participant-connect
+ `eventSource`: participant-connect.amazonaws.com

```
{
  "source": ["aws.participant-connect"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["participant-connect.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.participant-connect"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["participant-connect.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```