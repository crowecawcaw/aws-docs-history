

# AWS Systems Manager GUI Connect events
<a name="events-ref-ssm-guiconnect"></a>

Systems Manager GUI Connect sends service events to EventBridge via AWS CloudTrail.

## Systems Manager GUI Connect events delivered via AWS CloudTrail
<a name="event-ref-ssm-guiconnect-events-via-CT"></a>

AWS CloudTrail sends events originating from Systems Manager GUI Connect to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.ssm-guiconnect
+ `eventSource`: ssm-guiconnect.amazonaws.com

```
{
  "source": ["aws.ssm-guiconnect"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ssm-guiconnect.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ssm-guiconnect"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ssm-guiconnect.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```