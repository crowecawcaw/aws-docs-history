

# Pricing professional service products in AWS Marketplace
<a name="proserv-variable-payments"></a>

As an AWS Marketplace seller with a Professional Services product, you can choose from three contract pricing options: installment plan, upfront payment, and variable payments. Variable payments allow you to set a total contract amount when creating a private offer. Once buyers accept the contract, you send payment requests, up to the total contract amount, over the duration of the contract.

## Creating a private offer with variable payment
<a name="proserv-variable-create-offer"></a>

**To create a private offer with variable payment**

1. Open a web browser and sign into the [AWS Marketplace Management Portal](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Choose **Private offers**.

1. The first step is to **Provide offer information**. You must enter an offer name. Providing an offer description is optional. Indicate whether this private offer is a renewal or not.

1. Set the offer expiration date. Your buyer must respond to your offer by the provided date before 23:59 (UTC), otherwise the offer will expire.

1. The second step is to **Configure offer pricing and duration**. In this step, choose **Contract pricing with variable payments**.

1. Choose the contract duration and offer currency.

1. Specify the contract total amount. You can bill your buyer up to this amount over the course of the contract. Your cumulative payment requests cannot exceed the total contract amount.

## Payment requests
<a name="proserv-payment-requests"></a>

Once your buyer accepts a professional services private offer with variable payments contract pricing, you can send payment requests up to the total contract value, over the duration of the contract.

### Creating payment requests
<a name="proserv-create-payment-request"></a>

**To create payment requests**

1. You view and manage agreements from the **Agreements** page in the [AWS Marketplace Management Portal](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Select **Agreements** from the menu.

1. In the **Agreements** table, select the option next to the agreement and choose **View details**. Alternatively, you can choose the link for the agreement in the **Agreement ID** column.

1. On the agreement detail page, choose **Request payment**.

1. On the Create payment request page, specify the **Requested amount**. Your payment request cannot exceed the **Remaining amount**.
**Note**  
The **Remaining amount** is the available balance of payment requests from your Total Contract amount. You can send your customers additional payment requests as long as it does not exceed this amount. You can no longer send payment requests when the remaining amount is zero or the agreement has expired.

1. You also have the option to describe what you delivered to the buyer in the **Deliverables**. Tell the buyer about the work associated with this payment request.

1. Submit your payment request by selecting **Create**.

### Canceling payment requests
<a name="proserv-cancel-payment-request"></a>

**To cancel payment request**

1. You view and manage agreements from the **Agreements** page in the [AWS Marketplace Management Portal](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Select **Agreements** from the menu.

1. In the **Agreements** table, select the option next to the agreement and choose **View details**. Alternatively, you can choose the link for the agreement in the **Agreement ID** column.

1. On the agreement detail page, under the **Payment request** panel, select the option next to the payment request ID and choose **View details**.

1. On the payment request detail page, choose **Cancel Payment Request**.
**Note**  
You may cancel your payment request at any time while it is in pending state. You can no longer cancel the payment once the buyer has approved the payment request.

### Payment request statuses
<a name="proserv-payment-request-statuses"></a>

Pending  
Your payment request has been submitted and is pending buyer action. You can cancel the payment request if it is in pending state.

Canceled  
The payment request has been cancelled by the seller. Cancelled payment requests are no longer active/valid.

Accepted  
The buyer has accepted your payment.

Declined  
The buyer has declined to approve this payment request. You should contact your buyer to address any payment issues.