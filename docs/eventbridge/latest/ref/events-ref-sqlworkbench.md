

# AWS SQL Workbench events
<a name="events-ref-sqlworkbench"></a>

AWS SQL Workbench sends service events to EventBridge via AWS CloudTrail.

## AWS SQL Workbench events delivered via AWS CloudTrail
<a name="event-ref-sqlworkbench-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS SQL Workbench to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.sqlworkbench
+ `eventSource`: sqlworkbench.amazonaws.com

```
{
  "source": ["aws.sqlworkbench"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["sqlworkbench.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.sqlworkbench"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["sqlworkbench.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```