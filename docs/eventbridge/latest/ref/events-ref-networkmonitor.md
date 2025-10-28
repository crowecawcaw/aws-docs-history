# CloudWatch Network Monitor events

Amazon CloudWatch Network Monitor sends service events to EventBridge via AWS CloudTrail.

## Amazon CloudWatch Network Monitor events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon CloudWatch Network Monitor to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.networkmonitor
- `eventSource`: networkmonitor.amazonaws.com

```
{
  "source": ["aws.networkmonitor"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["networkmonitor.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.networkmonitor"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["networkmonitor.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
