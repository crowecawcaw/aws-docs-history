# Amazon One Enterprise events

Amazon One Enterprise sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon One Enterprise service events

Amazon One Enterprise sends the following events directly to EventBridge:

- Device Health Status Changed To Healthy
- Device Health Status Changed To Critical
- Device Connectivity Changed To Online
- Device Connectivity Changed To Offline
- New Alert(s) Detected
- Some Alert(s) Cleared
- New Successful Enrollment
- New Successful Un-enrollment
- Unsuccessful Enrollment
- Unsuccessful Un-enrollment
- Successful Recognition
- Unsuccessful Recognition
- User Deleted
- User Created
- User Authenticated

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.one

```
{
  "source": ["aws.one"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.one"],
  "detail-type": ["`Device Health Status Changed To Healthy`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Amazon One Enterprise events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon One Enterprise to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.one
- `eventSource`: one.amazonaws.com

```
{
  "source": ["aws.one"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["one.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.one"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["one.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
