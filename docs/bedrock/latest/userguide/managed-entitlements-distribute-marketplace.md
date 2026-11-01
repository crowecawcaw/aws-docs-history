

# Distributing from AWS Marketplace
<a name="managed-entitlements-distribute-marketplace"></a>

Use the following steps to distribute a private offer to every account in your organization when you accept it. You don't need to set up AWS License Manager, create grants, or activate them first.

**Note**  
You can distribute from AWS Marketplace only on the purchase confirmation page, right after you accept the offer. Distribution always targets your entire organization.

## Before you begin
<a name="managed-entitlements-distribute-marketplace-prereqs"></a>
+ Make sure your organization has all features enabled. To check, open the AWS Organizations console, choose **Settings**, and confirm that **Feature set** shows **All features**. For more information, see [Enabling all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the *AWS Organizations User Guide*.
+ Sign in to your organization's management account or your delegated administrator account. The account that you sign in to must be the account that accepts the private offer. If you use a delegated administrator, register it before you accept the offer, as described in [Step 1: Determine if you need a delegated admin](managed-entitlements-setup.md#managed-entitlements-delegated-admin).
+ Make sure that your IAM identity has the permissions listed in [Granting permissions to distribute from AWS Marketplace](managed-entitlements-prerequisites.md#managed-entitlements-marketplace-permissions).

## Distributing a private offer when you accept it
<a name="managed-entitlements-distribute-marketplace-steps"></a>

**To distribute a private offer when you accept it**

1. Open the [AWS Marketplace console](https://console.aws.amazon.com/marketplace/), choose **Private offers**, and then choose the offer. Alternatively, choose the private offer link that the seller sent you. For more information, see [Private offers page in AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/private-offers-page.html) in the *AWS Marketplace Buyer Guide*.

1. Review the subscription agreement and pricing details.

1. Choose **Subscribe** to accept the offer.

1. On the purchase confirmation page, review the distribution details.

1. Choose **Distribute**.

1. Wait for distribution to complete. AWS Marketplace shows that distribution is in progress. You can leave the page, because distribution continues in the background. Most distributions complete within an hour. Depending on the size of your organization, distribution might take longer.

**Important**  
If you leave the purchase confirmation page without choosing **Distribute**, member accounts continue to be billed at public rates until you distribute grants. To distribute the offer later, see [Distribute through AWS License Manager](managed-entitlements-license-manager.md).

## Understanding what AWS sets up when you choose Distribute
<a name="managed-entitlements-distribute-marketplace-setup"></a>

If your organization is not already set up, AWS License Manager performs the following actions for you:

1. Adds [service-linked roles](https://docs.aws.amazon.com/license-manager/latest/userguide/using-service-linked-roles.html) to every account in your organization.

1. Creates a resource share and adds every account in your organization to it.

1. Turns on grant distribution to your organization ID, so you can distribute grants to every account at once.

1. Turns on automatic grant acceptance, so accounts in your organization accept grants that you distribute to them or to your organization ID.

**Important**  
This setup stays in place for future distributions. Grants that your management account or delegated administrator account later distributes to accounts in your organization, including grants for other products, are also accepted automatically.

## Reviewing grants after you distribute
<a name="managed-entitlements-distribute-marketplace-after"></a>

Grants distributed from AWS Marketplace are created in the Active state for every account in your organization. Member accounts don't need to accept or activate the grant.

For information about viewing the grants, see [Tracking distributed grants](managed-entitlements-distributing.md#managed-entitlements-tracking-grants). You can deactivate or delete these grants in AWS License Manager.