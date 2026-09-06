

# Amazon S3 on Outposts events
<a name="events-ref-s3-outposts"></a>

S3 on Outposts sends service events directly to EventBridge, as well as via AWS CloudTrail.

## S3 on Outposts service events
<a name="events-ref-s3-outposts-events"></a>

S3 on Outposts sends the following events directly to EventBridge: 
+ Object Replication Failed

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.s3-outposts

```
{
  "source": ["aws.s3-outposts"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.s3-outposts"],
  "detail-type": ["{{Object Replication Failed}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## S3 on Outposts events delivered via AWS CloudTrail
<a name="event-ref-s3-outposts-events-via-CT"></a>

AWS CloudTrail sends events originating from S3 on Outposts to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.s3-outposts
+ `eventSource`: s3-outposts.amazonaws.com

```
{
  "source": ["aws.s3-outposts"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["s3-outposts.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.s3-outposts"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["s3-outposts.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```