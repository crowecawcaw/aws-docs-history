

# Amazon Connect Customer Contact Lens events
<a name="events-ref-contact-lens"></a>

Connect Customer Contact Lens sends service events to EventBridge via AWS CloudTrail.

## Connect Customer Contact Lens events delivered via AWS CloudTrail
<a name="event-ref-contact-lens-events-via-CT"></a>

AWS CloudTrail sends events originating from Connect Customer Contact Lens to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.contact-lens
+ `eventSource`: contact-lens.amazonaws.com

```
{
  "source": ["aws.contact-lens"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["contact-lens.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.contact-lens"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["contact-lens.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```