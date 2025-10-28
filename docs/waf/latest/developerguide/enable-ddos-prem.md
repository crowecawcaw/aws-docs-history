**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Subscribing to AWS Shield Advanced

This page explains how to subscribe your accounts to Shield Advanced, to start using the
service.

You must subscribe to Shield Advanced for each AWS account that you want to protect. You do not need to subscribe to Shield Standard.

###### Shield Advanced subscription billing

If you’re an AWS Channel Reseller, talk to your account team for information and guidance. This billing information is for customers that are not AWS Channel Resellers.

For all others, the following subscription and billing guidelines apply:

- For accounts that are members of an AWS Organizations organization, AWS bills the Shield Advanced
  subscriptions against the payer account for the organization, regardless of whether the payer
  account itself is subscribed.
- When you subscribe multiple accounts that are in the same [AWS Organizations
  consolidated billing account family](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md"), one subscription price covers all
  subscribed accounts in the family. The organization must own all of the AWS accounts
  and all of their resources.
- When you subscribe multiple accounts for multiple organizations, you can still pay one
  subscription fee across all of the organizations, accounts, and resources providing you
  own all of them. Contact your account manager or AWS support and request a fee waiver
  on the AWS Shield Advanced subscription charges for all but one of the organizations.
  For detailed pricing information and examples, see [AWS Shield Pricing](https://aws.amazon.com/shield/pricing/ "https://aws.amazon.com/shield/pricing/").

###### Consider simplifying subscriptions with AWS Firewall Manager

If your accounts are part of an organization, we recommend that you use AWS Firewall Manager
if you can, to automate your subscriptions and protections for the organization.
Firewall Manager supports all protected resource types except for Amazon Route 53 and AWS Global Accelerator. To
use Firewall Manager, see [AWS Firewall Manager](fms-chapter.md "fms-chapter.md") and [Setting up AWS Firewall Manager​ AWS Shield Advanced policies](getting-started-fms-shield.md "getting-started-fms-shield.md").

If you don't use Firewall Manager, for each account with resources to protect, subscribe and add
protections using the following procedures.

###### To subscribe an account to AWS Shield Advanced

1. Sign in to the AWS Management Console and open the AWS WAF & Shield console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").
2. In the **AWS Shield** navigation bar, choose **Getting
   started**. Choose **Subscribe to Shield Advanced**.
3. In the **Subscribe to Shield Advanced** page, read each term of the
   agreement, and then select all of the check boxes to indicate that you accept
   the terms. For accounts in a consolidated billing family, you must agree to the
   terms for each account.

###### Important

When you are subscribed, to unsubscribe you must contact [AWS Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").

To disable autorenewal for your subscription, you must use the Shield API
operation [UpdateSubscription](../DDOSAPIReference/API_UpdateSubscription.md "../DDOSAPIReference/API_UpdateSubscription.md") or the CLI command [update-subscription](../../../cli/latest/reference/shield/update-subscription.md "../../../cli/latest/reference/shield/update-subscription.md").

Choose **Subscribe to Shield Advanced**. This subscribes your
account to Shield Advanced and activates the service.
Your account is subscribed. Continue through the following steps to protect your
account's resources with Shield Advanced.

###### Note

Shield Advanced doesn't automatically protect your resources after you subscribe. You
must specify the resources you want Shield Advanced to protect.
