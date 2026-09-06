# Net payment terms for private offers

When you accept a private offer with net payment terms, your invoice payment due dates
reflect the seller's negotiated terms instead of your standard AWS payment terms. For example,
if a seller extends `Net 60` terms through a private offer, AWS sets the payment
due date to 60 days from the invoice date, regardless of your default AWS terms. If sellers do
not specifically set net payment terms in a private offer, you won't see that field defined and
AWS continues to charge using your standard payment terms.

Supported net payment term values are `Net 15`, `Net 30`, `Net
 45`, `Net 60`, `Net 90`, and `Net 120`.

Net payment terms are supported for all product types (with the exception of AWS Data Exchange) and
pricing models in AWS Marketplace private offers (MPPO) and channel partner private offers (CPPO). Net
payment terms apply only to charges from the private offer agreement. Charges for AWS 1P,
AWS Marketplace 2P, or Amazon Bedrock products are not eligible and continue to use your standard
AWS payment terms.

###### Note

Net payment terms determine the number of days between the invoice date and payment due
date. Net payment terms for AWS Marketplace private offers are supported exclusively for
pay-by-invoice payment method.

###### Topics

- [How net payment terms for private offers work](#buyer-net-payment-terms-how-it-works "#buyer-net-payment-terms-how-it-works")
- [Prerequisites](#buyer-net-payment-terms-prerequisites "#buyer-net-payment-terms-prerequisites")
- [Accept a private offer with custom payment terms](#buyer-accept-offer-custom-payment-terms "#buyer-accept-offer-custom-payment-terms")
- [Viewing payment terms](#buyer-viewing-payment-terms "#buyer-viewing-payment-terms")
- [Invoice splitting by payment terms](#buyer-invoice-splitting-by-payment-terms "#buyer-invoice-splitting-by-payment-terms")
- [Aligning payment terms with your purchase orders](#buyer-aligning-payment-terms-with-pos "#buyer-aligning-payment-terms-with-pos")

## How net payment terms for private offers work

Sellers can configure net payment terms when creating a private offer. When you review a
private offer, the procurement page displays the net payment terms prominently, if they are set
by the seller. If you don't see net payment terms defined, then AWS uses your default
payment terms. After you accept the offer, the specified terms apply to all charges associated
with the agreement, including upfront fees, scheduled payments, and usage charges. You cannot
have different net payment terms for different charge types within a single agreement.

###### Important

Payment terms set by the seller take precedence over your standard AWS payment terms
only for that specific private offer subscription. Net payment terms are supported
exclusively for pay-by-invoice payment method.

## Prerequisites

To use net payment terms, you must meet the following requirements:

- The seller must configure custom payment terms when creating the private
  offer.

You don't need additional setup or permissions.

## Accept a private offer with custom payment terms

###### To accept a private offer with custom payment terms

1. Negotiate payment terms with the seller for your private offer.
2. Ask the seller to create the private offer with the agreed-upon payment terms in
   AWS Marketplace.
3. When you receive the private offer, review the payment terms on the
   **Procurement** page to confirm they match your agreement.
4. Accept the private offer. The payment terms automatically apply to all invoices for
   that agreement.

## Viewing payment terms

You can view payment terms for private offers in the following locations:

- **Procurement page** – Shows payment terms when you
  review a private offer, before you accept it.
- **Subscription detail page** – After you accept the
  offer, the charge summary section displays the payment terms.
- **AWS invoices** – Displays the payment due date,
  calculated as the invoice issuance date plus the net payment term days.

## Invoice splitting by payment terms

When you have multiple subscriptions with different payment terms, AWS generates
separate monthly invoices grouped by payment terms. Each invoice has a single payment due date.
For example, subscriptions with standard AWS terms appear on your regular monthly invoice,
although subscriptions with `Net 60` terms have a separate invoice.

If a seller sets the same payment terms as your standard AWS terms, AWS groups those
charges on one invoice.

## Aligning payment terms with your purchase orders

When you accept a private offer with custom payment terms, you can set the net payment
terms on the purchase requisition or purchase order to match the private offer. This might help
accounts payable teams process the invoice, with consistent payment terms across the purchase
order and invoice.

###### Note

If you typically set payment terms at the vendor or contract level in your
procure-to-pay tool, you can override this at the purchase order level for subscriptions with
custom payment terms.

For more information about purchase orders, see [Using purchase orders for AWS Marketplace transactions](buyer-purchase-orders.md "buyer-purchase-orders.md"). For more information about private offers, see [Private offers in AWS Marketplace](buyer-private-offers.md "buyer-private-offers.md").
