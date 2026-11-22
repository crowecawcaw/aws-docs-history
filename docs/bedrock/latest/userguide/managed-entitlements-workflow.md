

# Workflow overview

You can distribute a license in two ways. The method that you use depends on what you subscribed to, how you accepted it, and which accounts you want to receive it.


**Distribution methods**  

| Distribution method | Use it when | 
| --- | --- | 
| [Distribute through AWS Marketplace](managed-entitlements-marketplace.md) | You have a private offer for a third-party model in Amazon Bedrock that you accept from your management account or delegated administrator account, and you want to distribute it to your entire organization. AWS handles setup and activation for you. You can distribute in either of the following ways:+  When you accept the offer, on the purchase confirmation page. This isn't available for private offers that you accept as part of an offer set. <br />+  Later, from the agreement on the **Manage subscriptions** page.  | 
| [Distribute through AWS License Manager](managed-entitlements-license-manager.md) | You create and activate the grants yourself. Use this method when any of the following apply:+  You want to distribute to specific accounts or organizational units (OUs) instead of your entire organization. <br />+  You have a public offer subscription, including a subscription that Amazon Bedrock created when you first invoked a model.  | 

You can't distribute private offers that you accept as part of an offer set on the purchase confirmation page. After you accept an offer set, each offer has its own agreement, which you can distribute later from the **Manage subscriptions** page. An offer set groups two to seven private offers from a seller into one package that you accept with a single action. Each offer keeps its own pricing and terms, and each product creates its own agreement. For more information, see [Understanding offer sets](https://docs.aws.amazon.com/marketplace/latest/buyerguide/understanding-offer-sets.html) in the *AWS Marketplace Buyer Guide*.

After you distribute, you can view, deactivate, or delete grants in AWS License Manager, no matter which method you used.

## Distribute through AWS Marketplace
<a name="managed-entitlements-workflow-marketplace"></a>

The following steps summarize how distribution from AWS Marketplace works. For instructions on distributing through AWS Marketplace, see [Distribute through AWS Marketplace](managed-entitlements-marketplace.md).

1. **Accept the private offer**: Accept the offer in AWS Marketplace from your management account or your delegated administrator account. To distribute from the delegated administrator account, register it as the delegated administrator before you accept the offer, and then accept the offer from that account.

1. **Distribute**: On the purchase confirmation page, choose **Distribute**. If you didn't distribute then, choose **View distribution** for the agreement on the **Manage subscriptions** page, and then choose **Distribute**.

1. **AWS completes setup**: If your organization isn't already set up, AWS License Manager creates the required service-linked roles and links your AWS Organizations accounts. The setup stays in place for future distributions.

1. **Use the model**: AWS creates and activates grants for every account in your organization. Member accounts don't need to accept or activate the grant.

## Distribute through AWS License Manager
<a name="managed-entitlements-workflow-license-manager"></a>

The following steps summarize how distribution through AWS License Manager works. For instructions on distributing through AWS License Manager, see [Distribute through AWS License Manager](managed-entitlements-license-manager.md).

1. **Subscribe**: Subscribe to a third-party model in Amazon Bedrock through AWS Marketplace, either through a private offer or by invoking the model for the first time.

1. **Find the license**: AWS creates a license for your subscription in the US East (N. Virginia) Region. You can view it in AWS License Manager under **Granted licenses**.

1. **Create grants**: Create grants to distribute the license to any of the following recipients:
   + **Individual AWS account IDs**: The grant appears in each recipient account's AWS License Manager.
   + **Your organization ID**: The grant is distributed to every member account automatically.
   + **Organizational units (OUs)**: The grant is distributed to every account in the OU.

1. **Activate grants**: Activate the grants before member accounts can use the model.
   + **Individual account grants**: Each recipient accepts and activates its own grant.
   + **Organization and OU grants**: The management account can activate all grants at once, or each recipient can activate its own grant.

1. **Use the model**: After activation, invoke the model from the recipient account by using the Amazon Bedrock console, the AWS CLI, or the AWS SDKs.