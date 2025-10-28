# Amazon Elastic Kubernetes Service events

Amazon EKS sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon EKS service events

Amazon EKS sends the following events directly to EventBridge:

- EKS Fargate Pod Scheduled Termination
- EKS Addon Creation Failed
- EKS Addon Creation Succeeded
- EKS Addon Update Failed
- EKS Addon Update Succeeded
- EKS Addon Deletion Failed
- EKS Addon Deletion Succeeded
- EKS Addon Health Degraded
- EKS Addon Health Restored

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.eks

```
{
  "source": ["aws.eks"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.eks"],
  "detail-type": ["`EKS Fargate Pod Scheduled Termination`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Amazon EKS events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon EKS to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.eks
- `eventSource`: eks.amazonaws.com

```
{
  "source": ["aws.eks"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["eks.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.eks"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["eks.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
