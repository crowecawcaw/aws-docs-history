# Configuring net payment terms for private offers

When you create a private offer, specify net payment terms to honor your negotiated
agreements and close deals that require custom terms.

###### Note

Net payment terms apply to all private offer types, including AWS Marketplace private offers
(MPPO) and channel partner private offers (CPPO), and all product types and pricing models.
Net payment terms are not available for ADX, AWS 1P, 2P, or Amazon Bedrock
products.

###### Topics

- [How net payment terms for private offers work](#net-payment-terms-how-it-works "#net-payment-terms-how-it-works")
- [Prerequisites](#net-payment-terms-prerequisites "#net-payment-terms-prerequisites")
- [Setting payment terms for a private offer](#setting-net-payment-terms "#setting-net-payment-terms")
- [Setting payment terms for channel partner offers](#net-payment-terms-channel-partners "#net-payment-terms-channel-partners")
- [Viewing payment terms after offer creation](#viewing-net-payment-terms "#viewing-net-payment-terms")
- [Considerations](#net-payment-terms-considerations "#net-payment-terms-considerations")

## How net payment terms for private offers work

We pay sellers after receiving payment from customers. When you extend net payment
terms to a customer on a private offer, the value you select is how long the buyer has to pay
from the time of invoice issuance. For example, if you offer `Net 90` terms, the
buyer has 90 days to pay from the time we generate the invoice.

Consider your cash flow requirements when deciding which payment terms to offer.

## Prerequisites

To configure net payment terms, you must meet the following requirements:

- You must have at least one active public listing in AWS Marketplace.
- You must have access to create private offers in [AWS Partner Central](https://console.aws.amazon.com/partnercentral/home "https://console.aws.amazon.com/partnercentral/home").

## Setting payment terms for a private offer

You configure payment terms during the private offer creation process in [AWS Partner Central](https://console.aws.amazon.com/partnercentral/home "https://console.aws.amazon.com/partnercentral/home").

###### To set payment terms for a private offer

1. Sign in to [AWS Partner
   Central](https://console.aws.amazon.com/partnercentral/home "https://console.aws.amazon.com/partnercentral/home") and choose **Private offers**.
2. Create a new private offer or resume a draft offer. For more information about
   creating private offers, see [Creating and managing private offers](creating-private-offer.md "creating-private-offer.md").
3. On the **Configure offer pricing and duration** page, for
   **Payment Terms**, choose the terms for this offer. Options
   include:

   - **Customer's AWS default** (default) – The buyer's standard
     AWS payment terms apply.
   - **Net 30**, **Net 45**, **Net
     60**, or **Net 90** – Payment is due 30, 45, 60, or
     90 days from the invoice date, respectively.

4. Complete the remaining steps to create and publish the private offer.

###### Note

Payment terms apply uniformly to all charges within the offer, including upfront fees,
installments, recurring payments, and usage charges.

## Setting payment terms for channel partner offers

When you create a resale authorization for a channel partner, you can specify the maximum
net payment terms that the channel partner can extend to end customers.

- If you set `Net 60` in the resale authorization, the channel partner can
  offer `Net 30`, `Net 45`, or `Net 60` to the buyer, but
  not `Net 90`.
- If you select **Customer's AWS default**, the channel partner's offer
  defaults to the end buyer's AWS payment terms.

Channel partners creating CPPOs see the same **Payment Terms** dropdown,
limited to the maximum you specified in the resale authorization.

## Viewing payment terms after offer creation

After you create a private offer with custom payment terms, you can view the terms in the
following locations:

- **Private offers page** – The offer details display
  the payment terms you configured.
- **Agreements page** – After the buyer accepts the
  offer, you can view payment terms in the agreement details in [AWS Partner Central](https://console.aws.amazon.com/partnercentral/home "https://console.aws.amazon.com/partnercentral/home").
- **Seller insights dashboard** – Payment due dates
  for each invoice reflect the payment terms you set.

Buyers see the payment terms you configured in the following locations:

- **Procurement page** – The buyer views payment
  terms when reviewing the private offer.
- **Subscription detail page** – The buyer views
  payment terms after accepting the offer.
- **AWS invoices** – The payment due date reflects
  the negotiated terms.

For more information about how buyers experience payment terms, see [Net payment terms for
private offers](../buyerguide/buyer-net-payment-terms.md "../buyerguide/buyer-net-payment-terms.md") in the _AWS Marketplace Buyer Guide_.

## Considerations

When working with net payment terms, consider the following:

- You must align with the buyer before offering custom net payment terms on a private
  offer. Buyers otherwise expect their standard AWS net payment terms to apply.
- You cannot change payment terms after the buyer accepts the offer. To modify terms,
  create a new private offer.
- If you set terms less favorable than the buyer's standard AWS terms (for example,
  `Net 30` when the buyer has `Net 45`), the terms you set still
  apply. Buyers see the terms before accepting.
- Payment terms only apply to buyers who pay by invoice. Credit card customers are
  charged immediately regardless of the configured terms.
- Custom payment terms apply only to that specific agreement. The buyer's other
  AWS Marketplace purchases and AWS services continue to use their standard payment
  terms.
