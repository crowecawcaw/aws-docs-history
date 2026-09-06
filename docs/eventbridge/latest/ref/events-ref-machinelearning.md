

# Amazon Machine Learning events
<a name="events-ref-machinelearning"></a>

Amazon ML sends service events to EventBridge via AWS CloudTrail.

## Amazon ML events delivered via AWS CloudTrail
<a name="event-ref-machinelearning-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon ML to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.machinelearning
+ `eventSource`: machinelearning.amazonaws.com

```
{
  "source": ["aws.machinelearning"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["machinelearning.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.machinelearning"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["machinelearning.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```