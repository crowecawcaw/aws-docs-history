

# AWS Key Management Service events
<a name="events-ref-kms"></a>

AWS KMS sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS KMS service events
<a name="events-ref-kms-events"></a>

AWS KMS sends the following events directly to EventBridge: 
+ KMS Imported Key Material Expiration
+ KMS CMK Rotation
+ KMS CMK Deletion

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.kms

```
{
  "source": ["aws.kms"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.kms"],
  "detail-type": ["{{KMS Imported Key Material Expiration}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS KMS events delivered via AWS CloudTrail
<a name="event-ref-kms-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS KMS to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.kms
+ `eventSource`: kms.amazonaws.com

```
{
  "source": ["aws.kms"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["kms.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.kms"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["kms.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```