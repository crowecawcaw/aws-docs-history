

# Configuring purchase order number requirement settings

With purchase order number requirement settings, administrators can require buyers to enter a purchase order number before they subscribe to products in AWS Marketplace, for specific offer types and pricing types. Administrators can also display a custom message that explains your organization's procurement requirements to buyers on the procurement page.

Before you configure these settings, complete the setup in [Prerequisites for buying policies](buying-policies.md#buying-policies-prerequisites).

## Configuring mandatory purchase orders
<a name="bp-configuring-mandatory-purchase-orders"></a>

Administrators can configure AWS Marketplace to require users to enter a purchase order number before subscribing to any product. This capability helps ensure that every AWS Marketplace subscription is properly authorized and tracked according to your organization's procurement policies.

When mandatory purchase orders are enabled, users cannot complete a subscription without providing a value in the purchase order field. This enforcement happens at the point of subscription, preventing unauthorized purchases before they occur.

**Configuration options**  
You can configure mandatory purchase order enforcement with the following flexibility:
+ **All purchases:** Require a PO for every AWS Marketplace subscription in your organization.
+ **Specific offer types:** Require a PO only for private offers, public offers, or both.
+ **Specific pricing types:** Require a PO for contract pricing, pay-as-you-go pricing, or both.

### Enabling mandatory purchase orders
<a name="bp-enabling-mandatory-purchase-orders"></a>

The following steps explain how to enable mandatory purchase orders for your organization.

**To enable mandatory purchase orders**

1. Using your AWS management account or a delegated administrator account, open [Buying policies](https://console.aws.amazon.com/marketplace/buying-policies) in the AWS Marketplace console.

1. In the left navigation pane, under **Buying policies**, choose **PO number requirement settings**.

1. Under **Mandatory purchase order settings**, choose **Edit**.

1. Select the offer types and pricing types for which you want to require purchase orders.

1. Choose **Save**.

The changes take a few hours for configuration to apply for all users in your organization.

**Note**  
If you choose to require purchase orders for pay-as-you-go public offers in AWS Marketplace, you prevent AWS Marketplace subscriptions through service consoles, like Amazon EC2, as those service consoles don't allow adding purchase orders. End buyers need to procure directly through AWS Marketplace. Mandatory purchase order settings do not apply for Amazon Bedrock serverless purchases made through the Amazon Bedrock console. You can update purchase orders for existing AWS Marketplace subscriptions post subscription in the AWS Marketplace console.

## Configuring custom procurement messaging
<a name="bp-custom-procurement-messaging"></a>

Administrators can configure custom messages that display to users when they encounter procurement requirements, such as mandatory purchase order fields. These messages help users understand why information is required and what they should enter.

**What to include in custom messages**  
Your custom message can include the following types of information:
+ **Policy references:** Link to your organization's procurement policies.
+ **Format requirements:** Explain the expected purchase order number format.
+ **Validation instructions:** Direct users to verify purchase order numbers in your procure-to-pay system.
+ **Compliance information:** Clarify the implications of non-compliance with procurement policies.
+ **Support contacts:** Provide resources for users who need assistance obtaining a purchase order.

The following example shows how you might structure a guidance message for your users:

**Example Sample custom procurement message**  
"A valid purchase order number is required for all AWS Marketplace subscriptions in accordance with our company procurement policy. Purchase order numbers must match an approved purchase order in our procurement system. AWS Marketplace subscriptions are logged in AWS CloudTrail. For assistance, contact your procurement team or refer to the procurement guidelines in the company portal."

**Note**  
You can customize this message with links to your internal procurement systems and policies.

When enabled, this message is displayed to your end buyers on the procurement page in AWS Marketplace.

### Adding a custom message
<a name="bp-adding-custom-message"></a>

The following steps explain how to add a custom procurement message for your organization.

**To add a custom procurement message**

1. Using your AWS management account or a delegated administrator account, open [Buying policies](https://console.aws.amazon.com/marketplace/buying-policies) in the AWS Marketplace console.

1. In the left navigation pane, under **Buying policies**, choose **PO number requirement settings**.

1. Under **Procurement administrator message**, choose **Edit**.

1. Enter your custom message text. Include relevant policy information, format requirements, and contact details for your procurement team.

1. Choose **Save**.

The custom message takes a few hours for configuration to apply and then displays to users in your organization when they encounter the purchase order field during the subscription process.

### Updating or removing a custom message
<a name="bp-updating-removing-custom-message"></a>

You can update or remove your custom procurement message at any time.

**To update a custom message**

1. Using your AWS management account or a delegated administrator account, open [Buying policies](https://console.aws.amazon.com/marketplace/buying-policies) in the AWS Marketplace console.

1. In the left navigation pane, under **Buying policies**, choose **PO number requirement settings**.

1. Under **Procurement administrator message**, choose **Edit**.

1. Update your message text, or clear the field to remove the message.

1. Choose **Save**.