

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Notifications for the AWS Partner Central Account API

Partner Account Connection notifications enable partners to stay informed about connection lifecycle events that directly impact their business relationships and operational workflows. These events are critical for partners to:
+ React promptly to new collaboration
+ Maintain awareness of their connection portfolio status
+ Take appropriate action when connections are established or terminated
+ Ensure business continuity by knowing when relationships change

Use business plan notifications to know when a plan's status changes, a submission task finishes, or a plan or item date is 30 days away. You can then update your own systems without polling the business plan API operations.

**Topics**
+ [Complete the prerequisite to monitor events](#events-prerequites)
+ [Configure Amazon EventBridge to monitor events](#eventbridge-setup)
+ [Account API events](#learn-about-events)

## Complete the prerequisite to monitor events
<a name="events-prerequites"></a>

Users require the appropriate IAM permissions to access and manage events published by the account connections API. For more information about the available actions, resources, and condition keys for EventBridge, see [Using IAM policy conditions in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-use-conditions.html#events-pattern-detail-type) in the *Amazon EventBridge User Guide*. One of the condition keys is `events:detail-type`, which can be used to scope permissions to specific event types.

The following example policy demonstrates how to customize and scope the permissions for the proposed events. The `AllowPutRuleForPartnercentralAccountEvents` statement allows the creation of rules, but only for events from the `aws.partnercentral-account` source. 

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
          "events:source": "aws.partnercentral-account"
        }
      }
    }
  ]
}
```

Business plan events use the same `aws.partnercentral-account` source, so this policy also covers rules for business plan events.

## Configure Amazon EventBridge to monitor events
<a name="eventbridge-setup"></a>

To monitor Account API events, including business plan events, you create an EventBridge rule that matches the events that you want to capture. You can use the AWS Management Console or the AWS SDKs to create and manage rules. The following sections explain how to create rules using both methods. Regardless of the method you use, you must create the rule in the US East (N. Virginia) `us-east-1` Region.

### AWS Management Console setup
<a name="eventbridge-console-setup"></a>

To set up an EventBridge rule using the AWS Management Console, follow the steps in [Creating rules that react to events in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) in the *Amazon EventBridge User Guide*. When creating the rule, you must set the event bus to **default**, and create the rule in the US East (N. Virginia) `us-east-1` Region.

Following is an example of an event rule:

```json
{
    "source": ["aws.partnercentral-account"],
    "detail": {
        "catalog": ["AWS"]
    }
}
```

Business plan events share the `aws.partnercentral-account` source with the account connection events. To match only business plan events, add a `prefix` match on `detail-type`, as in the following example. To match events from the Sandbox catalog, replace `AWS` with `Sandbox`.

```json
{
    "source": ["aws.partnercentral-account"],
    "detail-type": [{"prefix": "Business Plan"}],
    "detail": {
        "catalog": ["AWS"]
    }
}
```

### AWS SDK setup
<a name="eventbridge-sdk-setup"></a>

You can use the AWS SDKs to create and manage EventBridge rules programmatically. For more information, see [PutRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutRule.html) in the *Amazon EventBridge API Reference*.

The following example uses the AWS SDK for Python (Boto3):

```python
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

To create a rule for a business plan event, set `detail-type` in `EventPattern` to that event, such as `Business Plan Submission Task Succeeded`.

## Account API events
<a name="learn-about-events"></a>

The following sections describe the Account API event types, the scenarios that trigger them, the fields in business plan events, and event examples.

### Event types
<a name="types-of-events"></a>

The Account API publishes events for two resources: partner connections and business plans.

#### Partner connection events
<a name="account-connection-event-types"></a>

Partner connection events notify the sender or the receiver of a connection invitation when the invitation or the connection changes.
+ [Partner Connection Invitation Received](#connection-invitation-received) – Notifies the receiver that another partner wants to establish a connection.
+ [Partner Connection Invitation Accepted](#connection-invitation-accepted) – Notifies the sender that their invitation was accepted and a connection is now active.
+ [Partner Connection Invitation Rejected](#connection-invitation-rejected) – Notifies the sender that their invitation was declined.
+ [Partner Connection Cancelled](#connection-cancelled) – Notifies the other connected participant when an active connection is terminated.
+ [Partner Connection Invitation Cancelled](#connection-invitation-cancelled) – Notifies the receiver that the sender has withdrawn their invitation before any action was taken.
+ [Partner Connection Invitation Expired](#connection-invitation-expired) – Notifies both sender and receiver that the invitation has expired.

#### Business plan events
<a name="account-business-plan-event-types"></a>

Business plan events notify the AWS account that owns the business plan when the plan or one of its tasks changes status, or when a date in the plan is 30 days away.
+ [Business Plan Activated](#business-plan-activated) – The status of a business plan changes to `ACTIVE`.
+ [Business Plan Completed](#business-plan-completed) – The status of a business plan changes to `COMPLETED`.
+ [Business Plan Canceled](#business-plan-canceled) – The status of a business plan changes to `CANCELED`.
+ [Business Plan Submission Task Succeeded](#business-plan-submission-task-succeeded) – The status of a business plan submission task changes to `SUCCEEDED`.
+ [Business Plan Submission Task Failed](#business-plan-submission-task-failed) – The status of a business plan submission task changes to `FAILED`.
+ [Business Plan Ending In 30 Days](#business-plan-ending-in-30-days) – The end date of an `ACTIVE` business plan is 30 days away.
+ [Business Plan Item Due In 30 Days](#business-plan-item-due-in-30-days) – The due date of an open item in an `ACTIVE` business plan is 30 days away.

Other status changes, such as a plan moving to `IN_REVIEW` or back to `DRAFT`, publish no event. A submission task that you cancel with `CancelBusinessPlanSubmissionTask` also publishes no event.

### Plan event fields
<a name="business-plan-event-fields"></a>

Every business plan event has the standard EventBridge envelope. The `account` field is the AWS account that owns the business plan, and `resources` holds the business plan ARN. The `time` field is when the change happened. On the two 30-day events, it is when AWS found the date that is 30 days away.

The `detail` object carries identifiers, names, statuses, and dates only. It never carries the content of a business plan. To read anything else, call the business plan API operations, such as `GetBusinessPlan`, `GetBusinessPlanItem`, and `GetBusinessPlanSubmissionTask`.

The following table lists each field in the `detail` object, the events that include it, and what it contains.


| Field | Present on | Description | 
| --- | --- | --- | 
| catalog | All events | The catalog of the business plan: AWS or Sandbox. | 
| schemaVersion | All events | The version of the detail object. The current version is 1. | 
| businessPlan.arn | All events | The ARN of the business plan. | 
| businessPlan.id | All events | The ID of the business plan. | 
| businessPlan.name | All events | The name of the business plan. | 
| businessPlan.status | All events | The status of the business plan after the change. On the two 30-day events, the current status of the plan, which is always ACTIVE. | 
| businessPlan.endDate | Business Plan Ending In 30 Days | The end date of the business plan, in UTC. | 
| businessPlan.businessPlanItem.id | Business Plan Item Due In 30 Days | The ID of the business plan item. | 
| businessPlan.businessPlanItem.type | Business Plan Item Due In 30 Days | The type of the item, such as INITIATIVE. | 
| businessPlan.businessPlanItem.name | Business Plan Item Due In 30 Days | The name of the item. Not present when the item has no name. | 
| businessPlan.businessPlanItem.dueDate | Business Plan Item Due In 30 Days | The due date of the item, in UTC. | 
| submissionTask.taskId | Submission task events | The ID of the submission task. This is the TaskId that StartBusinessPlanSubmissionTask returns. | 
| submissionTask.startedAt | Submission task events | When the submission task started. | 
| submissionTask.endedAt | Submission task events | When the submission task finished. | 
| submissionTask.changedBy | Submission task events | Who decided the submission. The value is always AWS. | 

You might receive an event more than once, and events might arrive out of order. To detect a duplicate, compare the `resources`, `detail-type`, and `time` fields. Items of the same plan that are due on the same day send Business Plan Item Due In 30 Days events with the same values in these fields, so for that event also compare `businessPlan.businessPlanItem.id`. To get the current state of a business plan, call `GetBusinessPlan`.

### Example events
<a name="example-rules"></a>

The following sections provide examples of the events listed earlier in the previous section.

**Topics**
+ [Partner Connection Invitation Received](#connection-invitation-received)
+ [Partner Connection Invitation Accepted](#connection-invitation-accepted)
+ [Partner Connection Invitation Rejected](#connection-invitation-rejected)
+ [Partner Connection Cancelled](#connection-cancelled)
+ [Partner Connection Invitation Cancelled](#connection-invitation-cancelled)
+ [Partner Connection Invitation Expired](#connection-invitation-expired)
+ [Business Plan Activated](#business-plan-activated)
+ [Business Plan Completed](#business-plan-completed)
+ [Business Plan Canceled](#business-plan-canceled)
+ [Business Plan Submission Task Succeeded](#business-plan-submission-task-succeeded)
+ [Business Plan Submission Task Failed](#business-plan-submission-task-failed)
+ [Business Plan Ending In 30 Days](#business-plan-ending-in-30-days)
+ [Business Plan Item Due In 30 Days](#business-plan-item-due-in-30-days)

#### Partner Connection Invitation Received
<a name="connection-invitation-received"></a>

##### Triggering Context
<a name="connection-invitation-received-context"></a>

This event is generated when a connection invitation is successfully created and persisted in PAC's data store via the CreateConnectionInvitation API. The event is sent immediately after the invitation creation completes successfully and is persisted in PAC's data store, not just when the API call is made.

The event will be automatically sent when a new connection invitation is created. One event per invitation created with no duplicate events for the same invitation.

##### Recipients
<a name="connection-invitation-received-recipients"></a>

The AWS account of the receiver in the connection invitation.

##### Expected handling
<a name="connection-invitation-received-handling"></a>

Typical Customer Actions:
+ Immediate Notification: Trigger alerts to business teams about new partnership opportunities
+ Workflow Automation: Automatically update partner management systems with pending invitations
+ Decision Support: Route invitations to appropriate decision makers based on connection type
+ Audit Logging: Record invitation receipt for compliance and partnership tracking
+ Response Automation: For trusted partners, potentially auto-accept certain invitation types

Common Integration Patterns:
+ Lambda function → Update partner portal dashboard
+ SQS queue → Batch process invitations for review
+ SNS topic → Email/Slack notifications to business teams
+ API destination → Webhook to external CRM/partner management systems

##### Example
<a name="connection-invitation-received-example"></a>

```json
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
<a name="connection-invitation-accepted"></a>

##### Triggering Context
<a name="connection-invitation-accepted-context"></a>

This event is generated when a connection invitation is successfully accepted and a connection is created and persisted in PAC's data store via the AcceptConnectionInvitation API. The event is sent immediately after the invitation acceptance completes successfully and the connection is established.

The event will be automatically sent when a connection invitation is accepted. One event per invitation accepted with no duplicate events for the same acceptance.

##### Recipients
<a name="connection-invitation-accepted-recipients"></a>

Both AWS accounts involved in the connection invitation: the sender account that originally sent the invitation and the receiver account that accepted the invitation.

##### Expected handling
<a name="connection-invitation-accepted-handling"></a>

Typical Customer Actions:
+ Partnership Activation: Trigger workflows to enable Layer 2 business activities
+ Status Updates: Update partner management systems with active connection status
+ Notification: Alert business teams about successful partnership establishment
+ Access Provisioning: Automatically grant appropriate permissions for collaboration
+ Analytics: Track partnership conversion rates and success metrics

Common Integration Patterns:
+ Lambda function → Enable data sharing permissions and update partner portal
+ SQS queue → Batch process connection activations for business setup
+ SNS topic → Email/Slack notifications to business and technical teams
+ API destination → Webhook to CRM systems to update partnership status

##### Example
<a name="connection-invitation-accepted-example"></a>

```json
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
<a name="connection-invitation-rejected"></a>

##### Triggering Context
<a name="connection-invitation-rejected-context"></a>

This event is generated when a connection invitation is successfully rejected via the RejectConnectionInvitation API. The event is sent immediately after the invitation rejection is processed and persisted in PAC's data store.

The event will be automatically sent when a connection invitation is rejected. One event per invitation rejected with no duplicate events for the same rejection.

##### Recipients
<a name="connection-invitation-rejected-recipients"></a>

The AWS account that originally sent the connection invitation (the sender account).

##### Expected handling
<a name="connection-invitation-rejected-handling"></a>

Typical Customer Actions:
+ Status Updates: Update partner management systems with rejection status
+ Follow-up Actions: Trigger workflows for alternative partnership approaches
+ Notification: Alert business teams about partnership decision
+ Cleanup: Remove pending invitation references from internal systems

Common Integration Patterns:
+ Lambda function → Update partner portal and trigger follow-up workflows
+ SQS queue → Batch process rejections for business analysis
+ SNS topic → Email/Slack notifications to business development teams
+ API destination → Webhook to CRM systems to update opportunity status

##### Example
<a name="connection-invitation-rejected-example"></a>

```json
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
<a name="connection-cancelled"></a>

##### Triggering Context
<a name="connection-cancelled-context"></a>

This event is generated when an active connection is successfully cancelled and the active status is updated to terminated in PAC's data store via the CancelConnection API. The event is sent immediately after the connection cancellation is processed and the connection status is updated.

The event will be automatically sent when a connection is terminated. One event per connection cancelled with no duplicate events for the same cancellation.

##### Recipients
<a name="connection-cancelled-recipients"></a>

The AWS account of the other participant in the connection (not the one who initiated cancellation).

##### Expected handling
<a name="connection-cancelled-handling"></a>

Typical Customer Actions:
+ Access Revocation: Immediately revoke permissions and disable data sharing
+ Status Updates: Update partner management systems with terminated connection status
+ Notification: Alert business and technical teams about partnership termination
+ Cleanup: Remove connection references and clean up shared resources
+ Analytics: Track connection duration and termination patterns

Common Integration Patterns:
+ Lambda function → Revoke permissions and update partner portal status
+ SQS queue → Batch process connection terminations for cleanup workflows
+ SNS topic → Email/Slack notifications to business and technical teams
+ API destination → Webhook to CRM systems to update partnership status

##### Example
<a name="connection-cancelled-example"></a>

```json
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
<a name="connection-invitation-cancelled"></a>

##### Triggering Context
<a name="connection-invitation-cancelled-context"></a>

This event is generated when a pending connection invitation is successfully cancelled via the CancelConnectionInvitation API. The event is sent immediately after the invitation cancellation is processed and the invitation status is updated to CANCELED.

The event will be automatically sent when a connection invitation is canceled. One event per connection invitation cancelled with no duplicate events for the same cancellation.

##### Recipients
<a name="connection-invitation-cancelled-recipients"></a>

The AWS account that was supposed to receive the connection invitation (the receiver account).

##### Expected handling
<a name="connection-invitation-cancelled-handling"></a>

Typical Customer Actions:
+ Status Updates: Update partner management systems to remove pending invitation references
+ Notification: Alert business teams that a potential partnership opportunity was withdrawn
+ Cleanup: Remove invitation references from internal tracking systems
+ Analytics: Track invitation cancellation patterns for partnership insights

Common Integration Patterns:
+ Lambda function → Update partner portal and remove pending invitation notifications
+ SQS queue → Batch process cancellations for business analysis
+ SNS topic → Email/Slack notifications to business development teams
+ API destination → Webhook to CRM systems to update opportunity status

##### Example
<a name="connection-invitation-cancelled-example"></a>

```json
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
<a name="connection-invitation-expired"></a>

##### Triggering Context
<a name="connection-invitation-expired-context"></a>

This event is generated when a pending connection invitation automatically expires after reaching its ExpiresAt timestamp without being accepted or rejected by the receiver. The event is automatically triggered by the system when the invitation expiration time is reached.

The event will be automatically sent when a connection invitation expires. One event per invitation expired with no duplicate events for the same expiration.

##### Recipients
<a name="connection-invitation-expired-recipients"></a>

Both AWS accounts involved in the connection invitation: the sender account that originally sent the invitation and the receiver account that received the invitation.

##### Expected handling
<a name="connection-invitation-expired-handling"></a>

Typical Customer Actions:
+ Status Updates: Update partner management systems to mark invitation as expired
+ Follow-up Actions: Trigger workflows for re-engagement or alternative partnership approaches
+ Notification: Alert business teams about missed partnership opportunities
+ Cleanup: Remove expired invitation references from internal tracking systems

Common Integration Patterns:
+ Lambda function → Update partner portal and trigger follow-up workflows
+ SQS queue → Batch process expirations for business analysis
+ SNS topic → Email/Slack notifications to business development teams
+ API destination → Webhook to CRM systems to update opportunity status

##### Example
<a name="connection-invitation-expired-example"></a>

```json
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

#### Business Plan Activated
<a name="business-plan-activated"></a>

##### Triggering Context
<a name="business-plan-activated-context"></a>

You receive this event after the status of a business plan changes to `ACTIVE` and the new status is stored. A plan becomes `ACTIVE` when AWS approves its submission, so you also get the [Business Plan Submission Task Succeeded](#business-plan-submission-task-succeeded) event, described later on this page. These two events can arrive in either order.

Only AWS changes the status of a plan to `ACTIVE`. You can't change it directly. If an update doesn't change the status, you don't receive an event.

##### Recipients
<a name="business-plan-activated-recipients"></a>

The AWS account that owns the business plan.

##### Example – Business Plan Activated event
<a name="business-plan-activated-example"></a>

```json
{
  "version": "0",
  "id": "21234567-0123-0123-0123-EXAMPLE1111a",
  "detail-type": "Business Plan Activated",
  "source": "aws.partnercentral-account",
  "account": "111122223333",
  "time": "2026-11-04T16:42:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3"
  ],
  "detail": {
    "catalog": "AWS",
    "schemaVersion": "1",
    "businessPlan": {
      "arn": "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3",
      "id": "bp-7f8e9d0c1b2a3",
      "name": "2027 Joint Business Plan",
      "status": "ACTIVE"
    }
  }
}
```

For a description of each field in the `detail` object, see [Plan event fields](#business-plan-event-fields).

#### Business Plan Completed
<a name="business-plan-completed"></a>

##### Triggering Context
<a name="business-plan-completed-context"></a>

You receive this event after the status of a business plan changes to `COMPLETED` and the new status is stored. `COMPLETED` is a terminal status: the plan can no longer be changed.

Only AWS changes the status of a plan to `COMPLETED`, after the end date of an `ACTIVE` plan is reached. You can't change it directly. If an update doesn't change the status, you don't receive an event.

##### Recipients
<a name="business-plan-completed-recipients"></a>

The AWS account that owns the business plan.

##### Example – Business Plan Completed event
<a name="business-plan-completed-example"></a>

```json
{
  "version": "0",
  "id": "22234567-0123-0123-0123-EXAMPLE2222a",
  "detail-type": "Business Plan Completed",
  "source": "aws.partnercentral-account",
  "account": "111122223333",
  "time": "2027-12-31T00:05:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3"
  ],
  "detail": {
    "catalog": "AWS",
    "schemaVersion": "1",
    "businessPlan": {
      "arn": "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3",
      "id": "bp-7f8e9d0c1b2a3",
      "name": "2027 Joint Business Plan",
      "status": "COMPLETED"
    }
  }
}
```

For a description of each field in the `detail` object, see [Plan event fields](#business-plan-event-fields).

#### Business Plan Canceled
<a name="business-plan-canceled"></a>

##### Triggering Context
<a name="business-plan-canceled-context"></a>

You receive this event after the status of a business plan changes to `CANCELED` and the new status is stored. You receive this event whether you canceled the plan with `CancelBusinessPlan` or AWS canceled it on your behalf. `CANCELED` is a terminal status: the plan can no longer be changed.

If an update doesn't change the status, you don't receive an event.

##### Recipients
<a name="business-plan-canceled-recipients"></a>

The AWS account that owns the business plan.

##### Example – Business Plan Canceled event
<a name="business-plan-canceled-example"></a>

```json
{
  "version": "0",
  "id": "23234567-0123-0123-0123-EXAMPLE3333a",
  "detail-type": "Business Plan Canceled",
  "source": "aws.partnercentral-account",
  "account": "111122223333",
  "time": "2026-12-10T14:02:30Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3"
  ],
  "detail": {
    "catalog": "AWS",
    "schemaVersion": "1",
    "businessPlan": {
      "arn": "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3",
      "id": "bp-7f8e9d0c1b2a3",
      "name": "2027 Joint Business Plan",
      "status": "CANCELED"
    }
  }
}
```

For a description of each field in the `detail` object, see [Plan event fields](#business-plan-event-fields).

#### Business Plan Submission Task Succeeded
<a name="business-plan-submission-task-succeeded"></a>

##### Triggering Context
<a name="business-plan-submission-task-succeeded-context"></a>

You receive this event after a submission task that you started with `StartBusinessPlanSubmissionTask` reaches the `SUCCEEDED` status. During the review, the plan is `IN_REVIEW`. When AWS approves it, the plan becomes `ACTIVE`, so `businessPlan.status` is `ACTIVE`. You also receive the [Business Plan Activated](#business-plan-activated) event, described earlier on this page.

Each submission task sends at most one event.

##### Recipients
<a name="business-plan-submission-task-succeeded-recipients"></a>

The AWS account that owns the business plan.

##### Example – Business Plan Submission Task Succeeded event
<a name="business-plan-submission-task-succeeded-example"></a>

```json
{
  "version": "0",
  "id": "31234567-0123-0123-0123-EXAMPLE4444a",
  "detail-type": "Business Plan Submission Task Succeeded",
  "source": "aws.partnercentral-account",
  "account": "111122223333",
  "time": "2026-11-04T16:42:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3"
  ],
  "detail": {
    "catalog": "AWS",
    "schemaVersion": "1",
    "businessPlan": {
      "arn": "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3",
      "id": "bp-7f8e9d0c1b2a3",
      "name": "2027 Joint Business Plan",
      "status": "ACTIVE"
    },
    "submissionTask": {
      "taskId": "bptask-9a8b7c6d5e4f3",
      "startedAt": "2026-11-03T09:15:00Z",
      "endedAt": "2026-11-04T16:42:00Z",
      "changedBy": "AWS"
    }
  }
}
```

For a description of each field in the `detail` object, see [Plan event fields](#business-plan-event-fields).

#### Business Plan Submission Task Failed
<a name="business-plan-submission-task-failed"></a>

##### Triggering Context
<a name="business-plan-submission-task-failed-context"></a>

You receive this event after a submission task that you started with `StartBusinessPlanSubmissionTask` reaches the `FAILED` status. The plan returns from `IN_REVIEW` to `DRAFT` when AWS doesn't approve the submission, so `businessPlan.status` is `DRAFT`.

The event doesn't include the reason. To read it, call `GetBusinessPlanSubmissionTask` with the `submissionTask.taskId` from the event, and read `ErrorDetailList` in the response.

Each submission task sends at most one event.

##### Recipients
<a name="business-plan-submission-task-failed-recipients"></a>

The AWS account that owns the business plan.

##### Example – Business Plan Submission Task Failed event
<a name="business-plan-submission-task-failed-example"></a>

```json
{
  "version": "0",
  "id": "32234567-0123-0123-0123-EXAMPLE5555a",
  "detail-type": "Business Plan Submission Task Failed",
  "source": "aws.partnercentral-account",
  "account": "111122223333",
  "time": "2026-11-04T16:42:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3"
  ],
  "detail": {
    "catalog": "AWS",
    "schemaVersion": "1",
    "businessPlan": {
      "arn": "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3",
      "id": "bp-7f8e9d0c1b2a3",
      "name": "2027 Joint Business Plan",
      "status": "DRAFT"
    },
    "submissionTask": {
      "taskId": "bptask-9a8b7c6d5e4f3",
      "startedAt": "2026-11-03T09:15:00Z",
      "endedAt": "2026-11-04T16:42:00Z",
      "changedBy": "AWS"
    }
  }
}
```

For a description of each field in the `detail` object, see [Plan event fields](#business-plan-event-fields).

#### Business Plan Ending In 30 Days
<a name="business-plan-ending-in-30-days"></a>

##### Triggering Context
<a name="business-plan-ending-in-30-days-context"></a>

You receive this event when the end date of a business plan is 30 days away and the plan is `ACTIVE`. If the plan has any other status on that day, you don't receive the event. The event gives the end date in `businessPlan.endDate`.

##### Recipients
<a name="business-plan-ending-in-30-days-recipients"></a>

The AWS account that owns the business plan.

##### Example – Business Plan Ending In 30 Days event
<a name="business-plan-ending-in-30-days-example"></a>

```json
{
  "version": "0",
  "id": "41234567-0123-0123-0123-EXAMPLE1111a",
  "detail-type": "Business Plan Ending In 30 Days",
  "source": "aws.partnercentral-account",
  "account": "111122223333",
  "time": "2027-12-01T09:00:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3"
  ],
  "detail": {
    "catalog": "AWS",
    "schemaVersion": "1",
    "businessPlan": {
      "arn": "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3",
      "id": "bp-7f8e9d0c1b2a3",
      "name": "2027 Joint Business Plan",
      "status": "ACTIVE",
      "endDate": "2027-12-31T00:00:00Z"
    }
  }
}
```

For a description of each field in the `detail` object, see [Plan event fields](#business-plan-event-fields).

#### Business Plan Item Due In 30 Days
<a name="business-plan-item-due-in-30-days"></a>

##### Triggering Context
<a name="business-plan-item-due-in-30-days-context"></a>

You receive this event when the due date of a business plan item is 30 days away, the item is open, and its plan is `ACTIVE`. An open item has the status `NOT_STARTED`, `ON_TRACK`, or `AT_RISK`. If the item or the plan has any other status on that day, you don't receive the event.

Each item that is due sends its own event, and the event gives the due date in `businessPlan.businessPlanItem.dueDate`. To read the item, call `GetBusinessPlanItem` with the `businessPlan.businessPlanItem.id` from the event.

##### Recipients
<a name="business-plan-item-due-in-30-days-recipients"></a>

The AWS account that owns the business plan.

##### Example – Business Plan Item Due In 30 Days event
<a name="business-plan-item-due-in-30-days-example"></a>

```json
{
  "version": "0",
  "id": "42234567-0123-0123-0123-EXAMPLE2222b",
  "detail-type": "Business Plan Item Due In 30 Days",
  "source": "aws.partnercentral-account",
  "account": "111122223333",
  "time": "2027-05-31T09:00:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3"
  ],
  "detail": {
    "catalog": "AWS",
    "schemaVersion": "1",
    "businessPlan": {
      "arn": "arn:aws:partnercentral:us-east-1:111122223333:catalog/AWS/business-plan/bp-7f8e9d0c1b2a3",
      "id": "bp-7f8e9d0c1b2a3",
      "name": "2027 Joint Business Plan",
      "status": "ACTIVE",
      "businessPlanItem": {
        "id": "bpitem-4d5e6f7081924",
        "type": "INITIATIVE",
        "name": "AWS Co-Sell Revenue Growth Initiative",
        "dueDate": "2027-06-30T00:00:00Z"
      }
    }
  }
}
```

For a description of each field in the `detail` object, see [Plan event fields](#business-plan-event-fields).