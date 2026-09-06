

# AWS HealthOmics events
<a name="events-ref-omics"></a>

HealthOmics sends service events directly to EventBridge, as well as via AWS CloudTrail.

## HealthOmics service events
<a name="events-ref-omics-events"></a>

HealthOmics sends the following events directly to EventBridge: 
+ Reference Store Status Change
+ Reference Status Change
+ Reference Import Job Status Change
+ Sequence Store Status Change
+ Read Set Status Change
+ Read Set Import Job Status Change
+ Read Set Export Job Status Change
+ Read Set Activation Job Status Change
+ Workflow Status Change
+ RunGroup Status Change
+ Run Status Change
+ Task Status Change
+ Variant Import Job Status Change
+ Annotation Import Job Status Change
+ Variant Store Status Change
+ Annotation Store Status Change
+ Variant Store Share Status Change
+ Annotation Store Share Status Change
+ Workflow Share Status Change
+ S3 Access Policy Status Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.omics

```
{
  "source": ["aws.omics"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.omics"],
  "detail-type": ["{{Reference Store Status Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## HealthOmics events delivered via AWS CloudTrail
<a name="event-ref-omics-events-via-CT"></a>

AWS CloudTrail sends events originating from HealthOmics to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.omics
+ `eventSource`: omics.amazonaws.com

```
{
  "source": ["aws.omics"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["omics.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.omics"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["omics.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```