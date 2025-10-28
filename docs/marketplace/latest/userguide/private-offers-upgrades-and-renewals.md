# Amending agreements in AWS Marketplace

AWS Marketplace sellers, Channel Partners, and ISVs can offer upgrades, renewals, and amendments to replace active
agreements. For example, you can grant new entitlements, offer pricing discounts, adjust payment
schedules, or change the end user license agreement (EULA) to use [standardized license terms](standardized-license-terms.md "standardized-license-terms.md"). You can also change
the number of units and payment schedule and add a custom end date.

Software as service (SaaS) contract and SaaS contract with consumption products support public and private offer
amendments. All AWS Marketplace sellers can upgrade, renew, or amend private offers for these product
types, including independent software vendors (ISVs) and channel partners. The following
sections provide information about the process.

An _offer_ becomes an _agreement_
when a buyer accepts its terms:

- An **offer** is a set of terms for the use of a
  product. Offers can be public or private.
- An **agreement** is an offer that a buyer accepted.
  Agreements include purchased and free products that a seller made available using a public
  or private offer.
  You can't amend an agreement to specify a seller of record that's different from the seller
  of record from the original agreement. To use this feature, you must have permissions to use the
  **Agreements** tab in the AWS Marketplace Management Portal. For information, see [Permissions for AWS Marketplace sellers](detailed-management-portal-permissions.md#seller-ammp-permissions "detailed-management-portal-permissions.md#seller-ammp-permissions").

###### Topics

- [Supported product
  types for public and private offer amendments](#private-offers-upgrades-and-renewals-supported-products "#private-offers-upgrades-and-renewals-supported-products")
- [Creating public and private offer upgrades, renewals, and amendments](#private-offers-upgrades-and-renewals-process "#private-offers-upgrades-and-renewals-process")
- [Reporting for upgrades,
  renewals, and amendments](#private-offers-upgrades-and-renewals-reporting "#private-offers-upgrades-and-renewals-reporting")

## Supported product

types for public and private offer amendments

Only the following product types support offer amendments:

- SaaS contracts
- SaaS contracts with consumption

You can see the following additional product types on the **Agreements**
tab in the AWS Marketplace Management Portal. However, these product types don't support amendments:

- SaaS usage-based products
- AMI-based products
- Container-based products
- Server contract
- Professional services products

## Creating public and private offer upgrades, renewals, and amendments

You can create offer upgrades, renewals, and amendments from the AWS Marketplace Management Portal using the
following procedure. For Channel Partner private offers, the Channel Partner must use the currency defined in the selling authorization when
creating amendments.

###### Note

- Amended offers cannot have a future agreement start date. Amended offers only target active agreements,
  and once accepted, the amended agreements immediately become active making future dating impossible.
- If you amend an accepted public offer, it becomes a private offer and no longer auto-renews.
  To maintain automatic renewal, a buyer must subscribe to a public offer.
  For more information, see [How private offers work](private-offers-overview.md#how-private-offers-work "private-offers-overview.md#how-private-offers-work").

###### To create offer upgrades, renewals, and amendments

1. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management") and choose **Agreements**.
2. On the **Agreements** page, choose a check box next to an agreement,
   and then choose **View Details**.
3. On the **View agreement** page, choose **Amend agreement**.
4. On the **Amend agreement details** page, you can also make changes to
   service dates, product dimensions, offer currency (for AWS MP direct PO), payment
   schedule, usage dimensions, renewal status, EULA, and the offer expiration date.
5. Review the offer and choose **Create offer**.

###### Tip

Entering descriptive custom offer names can help you distinguish between your active
offers on the **Offers** page. Custom offer names are also visible to
buyers.

AWS recommends using a custom offer name that includes any additional
identifying details, such as your own IDs and purchase order numbers. Using high-level
descriptions such as `upgrade` or `renewal` and
custom company names are also recommended. Don't use any personally identifiable data
(for example, first or last names, phone numbers, or addresses). You can enter up to 150
characters for this field.

### More about amended offers

An amended offer will appear on the **Private Offer** page within
approximately 45 minutes. To view the offer, sign in to the AWS Marketplace Management Portal and choose
**Offers**. On the **Private Offer** page, the buyer has
the option to accept the offer or to continue the original agreement.

If the buyer accepts the public or private offer upgrade or renewal, the new agreement takes
effect immediately and the agreement is listed on the **Agreements** page
in the AWS Marketplace Management Portal. Any remaining scheduled payments from previous agreements are
cancelled. Buyers accept amendments the same way they accept private offers.
For more information about the buyer experience for private offers, see [Private offers](../buyerguide/buyer-private-offers.md "../buyerguide/buyer-private-offers.md") in the _AWS Marketplace Buyer Guide_.

If the buyer doesn't accept the public or private offer upgrade or renewal before it expires,
the original agreement will continue unchanged.

###### Note

For [Amazon SNS notifications for SaaS products](saas-notification.md#saas-sns-subscription-message-body "saas-notification.md#saas-sns-subscription-message-body"), a
`subscribe-success` message is sent with the new `offer-identifier`
when the buyer accepts the amendment.

## Reporting for upgrades,

renewals, and amendments

Public and private offer upgrades and renewals appear on the existing seller reports and
in the reports relevant to the offer. The [Daily customer subscriber report](daily-customer-subscriber-report.md "daily-customer-subscriber-report.md") and [Daily business report](daily-business-report.md "daily-business-report.md") are generated daily. The [Monthly billed revenue report](monthly-billed-revenue-report.md "monthly-billed-revenue-report.md") is
generated monthly.

In the Daily customer subscriber report, the **Subscription intent**
field indicates whether the report entry is a new private offer. The **Previous offer
ID** field displays the ID of any preceding offer. All private offers are labeled
as "private" in the report.

###### Important

An amendment replaces a buyer's current subscription. Existing invoices remain
unchanged. However, the payment schedule in the amendment replaces pending invoices from the
previous subscription.
