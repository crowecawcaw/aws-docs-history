# Amazon EMR Serverless events

EMR Serverless sends service events directly to EventBridge, as well as via AWS CloudTrail.

## EMR Serverless service events

EMR Serverless sends the following events directly to EventBridge:

- EMR Serverless Application State Change
- EMR Serverless Job Run State Change
- EMR Serverless Job Run Retry
- EMR Serverless Job Resource Utilization Update

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.emr-serverless

```
{
  "source": ["aws.emr-serverless"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.emr-serverless"],
  "detail-type": ["`EMR Serverless Application State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## EMR Serverless events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from EMR Serverless to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.emr-serverless
- `eventSource`: emr-serverless.amazonaws.com

```
{
  "source": ["aws.emr-serverless"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["emr-serverless.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.emr-serverless"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["emr-serverless.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
