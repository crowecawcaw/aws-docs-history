# User subscriptions in AWS License Manager events

User subscriptions in License Manager sends service events directly to EventBridge, as well as via AWS CloudTrail.

## User subscriptions in License Manager service events

User subscriptions in License Manager sends the following events directly to EventBridge:

- Identity Provider Registered
- Identity Provider Registration Failed
- Identity Provider Deregistered
- Identity Provider Deregistration Failed
- License Server Endpoint Healthy
- License Server Endpoint Unhealthy
- License Server Endpoint Provisioned
- License Server Endpoint Provisioning Failed
- License Server Endpoint Updated
- License Server Endpoint Update Failed
- License Server Endpoint Deleted
- License Server Endpoint Deletion Failed
- User Subscribed
- User Subscription Failed
- User Unsubscribed
- User Unsubscription Failed
- User Associated
- User Association Failed
- User Disassociated
- User Disassociation Failed
- Instance Activated
- Instance Activation Failed
- Instance Terminated
- Instance Unhealthy

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.license-manager-user-subscriptions

```
{
  "source": ["aws.license-manager-user-subscriptions"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.license-manager-user-subscriptions"],
  "detail-type": ["`Identity Provider Registered`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## User subscriptions in License Manager events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from User subscriptions in License Manager to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.license-manager-user-subscriptions
- `eventSource`: license-manager-user-subscriptions.amazonaws.com

```
{
  "source": ["aws.license-manager-user-subscriptions"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["license-manager-user-subscriptions.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.license-manager-user-subscriptions"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["license-manager-user-subscriptions.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
