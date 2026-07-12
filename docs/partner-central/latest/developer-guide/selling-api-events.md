The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Notifications for the AWS Partner Central Selling API

Events for the selling API provide real-time notifications about changes in the status or
the details of opportunities. These events help keep your systems in sync with AWS Partner Central,
and help ensure timely responses and updates.

###### Topics

- [Complete the prerequisite to monitor events](#events-prerequites "#events-prerequites")
- [Configure Amazon EventBridge to monitor events](#eventbridge-setup "#eventbridge-setup")
- [Learn more about selling API events](#learn-about-events "#learn-about-events")

## Complete the prerequisite to monitor events

Users require the appropriate IAM permissions to access and manage events published by
the Partner Central selling API. For more information about the available actions, resources, and
condition keys for EventBridge, see [Using IAM policy conditions in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-use-conditions.md#events-pattern-detail-type "../../../eventbridge/latest/userguide/eb-use-conditions.md#events-pattern-detail-type") in the _Amazon EventBridge User
Guide_. One of the condition keys is `events:detail-type`,
which can be used to scope permissions to specific event types.

The following example policy demonstrates how to customize and scope the permissions
for the proposed events. The `AllowPutRuleForPartnercentralSellingEvents`
statement allows the creation of rules, but only for events from the
`aws.partnercentral-selling` source.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "AllowPutRuleForPartnercentralSellingEvents",
 "Effect": "Allow",
 "Action": "events:PutRule",
 "Resource": "*",
 "Condition": {
 "ForAllValues:StringEquals": {
 "events:source": "aws.partnercentral-selling"
 }
 }
 }
}`

```

## Configure Amazon EventBridge to monitor events

To monitor selling API events, you create an EventBridge rule that matches the events that
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
    "source": ["aws.partnercentral-selling"],
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
    Name='MyOpportunityCreatedRule',
    EventPattern=
    '{
        "source": ["aws.partnercentral-selling"],
        "detail-type": ["Opportunity Created"],
        "detail": {"catalog": ["AWS"]}
    }',
    State='ENABLED'
)
print('Rule ARN:', response['RuleArn'])
```

## Learn more about selling API events

The following sections describe the selling API event types, scenarios that trigger
them, and event examples.

### Event types

Following are the event types and their triggers.

- [Opportunity Created](#opportunity-created "#opportunity-created"): Triggered
  when a new opportunity is created.
- [Opportunity Updated](#opportunity-updated "#opportunity-updated"): Triggered
  when an opportunity (Opportunity or its corresponding AWS Opportunity
  Summary) is updated.
- [Engagement Invitation
  Created](#engagement-invitation-created "#engagement-invitation-created"): Triggered when an AWS Referral invitation is
  created.
- [Engagement Invitation
  Accepted](#engagement-invitation-accepted "#engagement-invitation-accepted"): Triggered when a partner accepts an AWS Engagement
  Invitation, confirming their interest in collaborating with AWS on the
  opportunity.
- [Engagement Invitation
  Rejected](#engagement-invitation-rejected "#engagement-invitation-rejected"): Triggered when a partner rejects an AWS Engagement
  Invitation.
- [Engagement Invitation
  Expired](#engagement-invitation-expired "#engagement-invitation-expired"): This event is triggered when a Partner rejects an
  EngagementInvitation. It notifies the sending and receiving partner that the
  invitation has expired.
- [Engagement Member Added](#engagement-member-added "#engagement-member-added"):
  This event is triggered when a new member joins the Engagement after
  accepting an invitation. It notifies all current members of the Engagement
  about the new member being added to the Engagement.
- [Engagement Resource
  Snapshot Created](#engagement-resource-snapshot-created "#engagement-resource-snapshot-created"): This event is triggered when the new revision
  of the Snapshot of the resources (such as opportunities) associated with an
  Engagement is created. It notifies all the current members of the Engagement
  about the changes to the associated resource Snapshot.
- [Engagement Created](#engagement-created "#engagement-created"): Triggered
  when a new engagement is created.
- [Engagement Updated](#engagement-updated "#engagement-updated"): Triggered
  when an engagement is updated.

### Event scenarios

The following table describes how events operate under different scenarios. The
following assumptions are made for these scenarios:

- AWS is also a partner in these scenarios.
- `ResourceSnapshotJob` is configured correctly by the
  partner.
- The fields updated on the opportunity are also on the opportunity template
  for Resource Snapshot.

| **Action by you as a<br>partner**                                                                                         | **Events received**                                                                                                                                     | **Participant type** |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| You create an opportunity                                                                                                 | Opportunity Created                                                                                                                                     |                      |
| You use `StartEngagementFromOpportunityTask` to submit<br>an opportunity                                                  | Opportunity Updated, Engagement Created, Engagement Resource Snapshot Created,<br>Engagement Member Added, Engagement Invitation Created                |                      |
| AWS approves your submitted opportunity                                                                                   | Engagement Invitation Accepted, Engagement Member Added,<br>Opportunity Updated, Engagement Resource Snapshot Created                                   |                      |
| AWS rejects your submitted opportunity                                                                                    | Engagement Invitation Rejected, Opportunity Updated, Engagement<br>Resource Snapshot Created                                                            |                      |
| You associate an AWS Marketplace offer with an opportunity                                                                | Opportunity Updated                                                                                                                                     |                      |
| You associate a solution with an opportunity                                                                              | Opportunity Updated, Engagement Resource Snapshot Created                                                                                               |                      |
| You update an opportunity                                                                                                 | Opportunity Updated, Engagement Resource Snapshot Created<br>(Optional if `ResourceSnapshotJob` is set up and the<br>field updates are on the template) |                      |
| AWS updates your opportunity                                                                                              | Opportunity Updated, Engagement Resource Snapshot Created                                                                                               |                      |
| You invite another partner to an engagement                                                                               | Engagement Invitation Created                                                                                                                           | Sender               |
| Your invitation to join an engagement is accepted by a<br>partner                                                         | Engagement Invitation Accepted, Engagement Member Added                                                                                                 | Sender               |
| Your invitation to join an engagement is rejected by a<br>partner                                                         | Engagement Invitation Rejected                                                                                                                          | Sender               |
| Your invitation to join an engagement is not acted on by a<br>partner for 15 days                                         | Engagement Invitation Expired                                                                                                                           | Sender               |
| You receive an invitation from another partner to join an<br>engagement                                                   | Engagement Invitation Created                                                                                                                           | Receiver             |
| You accept the invitation from another partner to join an<br>engagement via<br>`StartEngagementByAcceptingInvitationTask` | Engagement Invitation Accepted, Engagement Member Added,<br>Opportunity Created, Opportunity Updated, Engagement Resource<br>Snapshot Created           | Receiver             |
| You reject the invitation to join an engagement from another<br>partner                                                   | Engagement Invitation Rejected                                                                                                                          | Receiver             |
| You do not act on invitation to join an engagement from another<br>partner for 15 days                                    | Engagement Invitation Expired                                                                                                                           | Receiver             |
| You create an engagement                                                                                                  | Engagement Created                                                                                                                                      | Sender               |
| You update an engagement                                                                                                  | Engagement Updated                                                                                                                                      | Sender, Receiver     |

### Example events

The following sections provide examples of the events listed earlier in the
previous section.

###### Topics

- [Opportunity Created](#opportunity-created "#opportunity-created")
- [Opportunity Updated](#opportunity-updated "#opportunity-updated")
- [Engagement Invitation Created](#engagement-invitation-created "#engagement-invitation-created")
- [Engagement Invitation Accepted](#engagement-invitation-accepted "#engagement-invitation-accepted")
- [Engagement Invitation Rejected](#engagement-invitation-rejected "#engagement-invitation-rejected")
- [Engagement Invitation Expired](#engagement-invitation-expired "#engagement-invitation-expired")
- [Engagement Member Added](#engagement-member-added "#engagement-member-added")
- [Engagement Resource Snapshot Created](#engagement-resource-snapshot-created "#engagement-resource-snapshot-created")
- [Engagement Created](#engagement-created "#engagement-created")
- [Engagement Updated](#engagement-updated "#engagement-updated")

#### Opportunity Created

Partners use this event to:

- Notify their users that a new Opportunity has been created.
- Trigger automated workflows such as updating CRM systems or notifying
  sales teams about new opportunity creations.

The following example shows a typical Opportunity Created event.

```
{
    "version": "1",
    "id": "01234567-0123-0123-0123-0123456789ab",
    "source": "aws.partnercentral-selling",
    "detail-type": "Opportunity Created",
    "time": "2023-04-16T15:23:45Z",
    "region": "us-east-1",
    "account": "123456789012",
    "detail": {
        "schemaVersion": "`<version number>`",
        "catalog": "`<Sandbox | AWS>`",
        "opportunity": {
            "identifier": "String"
        }
    }
}
```

#### Opportunity Updated

Partners use this event to:

- Notify their users that an existing Opportunity has been
  updated.
- Trigger automated workflows such as updating CRM systems or notifying
  sales teams.

The following example shows a typical Opportunity Updated event.

```
{
    "version": "1",
    "id": "01234567-0123-0123-0123-0123456789ab",
    "source": "aws.partnercentral-selling",
    "detail-type": "Opportunity Updated",
    "time": "2023-04-16T15:23:45Z",
    "region": "us-east-1",
    "account": "123456789012",
    "detail": {
        "schemaVersion": "`<version number>`",
        "catalog": "`<Sandbox | AWS>`",
        "opportunity": {
             "identifier": "String"
        }
    }
}
```

#### Engagement Invitation Created

Partners use this event to:

- Notify their users about the new EngagementInvitation they have
  received.
- Trigger automated workflows to accept or reject the invitation, such
  as updating CRM systems or notifying sales teams.

The following example shows a typical Engagement Invitation Created
event.

```
{
    "version": "0",
    "id": "01234567-0123-0123-0123-0123456789ab",
    "detail-type": "Engagement Invitation Created",
    "source": "aws.partnercentral-selling",
    "account": "123456789012",
    "time": "2023-04-15T12:34:56Z",
    "region": "us-east-1",
    "resources": [
      "arn:aws:partnercentral:us-east-1::catalog/AWS/engagement-invitation/engi-v7p8z56whnauo"
    ],
    "detail": {
      "catalog": "AWS",
      "engagementInvitation": {
        "arn": "arn:aws:partnercentral:us-east-1::catalog/AWS/engagement-invitation/engi-v7p8z56whnauo",
        "id": "engi-v7p8z56whnauo",
        "engagementId": "eng-12345678901234",
        "senderAccountId": "string",
        "receiverAccountId": "string",
        "senderCompanyName": "string",
        "expirationDate": "string",
        "participantType": "Enum", //Sender/Receiver
		"payloadType": "LeadInvitation" //OpportunityInvitation|LeadInvitation
      }
    }
}
```

#### Engagement Invitation Accepted

Partners use this event to:

- Notify their users that the EngagementInvitation has been
  accepted.
- Update their internal records to reflect the new partner in the
  Engagement.
- Trigger automated workflows to synchronize data or notify other team
  members about the new Engagement member.

The following example shows a typical Engagement Invitation Accepted
event.

```
{
    "version": "0",
    "id": "01234567-0123-0123-0123-0123456789ab",
    "detail-type": "Engagement Invitation Accepted",
    "source": "aws.partnercentral-selling",
    "account": "123456789012",
    "time": "2023-04-16T15:23:45Z",
    "region": "us-east-1",
    "resources": ["arn:aws:partnercentral:us-east-1::catalog/AWS/engagement-invitation/engi-v7p8z56whnauo"],
    "detail": {
        "catalog": "AWS",
        "engagementInvitation": {
            "arn": "arn:aws:partnercentral:us-east-1::catalog/AWS/engagement-invitation/engi-v7p8z56whnauo",
            "id": "engi-v7p8z56whnauo",
            "engagementId": "eng-12356whnauo",
            "participantType": "Enum", //Sender/Receiver
            "senderAccountId": "string",
            "receiverAccountId": "string",
            "payloadType": "LeadInvitation" //OpportunityInvitation|LeadInvitation
        }
    }
}
```

#### Engagement Invitation Rejected

Partners use this event to:

- Notify their users that the EngagementInvitation has been
  rejected.
- Update their internal records to reflect the rejected
  invitation.
- Trigger any necessary workflows, such as notifying the sales team
  about the rejection.

The following example shows a typical Engagement Invitation Rejected
event.

```
{
    "version": "0",
    "id": "01234567-0123-0123-0123-0123456789ab",
    "detail-type": "Engagement Invitation Rejected",
    "source": "aws.partnercentral-selling",
    "account": "123456789012",
    "time": "2023-04-17T09:48:27Z",
    "region": "us-east-1",
    "resources": ["arn:aws:partnercentral:us-east-1::catalog/AWS/engagement-invitation/engi-v7p8z56whnauo"],
    "detail": {
        "catalog": "AWS",
        "engagementInvitation": {
            "arn": "arn:aws:partnercentral:us-east-1::catalog/AWS/engagement-invitation/engi-v7p8z56whnauo",
            "id": "engi-v7p8z56whnauo",
            "engagementId": "eng-12356whnauo",
            "participantType": "Enum", //Sender/Receiver
            "senderAccountId": "string",
            "receiverAccountId": "string",
            "payloadType": "LeadInvitation" //OpportunityInvitation|LeadInvitation
        }
    }
}
```

#### Engagement Invitation Expired

Partners use this event to:

- Notify their users that the EngagementInvitation has expired and can
  no longer be acted upon.
- Update their internal records to reflect the expired
  invitation.
- Trigger any necessary workflows, such as notifying the sales team
  about the expired invitation.

The following example shows a typical Engagement Invitation Expired
event.

```
{
    "version": "0",
    "id": "01234567-0123-0123-0123-0123456789ab",
    "detail-type": "Engagement Invitation Expired",
    "source": "aws.partnercentral-selling",
    "account": "123456789012",
    "time": "2023-04-18T18:20:15Z",
    "region": "us-east-1",
    "resources": [
      "arn:aws:partnercentral:us-east-1::catalog/AWS/engagement-invitation/engi-v7p8z56whnauo"
    ],
    "detail": {
      "catalog" : "AWS",
      "engagementInvitation": {
        "arn": "arn:aws:partnercentral:us-east-1::catalog/AWS/engagement-invitation/engi-v7p8z56whnauo",
        "id": "engi-v7p8z56whnauo",
        "engagementId": "eng-12356whnauo",
        "participantType": "Enum", //Sender/Receiver
        "senderAccountId": "string",
        "receiverAccountId": "string",
        "payloadType": "LeadInvitation" //OpportunityInvitation|LeadInvitation
      }
    }
}
```

#### Engagement Member Added

Partners use this event to:

- Notify their users about the changes to the Engagement
  membership.
- Update their internal records to reflect the new Engagement
  member.
- Trigger any necessary workflows, such as notifying team members about
  the changes.

The following example shows a typical Engagement Member Added event.

```
{
    "version": "0",
    "id": "01234567-0123-0123-0123-0123456789ab",
    "detail-type": "Engagement Member Added",
    "source": "aws.partnercentral-selling",
    "account": "123456789012",
    "time": "2023-04-16T15:23:45Z",
    "region": "us-east-1",
    "resources": [
      "arn:aws:partnercentral:us-east-1::catalog/AWS/engagement/eng-v7p8z56whnauo"
    ],
    "detail": {
      "catalog" : "AWS",
      "engagement": {
        "id": "eng-v7p8z56whnauo"
      },
      "engagementMember": {
        "accountId": "string",
        "companyName": "string"
      }
    }
}
```

#### Engagement Resource Snapshot Created

Partners use this event to track changes to resources associated with an
engagement and trigger automated workflows, such as updating CRM systems or
notifying sales teams. The snapshot template determines the type of
update:

`OpportunitySummaryView`

- Notify all members of an engagement that the engagement
  has been updated.

`AwsOpportunitySummaryFullView`

- Track updates made specifically by AWS to opportunities
  within an engagement.
- This notification and snapshot are only visible to the
  opportunity owner.
- Includes deal sizing updates, which are not available
  through the `OpportunitySummaryView`
  template.

The following example shows a typical Engagement Resource Snapshot Created
event.

```
{
    "version": "0",
    "id": "01234567-0123-0123-0123-0123456789ab",
    "detail-type": "Engagement Resource Snapshot Created",
    "source": "aws.partnercentral-selling",
    "account": "123456789012",
    "time": "2023-04-18T18:20:15Z",
    "region": "us-east-1",
    "resources": [
      "arn:aws:partnercentral:us-east-1::catalog/AWS/engagement/eng-v7p8z56whnauo"
    ],
    "detail": {
      "catalog" : "AWS",
      "resourceSnapshot": {
        "arn": "arn:aws:partnercentral-selling:us-east-1::catalog/AWS/engagement/eng-v7p8z56whnauo/resource/Opportunity/o-12312/template/temp-name/snapshot/snapshot-19232",
        "engagementId": "eng-v7p8z56whnauo",
        "resourceType": "Opportunity",
        "resourceId" : "O123211231",
        "createdBy": "123123123123",
        "targetMemberAccounts": ["123123123123", "aws"],
        "resourceSnapshotTemplateName": "temp-name"
      }
    }
}
```

#### Engagement Created

Partners use this event to:

- Notify their users that a new Engagement has been created.
- Trigger automated workflows such as updating CRM systems or notifying
  sales teams about new engagement creations.

The following example shows a typical Engagement Created event.

```
{
    "version": "0",
    "id": "01234567-0123-0123-0123-0123456789ab",
    "detail-type": "Engagement Created",
    "source": "aws.partnercentral-selling",
    "account": "123456789012",
    "time": "2023-04-18T18:20:15Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:partnercentral:us-east-1::catalog/AWS/engagement/eng-567a1j5hxp35lo"
    ],
    "detail": {
        "catalog": "AWS",
        "engagement": {
            "engagementArn": "arn:aws:partnercentral:us-east-1::catalog/AWS/engagement/eng-567a1j5hxp35lo",
            "engagementId": "eng-567a1j5hxp35lo",
            "CreatedAt": "2023-04-18T18:20:15Z",
            "CreatedBy": "aws",
            "ContextTypes": ["Lead"]

        }
    }
}
```

#### Engagement Updated

Partners use this event to:

- Notify their users that an existing Engagement has been
  updated.
- Trigger automated workflows such as updating CRM systems or notifying
  sales teams.

The following example shows a typical Engagement Updated event.

```
{
    "version": "0",
    "id": "01234567-0123-0123-0123-0123456789ab",
    "detail-type": "Engagement Updated",
    "source": "aws.partnercentral-selling",
    "account": "123456789012",
    "time": "2023-04-18T18:20:15Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:partnercentral:us-east-1::catalog/AWS/engagement/eng-567a1j5hxp35lo"
    ],
    "detail": {
        "catalog": "AWS",
        "engagement": {
            "engagementArn": "arn:aws:partnercentral:us-east-1::catalog/AWS/engagement/eng-567a1j5hxp35lo",
            "engagementId": "eng-567a1j5hxp35lo",
            "LastModifiedAt": "2023-04-18T18:20:15Z",
            "LastModifiedBy": "aws",
            "ContextTypes": ["Lead", "CustomerProject"]
        }
    }
}
```
