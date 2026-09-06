

# Amazon Redshift events
<a name="events-ref-redshift"></a>

Amazon Redshift sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Redshift service events
<a name="events-ref-redshift-events"></a>

Amazon Redshift sends the following events directly to EventBridge: 
+ Redshift Integration Monitoring
+ Redshift Integration Configuration
+ Redshift Integration Operation

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.redshift

```
{
  "source": ["aws.redshift"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.redshift"],
  "detail-type": ["{{Redshift Integration Monitoring}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon Redshift events delivered via AWS CloudTrail
<a name="event-ref-redshift-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Redshift to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.redshift
+ `eventSource`: redshift.amazonaws.com

```
{
  "source": ["aws.redshift"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["redshift.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.redshift"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["redshift.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```