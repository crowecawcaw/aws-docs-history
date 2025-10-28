# Amazon Simple Storage Service events

Amazon S3 sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon S3 service events

Amazon S3 sends the following events directly to EventBridge:

- Async Copy Completion
- Object Created
- Object Deleted
- Object Restore Initiated
- Object Restore Completed
- Object Restore Expired
- Object Tags Added
- Object Tags Deleted
- Object ACL Updated
- Object Storage Class Changed
- Object Access Tier Changed

_Delivery type_:
[Durable](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.s3

```
{
  "source": ["aws.s3"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.s3"],
  "detail-type": ["`Async Copy Completion`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Amazon S3 events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon S3 to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.s3
- `eventSource`: s3.amazonaws.com

```
{
  "source": ["aws.s3"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["s3.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.s3"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["s3.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
