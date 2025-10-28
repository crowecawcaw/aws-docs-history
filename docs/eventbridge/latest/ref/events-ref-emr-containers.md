# Amazon EMR Containers events

Amazon EMR Containers sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon EMR Containers service events

Amazon EMR Containers sends the following events directly to EventBridge:

- EmrContainers Job Run State Change
- EMR Job Run State Change
- EMR Job Run New Driver Attempt

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.emr-containers

```
{
  "source": ["aws.emr-containers"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.emr-containers"],
  "detail-type": ["`EmrContainers Job Run State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Amazon EMR Containers events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon EMR Containers to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.emr-containers
- `eventSource`: emr-containers.amazonaws.com

```
{
  "source": ["aws.emr-containers"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["emr-containers.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.emr-containers"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["emr-containers.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
