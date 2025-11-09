# Using variable payments with private offers for professional services

The following topics explain how to add and manage variable payments for private offers created for professional services products.
You set a total contract amount when creating a private offer with a variable payments. After a buyer accepts the contract,
you bill in custom increments up to the total price over the duration of the contract.

###### Topics

- [Adding variable payments to a private
  offer](#add-variable-payment "#add-variable-payment")
- [Creating variable payment requests](#create-variable-request "#create-variable-request")
- [Canceling variable payment requests](#cancel-variable-request "#cancel-variable-request")
- [Payment request statuses](#payment-request-statuses "#payment-request-statuses")

## Adding variable payments to a private

offer

The following steps explain how to create a private offer for professional services with variable payments.

###### To add variable payment

1. Complete steps 1-4 in In [Creating private offers](proserv-create-offer.md "proserv-create-offer.md") above.
2. On the **Configure offer pricing and duration** page, for **Offer pricing**, choose **Contract
   pricing with variable payment**.
3. Choose the **contract duration** and
   **offer currency**.
4. Specify the total contract amount. You bill your buyers up to this
   amount over the course of the contract. Your cumulative payment
   requests cannot exceed the total contract amount.
5. Return to [Creating private offers](proserv-create-offer.md "proserv-create-offer.md") and complete the remaining steps.

You can start billing after the buyer accepts the offer. Buyers must also accept each payment request. You can bill up to the total price over the duration of the contract.

## Creating variable payment requests

The following steps explain how to create variable billing payment requests.

###### To create a request

1. Sign in to the [AWS Marketplace
   Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management") and choose **Agreements**.
2. In the **Agreements** table, select
   the checkbox next to the agreement and choose
   **View details**.
3. On the agreement detail page, choose **Request payment**
4. On the **Create payment request** page, specify the
   **Requested amount**. That amount can't exceed the **Remaining
   amount**.
5. (Optional) In the **Deliverables** box, describe
   the work associated with the request.
6. Choose **Create** to submit the request.

## Canceling variable payment requests

The following steps explain how to cancel variable payment requests. You can cancel a request at any time until the buyer approves it.

###### To cancel a request

1. Sign in to the [AWS Marketplace
   Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management") and choose **Agreements**.
2. In the **Agreements** table, select
   the checkbox next to the agreement and choose
   **View details**.
3. On the agreement detail page, under the
   **Payment request** panel, select
   the option next to the payment request ID and choose
   **View details**
4. On the payment request detail page, choose **Cancel Payment**.

## Payment request statuses

Payment requests can have one of the following statuses:

- **Pending** – Your payment request has been submitted and is pending
  buyer action. You can cancel pending requests until the buyer approves them.
- **Canceled** – You canceled the payment request, making it inactive.
- **Accepted** – The buyer has accepted the request.
- **Declined** – The buyer has declined the request.
  Contact the buyer to resolve any payment issues.
