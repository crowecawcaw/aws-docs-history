# Delivery channels for AWS managed notifications in AWS User Notifications

Delivery channels are locations where you can send notifications. You can send notifications to multiple channels, including email addresses,
chat channels, and mobile devices.

###### Topics

- [Adding delivery channels for AWS managed notifications in AWS User Notifications](#Add-delivery-channels-managed-notifications "#Add-delivery-channels-managed-notifications")
- [Removing delivery channels for AWS managed notifications in AWS User Notifications](#remove-delivery-channel-managed-notifications "#remove-delivery-channel-managed-notifications")

## Adding delivery channels for AWS managed notifications in AWS User Notifications

You can add delivery channels from the console to have your AWS managed notifications sent to other locations. Available delivery channels include, email addresses, and chat channels

###### Note

Emails you receive from User Notifications are sent from the domain `@aws.com`. The prefix of the emails you receive reflect the AWS service
sending the communication. For example, notifications from AWS Health are sent from the email `health@aws.com`.

###### To add delivery channels

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the navigation pane, choose **AWS managed notifications subscriptions**.
3. In **Delivery channels**, choose **Add delivery channels**.
4. In **Emails**, choose or enter the recipient's email address.

###### Note

A verification email is sent to newly added email addresses. You can generate another
verification email for pending addresses by choosing **Reverify**.
Verified emails have a green checkmark next to the email address when added as a
**Recipient**.

###### Tip

You can use your email distribution lists as an email delivery channel to easily subscribe multiple email addresses to User Notifications with a single verification flow.
You can separately add and remove emails to the distribution list without requiring further verification with User Notifications. 5. For **Name**, enter the recipient's name. 6. (Optional) Choose **Add another recipient** to add more recipients. 7. (Optional) Add mobile devices:

    1. In **AWS Console Mobile Application** select mobile devices to add.

8. (Optional) Add chat channels:
   1. In **Chat channels** select chat channels to add.

9. Choose **Add delivery channels**.

## Removing delivery channels for AWS managed notifications in AWS User Notifications

You can remove delivery channels if you no longer want your AWS managed notifications sent to those locations.

###### To remove delivery channels

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the navigation pane, choose **AWS managed notifications subscriptions**.
3. In **Delivery channels**, select the delivery channels you want to remove.
4. Choose **Remove delivery channels**.
5. Confirm removal by choosing
   **Remove**.
