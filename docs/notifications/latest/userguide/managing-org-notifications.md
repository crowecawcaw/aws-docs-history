# Managing notifications across your organization with AWS User Notifications

By default, you can use User Notifications to configure and view notifications for a single AWS account.
If you use AWS Organizations, you can also configure and view notifications centrally across your organization.
This provides access to the same information as single account operations.
You can configure and view notifications about accounts included in specific organizational units (OUs) or
all accounts in an organization.

You can create Notification Configurations to filter events across accounts in your organization.
When an event from any member account matches the event rules, User Notifications generates a notification
in the management account.

We recommend using [delegated administrators](../../../health/latest/ug/delegated-administrator-organizational-view.md "../../../health/latest/ug/delegated-administrator-organizational-view.md")
to delegate access for managing notifications across accounts with organizations integration to a member account.
This allows you to keep your management account restricted while providing members with the visibility they need.

###### Important

- User Notifications doesn't record events that occurred before you enabled trusted access to AWS Organizations. For example, if a member account (111122223333) in your organization received an EC2 event before you enabled this feature, this event won't generate a notification in the management account.
- Notification configurations automatically update as you add or remove accounts from your organization. You don't need to update existing configurations when organization membership changes.
- Notifications for accounts in your organization appear in User Notifications for up to 90 days, even if accounts leave your organization.
- Events that occurred before accounts joined the organization or before you configured notifications won't generate notifications.

## Prerequisites

Before enabling AWS Organizations in User Notifications, you must:

- Be part of an organization with [all features](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#feature-set-all "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#feature-set-all") enabled
- Sign in to the management account as an IAM user or assume an IAM role

## Configuring notifications for your organization

Configuring notifications about events across your organization is available to all management accounts
and delegated administrators that [enable trusted access](uno-orgs.md "uno-orgs.md") with AWS Organizations.
You can create notification configurations for the organization or OUs,
filtered for specific events. For example, Health events where `TypeCategory = scheduledChange` and `service = EC2`.

To receive notifications across accounts,
create notification configurations for the organization or OUs.
A notification configuration contains the services and event rules you want notifications for.
An event rule specifies which events generate notifications in the AWS Management Console and which delivery channels to use.

###### Important

Configuring notifications for organization accounts
creates read-only notification configurations in member accounts.
These configurations don't generate notifications in member accounts, only the management account
receives organization notifications. To configure notification for a member account, see [Step 1: Creating a notification configuration](getting-started.md#getting-started-step1 "getting-started.md#getting-started-step1").

###### To create a notification configuration for your organization

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications/ "https://console.aws.amazon.com/notifications/"):
   1. Choose
      the
      bell icon in the top navigation bar.
   2. Choose **Notification center**.
   3. In the navigation pane, choose **Notification configurations**.
   4. Choose **Create notification configuration**.
   5. Select at least one notification hub.

2. ###### Add a name and description:
   1. Enter a name for your configuration.
   2. (Optional) Enter a description for your configuration.

3. Select the OUs you're notified about. You can only select your organization or OUs, not individual accounts. To select individual accounts, use the [advanced filter](common-usecases.md "common-usecases.md").

###### Note

This only generates notifications in the management or delegated administrator accounts about relevant member accounts. 4. ###### Create an Event Rule:

    1. For **AWS service name**, select the name of an AWS service to use
     as the event source.
    2. For **Event type**,
     select
     event types.
    3. For **Regions**, select the AWS Regions where your service data is
     located.


    ###### Note

    You can filter event rules further by using the code editor under **Advanced
     filter (optional)**. The **Advanced filter** doesn't currently support wildcards. To view examples of Event Patterns that you can use, see
     [Filtering event rules using customized JSON event patterns in AWS User Notifications](common-usecases.md "common-usecases.md").

5. ###### Define aggregation settings:

###### Tip

Aggregation settings reduce the number of notifications that you receive by combining
multiple events into fewer notifications based on the option you choose. Aggregation settings
are turned on by default. We recommend you use aggregation settings.

    1. Choose if you would like to **Receive within 5 minutes (recommended)**, **Receive within 12 hours**, or **Do not aggregate**.


    ###### Tip

    Choose **Receive fewer notifications** for low priority notifications.
     Choose **Reduce notifications delivery time** for high priority
     notifications.

6.  ###### (Optional) Add delivery channels:
    1. Select your delivery channels. We recommend that you view an event before adding
       additional recipients.

    Email

    ###### Note

    A verification email is sent to newly added email addresses once you create the
    notification configuration. You can generate another verification email for pending
    addresses by choosing **Reverify**.

        1. Choose **Add emails**.


        ###### Tip

        You can use your email distribution lists as an email delivery channel to easily subscribe multiple email addresses to User Notifications with a single verification flow.
         You can separately add and remove emails to the distribution list without requiring further verification with User Notifications.
        2. For **Recipient**, enter or choose the recipient's email
         address.
        3. For **Name**, enter the recipient's name.
        4. (Optional) Choose **Add another recipient** to add more
         recipients.
        5. Choose **Add emails**.

    Amazon Q Developer

        1. For **Channel**, add a new channel or select the existing channels
         you want to send notifications to.

    ###### Note

    For more information about Amazon Q Developer in chat applications, see [What is Amazon Q Developer in chat applications?](../../../chatbot/latest/adminguide/what-is.md "../../../chatbot/latest/adminguide/what-is.md") in the
    _Amazon Q Developer in chat applications Administrator Guide_.

    AWS Console Mobile Application

    ###### Note

    Before you add a mobile device as a delivery channel, you must:

        * Add the appropriate IAM permissions to make mobile device available in theUser Notifications
         console. For more information, see [IAM permissions for
         listing mobile devices as delivery channels](../../../consolemobileapp/latest/userguide/permissions-policies.md "../../../consolemobileapp/latest/userguide/permissions-policies.md") in the *AWS Console Mobile Application User
         Guide*.
        * Install the AWS Console Mobile Application on to your device with push notifications enabled. Note
         that the notifications you receive are push notifications, not Short Message Service
         (SMS). For more information, see [Step 1: Get started with push notifications](../../../consolemobileapp/latest/userguide/managing-notifications.md#step-1-get-started-with-push-notifications "../../../consolemobileapp/latest/userguide/managing-notifications.md#step-1-get-started-with-push-notifications") in the *AWS Console Mobile Application User
         Guide*.

        1. For **Device**, select the devices you want to send notifications
         to.

7.  ###### (Optional) Manage tags:

###### Tip

A tag is a label that you assign to an AWS resource. Tags help you organize your
resources. For more information, see [Tagging your resources](tagging-resources.md "tagging-resources.md").

    1. For **Key**, enter the key name you want to use.
    2. (Optional) For **Value**, enter a value for the specified key.
    3. (Optional) Choose **Add new tag** to add more tags.

8. Review your configuration and confirm its details.
9. Choose **Create notification configuration**.

###### Tip

To edit or delete notification configurations, see [Notification configurations in AWS User Notifications](managing-notifications.md "managing-notifications.md").
