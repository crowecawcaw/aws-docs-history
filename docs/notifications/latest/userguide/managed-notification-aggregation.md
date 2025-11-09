# Aggregating and deduplicating AWS managed notifications in AWS User Notifications

AWS managed notification aggregation is a standard feature available to all management accounts and delegated administrators that have [enabled trusted access](uno-orgs.md "uno-orgs.md") with AWS Organizations. Managed notification aggregation organizes and streamlines your view of events that impact multiple accounts within an organization. User Notifications uses information from AWS Organizations
to aggregate events across accounts within an organization and provides an organized view of events affecting multiple accounts.

In addition, User Notifications deduplicates emails when an account contact is shared between the management account (or delegated administrator) and the member account. This reduces the total number of individual notifications you receive.

## Event aggregation process

AWS managed notifications use an event aggregation logic that combines related events to reduce notification volume while maintaining timely delivery
of critical information. Events are aggregated based on two key factors:

###### Topics

- Communication ID - Events sharing the same `communicationId` are considered related

###### Note

Events are sent to User Notifications via an API integration that uses the same format as Amazon EventBridge.
For more information, see
[Reference: AWS Health
events Amazon EventBridge schema](../../../health/latest/ug/aws-health-events-eventbridge-schema.md "../../../health/latest/ug/aws-health-events-eventbridge-schema.md") in the _AWS Health User Guide_.

- Time window - Events with the same `communicationId` are aggregated within specific time periods based on managed notification sub-category:

| `Sub-category`            | Time window |
| ------------------------- | ----------- |
| `Account-Specific Issues` | 1 minute    |
| `Security`                | 10 minutes  |
| `Health Operations`       | 10 minutes  |
| `Billing Notification`    | 10 minutes  |

## Aggregating AWS managed notifications

###### Note

Aggregation only requires the management account (or delegated administrator) to enable managed notifications.
For more information, see [Disabling or re-enabling AWS managed notifications for AWS Health in AWS User Notifications](managing-notification-features.md "managing-notification-features.md").

User Notifications aggregates event information across accounts as follows:

- **The same event occurs across multiple accounts within the same organization** – The management account and delegated administrators receive a single aggregate notification containing information about all affected accounts.
  Each impacted member account receives an individual notification specific to their account.

###### Note

Aggregation behavior is identical for both the management account and delegated administrator account.

## Deduplicating AWS managed notifications

###### Note

Deduplication requires both the management
account and member accounts to enable managed notifications. For more information, see [Disabling or re-enabling AWS managed notifications for AWS Health in AWS User Notifications](managing-notification-features.md "managing-notification-features.md").

When the management and member accounts [enable managed notifications](managing-notification-features.md "managing-notification-features.md"), User Notifications deduplicates event information across account contacts as follows:

- **An account contact (root user email or alternate contact email) is shared between the management account and a member account** – User Notifications sends the aggregate notification about all accounts to the management account or delegated administrator. Individual email notifications to the shared
  email addresses in member accounts are suppressed.
- **An account contact (root user email or alternate contact email) is shared between member accounts, but not the management account or the delegated administrator** – Individual notifications are sent per account for each account contact
  as default notifications.
- **Plus address handling** – Plus addressing is a method used to create unique, receive-only email addresses based on an existing email address.
  You can use plus addressing by adding a plus sign (+) and any word at the end of your email address. For example, email@example.com and email+devops@example.com. User Notifications treats email addresses with plus addressing as the same email address. This prevents the same email
  from being sent to the same inbox multiple times.

Deduplication only applies to account contact emails. AWS managed notifications sent to other member account delivery channels (for example, the Notification Center) are always sent.

###### Note

User Notifications won't deduplicate events across shared account contacts within the same account. For example, email@example.com and email+devops@example.com. We recommend you unsubscribe identical account contacts. For more information, see [Adding and removing account contacts for AWS managed notifications in AWS User Notifications](Add-remove-account-contacts.md "Add-remove-account-contacts.md").
