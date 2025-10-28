# Private offers page in AWS Marketplace

In AWS Marketplace, the **Private offers** page lists all the private offers that
have been extended to your AWS account for both private and public products. All offers
available to you are displayed for each product. You can accept one offer for each
product.

## Understanding the Private offers page

You can view your **Private offers** page by signing in to the AWS Marketplace
console and navigating to **Private
offers**.
Private offers extended to your AWS account are listed under **Private
offers**, including the offer ID, product, seller of record (ISV or channel
partner), publisher, active agreements (if applicable), and the offer expiration date. You can
select the **Offer ID** for the offer of interest to view the offer details
and subscribe to a private offer.

The **Private offers** page includes the following
information:

- The **Available offers** tab lists the private offers extended to
  your account that are available to accept. The **Offer ID** link on this
  tab is the same link that the seller might have provided to you to access the private
  offer details.
- The **Accepted and expired offers** tab lists the offers that you
  accepted and resulted in an agreement being created. It also lists offers that reached the
  offer expiration date set by the seller. This tab can be useful to retrieve a previous
  offer-ID and agreement-ID (if available) when renewing with a seller. If the offer
  resulted in an agreement and the agreement is active, you can choose the agreement to view
  the subscription detail page.

###### Note

Future-dated private offers are listed as **Early renewals**. For
more information, see [Future dated agreements and private offers in AWS Marketplace](private-offers-buyer-future-dated-private-offers-and-agreements.md "private-offers-buyer-future-dated-private-offers-and-agreements.md").

The following video provides more information about accessing a consolidated view of all
your private
offers.

For more information about modifying, upgrading, or renewing a private offer, see [Modifying or unsubscribing from a private offer in AWS Marketplace](buyer-private-offers-modifying.md "buyer-private-offers-modifying.md").

## Required permissions to view the Private

offers page

To view the **Private offers** page in the AWS Marketplace console, you must have
the following permissions:

- If you use AWS managed policies: `AWSMarketplaceRead-only`,
  `AWSMarketplaceManageSubscriptions`, or
  `AWSMarketplaceFullAccess`
- If you aren't using AWS managed policies: IAM action
  `aws-marketplace:ListPrivateListings`and
  `aws-marketplace:ViewSubscriptions`

If you're unable to view the **Private offers** page, contact your
administrator to set up the correct AWS Identity and Access Management (IAM) permissions. For more information about
the necessary IAM permissions for AWS Marketplace, see [AWS managed policies for AWS Marketplace
buyers](buyer-security-iam-awsmanpol.md "buyer-security-iam-awsmanpol.md").
