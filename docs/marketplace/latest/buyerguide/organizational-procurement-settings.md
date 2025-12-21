# Configuring organizational procurement settings

AWS Marketplace provides organizational procurement settings that give procurement, software asset management, and cloud governance teams greater control over purchasing processes. These capabilities help enforce compliance with internal policies while maintaining the speed and flexibility that makes AWS Marketplace valuable to end users.

With organizational procurement settings, administrators can:

- Require users to enter a purchase order number before subscribing to products
- Display custom messages to guide users through procurement requirements
- Configure different requirements for specific offer types and pricing models

###### Note

Organizational procurement settings require administrative access to the management account of your AWS organization. You must have the `AWSPrivateMarketplaceAdminFullAccess` policy attached to your user or role to configure these settings.

## Prerequisites for organizational procurement settings

Before you can configure organizational procurement settings, you must complete a one-time setup from your AWS management account. This setup enables trusted access across your organization and creates the necessary service-linked role.

###### To set up organizational procurement settings

1. Sign in to the AWS Management Console using your AWS management account.
2. Open the AWS Marketplace console.
3. In the left navigation pane, choose **Settings**.
4. Under **Private Marketplace Settings**, choose **Edit integrations**.
5. Choose **Enable trusted access across your organization**.
6. Choose **Create a Private Marketplace service-linked role for this account**.
7. Choose **Create integration**.

After completing this setup, you can configure mandatory purchase orders and custom messaging for your organization.

## Configuring mandatory purchase orders

Administrators can configure AWS Marketplace to require users to enter a purchase order number before subscribing to any product. This capability helps ensure that every AWS Marketplace subscription is properly authorized and tracked according to your organization's procurement policies.

When mandatory purchase orders are enabled, users cannot complete a subscription without providing a value in the purchase order field. This enforcement happens at the point of subscription, preventing unauthorized purchases before they occur.

###### Configuration options

You can configure mandatory purchase order enforcement with the following flexibility:

- **All purchases:** Require a PO for every AWS Marketplace subscription in your organization.
- **Specific offer types:** Require a PO only for private offers, public offers, or both.
- **Specific pricing types:** Require a PO for contract pricing, pay-as-you-go pricing, or both.

### Enabling mandatory purchase orders

The following steps explain how to enable mandatory purchase orders for your organization.

###### To enable mandatory purchase orders

1. Sign in to the AWS Management Console using your AWS management account.
2. Open the AWS Marketplace console.
3. In the left navigation pane, choose **Organizational procurement settings**.
4. Under **Mandatory purchase orders**, choose **Configure**.
5. Select the offer types and pricing types for which you want to require purchase orders.
6. Choose **Save**.

The changes take a few hours for configuration to apply for all users in your organization.

###### Note

If you choose to require purchase orders for pay-as-you-go public offers in AWS Marketplace, you will prevent AWS Marketplace subscriptions through service consoles, like Amazon EC2, as those service consoles don't allow adding purchase orders. End buyers will need to procure directly through AWS Marketplace. Mandatory purchase order settings do not apply for Amazon Bedrock serverless purchases made through the Amazon Bedrock console. You can update purchase orders for existing AWS Marketplace subscriptions post subscription in the AWS Marketplace console.

## Configuring custom procurement messaging

Administrators can configure custom messages that display to users when they encounter procurement requirements, such as mandatory purchase order fields. These messages help users understand why information is required and what they should enter.

###### What to include in custom messages

Your custom message can include the following types of information:

- **Policy references:** Link to your organization's procurement policies.
- **Format requirements:** Explain the expected purchase order number format.
- **Validation instructions:** Direct users to verify purchase order numbers in your procure-to-pay system.
- **Compliance information:** Clarify the implications of non-compliance with procurement policies.
- **Support contacts:** Provide resources for users who need assistance obtaining a purchase order.

The following example shows how you might structure a guidance message for your users:

###### Example Sample custom procurement message

"A valid purchase order number is required for all AWS Marketplace subscriptions in accordance with our company procurement policy. Purchase order numbers must match an approved purchase order in our procurement system. AWS Marketplace subscriptions are logged in AWS CloudTrail. For assistance, contact your procurement team or refer to the procurement guidelines in the company portal."

###### Note

You can customize this message with links to your internal procurement systems and policies.

When enabled, this message will be displayed to your end buyers on the procurement page in AWS Marketplace.

### Adding a custom message

The following steps explain how to add a custom procurement message for your organization.

###### To add a custom procurement message

1. Sign in to the AWS Management Console using your AWS management account.
2. Open the AWS Marketplace console.
3. In the left navigation pane, choose **Organizational procurement settings**.
4. Under **Custom messaging**, choose **Add message**.
5. Enter your custom message text. Include relevant policy information, format requirements, and contact details for your procurement team.
6. Choose **Save**.

The custom message takes a few hours for configuration to apply and then displays to users in your organization when they encounter the purchase order field during the subscription process.

### Updating or removing a custom message

You can update or remove your custom procurement message at any time.

###### To update a custom message

1. Sign in to the AWS Management Console using your AWS management account.
2. Open the AWS Marketplace console.
3. In the left navigation pane, choose **Organizational procurement settings**.
4. Under **Custom messaging**, choose **Edit**.
5. Update your message text, or clear the field to remove the message.
6. Choose **Save**.
