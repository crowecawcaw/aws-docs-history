

# Amazon Redshift Data API events
<a name="events-ref-redshift-data"></a>

Redshift Data API sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Redshift Data API service events
<a name="events-ref-redshift-data-events"></a>

Redshift Data API sends the following events directly to EventBridge: 
+ Redshift Data Statement Status Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.redshift-data

```
{
  "source": ["aws.redshift-data"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.redshift-data"],
  "detail-type": ["{{Redshift Data Statement Status Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Redshift Data API events delivered via AWS CloudTrail
<a name="event-ref-redshift-data-events-via-CT"></a>

AWS CloudTrail sends events originating from Redshift Data API to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.redshift-data
+ `eventSource`: redshift-data.amazonaws.com

```
{
  "source": ["aws.redshift-data"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["redshift-data.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.redshift-data"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["redshift-data.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```