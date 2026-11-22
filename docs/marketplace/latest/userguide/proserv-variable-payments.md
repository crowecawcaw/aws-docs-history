

# Pricing professional service products in AWS Marketplace

As an AWS Marketplace seller with a Professional Services product, you can choose from three contract pricing options: installment plan, upfront payment, and variable payments. Variable payments allow you to set a total contract amount when creating a private offer. Once buyers accept the contract, you send payment requests, up to the total contract amount, over the duration of the contract.

## Creating a private offer with variable payment
<a name="proserv-variable-create-offer"></a>

**To create a private offer with variable payment**

1. Open the [**Offers**](https://console.aws.amazon.com/partnercentral/offers) page in AWS Partner Central, and sign in to your seller account.

1. On the **Private offers** tab, choose **Create private offer**.

1. For **Product type**, choose **Professional service product**, and then choose your product under **Product**.

1. Choose **Continue to offer details**.

1. On the **Provide offer information** step, enter an **Offer name** and an **Offer expiration date**, and then choose **Next**.

   The buyer must respond to your offer by 23:59 UTC on the expiration date, or the offer expires. **Offer purpose** defaults to **Not a renewal**.

1. On the **Configure offer pricing and duration** step, choose **Variable payments**, and then enter the **Contract total**.

   The contract total is the most that your payment requests can add up to. Set the contract duration and offer currency on the same step.

1. Complete the remaining steps, and then on the **Review and create** step, choose **Create offer**.

## Payment requests
<a name="proserv-payment-requests"></a>

Once your buyer accepts a professional services private offer with variable payments contract pricing, you can send payment requests up to the total contract value, over the duration of the contract.

### Creating payment requests
<a name="proserv-create-payment-request"></a>

**To create payment requests**

1. Open the [**Agreements**](https://console.aws.amazon.com/partnercentral/agreements) page in AWS Partner Central, and sign in to your seller account.

1. On the **Active agreements** tab, choose the agreement in the **Agreement ID** column.

1. Choose **Request payment**.

   This button appears only for agreements with variable payments. It's unavailable when the agreement isn't active or the remaining amount is zero.

1. For **Requested amount**, enter the amount to bill.

   The amount can't exceed the **Remaining amount** under **Agreement information**.

1. For **Payment request title**, enter a title of 6 to 64 characters that starts with a letter.

1. (Optional) Enter a **Description** of the deliverables and an **Invoice memo**.

   The description can have up to 2,000 characters. The invoice memo appears on the AWS invoice PDF that the buyer receives, and can have up to 255 characters.

1. Choose **Create**.

The buyer receives an email message to review the payment request. The request appears on the agreement's **Payment requests** tab with a status of **Pending response**.

### Canceling payment requests
<a name="proserv-cancel-payment-request"></a>

**To cancel a payment request**

1. Open the [**Agreements**](https://console.aws.amazon.com/partnercentral/agreements) page in AWS Partner Central, and sign in to your seller account.

1. On the **Active agreements** tab, choose the agreement in the **Agreement ID** column.

1. Choose the **Payment requests** tab.

1. Select the payment request, and then choose **Cancel payment request**.

   You can cancel a request only while its status is **Pending response**.

1. In the **Cancel payment request** dialog box, choose **Confirm cancellation**.

AWS Partner Central cancels the request and notifies the buyer. You can't undo a cancellation.

### Payment request statuses
<a name="proserv-payment-request-statuses"></a>

Pending response  
Your payment request has been submitted and is pending buyer action. You can cancel a payment request with this status.

Canceled  
The payment request has been cancelled by the seller. Cancelled payment requests are no longer active/valid.

Accepted  
The buyer has accepted your payment.

Declined  
The buyer has declined to approve this payment request. You should contact your buyer to address any payment issues.