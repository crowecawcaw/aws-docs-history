# Amazon EC2 Systems Manager events

SSM sends service events directly to EventBridge, as well as via AWS CloudTrail.

## SSM service events

SSM sends the following events directly to EventBridge:

- EC2 Command Status-change Notification
- EC2 Command Invocation Status-change Notification
- EC2 State Manager Association State Change
- EC2 State Manager Instance Association State Change
- Parameter Store Change
- Parameter Store Policy Action
- EC2 Automation Step Status-change Notification
- EC2 Automation Execution Status-change Notification
- Impact Assessment Created
- Approver Access Request Status Update
- Requester Access Request Status Update
- JITNA Access Request Failed
- OpsItem Create
- OpsItem Update
- Change Request Status Update
- Maintenance Window State-change Notification
- Maintenance Window Execution State-change Notification
- Maintenance Window Task Execution State-change Notification
- Maintenance Window Target Registration Notification
- Maintenance Window Task Target Invocation State-change Notification
- Maintenance Window Task Registration Notification
- Configuration Compliance State Change
- Inventory Resource State Change
- Calendar State Change
- SSM Managed Instance Deregistration
- SSM Managed Instance Registration
- SSM Managed Instance Public Key Update
- Change Request Template Document Review Status Update
- Document Review Status Update

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.ssm

```
{
  "source": ["aws.ssm"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.ssm"],
  "detail-type": ["`EC2 Command Status-change Notification`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## SSM events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from SSM to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.ssm
- `eventSource`: ssm.amazonaws.com

```
{
  "source": ["aws.ssm"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ssm.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ssm"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ssm.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
