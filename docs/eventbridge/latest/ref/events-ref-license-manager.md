# AWS License Manager events

License Manager sends service events directly to EventBridge, as well as via AWS CloudTrail.

## License Manager service events

License Manager sends the following events directly to EventBridge:

- Grant Change
- License Change
- License Consumption Change
- License Token Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.license-manager

```
{
  "source": ["aws.license-manager"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.license-manager"],
  "detail-type": ["`Grant Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## License Manager events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from License Manager to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.license-manager
- `eventSource`: license-manager.amazonaws.com

```
{
  "source": ["aws.license-manager"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["license-manager.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.license-manager"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["license-manager.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
