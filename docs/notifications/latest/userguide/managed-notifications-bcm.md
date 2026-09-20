

# AWS Billing and Cost Management notifications
<a name="managed-notifications-bcm"></a>

Billing and Cost Management sends managed notifications about your billing, payment, and account activity through AWS User Notifications. You receive these notifications in the Console Notification Center, by email (your account's root user email address, plus additional addresses that you add), in the AWS Console Mobile Application, and in Amazon Q Developer in chat applications (such as Slack and Microsoft Teams).

Billing and Cost Management notifications include the following categories:
+ **Billing and Invoices** – Notifications about invoices and billing activity
+ **Payment** – Notifications about payments and payment methods
+ **Financing** – Notifications about financing activity
+ **Fraud Prevention** – Notifications about suspected fraudulent activity
+ **Subscriptions** – Notifications about your AWS subscriptions

For each subcategory, you can choose which account contacts are notified, opt out of non-critical subcategories for each contact type, and review which contacts are subscribed to which categories. User Notifications also supports the AWS SDKs, the AWS Command Line Interface, and AWS CloudFormation for programmatic configuration and consumption of these notifications.

To choose which contacts receive Billing and Cost Management notifications and to add delivery channels, see [AWS managed notification subscriptions in AWS User Notifications](manage-mns.md). To view your notifications, see [Viewing AWS managed notifications in AWS User Notifications](viewing-managed-notifications.md).

## Configure your managed notifications subscription
<a name="bcm-configure-subscription"></a>

To configure your AWS managed notifications subscription for Billing and Cost Management, complete the following steps.

**To configure your Billing and Cost Management notification subscription**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/).

1. In the navigation pane, choose **AWS managed notifications subscriptions**.

1. Under the **AWS Billing and Cost Management** category, manage your notifications by subcategory:
   + Billing and Invoices
   + Payment
   + Financing
   + Fraud Prevention
   + Subscriptions

1. For each subcategory, choose the account contacts that are notified.

1. Add delivery channels. By default, User Notifications sends notifications to your account's root user email address. You can add more email addresses, Amazon Q Developer in chat applications, and the AWS Console Mobile Application.

For detailed steps, see [AWS managed notification subscriptions in AWS User Notifications](manage-mns.md).

## Default email notifications
<a name="bcm-default-email-notifications"></a>

By default, Billing and Cost Management sends billing notification emails to your existing account contacts: the root user, operations, billing, and security email addresses.

## Email domain change
<a name="bcm-email-domain-change"></a>

Billing and Cost Management sends emails from new `@aws.com` sender addresses, based on the notification subcategory, instead of `no-reply@amazonaws.com`.

**Action required**  
If you have email filters, forwarding rules, or allow lists configured for the previous sender domain, add the new sender addresses so that you continue to receive billing notifications.

The following table shows the new sender address for each notification subcategory.


| Subcategory | New sender address | 
| --- | --- | 
| Billing and Invoices | `invoicing@aws.com` | 
| Payment | `payment@aws.com` | 
| Financing | `financing@aws.com` | 
| Fraud Prevention | `fraud-prevention@aws.com` | 
| Subscriptions | `billing-subscriptions@aws.com` | 

**Note**  
Notification emails have an updated visual design, including a standardized footer. The content of the emails remains the same. Only the presentation changes.

## Sensitive information
<a name="bcm-sensitive-information"></a>

Some billing notifications contain sensitive information, such as payment and contact details. By default, User Notifications excludes sensitive events from additional delivery channels, such as chat and mobile push. To include sensitive events for a specific channel, turn on the **Include sensitive events** toggle in that channel's configuration.

To view and subscribe to sensitive events, you need the following AWS Identity and Access Management (IAM) permissions:
+ `notifications:AccessSensitiveEvents` – Required to view sensitive event content.
+ `notifications:SubscribeSensitiveEvents` – Required to associate delivery channels that receive sensitive events.

## Seller of Record based language preference
<a name="bcm-sor-language"></a>

Billing and Cost Management emails respect the Seller of Record (SOR) language associated with your account. If your account has an SOR language other than English, AWS sends emails in both the SOR language and English. If no SOR language is set, AWS sends emails in English only.

If you set a customer language preference (Customer Language Locale) that differs from your SOR language, emails include content in both your preferred language and the SOR language.

## Email To and CC formatting and deduplication
<a name="bcm-email-dedup"></a>

For all subcategories in Billing and Cost Management, AWS sends email communications by using To and CC formatting. User Notifications combines all email channels associated with a subcategory in an account into a single email that uses To and CC recipients. To reduce noise, User Notifications applies account-level deduplication for email addresses that use plus addressing (a plus sign in the address).

## Notification retention
<a name="bcm-retention"></a>

User Notifications retains all Billing and Cost Management notifications for 3 years in the User Notifications console.