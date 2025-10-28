# AWS Resource Explorer events

Resource Explorer sends service events to EventBridge via AWS CloudTrail.

## Resource Explorer events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Resource Explorer to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.resource-explorer-2
- `eventSource`: resource-explorer-2.amazonaws.com

```
{
  "source": ["aws.resource-explorer-2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["resource-explorer-2.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.resource-explorer-2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["resource-explorer-2.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
