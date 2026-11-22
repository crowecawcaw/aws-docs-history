

# Managing opportunity notifications

AWS Partner Central in the AWS Management Console sends notifications about existing opportunities and about new opportunities. Each type has its own default recipients and its own way to change them.

## Interactive demo
<a name="managing-notifications-demo"></a>

To see how to set up opportunity notifications, view the [Opportunity notifications demo](https://awsmarketplace.storylane.io/share/5pdkwomvfdq6) on the Storylane website.

## Opportunity notification types
<a name="notification-categories"></a>


| Type | What it covers | Default recipients | How to manage it | 
| --- | --- | --- | --- | 
| Updates for existing opportunities | Stage changes, validation requests, and multi-partner opportunity invitations for opportunities that already exist. | The Opportunity Owner, the primary account email, and anyone subscribed through AWS User Notifications. | Update the Opportunity Owner on the opportunity. To add recipients, subscribe them in AWS User Notifications. Each recipient verifies their email address. | 
| New opportunities | AWS-originated referrals and other opportunity creation events. | The primary account email only. | Set forwarding rules on the primary account mailbox. | 

**Important**  
Roles that received notifications in the legacy AWS Partner Central experience, such as Alliance Team or ACE Manager, don't carry over. These team members don't receive opportunity notifications until you complete the steps in [Set up opportunity notifications](#notifications-setup).

IAM permissions don't affect who receives notifications. The recipients depend only on the settings in the preceding table.

## Set up opportunity notifications
<a name="notifications-setup"></a>

### Updates for existing opportunities
<a name="notifications-existing-opportunities"></a>

AWS Partner Central sends updates about existing opportunities to the Opportunity Owner and the primary account email. To send updates to the right people, use one or both of the following routes.

#### Route 1: Set the Opportunity Owner on each existing opportunity
<a name="notifications-opportunity-owner"></a>

Open each active opportunity, and confirm that the Opportunity Owner is the person who should receive updates for that deal. Each opportunity can have a different owner.
+ Updates go to the Opportunity Owner automatically.
+ To hand off a deal, update the Opportunity Owner. The notifications follow the new owner.
+ AWS sellers can also see and update the Opportunity Owner.

#### Route 2: Subscribe more team members in AWS User Notifications
<a name="notifications-user-notifications"></a>

To add team members beyond the Opportunity Owner and the primary account email, create user-configured notifications in AWS User Notifications.

1. Open the AWS User Notifications console, and start a new notification configuration.

1. For the service name, enter **AWS Partner Central Selling**.

1. Choose the event type that you want to subscribe to, for example **Opportunity Updated**.

1. For Regions, choose **US East (N. Virginia)**.

1. To subscribe to more event types, choose **Add another event rule**, and repeat steps 3 and 4.

1. For the delivery channel, choose **Email**. Enter the recipient's email address and name.

1. Choose **Create notification configurations**.

1. The recipient receives a verification email from AWS User Notifications. After the recipient chooses the verification link, they start receiving notifications.

For more information, see the [AWS User Notifications User Guide](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html).

### New opportunities
<a name="notifications-new-opportunities"></a>

Only the primary account email receives notifications about new opportunities. To route these notifications to the right people, set forwarding rules on that mailbox.

## Checklist
<a name="notifications-checklist"></a>

Updates for existing opportunities:
+ Review the Opportunity Owner on each active opportunity, and update it as needed.
+ Subscribe more team members in AWS User Notifications for the opportunity event types they need. Confirm that each recipient verifies their email address.

New opportunities:
+ Set forwarding rules on the primary account email.

## Frequently asked questions
<a name="notifications-faq"></a>

**How do I get more than one person to receive notifications on an existing opportunity?**

The Opportunity Owner and the primary account email always receive them. Subscribe more team members in AWS User Notifications for the event types you want. Each recipient verifies their email address.

**How do I get more people notified about new opportunities?**

Set forwarding rules on the primary account email.

**Our previous contacts didn't carry over. How do I get them notified again?**
+ On each active opportunity, set the Opportunity Owner to the person responsible.
+ Subscribe more team members in AWS User Notifications for the opportunity event types they need.
+ Set forwarding rules on the primary account email for new opportunities.

**If a team member leaves, how do I stop their notifications?**
+ For AWS User Notifications subscriptions, remove them as a recipient in AWS User Notifications.
+ For legacy notifications that still arrive, message [AWS Partner Central Support](https://us-east-1.console.aws.amazon.com/partnercentral/support) to remove them.
+ For any notification email, the team member can choose the unsubscribe link. If they no longer have access to the mailbox, message [AWS Partner Central Support](https://us-east-1.console.aws.amazon.com/partnercentral/support) to unsubscribe them.

**How do I change who receives updates for a specific opportunity?**

Update the Opportunity Owner on the opportunity, or change the AWS User Notifications subscribers for that event type.

**Can team members subscribe to opportunity notifications individually?**

Yes, for existing opportunities. Each team member can be subscribed through AWS User Notifications.

**Where can I get a full list of opportunity notification events and their recipients?**

Message [AWS Partner Central Support](https://us-east-1.console.aws.amazon.com/partnercentral/support).