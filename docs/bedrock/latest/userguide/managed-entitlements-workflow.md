

# Workflow overview
<a name="managed-entitlements-workflow"></a>

You can distribute a license in two ways. How you distribute depends on what you subscribed to and how you accepted it.

Distribution from AWS Marketplace isn't available for private offers that you accept as part of an offer set. An offer set groups two to seven private offers from a seller into one package that you accept with a single action. Each offer keeps its own pricing and terms, and each product creates its own agreement. For more information, see [Understanding offer sets](https://docs.aws.amazon.com/marketplace/latest/buyerguide/understanding-offer-sets.html) in the *AWS Marketplace Buyer Guide*.

The following table describes when to use each distribution method.


| Use case | Use | 
| --- | --- | 
| You received a private offer for a third-party model in Amazon Bedrock, not as part of an offer set, and haven't accepted it yet | Distribute through AWS Marketplace. Accept the offer from your management account or delegated administrator account, and then choose Distribute on the purchase confirmation page. AWS handles setup and activation for you. | 
| You already accepted a private offer for a third-party model but didn't distribute it at that time | Distribute through AWS License Manager | 
| You want to distribute to specific accounts or organizational units (OUs) instead of your entire organization | Distribute through AWS License Manager | 
| You received a private offer as part of an offer set | Distribute through AWS License Manager | 
| You have a public offer subscription, including a subscription that Amazon Bedrock created when you first invoked a model | Distribute through AWS License Manager | 

After you distribute, you can view, deactivate, or delete grants in AWS License Manager, no matter which option you used.

## Distribute through AWS Marketplace
<a name="managed-entitlements-workflow-marketplace"></a>

Use this option for private offers for third-party models in Amazon Bedrock that you accept from your management account or delegated administrator account. You distribute on the purchase confirmation page. Private offers that you accept as part of an offer set are not supported.

1. **Accept the private offer**: Accept the offer in AWS Marketplace from your management account or your delegated administrator account. To distribute from the delegated administrator account, register it as the delegated administrator before you accept the offer, and then accept the offer from that account.

1. **Distribute**: On the purchase confirmation page, choose **Distribute**.

1. **AWS completes setup**: If your organization is not already set up, License Manager creates the required service-linked roles and links your AWS Organizations accounts. The setup stays in place for future distributions.

1. **Use the model**: AWS creates and activates grants for every account in your organization. Member accounts do not need to accept or activate the grant.

For more information, see [Distribute through AWS Marketplace](managed-entitlements-marketplace.md).

## Distribute through AWS License Manager
<a name="managed-entitlements-workflow-license-manager"></a>

Use this option for public offers and for private offers that you accept as part of an offer set. For other private offers, use this option if you did not distribute from the purchase confirmation page, or if you want to distribute to specific accounts or OUs. For more information, see [Distribute through AWS License Manager](managed-entitlements-license-manager.md).

**Step 1 - Subscribe**: Subscribe to a third-party Bedrock serverless model through AWS Marketplace (either through auto-enablement or private offer).

**Step 2 - License creation**: A license is automatically generated in us-east-1, representing your entitlement. You can view this license in AWS License Manager under Granted Licenses.

**Steps 3 - Create and distribute grants**: Create grants to distribute the license. Grants can target individual AWS account IDs, your entire organization ID, or specific organizational units (OUs).
+ Individual AWS account IDs – The grant appears in the recipient's AWS License Manager
+ Organization ID – Grants are distributed to all member accounts automatically
+ Organizational units (OUs) – Grants are distributed to all accounts in the OU

**Step 4 - Activate**: Grants must be activated before the model can be used:
+ Individual grants: Recipient accepts and activates their own grant
+ Organization/OU grants: Management account can bulk-activate all grants, or recipients activate individually

**Step 5 - Use the model**: After activation, you can invoke the model in your entitled account using the Amazon Bedrock console, AWS CLI, or AWS SDKs.