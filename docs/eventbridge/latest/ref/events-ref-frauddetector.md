

# Amazon Fraud Detector events
<a name="events-ref-frauddetector"></a>

Amazon Fraud Detector sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Fraud Detector service events
<a name="events-ref-frauddetector-events"></a>

Amazon Fraud Detector sends the following events directly to EventBridge: 
+ Event Prediction Result Returned

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.frauddetector

```
{
  "source": ["aws.frauddetector"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.frauddetector"],
  "detail-type": ["{{Event Prediction Result Returned}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon Fraud Detector events delivered via AWS CloudTrail
<a name="event-ref-frauddetector-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Fraud Detector to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.frauddetector
+ `eventSource`: frauddetector.amazonaws.com

```
{
  "source": ["aws.frauddetector"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["frauddetector.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.frauddetector"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["frauddetector.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```