

# Delivery channels for AWS managed notifications in AWS User Notifications
<a name="delivery-channels-managed-notifications"></a>

Delivery channels are locations where you can send notifications. You can send notifications to multiple channels, including email addresses, chat channels, and mobile devices.

**Topics**
+ [Adding delivery channels for AWS managed notifications in AWS User Notifications](#Add-delivery-channels-managed-notifications)
+ [Removing delivery channels for AWS managed notifications in AWS User Notifications](#remove-delivery-channel-managed-notifications)

## Adding delivery channels for AWS managed notifications in AWS User Notifications
<a name="Add-delivery-channels-managed-notifications"></a>

You can add delivery channels from the console to have your AWS managed notifications sent to other locations. Available delivery channels include, email addresses, and chat channels

**Note**  
Emails you receive from User Notifications are sent from the domain `@aws.com`. The prefix of the emails you receive reflect the AWS service sending the communication. For example, notifications from AWS Health are sent from the email `health@aws.com`, and notifications from AWS Marketplace are sent from `marketplace@aws.com`.  
Aggregated notifications are sent from `notifications@aws.com`. If your organization uses an email allow list, add the `@aws.com` domain to ensure you receive all User Notifications emails.

**To add delivery channels**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/).

1. In the navigation pane, choose **AWS managed notifications subscriptions**.

1. In **Delivery channels**, choose **Add delivery channels**.

1. In **Emails**, choose or enter the recipient's email address.
**Note**  
A verification email is sent to newly added email addresses. You can generate another verification email for pending addresses by choosing **Reverify**. Verified emails have a green checkmark next to the email address when added as a **Recipient**.  
The recipient must be signed in to the AWS account that added the email address to complete the verification process. The verification link directs to the AWS Management Console.
**Tip**  
You can use your email distribution lists as an email delivery channel to easily subscribe multiple email addresses to User Notifications with a single verification flow. You can separately add and remove emails to the distribution list without requiring further verification with User Notifications. 

1. For **Name**, enter the recipient's name.

1. (Optional) Choose **Add another recipient** to add more recipients.

1. (Optional) Add mobile devices:

   1. In **AWS Console Mobile Application** select mobile devices to add.

1. (Optional) Add chat channels:

   1. In **Chat channels** select chat channels to add.

1. Choose **Add delivery channels**.

## Removing delivery channels for AWS managed notifications in AWS User Notifications
<a name="remove-delivery-channel-managed-notifications"></a>

You can remove delivery channels if you no longer want your AWS managed notifications sent to those locations.

**To remove delivery channels**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/).

1. In the navigation pane, choose **AWS managed notifications subscriptions**.

1. In **Delivery channels**, select the delivery channels you want to remove.

1. Choose **Remove delivery channels**.

1. Confirm removal by choosing **Remove**.