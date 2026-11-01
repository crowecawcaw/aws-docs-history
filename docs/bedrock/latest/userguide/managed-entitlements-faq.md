

# Frequently asked questions
<a name="managed-entitlements-faq"></a>

## Setup and configuration
<a name="managed-entitlements-faq-setup"></a>

**Q: My organization uses consolidated billing only. Can I still use managed entitlements?**

A: Yes, but with limitations. Organizations with consolidated billing can use managed entitlements, but grants will require manual acceptance in each recipient account. For the best experience, we recommend enabling all features in your organization, which allows automatic grant acceptance and organization-wide distribution.

**Q: Can I use a member account instead of the management account to manage licenses?**

A: Yes. You can designate a delegated administrator account to manage license distribution. This member account can create and distribute grants independently from the management account. However, only one delegated administrator is supported per organization.

**Q: Which account should I use to accept a private offer so that I can distribute it from AWS Marketplace?**

A: If you use AWS Organizations, request that the private offer be issued to your management account, and accept it from that account. To use a different account, register it as your delegated administrator first. Then accept the offer from that account. If you accept the offer from any other account, you cannot distribute it from AWS Marketplace, and you must create grants in AWS License Manager instead.

**Q: Do I need to set up managed entitlements in every AWS Region?**

A: No. All license management happens in the us-east-1 (N. Virginia) region regardless of where you use Bedrock models. Once you complete setup in us-east-1, you can invoke licensed models in any supported Bedrock region.

## Private Offers and pricing
<a name="managed-entitlements-faq-pricing"></a>

**Q: How does managed entitlements work with AWS Marketplace Private Offers?**

A: Managed entitlements allows you to accept Private Offers in your management account and then distribute access to additional linked accounts. When you create grants, the Private Offer pricing and terms automatically apply to all recipient accounts. This ensures consistent pricing across your organization and eliminates the need for each account to individually accept the offer.

**Q: Who gets billed when a member account uses a granted license?**

A: Your organization's management account is billed for all usage across granted accounts. This applies regardless of which account holds the original subscription. For example, if a delegated administrator account subscribes and distributes grants, the charges still go to the management account. This centralized billing provides clear visibility into total Amazon Bedrock costs across your organization.

**Q: Can different member accounts have different pricing for the same model?**

A: No. When you distribute licenses through managed entitlements, all recipient accounts use the same pricing terms as the original subscription, including any Private Offer discounts.

**Q: I accepted a private offer in my management account or delegated administrator account. Why are member accounts still billed at public rates?**

A: A private offer applies only to the account that accepts it. Member accounts that invoke the model without an active grant are billed at public rates. To apply your negotiated pricing, distribute grants from the purchase confirmation page when you accept the offer, or later from AWS License Manager.

**Q: Which subscriptions can I distribute from AWS Marketplace?**

A: Distribution from AWS Marketplace is available for private offers for third-party models in Amazon Bedrock, except private offers that you accept as part of an offer set. For all other subscriptions, including public offers, offer sets, and other AWS Marketplace products such as AMIs, create and activate grants in AWS License Manager, as described in [Distribute through AWS License Manager](managed-entitlements-license-manager.md).

**Q: Can I distribute a private offer that I accepted as part of an offer set from AWS Marketplace?**

A: No. Private offers that you accept as part of an offer set are not supported for distribution from AWS Marketplace. To distribute these private offers, create grants in AWS License Manager, as described in [Distribute through AWS License Manager](managed-entitlements-license-manager.md).

## License distribution
<a name="managed-entitlements-faq-distribution"></a>

**Q: How long does it take for grants to appear in recipient accounts?**

A: For organization grants, most distributions complete within an hour. Depending on the size of your organization, distribution might take longer. To verify grant status, review the grant in AWS License Manager.

**Q: Do I need to create a grant for every account that needs access?**

A: No. If your organization has all features enabled, create a single grant to your Organization ID to automatically distribute licenses to all member accounts, including accounts that join later. Otherwise, create individual grants or grants to organizational units (OUs).

**Q: What happens when a new account joins my organization?**

A: If you distributed a grant to your Organization ID, new accounts automatically receive the license and access to the model. For individual account grants, you must manually create a grant for the new account.

**Q: Can I distribute licenses to accounts outside my organization?**

A: No. Managed entitlements only works within your AWS Organization. You cannot share licenses with accounts that are not part of your organization structure.

**Q: Can I grant access to specific organizational units (OUs) instead of my entire organization?**

A: Yes. When creating a grant, you can specify an OU ID to distribute licenses only to accounts within that OU. This provides a middle ground between individual account control and organization-wide distribution.

**Q: I have existing subscriptions in multiple member accounts. How do I migrate to centralized management?**

A: When member accounts have active Bedrock models and their payer account distributes them a subscription to the same model, grant swap takes effect, the entitlements to the first subscription is disabled and they now have entitlements on the new distributed grant.

**Q: Do member accounts need to accept or activate grants distributed from AWS Marketplace?**

A: No. When you distribute from AWS Marketplace, AWS creates and activates grants for every account in your organization, and member accounts do not need to take any action. For grants that you create in AWS License Manager, the steps in [Accepting and activating grants](managed-entitlements-accepting.md) still apply.

**Q: Can I choose which accounts receive a grant when I distribute from AWS Marketplace?**

A: No. Distribution from AWS Marketplace targets your entire organization. To distribute to specific accounts or OUs, create grants in AWS License Manager.

**Q: I accepted a private offer for a third-party model in Amazon Bedrock but did not distribute it to my organization at that time. How do I distribute it now?**

A: Distribute it through AWS License Manager. Create grants as described in [Distributing licenses](managed-entitlements-distributing.md), and then activate them as described in [Accepting and activating grants](managed-entitlements-accepting.md). You can distribute from AWS Marketplace only on the purchase confirmation page, right after you accept a private offer. Until you distribute it, member accounts are billed at public rates.

**Q: What happens if distribution fails for some accounts?**

A: Check the status of the license and its grants in AWS License Manager, as described in [Tracking distributed grants](managed-entitlements-distributing.md#managed-entitlements-tracking-grants). Accounts that succeeded keep their grants. After you resolve the issue for the remaining accounts, create grants for them in AWS License Manager.

## Grant management
<a name="managed-entitlements-faq-management"></a>

**Q: Can I temporarily revoke access without deleting the grant?**

A: Yes. You can deactivate the grant to move it to a Disabled state. However, deactivating a grant does not block model access — the member account can still invoke the model. What changes is the billing: while the grant is disabled, the member account will be billed at public rates instead of your negotiated private offer pricing. You can reactivate the grant later to restore private offer terms without needing to recreate it.

**Q: What happens to model access if I delete or deactivate a grant?**

A: The member account will continue to have model access — deleting or deactivating a grant does not interrupt the ability to invoke the model. However, without an active grant, the member account will be billed at public rates instead of any negotiated private offer pricing.

**Q: Can I see which accounts are actually using the licenses I distributed?**

A: In AWS License Manager, you can view which accounts have grants and their activation status. For detailed usage metrics and API call tracking, use AWS CloudTrail. For model invocation metrics, use the Amazon Bedrock console or CloudWatch metrics in each account.

**Q: If I delete a grant by mistake, can I restore it?**

A: No. Deleting a grant is permanent and cannot be undone. However, you can create a new grant to the same account with the same configuration. Model access will not be disrupted — the member account can continue invoking the model during the gap. The key impact is billing: for the duration between the grant deletion and the new grant activation, the member account will be billed at public rates rather than any negotiated private offer pricing.

**Q: What happens to granted licenses in linked accounts when the parent subscription expires in the management account?**

A: The linked accounts will lose access to the model when the parent subscription expires in the management account.

**Q: What happens to distributed grants when my private offer renews or is upgraded?**

A: Grants that you already distributed to member accounts carry forward automatically. You do not need to redistribute when your private offer renews or is upgraded with a new agreement. Member accounts continue to be billed at your negotiated rate without any action from the management account or delegated administrator.

## Special configurations
<a name="managed-entitlements-faq-special"></a>

**Q: How does managed entitlements work for AWS GovCloud customers?**

A: GovCloud customers have a commercial AWS account linked to a GovCloud account. Subscribe to Bedrock models and manage licenses in the commercial account organization hierarchy. When you grant a license to a commercial linked account, the associated GovCloud account automatically receives entitlement and can invoke the model.

**Q: Can I use managed entitlements with AWS Control Tower or AWS Service Catalog?**

A: Yes. You can integrate managed entitlements APIs into your AWS Control Tower account factory or Service Catalog portfolios to automate license distribution when new accounts are created.

**Q: Can multiple management accounts subscribe to the same Bedrock model?**

A: Yes. Different accounts can subscribe to the same model independently. Each subscription creates its own separate license that can be distributed to different sets of member accounts.

## Troubleshooting
<a name="managed-entitlements-faq-troubleshooting"></a>

**Q: Why don't I see my license in License Manager after subscribing?**

A: Licenses can take 1-2 minutes to appear after subscription. Make sure you're viewing License Manager in the us-east-1 Region, as all licenses are created there regardless of where you subscribed. If it still doesn't appear after 5 minutes, verify your subscription is active in the AWS Marketplace console.

**Q: My recipient account can't see the grant I created. What should I check?**

A: Verify the recipient is checking License Manager in the us-east-1 Region. Confirm you entered the correct 12-digit account ID when creating the grant. Allow time for grant distribution. Most distributions complete within an hour, and larger organizations might take longer. For organizations without all features enabled, ensure the recipient account has service-linked roles created.

**Q: Why can't I activate a grant in my account?**

A: Check that the grant is in Disabled or Pending Acceptance state. If you already have an active license for the same model, deactivate or delete it first. Make sure you have the `license-manager:CreateGrantVersion` IAM permission. For consolidated billing organizations, confirm you accepted the grant before attempting activation.