

# AWS Glue DataBrew events
<a name="events-ref-databrew"></a>

DataBrew sends service events directly to EventBridge, as well as via AWS CloudTrail.

## DataBrew service events
<a name="events-ref-databrew-events"></a>

DataBrew sends the following events directly to EventBridge: 
+ DataBrew Job State Change
+ DataBrew Ruleset Validation Result

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.databrew

```
{
  "source": ["aws.databrew"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.databrew"],
  "detail-type": ["{{DataBrew Job State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## DataBrew events delivered via AWS CloudTrail
<a name="event-ref-databrew-events-via-CT"></a>

AWS CloudTrail sends events originating from DataBrew to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.databrew
+ `eventSource`: databrew.amazonaws.com

```
{
  "source": ["aws.databrew"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["databrew.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.databrew"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["databrew.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```