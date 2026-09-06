

# AWS Resource Explorer events
<a name="events-ref-resource-explorer-2"></a>

Resource Explorer sends service events to EventBridge via AWS CloudTrail.

## Resource Explorer events delivered via AWS CloudTrail
<a name="event-ref-resource-explorer-2-events-via-CT"></a>

AWS CloudTrail sends events originating from Resource Explorer to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.resource-explorer-2
+ `eventSource`: resource-explorer-2.amazonaws.com

```
{
  "source": ["aws.resource-explorer-2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["resource-explorer-2.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.resource-explorer-2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["resource-explorer-2.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```