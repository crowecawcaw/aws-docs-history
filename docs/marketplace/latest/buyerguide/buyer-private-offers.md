# Private offers in AWS Marketplace

The AWS Marketplace seller private offer feature enables you to receive product pricing and EULA
terms from a seller. These terms aren't publicly available. You negotiate pricing and terms with the
seller, and the seller creates a private offer for the AWS account that you designate. You
accept the private offer and start receiving the negotiated price and terms of use.

After you subscribe to the private offer, the outcome when the agreement expires depends on the product type. You will either automatically move to the product's public pricing or lose your subscription to the product.

If you're using the consolidated billing feature in AWS Organizations, you can accept the private
offer from either the organization's management account or from a member account. If you accept
from the management account, the private offer can be shared with all member accounts in the
organization. Member accounts that were previously subscribed to the product must also accept
the new private offer to benefit from the pricing. Alternatively, for AMI and Container
products, you can share the license from the management account to member accounts using AWS
License Manager. Member accounts that weren't previously subscribed to the product must accept
the private offer to be able to deploy the product.

For more information on consolidated billing, see [Consolidated Billing for Organizations](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md")
in the _AWS Billing User Guide_. The following are key points to
remember as you start using your private offers.

- AWS Marketplace buyers can access third-party financing services for private offers. For more
  information, see [Customer financing is now available in AWS Marketplace](https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/Financing+External+Briefing+Document+Customer+Facing.pdf "https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/Financing+External+Briefing+Document+Customer+Facing.pdf").
- There is no difference in the software product that you purchase using a private offer.
  The software you purchase through a private offer functions the same as if you purchased it
  without a private offer.
- Product subscriptions you purchase with a private offer show up like any other AWS Marketplace
  product in your monthly bill. You can use detailed billing to view your usage for each of
  your AWS Marketplace-purchased products. Each of your private offers has a line item corresponding to
  each kind of usage.
- Subscribing to a private offer doesn't require launching a new instance of the software.
  Accepting the private offer modifies the price to correspond to your private offer price. If
  a product offers a 1-click launch, you can deploy a new instance of the software. If a
  product defaults to 1-click launch, you can accept a private offer without launching a new
  instance. To launch without deploying a new instance, choose **Manual
  Launch** on the fulfillment page. You can use the Amazon Elastic Compute Cloud console to deploy
  additional instances, just as you would for other AWS Marketplace products.
- When a seller extends a private offer to you, you receive confirmation on the account
  the seller included in a private offer. Private offers are linked to the specific
  buyer's account listed. The software seller creates the private offer for the account that
  you specify. Each private offer can be made to up to 25 accounts.
- When you accept a private offer, it becomes an _agreement_ (also
  known as a _contract_ or _subscription_) between you
  and the seller.
- Sellers may offer to upgrade or renew your purchase of a SaaS contract or SaaS contract
  with consumption product. For example, a seller can create a new private offer to grant new
  entitlements, offer pricing discounts, adjust payment schedules, or change the end user
  license agreement (EULA) to use [standardized license
  terms](../userguide/standardized-license-terms.md "../userguide/standardized-license-terms.md").

These renewals or upgrades are changes to the original private offer that you accepted,
and you use the same process for accepting them. If you accept the new upgrade or renewal
private offer, the new agreement terms take effect immediately, without any break in
software service. Any previous terms or remaining scheduled payments are cancelled and
replaced by this new agreement's terms.

- You can review all of your annual software subscriptions in AWS Marketplace under **Your
  Software**. If an annual subscription is purchased by one account using AWS Organizations
  for consolidated billing, it is shared across the entire linked account family. If the
  purchasing account doesn't have any running instances, the annual subscription is counted
  toward the usage in another linked account running that software. For more information about
  annual subscriptions, see [AMI subscriptions in AWS Marketplace](buyer-ami-subscriptions.md "buyer-ami-subscriptions.md").
- When a private offer expires, you can't subscribe to it. However, you can contact the
  seller. Ask the seller to change the expiration date on the current offer to a future date
  or create a new private offer for you.
