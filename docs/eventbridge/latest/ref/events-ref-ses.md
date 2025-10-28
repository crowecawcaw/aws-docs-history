# Amazon Simple Email Service events

Amazon SES sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon SES service events

Amazon SES sends the following events directly to EventBridge:

- Advisor Recommendation Status Open
- Advisor Recommendation Status Resolved
- Sending Status Enabled
- Sending Status Disabled
- Email Delivered
- Email Bounced
- Email Complaint Received
- Email Rejected
- Email Sent
- Email Opened
- Email Rendering Failed
- Email Clicked
- Email Delivery Delayed
- Email Subscribed

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.ses

```
{
  "source": ["aws.ses"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.ses"],
  "detail-type": ["`Advisor Recommendation Status Open`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Amazon SES events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon SES to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.ses
- `eventSource`: ses.amazonaws.com

```
{
  "source": ["aws.ses"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ses.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ses"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ses.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
