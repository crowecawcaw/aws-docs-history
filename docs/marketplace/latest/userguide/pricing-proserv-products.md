# Pricing professional services products in AWS Marketplace

When you sell professional services products on AWS Marketplace, you must negotiate a private offer with each buyer.
Private offers are negotiated terms used to purchase a product from AWS Marketplace. With seller private offers, there are options available for multi-year
and custom duration contracts. This topic provides more information about professional services
product pricing and private offers.

For more information about multi-year and custom duration contracts, see [Preparing a private offer for your AWS Marketplace product](private-offers-overview.md "private-offers-overview.md") and [Private offer installment plans](installment-plans.md "installment-plans.md").

You can set only one price per product. For more information about pricing AWS Marketplace products,
refer to [Product pricing for AWS Marketplace](pricing.md "pricing.md").

In addition, you can create variable payment offers that enable you to bill buyers as you complete work.
You agree on a set of milestones with the buyer, and you submit payment requests at each milestone. For more information, refer to
[Using variable payments with private offers for professional services](proserve-variable-payment.md "proserve-variable-payment.md") later in this section.

## How private offers work

You use **Offers** page in the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management") to create and manage your private offers. The process follows these broad steps:

- You specify the product. This generates a unique ID and URL for the offer
- Create a pricing plan.
- Add legal terms and sales documents.
- Extend the offer to specific buyer AWS accounts. Only the members of those accounts can view and accept the offer, and they must sign in to the account.
  Finally, the accounts must be linked or management accounts.

After you create a private offer and notify potential buyers, they can view and accept the
offer.

###### Note

You can't set service limits in the offer, so the buyer can use as
much of your product at the negotiated prices as they want, unless the product has a
limit.

For information on creating a private offer, refer to [Creating and managing private
offers](creating-private-offer.md "creating-private-offer.md").

Seller reports track private offers. For more information, refer to [Reporting for private offers](private-offers-overview.md#reporting-for-seller-private-offers "private-offers-overview.md#reporting-for-seller-private-offers") in this guide and the downloadable [Seller reports guide](https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/Seller+Reports+Guide.pdf "https://s3.us-west-2.amazonaws.com/external-mp-channel-partners/Seller+Reports+Guide.pdf") PDF.

## Pricing model for private offers

Private offers use the contract pricing model. The model provides the following billing options:

- Installment plans with a custom billing schedule. Invoiced at 00:00 UTC on dates that you define. Invoices contain payment instructions for the buyer.
- Upfront billing paid immediately upon subscription.
- Variable payments. As you reach work milestones, you create payment requests that buyers accept or decline. Buyers receive an invoice when they accept a payment request.

### Creating a private offer with variable payment

You set a total contract amount when creating a private offer with a variable billing. Once buyers accept the contract, you bill in custom increments, up to the total price, over the duration of the contract.

###### To create a private offer with variable payment

1. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management").
2. Choose **Offers**, then **Create private offer.**
3. On the **Configure offer pricing and duration** page, for **Offer pricing**, choose **Contract pricing with variable payment.**
4. Choose the contract duration and offer currency.
5. Specify the total contract amount. You bill your buyers up to this amount over the course of the contract. Your cumulative payment requests cannot exceed the total contract amount.

You can start billing custom payment requests after the buyer accepts, up to the total price, over the duration of the contract.

###### To create payment requests

1. You view and manage agreements from the **Agreements** page in the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management").
2. Select **Agreements** from the menu
3. In the **Agreements** table, select the option next to the agreement and choose **View details**. Alternatively, you can choose the link for the agreement in the **Agreement ID** column.
4. On the agreement detail page, choose **Request payment**
5. On the **Create payment request** page, specify the **Requested amount**. The requested amount can't exceed the **Remaining amount**.

###### Note

The **Remaining amount** is the available balance of payment requests from your Total Contract amount. You can send your customers additional payment requests as long as it does not exceed this amount. You can no longer send payment requests when the remaining amount is zero. 6. You also have the option to describe what you delivered to the buyer in the **Deliverables**. Tell the buyer about the work associated with this payment request. 7. Select **Create** to submit the payment request.

###### To cancel payment request

1. Select **Agreements** from the menu
2. In the **Agreements** table, select the option next to the agreement and choose **View details**. Alternatively, you can choose the link for the agreement in the **Agreement ID** column.
3. On the agreement detail page, under the **Payment request** panel, select the option next to the payment request ID and choose **View details**
4. On the payment request detail page, choose **Cancel Payment**.

###### Note

You may cancel your payment request at any time while it is in pending state. You can no longer cancel the payment once the buyer has approved the payment request.

### Payment Request Statuses:

Payment requests can have one of the following statuses:

- **Pending** – Your payment request has been submitted and is pending buyer action. You can cancel the payment request if it is in pending state.
- Canceled: The payment request has been cancelled by the seller. Cancelled payment requests are no longer active/valid.
- Accepted: The buyer has accepted your payment.
- Declined: The buyer has declined to approve this payment request. You should contact your buyer to address any payment issues.
