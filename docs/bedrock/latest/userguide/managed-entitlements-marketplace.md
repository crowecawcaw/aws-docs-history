

# Distribute through AWS Marketplace

When your management account or delegated administrator account accepts a private offer for a third-party model in Amazon Bedrock, you can distribute it from AWS Marketplace. You can distribute on the purchase confirmation page, right after you accept the offer. You can also distribute later from the agreement.

AWS sets up AWS License Manager, creates the grants, and activates them for every account in your organization. Member accounts don't need to take any action.

**Note**  
You can't distribute private offers that you accept as part of an offer set on the purchase confirmation page. After you accept an offer set, distribute each private offer later from its agreement, as described in [Distributing a private offer that you already accepted](#managed-entitlements-distribute-marketplace-later). An offer set is a package of two to seven private offers that a seller groups together so that you can review and accept them with a single action. Each offer in the set keeps its own pricing and terms, and each product creates its own agreement. For more information, see [Understanding offer sets](https://docs.aws.amazon.com/marketplace/latest/buyerguide/understanding-offer-sets.html) in the *AWS Marketplace Buyer Guide*.  
Distribution from AWS Marketplace always targets your entire organization. To distribute public offers, or to distribute to specific accounts or organizational units (OUs), see [Distribute through AWS License Manager](managed-entitlements-license-manager.md).

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
If you leave the purchase confirmation page without choosing **Distribute**, member accounts continue to be billed at public rates until you distribute grants. To distribute the offer later, see [Distributing a private offer that you already accepted](#managed-entitlements-distribute-marketplace-later).

## Distributing a private offer that you already accepted
<a name="managed-entitlements-distribute-marketplace-later"></a>

If you didn't distribute a private offer when you accepted it, you can distribute it later from the agreement. This includes private offers that you accepted as part of an offer set, because each offer in the set has its own agreement. Sign in to the account that accepted the offer. That account must be your management account or your delegated administrator account.

**To distribute a private offer that you already accepted**

1. Open the [Manage subscriptions](https://console.aws.amazon.com/marketplace/home#/subscriptions) page in the AWS Marketplace console.

1. To find agreements that you haven't distributed, filter the list by **Distribution status** = **Not distributed**.

1. For the agreement that you want to distribute, choose **View distribution**. The agreement details page opens.

1. In **Distribute to member accounts**, review the distribution details, and then choose **Distribute**.

1. You can leave the page, because distribution continues in the background. Most distributions complete within an hour. Depending on the size of your organization, distribution might take longer. When distribution is complete, the agreement shows **Distributed** in the **Distribution status** column.

## Understanding distribution status
<a name="managed-entitlements-distribute-marketplace-status"></a>

On the **Manage subscriptions** page, the **Distribution status** column shows whether you distributed each agreement for a private offer for a third-party model in Amazon Bedrock to your organization. Other agreements don't show a distribution status.


**Distribution status values**  

| Status | Description | 
| --- | --- | 
| Distributed | You distributed the agreement to your organization, or distribution is in progress. This status also appears when you already distributed the license to specific accounts or OUs in AWS License Manager. To change that distribution, use AWS License Manager. | 
| Not distributed | You haven't distributed the agreement to your organization, or the grant isn't active in every member account. Member accounts that don't have an active grant are billed at public rates. To distribute, choose View distribution. | 
| Unknown | AWS Marketplace couldn't read the distribution status, usually because your IAM identity is missing the permissions listed in [Granting permissions to distribute from AWS Marketplace](managed-entitlements-prerequisites.md#managed-entitlements-marketplace-permissions). To see the error message, filter the list by Distribution status = Unknown. | 

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