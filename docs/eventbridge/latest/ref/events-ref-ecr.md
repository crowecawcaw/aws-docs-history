# Amazon Elastic Container Registry events

Amazon ECR sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon ECR service events

Amazon ECR sends the following events directly to EventBridge:

- ECR Image Action
- ECR Image Scan
- ECR Replication Action
- ECR Artifact Action
- ECR Referrer Action
- ECR Scan Resource Change
- ECR Pull Through Cache Action

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.ecr

```
{
  "source": ["aws.ecr"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.ecr"],
  "detail-type": ["`ECR Image Action`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Amazon ECR events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon ECR to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.ecr
- `eventSource`: ecr.amazonaws.com

```
{
  "source": ["aws.ecr"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ecr.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ecr"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ecr.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
