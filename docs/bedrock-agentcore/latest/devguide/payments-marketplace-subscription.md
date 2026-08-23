# Subscribe to Coinbase Wallets for AgentCore Payments in AWS Marketplace

To use Coinbase as a payment provider with AgentCore payments, you must subscribe to the **Coinbase Wallets for AgentCore Payments** listing in AWS Marketplace. With this subscription, your Coinbase wallet usage charges are consolidated into your monthly AWS bill based on Coinbase’s [pricing](https://docs.cdp.coinbase.com/wallets/pricing "https://docs.cdp.coinbase.com/wallets/pricing") on the Coinbase website. There are no additional charges or obligations for the subscription. The subscription is mandatory. Until an active subscription exists in your AWS account, AgentCore payments rejects Coinbase connector creation and Coinbase wallet operations with a `SubscriptionRequiredException` error. For more information about this error, see [AWS Marketplace subscription errors](payments-troubleshooting.md#payments-troubleshooting-subscription "payments-troubleshooting.md#payments-troubleshooting-subscription").

###### Note

The AWS Marketplace subscription applies only to the Coinbase payment provider. Connectors that use other providers, such as Stripe (Privy), do not currently require a Marketplace subscription.

You can subscribe from all AWS Regions where AgentCore payments is available. See [Supported AWS Regions](agentcore-regions.md "agentcore-regions.md").

## How billing works

When you subscribe to the listing, your Coinbase wallet usage is metered through AWS Marketplace and billed on your AWS bill. Coinbase does not bill you separately for the wallet usage that you incur through AgentCore payments.

The metering is done based on Coinbase’s [public pricing](https://docs.cdp.coinbase.com/wallets/pricing "https://docs.cdp.coinbase.com/wallets/pricing") on the Coinbase website. There are no additional charges beyond that. Your account also remains eligible for the Coinbase free tier described in the [pricing page](https://docs.cdp.coinbase.com/wallets/pricing "https://docs.cdp.coinbase.com/wallets/pricing") on the Coinbase website.

For current pricing and terms, see the [Coinbase Wallets for AgentCore Payments](https://aws.amazon.com/marketplace/pp/prodview-ia2zd5puqyi7g "https://aws.amazon.com/marketplace/pp/prodview-ia2zd5puqyi7g") listing in AWS Marketplace.

## Required IAM permissions

The IAM identity that subscribes to the listing must be allowed to manage AWS Marketplace subscriptions. This is typically the administrator who creates payment managers and connectors (the ControlPlaneRole). For more information about this persona, see [Administrator permissions (ControlPlaneRole)](payments-iam-roles.md#payments-iam-admin "payments-iam-roles.md#payments-iam-admin").

Attach the AWS managed policy **AWSMarketplaceManageSubscriptions** to that identity. For more information, see [AWSMarketplaceManageSubscriptions](../../../aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.md") in the _AWS Managed Policy Reference Guide_.

## Subscribe to the listing

You can subscribe either directly from the AWS Marketplace listing page or from the Amazon Bedrock AgentCore console.

###### Example

AWS Marketplace

1. Open the [Coinbase Wallets for AgentCore Payments](https://aws.amazon.com/marketplace/pp/prodview-ia2zd5puqyi7g "https://aws.amazon.com/marketplace/pp/prodview-ia2zd5puqyi7g") listing in AWS Marketplace.
2. Choose **View purchase options**.
3. Review the pricing details and the terms and conditions.
4. Choose **Subscribe**.
5. Wait for the subscription to become active. When the subscription is active, you can create a Coinbase payment connector. See [Create a Payment Manager and Connector](payments-create-manager.md "payments-create-manager.md").

Amazon Bedrock AgentCore console
The Amazon Bedrock AgentCore console provides several entry points to subscribe:

- **Payments page** — In the navigation pane, under **Build**, choose **Payments**. In the **How it works** section, under **Create payment manager with connectors**, choose **Subscribe on AWS Marketplace**.
- **Create Payment Manager wizard** — On the **Add payment connector** step, if you configure a Coinbase connector and your account is not subscribed, the console displays a **Subscribe to Coinbase to enable billing through AWS** alert with a **Subscribe** button.
- **Create connector page** — If you create a Coinbase connector and your account is not subscribed, the page displays the same alert with a **Subscribe** button.

Choosing **Subscribe** opens the **Coinbase Wallets for AgentCore Payments** offer from AWS Marketplace in the console, where you can review the product details, pricing, and terms and conditions. Choose **Subscribe** to complete the subscription. After the subscription is active, continue creating your Coinbase connector. See [Create a Payment Manager and Connector](payments-create-manager.md "payments-create-manager.md").

After the subscription is active, continue with [creating a Payment Manager and Connector](payments-create-manager.md "payments-create-manager.md").
