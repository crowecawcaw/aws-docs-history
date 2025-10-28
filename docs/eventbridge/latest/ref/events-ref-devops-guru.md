# Amazon DevOps Guru events

DevOps Guru sends service events directly to EventBridge, as well as via AWS CloudTrail.

## DevOps Guru service events

DevOps Guru sends the following events directly to EventBridge:

- DevOps Guru New Insight Open
- DevOps Guru New Anomaly Association
- DevOps Guru Insight Severity Upgraded
- DevOps Guru New Recommendation Created
- DevOps Guru Insight Closed

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.devops-guru

```
{
  "source": ["aws.devops-guru"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.devops-guru"],
  "detail-type": ["`DevOps Guru New Insight Open`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## DevOps Guru events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from DevOps Guru to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.devops-guru
- `eventSource`: devops-guru.amazonaws.com

```
{
  "source": ["aws.devops-guru"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["devops-guru.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.devops-guru"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["devops-guru.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
