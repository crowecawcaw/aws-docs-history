# AWS Identity and Access Management Access Analyzer events

IAM Access Analyzer sends service events directly to EventBridge, as well as via AWS CloudTrail.

## IAM Access Analyzer service events

IAM Access Analyzer sends the following events directly to EventBridge:

- Access Analyzer Finding
- Access Preview State Change
- Unused Access Finding for IAM entities
- Internal Access Finding

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.access-analyzer

```
{
  "source": ["aws.access-analyzer"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.access-analyzer"],
  "detail-type": ["`Access Analyzer Finding`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## IAM Access Analyzer events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from IAM Access Analyzer to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.access-analyzer
- `eventSource`: access-analyzer.amazonaws.com

```
{
  "source": ["aws.access-analyzer"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["access-analyzer.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.access-analyzer"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["access-analyzer.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
