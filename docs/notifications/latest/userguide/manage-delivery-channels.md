# Adding delivery channels in AWS User Notifications

You can add delivery channels for both user-configured notifications and AWS managed notifications from the User Notifications console to have your notifications sent to other
locations.

###### Note

Emails you receive from User Notifications are sent from the domain `@aws.com`. The prefix of the emails you receive reflect the AWS service
sending the communication. For example, notifications from AWS Health are sent from the email `health@aws.com` and Amazon CloudWatch notifications
are sent from a `cloudwatch@aws.com` email address.

Emails

###### To add delivery channels

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications/ "https://console.aws.amazon.com/notifications/").
2. In the navigation panel, choose **Delivery channels**.
3. Choose **Emails**.

###### Note

A verification email is sent to newly added email addresses. You can generate another
verification email for pending addresses by choosing **Reverify**.
Verified emails have a green checkmark next to the email address when added as a
**Recipient**. 4. Choose **Add emails**.

###### Tip

You can use your email distribution lists as an email delivery channel to easily subscribe multiple email addresses to User Notifications with a single verification flow.
You can separately add and remove emails to the distribution list without requiring further verification with User Notifications. 5. For **Recipient**, choose or enter the recipient's email
address. 6. For **Name**, enter the recipient's name. 7. (Optional) Choose **Add another recipient** to add more
recipients. 8. ###### (Optional) Add tags for this delivery channel. To add tags, do the following:

###### Tip

A tag is a label that you assign to an AWS resource. Tags help you organize your
resources. For more information, see [Tagging your resources](tagging-resources.md "tagging-resources.md").

    1. Enter a key in **Key**.
    2. (Optional) Enter a value in **Value**.
    3. (Optional) Choose **Add new tag** to add more tags.

9. Choose **Add emails**

Mobile devices

###### Note

Before you add a mobile device as a delivery channel, you must do the following:

- Add the appropriate IAM permissions so that your mobile device is available in the
  User Notifications console. For more information, see [IAM permissions for
  listing mobile devices as delivery channels](../../../consolemobileapp/latest/userguide/permissions-policies.md "../../../consolemobileapp/latest/userguide/permissions-policies.md") in the _AWS Console Mobile Application User
  Guide_.
- Install the AWS Console Mobile Application to your device and enable push notifications from the app. Note
  that the notifications you receive are push notifications, not Short Message Service (SMS).
  For more information, see [Step 1: Get started with push notifications](../../../consolemobileapp/latest/userguide/managing-notifications.md#step-1-get-started-with-push-notifications "../../../consolemobileapp/latest/userguide/managing-notifications.md#step-1-get-started-with-push-notifications") in the _AWS Console Mobile Application User
  Guide_.

###### To add delivery channels

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications/ "https://console.aws.amazon.com/notifications/").
2. In the navigation panel, choose **Delivery channels**.
3. Choose **Mobile devices**.
4. Use the search box to find **Mobile devices** to add.

Chat channels

###### To add delivery channels

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications/ "https://console.aws.amazon.com/notifications/").
2. In the navigation panel, choose **Delivery channels**.
3. Choose **Chat channels**.
4. Select a chat client from the dropdown box.
5. Use the search box to find **Chat channels** to add.

###### Note

For more information about Amazon Q Developer in chat applications, see [Getting started with Amazon Q Developer in chat applications](../../../chatbot/latest/adminguide/getting-started.md "../../../chatbot/latest/adminguide/getting-started.md") in
the _Amazon Q Developer in chat applications Administrator Guide_.
