The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Notifications for the AWS Partner Central Account API

Partner Account Connection notifications enable partners to stay informed about connection lifecycle events that directly impact their business relationships and operational workflows. These events are critical for partners to:

- React promptly to new collaboration
- Maintain awareness of their connection portfolio status
- Take appropriate action when connections are established or terminated
- Ensure business continuity by knowing when relationships change

###### Topics

- [Complete the prerequisite to monitor events](#events-prerequites "#events-prerequites")
- [Configure Amazon EventBridge to monitor events](#eventbridge-setup "#eventbridge-setup")
- [Learn more about account connections API events](#learn-about-events "#learn-about-events")

## Complete the prerequisite to monitor events

Users require the appropriate IAM permissions to access and manage events published by
the account connections API. For more information about the available actions, resources, and
condition keys for EventBridge, see [Using IAM policy conditions in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-use-conditions.md#events-pattern-detail-type "../../../eventbridge/latest/userguide/eb-use-conditions.md#events-pattern-detail-type") in the _Amazon EventBridge User
Guide_. One of the condition keys is `events:detail-type`,
which can be used to scope permissions to specific event types.

The following example policy demonstrates how to customize and scope the permissions
for the proposed events. The `AllowPutRuleForPartnercentralAccountEvents`
statement allows the creation of rules, but only for events from the
`aws.partnercentral-account` source.

For detailed IAM policy examples, refer to the AWS documentation on EventBridge permissions.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowPutRuleForPartnerCentralAccountEvents",
      "Effect": "Allow",
      "Action": "events:PutRule",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "events:source": "aws.partnercentral-account.connection"
        }
      }
    }
  ]
}
```

## Configure Amazon EventBridge to monitor events

To monitor account connections API events, you create an EventBridge rule that matches the events that
you want to capture. You can use the AWS Management Console or the AWS SDKs to create and manage
rules. The following sections explain how to create rules using both methods. Regardless
of the method you use, you must create the rule in the US East (N. Virginia)
`us-east-1` Region.

### AWS Management Console setup

To set up an EventBridge rule using the AWS Management Console, follow the steps in [Creating rules that react to events in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the
_Amazon EventBridge User Guide_. When creating the rule, you must set
the event bus to **default**, and create the rule in the
US East (N. Virginia) `us-east-1` Region.

Following is an example of an event rule:

```
{
    "source": ["aws.partnercentral-account"],
    "detail": {
        "catalog": ["AWS"]
    }
}
```

### AWS SDK setup

You can use the AWS SDKs to create and manage EventBridge rules programmatically. For
more information, see [PutRule](../../../eventbridge/latest/APIReference/API_PutRule.md "../../../eventbridge/latest/APIReference/API_PutRule.md") in the
_Amazon EventBridge API Reference_.

The following example uses the AWS SDK for Python (Boto3):

```
import boto3

client = boto3.client('events', region_name='us-east-1')

response = client.put_rule(
    Name='MyConnectionInvitationReceivedRule',
    EventPattern=
    '{
        "source": ["aws.partnercentral-account"],
        "detail-type": ["Partner Connection Invitation Received"],
        "detail": {"catalog": ["AWS"]}
    }',
    State='ENABLED'
)
print('Rule ARN:', response['RuleArn'])
```

## Learn more about account connections API events

The following sections describe the account connections API event types, scenarios that trigger
them, and event examples.

### Event types

Following are the event types and their triggers.

- [Partner Connection Invitation Received](#connection-invitation-received "#connection-invitation-received"): Notifies the receiver that another partner wants to establish a connection
- [Partner Connection Invitation Accepted](#connection-invitation-accepted "#connection-invitation-accepted"): Notifies the sender that their invitation was accepted and a connection is now active
- [Partner Connection Invitation Rejected](#connection-invitation-rejected "#connection-invitation-rejected"): Notifies the sender that their invitation was declined
- [Partner Connection Cancelled](#connection-cancelled "#connection-cancelled"): Notifies the other connected participant when an active connection is terminated
- [Partner Connection Invitation Cancelled](#connection-invitation-cancelled "#connection-invitation-cancelled"): Notifies the receiver that the sender has withdrawn their invitation before any action was taken
- [Partner Connection Invitation Expired](#connection-invitation-expired "#connection-invitation-expired"): Notifies both sender and receiver that the invitation has expired

### Example events

The following sections provide examples of the events listed earlier in the
previous section.

###### Topics

- [Partner Connection Invitation Received](#connection-invitation-received "#connection-invitation-received")
- [Partner Connection Invitation Accepted](#connection-invitation-accepted "#connection-invitation-accepted")
- [Partner Connection Invitation Rejected](#connection-invitation-rejected "#connection-invitation-rejected")
- [Partner Connection Cancelled](#connection-cancelled "#connection-cancelled")
- [Partner Connection Invitation Cancelled](#connection-invitation-cancelled "#connection-invitation-cancelled")
- [Partner Connection Invitation Expired](#connection-invitation-expired "#connection-invitation-expired")

#### Partner Connection Invitation Received

##### Triggering Context

This event is generated when a connection invitation is successfully created and persisted in PAC's data store via the CreateConnectionInvitation API. The event is sent immediately after the invitation creation completes successfully and is persisted in PAC's data store, not just when the API call is made.

The event will be automatically sent when a new connection invitation is created. One event per invitation created with no duplicate events for the same invitation.

##### Recipients

The AWS account of the receiver in the connection invitation.

##### Expected handling

Typical Customer Actions:

- Immediate Notification: Trigger alerts to business teams about new partnership opportunities
- Workflow Automation: Automatically update partner management systems with pending invitations
- Decision Support: Route invitations to appropriate decision makers based on connection type
- Audit Logging: Record invitation receipt for compliance and partnership tracking
- Response Automation: For trusted partners, potentially auto-accept certain invitation types

Common Integration Patterns:

- Lambda function → Update partner portal dashboard
- SQS queue → Batch process invitations for review
- SNS topic → Email/Slack notifications to business teams
- API destination → Webhook to external CRM/partner management systems

##### Example

```
{
  "version": "1",
  "id": "<event id>",
  "detail-type": "Partner Connection Invitation Received",
  "source": "aws.partnercentral-account",
  "time": "<ISO 8601 date time>",
  "region": "us-east-1",
  "account": "<corresponding partner AWS account>",
  "resources": [ "<<Connection Invitation ARN>>" ],
  "detail": {
    "catalog": "AWS",
    "connectionInvitation" :{
        "arn": "<<Connection Invitation ARN>>",
        "id": "pacinv-****",
        "connectionType": "OpportunityCollaboration",
        "inviterEmail": "abc@def.com",
        "invitationMessage": "We'd like to collaborate on a joint solution for cloud security. Please accept this connection invitation to proceed.",
        "senderCompanyName": "<<Sender Partner Account Name>>",
        "senderProfileId": "pprofile-****",
        "expiresAt": "<ISO 8601 date time>"
    }
  }
}
```

#### Partner Connection Invitation Accepted

##### Triggering Context

This event is generated when a connection invitation is successfully accepted and a connection is created and persisted in PAC's data store via the AcceptConnectionInvitation API. The event is sent immediately after the invitation acceptance completes successfully and the connection is established.

The event will be automatically sent when a connection invitation is accepted. One event per invitation accepted with no duplicate events for the same acceptance.

##### Recipients

Both AWS accounts involved in the connection invitation: the sender account that originally sent the invitation and the receiver account that accepted the invitation.

##### Expected handling

Typical Customer Actions:

- Partnership Activation: Trigger workflows to enable Layer 2 business activities
- Status Updates: Update partner management systems with active connection status
- Notification: Alert business teams about successful partnership establishment
- Access Provisioning: Automatically grant appropriate permissions for collaboration
- Analytics: Track partnership conversion rates and success metrics

Common Integration Patterns:

- Lambda function → Enable data sharing permissions and update partner portal
- SQS queue → Batch process connection activations for business setup
- SNS topic → Email/Slack notifications to business and technical teams
- API destination → Webhook to CRM systems to update partnership status

##### Example

```
{
  "version": "1",
  "id": "<event id>",
  "detail-type":  "Partner Connection Invitation Accepted",
  "source": "aws.partnercentral-account",
  "time": "<ISO 8601 date time>",
  "region": "us-east-1",
  "resources": [ "<<Connection Invitation ARN>>" , "<<Connection ARN>>" ],
  "account": "<corresponding partner AWS account>",
  "detail": {
    "catalog": "AWS",
    "connectionInvitation" :{
        "arn": "<<Connection Invitation ARN>>",
        "id": "pacinv-****",
        "connectionType": "OpportunityCollaboration"
    },
    "connection": {
        "arn": "<<Connection ARN>>",
         "id": "pac-*****",
         "Participant1AccountId": "<<Sender AWS AccountId>>",
         "Participant2AccountId": "<<Receiver AWS AccountId>>",
         "status": "ACTIVE"
     }
  }
}
```

#### Partner Connection Invitation Rejected

##### Triggering Context

This event is generated when a connection invitation is successfully rejected via the RejectConnectionInvitation API. The event is sent immediately after the invitation rejection is processed and persisted in PAC's data store.

The event will be automatically sent when a connection invitation is rejected. One event per invitation rejected with no duplicate events for the same rejection.

##### Recipients

The AWS account that originally sent the connection invitation (the sender account).

##### Expected handling

Typical Customer Actions:

- Status Updates: Update partner management systems with rejection status
- Follow-up Actions: Trigger workflows for alternative partnership approaches
- Notification: Alert business teams about partnership decision
- Cleanup: Remove pending invitation references from internal systems

Common Integration Patterns:

- Lambda function → Update partner portal and trigger follow-up workflows
- SQS queue → Batch process rejections for business analysis
- SNS topic → Email/Slack notifications to business development teams
- API destination → Webhook to CRM systems to update opportunity status

##### Example

```
{
  "version": "1",
  "id": "<event id>",
  "detail-type": "Partner Connection Invitation Rejected",
  "source": "aws.partnercentral-account",
  "time": "<ISO 8601 date time>",
  "region": "us-east-1",
  "account": "<corresponding partner AWS account>",
  "resources": [ "<<Connection Invitation ARN>>" ],
  "detail": {
    "catalog": "AWS",
    "connectionInvitation" :{
        "arn": "<<Connection Invitation ARN>>",
        "id": "pacinv-****",
        "connectionType": "OpportunityCollaboration",
        "invitationMessage": "We'd like to collaborate on a joint solution for cloud security. Please accept this connection invitation to proceed.",
        "receiverProfileId": "pprofile-****"
    }
  }
}
```

#### Partner Connection Cancelled

##### Triggering Context

This event is generated when an active connection is successfully cancelled and the active status is updated to terminated in PAC's data store via the CancelConnection API. The event is sent immediately after the connection cancellation is processed and the connection status is updated.

The event will be automatically sent when a connection is terminated. One event per connection cancelled with no duplicate events for the same cancellation.

##### Recipients

The AWS account of the other participant in the connection (not the one who initiated cancellation).

##### Expected handling

Typical Customer Actions:

- Access Revocation: Immediately revoke permissions and disable data sharing
- Status Updates: Update partner management systems with terminated connection status
- Notification: Alert business and technical teams about partnership termination
- Cleanup: Remove connection references and clean up shared resources
- Analytics: Track connection duration and termination patterns

Common Integration Patterns:

- Lambda function → Revoke permissions and update partner portal status
- SQS queue → Batch process connection terminations for cleanup workflows
- SNS topic → Email/Slack notifications to business and technical teams
- API destination → Webhook to CRM systems to update partnership status

##### Example

```
{
  "version": "1",
  "id": "<event id>",
  "detail-type": "Partner Connection Cancelled",
  "source": "aws.partnercentral-account",
  "time": "<ISO 8601 date time>",
  "region": "us-east-1",
  "resources": [ "<<Connection ARN>>" ],
  "account": "<corresponding partner AWS account>",
  "detail": {
    "catalog": "AWS",
    "connection" :{
        "arn": "<<Connection Invitation ARN>>",
        "id": "pac-****",
        "connectionType": "OpportunityCollaboration",
        "canceledBy": "<<AWS account ID>>"
    }
  }
}
```

#### Partner Connection Invitation Cancelled

##### Triggering Context

This event is generated when a pending connection invitation is successfully cancelled via the CancelConnectionInvitation API. The event is sent immediately after the invitation cancellation is processed and the invitation status is updated to CANCELED.

The event will be automatically sent when a connection invitation is canceled. One event per connection invitation cancelled with no duplicate events for the same cancellation.

##### Recipients

The AWS account that was supposed to receive the connection invitation (the receiver account).

##### Expected handling

Typical Customer Actions:

- Status Updates: Update partner management systems to remove pending invitation references
- Notification: Alert business teams that a potential partnership opportunity was withdrawn
- Cleanup: Remove invitation references from internal tracking systems
- Analytics: Track invitation cancellation patterns for partnership insights

Common Integration Patterns:

- Lambda function → Update partner portal and remove pending invitation notifications
- SQS queue → Batch process cancellations for business analysis
- SNS topic → Email/Slack notifications to business development teams
- API destination → Webhook to CRM systems to update opportunity status

##### Example

```
{
  "version": "1",
  "id": "<event id>",
  "detail-type": "Partner Connection Invitation Cancelled",
  "source": "aws.partnercentral-account",
  "time": "<ISO 8601 date time>",
  "region": "us-east-1",
  "account": "<corresponding partner AWS account>",
  "resources": [ "<<Connection Invitation ARN>>" ],
  "detail": {
    "catalog": "AWS",
    "connectionInvitation" :{
        "arn": "<<Connection Invitation ARN>>",
        "id": "pacinv-****",
        "connectionType": "OpportunityCollaboration",
        "invitationMessage": "We'd like to collaborate on a joint solution for cloud security. Please accept this connection invitation to proceed.",
        "senderProfileId": "pprofile-****"
    }
  }
}
```

#### Partner Connection Invitation Expired

##### Triggering Context

This event is generated when a pending connection invitation automatically expires after reaching its ExpiresAt timestamp without being accepted or rejected by the receiver. The event is automatically triggered by the system when the invitation expiration time is reached.

The event will be automatically sent when a connection invitation expires. One event per invitation expired with no duplicate events for the same expiration.

##### Recipients

Both AWS accounts involved in the connection invitation: the sender account that originally sent the invitation and the receiver account that received the invitation.

##### Expected handling

Typical Customer Actions:

- Status Updates: Update partner management systems to mark invitation as expired
- Follow-up Actions: Trigger workflows for re-engagement or alternative partnership approaches
- Notification: Alert business teams about missed partnership opportunities
- Cleanup: Remove expired invitation references from internal tracking systems

Common Integration Patterns:

- Lambda function → Update partner portal and trigger follow-up workflows
- SQS queue → Batch process expirations for business analysis
- SNS topic → Email/Slack notifications to business development teams
- API destination → Webhook to CRM systems to update opportunity status

##### Example

```
{
  "version": "1",
  "id": "<event id>",
  "detail-type": "Partner Connection Invitation Expired",
  "source": "aws.partnercentral-account",
  "time": "<ISO 8601 date time>",
  "region": "us-east-1",
  "resources": [ "<<Connection Invitation ARN>>" ],
  "detail": {
    "catalog": "AWS",
    "connectionInvitation": {
        "arn": "<<Connection Invitation ARN>>",
        "id": "pacinv-****",
        "connectionType": "OpportunityCollaboration",
        "inviterEmail": "abc@def.com",
        "invitationMessage": "We'd like to collaborate on a joint solution for cloud security. Please accept this connection invitation to proceed.",
        "senderProfileId": "pprofile-****",
        "receiverProfileId": "pprofile-****"
    }
  }
}
```
