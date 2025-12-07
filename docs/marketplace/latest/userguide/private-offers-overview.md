# Preparing a private offer for your AWS Marketplace product

Private offers are negotiated terms used to purchase a product from AWS Marketplace. This can
involve a custom pricing plan, end user license agreement (EULA), or custom solutions. Sellers
and buyers negotiate before committing to a private offer that's different from the public
offer. You can create and extend multiple private offers to a single buyer. Buyers that you
extend a private offer to have the option to choose between the private offer and the public
offer. Buyers can only be subscribed to one offer at any given time. They can't be subscribed to
both a private offer and the public offer at the same time. This topic provides information
about how private offers work, including special considerations, buyer experience, and seller
reports.

###### Note

AWS allows buyers with unique or enterprise use cases to request a private
offer for your product directly from the product detail page. If you're an AWS Partner
Network (APN) partner who's eligible for [APN Customer Engagements (ACE)](https://aws.amazon.com/partners/programs/ace/ "https://aws.amazon.com/partners/programs/ace/")
and you'd like to provide this option to buyers, see [Adding private offer and demo request buttons](creating-private-offer.md#private-offer-requests-demos "creating-private-offer.md#private-offer-requests-demos") for more information.

###### Sellers in India

Sellers in India can create private offers in USD and INR, and can extend these offers to buyers in India only. For detailed information, see [Getting started as a seller in India](getting-started-seller-india.md "getting-started-seller-india.md").

###### Topics

- [How private offers work](#how-private-offers-work "#how-private-offers-work")
- [Private offer considerations](#private-offer-considerations "#private-offer-considerations")
- [Private offer experience for buyers](#private-offer-experience-buyers "#private-offer-experience-buyers")
- [Automatically create private offers](#streamline-private-offers "#streamline-private-offers")
- [Reporting for private offers](#reporting-for-seller-private-offers "#reporting-for-seller-private-offers")
- [Supported product types for AWS Marketplace private offers](private-offers-supported-product-types.md "private-offers-supported-product-types.md")
- [Creating and managing private offers](creating-private-offer.md "creating-private-offer.md")
- [Creating private offers as an AWS Marketplace Channel Partner](channel-partner-offers.md "channel-partner-offers.md")
- [Express private offers](express-private-offers.md "express-private-offers.md")
- [Private offer installment plans](installment-plans.md "installment-plans.md")
- [Creating future
  dated agreements for private offers](private-offers-seller-future-dated-private-offers-and-agreements.md "private-offers-seller-future-dated-private-offers-and-agreements.md")
- [Private offer FAQ](private-offer-faq.md "private-offer-faq.md")

## How private offers work

You use the **Offers** page in
the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management") to create, update, and manage your private offers. You specify the product for the offer, which generates a unique ID and URL.
You create a pricing plan for the private offer, add legal terms and sales documents, and
extend the offer to specific buyer AWS accounts. The offer is only visible to the accounts
for which you create the offer.

After you create a private offer and notify potential buyers, they can view and accept the
offer. To view the offer, the buyer must be signed into the AWS account that received the
offer.

###### Note

Buyers can't view the offer unless you extend it to either their linked account or their
management account. You can't provide service limits in the offer, so the buyer can use as
much of your product at the negotiated prices as they want, unless the product has a
limit.

For information on creating a private offer, see [Creating and managing private
offers](creating-private-offer.md "creating-private-offer.md").

For information about updating or amending a private offer, see [Amending agreements in AWS Marketplace](private-offers-upgrades-and-renewals.md "private-offers-upgrades-and-renewals.md").

Private offers are tracked in seller reports. For more information, see [Reporting for private offers](private-offers-overview.md#reporting-for-seller-private-offers "private-offers-overview.md#reporting-for-seller-private-offers").

## Private offer considerations

When working with private offers, consider the following:

- When you add support for a new instance type or AWS Region, customers already
  subscribed to private offers for your product won't be able to access the newly added
  instance or Region automatically. You must create another private offer with the instance
  and Region you want customers to access. After accepting the new offer, customers can
  access the newly added instance and Region. Customers who subscribe to your product at a
  future date can also access them, as long as they're included in the private offer. For
  more information about how to create a new private offer, see [Amending agreements in AWS Marketplace](private-offers-upgrades-and-renewals.md "private-offers-upgrades-and-renewals.md").
- You can't create private offers for second party, Amazon Machine Image (AMI) monthly,
  or multi-AMI-based delivery using AWS CloudFormation products, or for limiting customer
  usage.
- For private offers with an installment plan, it's possible to break upfront payments
  into multiple payments over time. For more information, see [Private offer installment plans](installment-plans.md "installment-plans.md").
- If the buyer account for your private offer is managed through a private marketplace,
  you must include both the buyer's account and the account that includes their private
  marketplace administrator in the offer.
- Private offers don't support the Bring Your Own License (BYOL) model.
- Use the **Custom EULA** option when creating a private offer with
  unique negotiated contract terms in your private offer. You can attach up to five
  documents.
- For software as a service (SaaS) contracts and SaaS contracts with consumption
  products, you can offer upgrades and renewals on agreements that were made when buyers
  accepted private offers. For example, you can do this to grant new entitlements, offer
  pricing discounts, adjust payment schedules, or change the end user license agreement
  (EULA) to use standardized license terms. For more information, see [Amending agreements in AWS Marketplace](private-offers-upgrades-and-renewals.md "private-offers-upgrades-and-renewals.md").

## Private offer experience for buyers

When the buyer navigates to your product's subscription page, a banner indicates that a
private offer is available. After the buyer accepts the offer, they're invoiced for the
purchase using the same portal tools used for all AWS Marketplace transactions. Accepted offers
become agreements. Buyers can find agreement details in the **Manage
Subscriptions** section of the AWS Management Console, and sellers can find details in the
**Agreements** tab of AWS Marketplace Management Portal.

AWS Marketplace buyers can access third-party financing for private offers. For more
information, see [Customer financing is now available in AWS Marketplace](https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/Financing+External+Briefing+Document+Customer+Facing.pdf "https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/Financing+External+Briefing+Document+Customer+Facing.pdf").

###### Note

An offer can only be accepted before the expiration date. If the offer expires, it's
moved to the **Accepted and expired offers** tab.

| To view and accept a private offer | The buyer can                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| From the AWS Marketplace console   | Navigate to **Private offers\*<br>• in the AWS Marketplace console and select<br>the offer ID from the **Available offers*<br>• tab.For more<br>information about the buyer experience for private offers, see [Private offers](../buyerguide/buyer-private-offers.md "../buyerguide/buyer-private-offers.md") in the<br>*AWS Marketplace Buyer Guide\*. |
| Using a seller-provided link       | Follow the link sent by the seller to directly access the private offer.<br>For more information, see [Sending a private<br>offer to a buyer](creating-private-offer.md#send-private-offer "creating-private-offer.md#send-private-offer").                                                                                                              |
| From your product page             | Navigate to the product page for the product, and choose the link in the banner<br>to view the private offer. For more information about the buyer experience for<br>private offers, see [Private<br>offers](../buyerguide/buyer-private-offers.md "../buyerguide/buyer-private-offers.md") in the _AWS Marketplace Buyer Guide_.                        |

## Automatically create private offers

AWS Marketplace provides _express private offers_ to automate the private offer creation process. Express private offers enable you to configure predefined pricing and qualification criteria through rate cards, allowing buyers to receive instant private offers for standard deals without manual intervention from your sales team.

For more information, see [Express private offers](express-private-offers.md "express-private-offers.md").

## Reporting for private offers

Private offers appear on the existing seller reports and in the reports relevant to the
offer. The [Monthly billed revenue report](monthly-billed-revenue-report.md "monthly-billed-revenue-report.md") is generated every month and has offer
visibility and offer ID information. When an invoice is generated for a buyer, it appears in
the report covering the appropriate billing period. For more information, see [Seller
dashboards](dashboards.md "dashboards.md").

The **Offer ID** field contains the unique offer ID generated for the
private offer. It's blank unless the report entry is for a private offer. The **Offer
Visibility** field indicates whether the report entry is a public or private offer.
For all private offers, the entry is marked private.
