

# Identity Store events
<a name="events-ref-identitystore"></a>

Identity Store sends service events to EventBridge via AWS CloudTrail.

## Identity Store events delivered via AWS CloudTrail
<a name="event-ref-identitystore-events-via-CT"></a>

AWS CloudTrail sends events originating from Identity Store to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.identitystore
+ `eventSource`: identitystore.amazonaws.com

```
{
  "source": ["aws.identitystore"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["identitystore.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.identitystore"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["identitystore.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```