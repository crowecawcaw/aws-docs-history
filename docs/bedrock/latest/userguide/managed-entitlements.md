

# Manage model subscriptions with AWS License Manager
<a name="managed-entitlements"></a>

**Note**  
The following guidance applies only to third-party serverless models that require AWS Marketplace subscriptions.

Organizations with multiple AWS accounts often need to provide third-party Bedrock model access across many accounts. Without centralized management, each account must have AWS Marketplace permissions and create its own subscriptions—adding operational overhead and making it difficult to enforce consistent access policies.

Managed entitlements for Amazon Bedrock solves this by letting you subscribe once from a management account and distribute access to member accounts across your AWS Organization. It works with both types of Bedrock subscriptions:
+ **Auto-enablement** – When Bedrock automatically creates a subscription on first model invocation
+ **Private offers** – Custom pricing and terms negotiated with a seller through AWS Marketplace. After you accept a private offer, you can distribute it to your organization directly from AWS Marketplace.

The distribution workflow uses AWS License Manager. When you subscribe to a model, a license is automatically created, and you create grants to share that license with other accounts in your organization.

You can distribute in two ways.
+ **Through AWS Marketplace** – Distribute a private offer for a third-party model in Amazon Bedrock on the purchase confirmation page, right after you accept it from your management account or delegated administrator account. AWS creates and activates grants for every account in your organization. This option isn't available for private offers that you accept as part of an offer set. An offer set is a package of private offers for multiple products that a seller groups together so that you can review and accept them with a single action. For more information about offer sets, see [Understanding offer sets](https://docs.aws.amazon.com/marketplace/latest/buyerguide/understanding-offer-sets.html) in the *AWS Marketplace Buyer Guide*. For more information about this option, see [Distribute through AWS Marketplace](managed-entitlements-marketplace.md).
+ **Through AWS License Manager** – Distribute any subscription, including public offers and offer sets, to your organization, organizational units (OUs), or specific accounts. You create and activate the grants yourself. You can use this option for all third-party Bedrock model subscriptions. For more information, see [Distribute through AWS License Manager](managed-entitlements-license-manager.md).

To distribute from the delegated administrator account through AWS Marketplace, register it as the delegated administrator before you accept the private offer. Then accept the offer from that account.

**Important**  
When your management account or delegated administrator account accepts a private offer, the negotiated pricing applies only to that account. Member accounts that invoke the model without an active grant are billed at public rates. To apply your private offer pricing across your organization, distribute grants after you accept the offer.

**Recommendation**: If you use AWS Organizations, request that private offers for third-party models in Amazon Bedrock be issued to your management account. Accept the offer from that account so that you can distribute it directly from AWS Marketplace. To use a different account, register it as your delegated administrator before you accept the offer. Then accept the offer from that account. Only the account that accepts a private offer can distribute it, and you can't change that account later. For more information about registering a delegated administrator, see [Step 1: Determine if you need a delegated admin](managed-entitlements-setup.md#managed-entitlements-delegated-admin).

**Note**  
All licenses are created in the us-east-1 region, regardless of where you subscribe or invoke models.