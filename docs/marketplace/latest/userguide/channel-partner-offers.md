# Creating private offers as an AWS Marketplace Channel Partner

AWS Marketplace Channel Partner private offers give Channel Partners the opportunity to resell independent software vendors' (ISVs) products in AWS Marketplace. The AWS Marketplace Channel Partner and ISV establish an agreement called a _selling authorization_ to resell one or more of the ISV's products. The Channel Partner then extends a private offer to the buyer for that product.

## Prerequisites to become a Channel Partner

To register as a Channel Partner to resell products on AWS Marketplace, you must meet the
following requirements:

- Registered as a paid seller on AWS Marketplace.
- Your tax interview location matches your business location.
- USD is set as one of your disbursement methods. _This is required for public offers and Professional Services product creation._

###### Sellers in India

Sellers in India have specific registration requirements and can only set INR for disbursement. For more information, see [Getting started as a seller in India](getting-started-seller-india.md "getting-started-seller-india.md"). For step-by-step onboarding instructions, see the [AWS Marketplace India Seller Registration Guide](https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/AWS+Marketplace+India+Registration+Guide.pdf "https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/AWS+Marketplace+India+Registration+Guide.pdf").

- Create the [service-linked role (SLR) in AWS Marketplace](using-roles-for-resale-authorization.md#create-slr "using-roles-for-resale-authorization.md#create-slr").

###### Important

To create, share, and accept selling authorizations, you must create a service-linked
role (SLR) that allows ISVs to create and share the authorizations, and allows Channel
Partners to accept them. For more information about creating the SLR, see [Creating a service-linked role for AWS Marketplace](using-roles-for-resale-authorization.md#create-slr "using-roles-for-resale-authorization.md#create-slr").

For step-by-step onboarding instructions, see the [Channel Partner Onboarding Guide](https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/Consulting+Partner+Private+Offers+-Seller+Sign+Up+Onboarding+Guide+2019.pdf "https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/Consulting+Partner+Private+Offers+-Seller+Sign+Up+Onboarding+Guide+2019.pdf"). After you complete these requirements, submit a
request using the [Contact Us](https://aws.amazon.com/marketplace/management/contact-us/?form=true "https://aws.amazon.com/marketplace/management/contact-us/?form=true")
form to complete your Channel Partner registration.

Upon approval, ISVs can create selling authorizations for approved Channel Partners to resell their products.

## Understanding Channel Partner Private Offers (CPPO)

The following diagram shows this relationship between an ISV, a Channel Partner, and a
buyer.

![Relationships and workflow between ISVs, Channel Partners, and buyers.](images/consulting-partner-images-3.png)

###### Note

For more information about creating a selling authorization for a Channel Partner, as an
ISV, see [Creating a selling authorization for an AWS Marketplace Channel Partner as an ISV](channel-partner-isv-info.md "channel-partner-isv-info.md").

Each AWS Marketplace Channel Partner private offer is visible only to a single buyer, with customized
pricing and unique commercial terms to meet that buyer's needs. When creating a private offer,
you start from a wholesale cost set by the ISV. Then you mark up that price to create the
buyer's offer price.

###### Note

When creating private offers, Channel Partners must use the currency that the ISV defines in the selling authorization.

You determine the wholesale cost in one of the following ways:

- **Recurring discount** – An ISV authorizes the AWS Marketplace
  Channel Partner to resell their product or products at an agreed to discount from their list
  price with a recurring selling authorization. The AWS Marketplace Channel Partner can use this
  discount to continue reselling the product without further price negotiation with the ISV.
  This discount can be set up to last until a specified date, or indefinitely, until ended by
  either the ISV or the Channel Partner.
- **Non-recurring discount** – The selling
  authorization that the ISV gives the AWS Marketplace Channel Partner is a one-time discount intended
  to be used only with a specific buyer.

In both cases, after the buyer pays for the private offer, AWS Marketplace uses the standard
process to distribute the funds to the AWS Marketplace Channel Partner and the ISV based on the agreed-to
pricing. Listing fees are deducted from the amount disbursed to the ISV. Listing fee is
calculated based on the discounted price offered by ISV to Channel Partner. For listing fee
tiers, see [Understanding listing fees for AWS Marketplace sellers](listing-fees.md "listing-fees.md").

###### Tip

ISVs and Channel Partners can use the **Partners** menu on the [AWS Marketplace Management Portal](https://us-east-1.console.aws.amazon.com/partnercentral/home "https://us-east-1.console.aws.amazon.com/partnercentral/home") to view selling authorizations.

For detailed instructions about creating private offers, see [AWS Marketplace Channel Partner Private Offer – Create Offer](<https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/Consulting+Partner+Creates+(1).pdf> "https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/Consulting+Partner+Creates+(1).pdf").

For information about third-party financing for private offers, see [Customer financing is now available in AWS Marketplace](https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/Financing+External+Briefing+Document+Customer+Facing.pdf "https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/Financing+External+Briefing+Document+Customer+Facing.pdf").
