# Responding to share requests in

AWS Audit Manager

This tutorial describes the actions to take when you receive a share request for a
custom framework. Audit Manager notifies you when you receive a share request. You also receive a
notification to remind you when a share request is due to expire in the next 30 days.

## Prerequisites

Before you get started, we recommend that you first learn more about Audit Manager [framework sharing concepts and terminology](share-custom-framework-concepts-and-terminology.md "share-custom-framework-concepts-and-terminology.md").

## Procedure

###### Tasks

- [Step 1: Check your
  received request notifications](#responding-to-shared-framework-requests-step-1 "#responding-to-shared-framework-requests-step-1")
- [Step 2: Take action on the request](#responding-to-shared-framework-requests-step-2 "#responding-to-shared-framework-requests-step-2")
- [Step 3: View a history of
  your received requests](#responding-to-shared-framework-requests-step-3 "#responding-to-shared-framework-requests-step-3")

### Step 1: Check your

received request notifications

Start by checking your share request notifications. The **Received
requests** tab displays a list of the share requests that you’ve received from
other AWS accounts. Requests that are awaiting your response appear with a blue dot. You
can also filter this view to display only requests that expire sometime within the next 30
days*.*

**To view received requests**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. If you have a share request notification, Audit Manager displays a red dot next to
   the navigation menu icon.

![Screenshot of the minimized navigation menu icon with a notification.](images/framework_sharing-navigation_minimized_notification-console.png) 3. Expand the navigation pane and look next to **Share requests**. A
notification badge indicates the number of share requests that need your attention.

![Screenshot of the expanded navigation menu, with share requests highlighted and a notification badge.](images/framework_sharing-navigation_expanded_notification-console.png) 4. Choose **Share requests**. By default, this page opens on the
**Received requests** tab. 5. Identify the share requests that need your action by looking for items with a blue
dot.

![Screenshot of a received request with a blue dot next to the framework name.](images/framework_sharing-blue_dot_notification-console.png) 6. (Optional) To view only requests that expire in the next 30 days, find the
**All statuses** dropdown list and select
**Expiring**.

### Step 2: Take action on the request

To remove the blue notification dot, you need to take action by either accepting or
declining the share request.

When you accept a share request, Audit Manager replicates a snapshot of the original
framework into the custom frameworks tab of your framework library. Audit Manager replicates
and encrypts the new custom framework using the KMS key that you specified in your
[Audit Manager
settings](settings-KMS.md "settings-KMS.md").

###### To accept a share request

1. Open the **Share requests** page and make sure
   that you're viewing the **Received requests**
   tab.
2. (Optional) Select **Active** or **Expiring** from the filter
   dropdown list.
3. (Optional) Choose a framework name to view the details of the share request.
   This includes information such as the framework description, the number of
   controls that are in the framework, and the message from the sender.
4. Select the share request that you want to accept, choose **Actions**, and then choose **Accept**.
   After you accept a share request, the status changes to _replicating_ while the shared custom framework is added to your framework
   library. If the framework contains custom controls, these controls are added to your
   control library at this time.

When the framework replication is complete, the status changes to _shared_. A success banner notifies you that the custom
framework is ready to use.

###### Tip

When you accept a custom framework, it's replicated only to your current AWS Region. You
might want the new shared framework to be available across all Regions in your
AWS account. If so, after you accept the share request you can [share the framework](framework-sharing.md "framework-sharing.md") to other Regions under your account as needed.

When you decline a share request, Audit Manager doesn’t add that custom framework to your
framework library. However, a record of the declined share request remains in the
**Received requests** tab, with a status of **Inactive**.

**To decline a share request**

1. Open the **Share requests** page and make sure
   that you're viewing the **Received requests**
   tab.
2. (Optional) Select **Active** or **Expiring**
   from the filter dropdown list.
3. (Optional) Choose a framework name to view the details of the share request.
   This includes information such as the framework description, the number of
   controls that are in the framework, and the message from the sender.
4. Select the share request that you want to decline, choose **Actions**, and then choose **Decline**.
5. In the dialog box that appears, choose **Decline** to confirm your choice.

###### Tip

If you change your mind and want access to a shared framework after you decline,
ask the sender to send you a new share request.

###### Note

It can take up to 10 minutes to process share request actions when a framework is shared
across AWS Regions. After taking action on a cross-Region share request, we recommend
that you check back later to confirm that the share request was successfully accepted or
declined.

### Step 3: View a history of

your received requests

After you accept or decline a shared framework, you can return to the **Share requests** page to see your share request history. You can
filter this list as needed. For example, you can apply filters to display only requests
that you accepted.

**To view a history of your share requests**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Share requests**.
3. Choose the **Received requests** tab.
4. Find the **All statuses** dropdown list, and select
   one of the following filters:

| Name         | Description                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Active**   | This filter displays share requests that you haven't yet accepted or declined.                                           |
| **Expiring** | This filter displays share requests that expire in the next 30 days.                                                     |
| **Shared**   | This filter displays share requests that you accepted. The shared framework is now available in your framework library.  |
| **Inactive** | This filter displays share requests that were declined or expired.                                                       |
| **Failed**   | This filter displays the share requests that weren't sent successfully. Choose the word **Failed** to view more details. | ## Next steps After you accept a shared custom framework, you can find it in the custom frameworks tab of the framework library. You can now use that framework to create an assessment. To learn more, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md"). For instructions on how to edit your new custom framework, see [Editing a custom framework in AWS Audit Manager](edit-custom-frameworks.md "edit-custom-frameworks.md"). ## Additional resources To find solutions to issues that you might encounter, see [Troubleshooting framework issues](framework-issues.md "framework-issues.md"). |
