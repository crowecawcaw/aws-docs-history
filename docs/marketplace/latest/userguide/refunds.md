

# Refunds and cancellations in AWS Marketplace
<a name="refunds"></a>

All paid products in AWS Marketplace must have a stated refund policy for software charges. The refund policy must include the terms of the refund and a method of contacting the seller to request a refund.

As a seller, you are responsible for defining the terms of your refund policy. However, we encourage you to offer buyers a refund option for usage of the product. You must comply with your posted refund policies.

AWS Marketplace provides self-service tools for sellers to initiate agreement cancellations and billing adjustments (refunds) directly from the [**Agreements** tab](https://aws.amazon.com/marketplace/management/agreements/) in AWS Partner Central (formerly AWS Marketplace Management Portal) or through the AWS Marketplace APIs, without requiring AWS Customer Service involvement. Billing adjustments are processed automatically after validation and do not require buyer approval. Cancellation requests are sent to buyers for approval with a 7-day response window.

For a walkthrough of how to request a cancellation and apply a billing adjustment, see the [self-service cancellations and billing adjustments demo video](https://vimeo.com/1178864627/3f8a6d5bbc) (5 minutes) on the Vimeo website.

**Note**  
In AWS Partner Central, refunds are referred to as *billing adjustments*. Both terms refer to the same process of returning funds to a buyer or reducing the outstanding balance on an invoice.

**Topics**
+ [Refund request types for AWS Marketplace products](#refund-requests)
+ [AWS Marketplace product refund policy and approvals](#refund-approval)
+ [Requesting an agreement cancellation](#requesting-cancellation)
+ [Requesting a billing adjustment (refund)](#refund-process)
+ [Tracking cancellation requests](#tracking-cancellations)
+ [Tracking billing adjustments](#tracking-billing-adjustments)
+ [Notifications](#scaba-notifications)
+ [Using the AWS Marketplace APIs](#scaba-apis)
+ [Channel Partner Private Offers (CPPO)](#cppo-cancellations-adjustments)
+ [Requesting a bulk refund](#bulk-refund-process)
+ [Requesting a refund or cancellation through AWS Support](#legacy-refund-process)

## Refund request types for AWS Marketplace products
<a name="refund-requests"></a>

Buyers can request different types of refunds for AWS Marketplace products. For AWS Marketplace products sold by AWS, refer to the refund policy page and then submit a support case using the [Support Center Console](https://console.aws.amazon.com/support/home?). If a buyer requests a software refund directly from AWS, we instruct them to contact the seller using the support contact information you provided for the product in question. Refunds of any AWS infrastructure charges are at the discretion of AWS and are handled separately from software refunds.

For products sold by a third-party seller, buyers must refer to the product detail page to view the refund policy. Software charges for AWS Marketplace subscriptions are paid to the seller of record, and refunds must be requested from the seller directly.

## AWS Marketplace product refund policy and approvals
<a name="refund-approval"></a>

The following list describes the AWS Marketplace refund policy and whether your approval is needed:
+ **Free trials** — If you list your software as a free trial product, AWS can issue refunds on your behalf for software charges that accrue within seven days of converting to a paid subscription. Refunds issued in connection with free trial conversions require no action on your part. By enabling a free trial on a product, you agree to this policy.
+ **Private offers** — All refunds for private offers must be authorized by you before AWS can process them.
+ **Software metering refunds** — If you use the AWS Marketplace Metering Service to meter the usage of your software, AWS can issue refunds on your behalf for software charges resulting from software metering errors. If these errors are common across multiple buyers, AWS reserves the right to determine an appropriate refund for each buyer and apply it directly to each buyer. By using the AWS Marketplace Metering Service with a product, you are agreeing to this policy.
+ **Subscription cancellation within 48 hours of purchase** — If a buyer cancels their subscription within 48 hours of a non-private offer purchase, AWS issues a full refund (cancel with 100 percent refund). Refunds issued in connection with cancellation within 48 hours of purchase require no action on your part. After 48 hours, such buyer request is at your discretion. By listing your product on AWS Marketplace, you agree to this policy. Buyers cancel pay-as-you-go (usage-based) subscriptions themselves in the AWS Marketplace console. For contract (upfront) pricing, self-service cancellation isn't available, so buyers request cancellation through AWS Customer Service. For requests made within 48 hours of purchase, AWS cancels and refunds the buyer directly, with no action on your part.
+ **Subscription upgrade** — If a buyer replaces an existing non-private offer subscription with a more expensive subscription or a subscription of equal value, AWS can issue refunds on your behalf for the lower-tier subscription.
+ **Subscription downgrade** — All downgrade subscription refund requests must be authorized by you before AWS can process them.
+ **Seller-initiated billing adjustments** — As the seller of record, you can initiate billing adjustments (refunds) for any agreement through the [**Agreements**](https://aws.amazon.com/marketplace/management/agreements/) page in AWS Partner Central or through the Billing Adjustments API. Billing adjustments don't require buyer approval and are processed automatically after validation. Refunds are irreversible after they've been processed.
+ **Seller-initiated cancellations** — As the seller of record, you can initiate agreement cancellation requests through the **Agreements** page in AWS Partner Central or through the Cancellation API. Cancellation requests are sent to the buyer for approval. If the buyer doesn't respond within 7 days, the cancellation is automatically approved and the agreement is canceled.

All AWS-authorized refunds are processed automatically and require no action on your part.

## Requesting an agreement cancellation
<a name="requesting-cancellation"></a>

You can initiate an agreement cancellation request from the [**Agreements**](https://aws.amazon.com/marketplace/management/agreements/) page in AWS Partner Central. Cancellation requests are sent to the buyer for approval. The buyer has 7 days to approve or deny the request. If the buyer doesn't respond within 7 days, the cancellation is automatically approved and the agreement is canceled.

**Important**  
Cancellation only cancels future invoices that have not been issued. It doesn't automatically refund existing open invoices. If you also need to refund past charges, you must submit a separate billing adjustment request. See [Requesting a billing adjustment (refund)](#refund-process).

### Prerequisites
<a name="cancellation-prerequisites"></a>
+ You must be the seller of record for the agreement. For Marketplace Private Offers (MPPO), this is the ISV. For Channel Partner Private Offers (CPPO), this is the channel partner (CP).
+ The agreement must be active.
+ There must not be an existing active cancellation request for the same agreement.
+ No related agreement should exist for the agreement being canceled. For instance, a usage agreement can't be canceled if it has an associated annual discount agreement.

### To request an agreement cancellation
<a name="cancellation-procedure"></a>

1. Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home) and go to the [**Agreements**](https://aws.amazon.com/marketplace/management/agreements/) page.

1. Select the agreement you want to cancel and choose **Request cancellation**.

1. Review the agreement information (Buyer account ID, Agreement ID, Offer ID). Choose a cancellation reason from the dropdown. In the **Additional details** field, you can optionally include a message to the buyer.

1. Choose **Submit request**.

1. Upon successful submission, you'll receive a link to the buyer response form. You can optionally expedite the process by sharing the response form link with the buyer directly. You can also copy the link later from the **Cancellation requests** tracking table.

### Withdrawing a cancellation request
<a name="withdrawing-cancellation"></a>

You can withdraw a pending cancellation request from either the **Cancellation requests** tab or the request details page. To withdraw a pending request from the **Cancellation requests** tab, select the request you want to withdraw and choose **Withdraw request**. In the dialog box, provide a withdrawal reason.

## Requesting a billing adjustment (refund)
<a name="refund-process"></a>

You can initiate billing adjustments (refunds) from the [**Agreements**](https://aws.amazon.com/marketplace/management/agreements/) page in AWS Partner Central. Billing adjustments allow you to either refund buyers for charges on existing invoices, or reduce the outstanding balance on invoices that have not yet been paid. Billing adjustments don't require buyer approval and are processed immediately upon successful validation.

**Important**  
If the billing adjustment you want to apply is dependent on cancellation of the agreement, submit the cancellation request first and wait for approval before submitting the billing adjustment.

### Prerequisites
<a name="billing-adjustment-prerequisites"></a>
+ You must be the seller of record for the agreement. For Marketplace Private Offers (MPPO), this is the ISV. For Channel Partner Private Offers (CPPO), this is the channel partner (CP).
+ To adjust invoices issued in countries with Know Your Customer (KYC) compliance requirements, you must first complete secondary user verification and enable multi-factor authentication (MFA). To become KYC-verified, see [Complete the Know Your Customer process](https://docs.aws.amazon.com/marketplace/latest/userguide/complete-kyc-process.html) and [Managing your secondary user for KYC](https://docs.aws.amazon.com/marketplace/latest/userguide/managing-secondary-users.html) for more information.

### To apply a billing adjustment
<a name="billing-adjustment-procedure"></a>

1. Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home) and go to the [**Agreements**](https://aws.amazon.com/marketplace/management/agreements/) page.

1. Select the agreement you want to adjust and choose **Apply billing adjustment**.

The billing adjustment wizard guides you through four steps:

**Step 1: Provide details**

Review the agreement information (Buyer account ID, Agreement ID, Offer ID). Choose a billing adjustment reason from the dropdown. In the **Additional details** field, you can optionally include a message to the buyer. Choose **Next**.

**Step 2: Select invoices**

In the **Available invoices** table, select the invoices you want to adjust. You can filter invoices by either invoice date or billing period. Choose **Next**.

**Step 3: Adjust billing amounts**

You can either start from zero and manually enter custom adjustment amounts for each selected invoice, or you can start from the maximum adjustment amount per invoice and optionally modify individual amounts as needed. The value you enter must be a positive number and can't exceed the maximum adjustment amount for that invoice, and is exclusive of taxes. If the maximum adjustment amount is less than the original charge amount, this indicates that a partial adjustment was previously applied. In this case, the maximum adjustment amount represents the remaining balance. After you've made your adjustments, choose **Next**.

**Step 4: Review and apply**

Review the details of your billing adjustment to ensure that all the information is correct. Next, choose **Apply billing adjustment**. In the confirmation window, provide written confirmation by typing the total adjustment amount.

**Important**  
Billing adjustments are irreversible after they have been processed. For unpaid invoices, adjustments are deducted from the total amount due. For paid invoices, adjustments are applied as either credit memos or cash refunds.

The buyer is notified by email and Amazon EventBridge event when the billing adjustment is processed.

## Tracking cancellation requests
<a name="tracking-cancellations"></a>

You can track all cancellation requests from the **Cancellation requests** tab on the [**Agreements**](https://aws.amazon.com/marketplace/management/agreements/) page.

1. Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Navigate to the **Agreements** page.

1. Choose the **Cancellation requests** tab.

The cancellation requests table displays the following columns: Request ID, Request status, Agreement ID, Buyer ID, Request date, and Response date.

You can filter by **status** or **agreement ID**.

To view details of a specific request, select the request and choose **View details**. You can also choose **Withdraw request** to withdraw a pending request, or **Copy link** to copy the buyer approval link.

### Cancellation request statuses
<a name="cancellation-statuses"></a>


| API status | UI label | Description | 
| --- | --- | --- | 
| Pending approval | Pending approval | The request has been submitted and is waiting for the buyer to approve or deny. The buyer has 7 days to respond. If no response is received, the request is automatically approved. | 
| Approved | Approved | The buyer approved the cancellation, or the request was automatically approved after 7 days. The agreement is canceled. | 
| Rejected | Denied | The buyer denied the cancellation request. You can submit a new request if needed. | 
| Canceled | Withdrawn | You withdrew the cancellation request before the buyer took action. | 
| Validation failed | Validation failed | The request did not pass automated validation. | 

## Tracking billing adjustments
<a name="tracking-billing-adjustments"></a>

You can track all billing adjustment requests from the **Billing adjustments** tab on the [**Agreements**](https://aws.amazon.com/marketplace/management/agreements/) page.

1. Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Navigate to the **Agreements** page.

1. Choose the **Billing adjustments** tab.

The billing adjustments table displays the following columns: Adjustment ID, Invoice ID, Status, Agreement ID, Buyer ID, Submitted, Processed, and Creation date.

You can filter by **agreement ID**, **creation date**, or **status**.

**Note**  
If you submitted billing adjustments for multiple invoices in a single request, each invoice appears as a separate row in the table. All rows from the same submission will have different billing adjustment request IDs.

### Billing adjustment statuses
<a name="billing-adjustment-statuses"></a>


| API status | UI label | Description | 
| --- | --- | --- | 
| Pending | In progress | The adjustment has been submitted and is being processed. | 
| Completed | Adjusted | The adjustment was processed successfully. The buyer receives a credit memo or cash refund. | 
| Validation failed | Failed | Your billing adjustment request failed automated checks. You may need to submit a new request with corrected information. | 

## Notifications
<a name="scaba-notifications"></a>

You receive automated notifications for cancellation and billing adjustment status updates through two channels:
+ **Email notifications** — Sent to the root email associated with your AWS account. You can also [add custom email aliases](https://docs.aws.amazon.com/marketplace/latest/userguide/email-notifications.html#adding-updating-email-addresses) for notifications and [unsubscribe recipients](https://docs.aws.amazon.com/marketplace/latest/userguide/email-notifications.html#unsubscribe-notifications) from email notifications.
+ **[Amazon EventBridge](https://docs.aws.amazon.com/marketplace/latest/userguide/notifications-eventbridge.html) events** — Sent to your account's default event bus, which you can use to trigger automated workflows.

### Cancellation notifications
<a name="cancellation-notifications"></a>


| Event | Recipients | Email subject (seller) | 
| --- | --- | --- | 
| Cancellation request submitted | Seller, Buyer, Manufacturer (CPPO) | "You submitted an agreement cancellation request" | 
| Cancellation request approved (by buyer or auto-approved) | Seller, Buyer, Manufacturer (CPPO) | "Agreement cancellation request approved" | 
| Cancellation request denied by buyer | Seller, Buyer, Manufacturer (CPPO) | "Agreement cancellation request denied" | 
| Cancellation request withdrawn by seller | Seller, Buyer, Manufacturer (CPPO) | "Agreement cancellation request withdrawn" | 
| Cancellation request failed validation | Submitter only | "Agreement cancellation request failed" | 

When a cancellation request is submitted, the seller's email also includes a **response form URL** that can be shared directly with the buyer to expedite approval.

### Billing adjustment notifications
<a name="billing-adjustment-notifications"></a>


| Event | Recipients | Email subject (seller) | 
| --- | --- | --- | 
| Billing adjustment processed | Seller, Buyer, Manufacturer (CPPO) | "Billing adjustment processed" | 
| Billing adjustment failed validation | Submitter only | "Billing adjustment request failed" | 

**Note**  
Billing adjustments don't generate a "submitted" notification. You receive a single notification when the adjustment is completed or if it fails.

**Note**  
If a billing adjustment fails instantly (for example, the refund amount exceeds the maximum refundable amount), the request is not created and no notification is sent. You see the error directly in the console or receive an error code through the API.

**Important**  
For CPPO agreements, the ISV (manufacturer) receives notifications when the channel partner submits or completes cancellation and billing adjustment requests. However, the refund amount and message to buyer are **not** included in ISV notifications to protect channel partner margin information.

## Using the AWS Marketplace APIs
<a name="scaba-apis"></a>

In addition to the console experience, you can manage cancellations and billing adjustments programmatically using the AWS Marketplace APIs.

### Cancellation API
<a name="cancellation-api"></a>

The AWS Marketplace Self-Service Cancellation API enables you to manage agreement cancellation requests programmatically.

**Endpoint:** `https://agreement-marketplace.us-east-1.amazonaws.com`


| Operation | Description | 
| --- | --- | 
| SendAgreementCancellationRequest | Initiate a new cancellation request for an agreement | 
| AcceptAgreementCancellationRequest | Accept a pending cancellation request (buyer action) | 
| RejectAgreementCancellationRequest | Reject a pending cancellation request with a reason (buyer action) | 
| CancelAgreementCancellationRequest | Withdraw a pending cancellation request (seller action) | 
| GetAgreementCancellationRequest | Retrieve details of a specific cancellation request | 
| ListAgreementCancellationRequests | List cancellation requests with optional filters. Supports pagination. | 

### Billing Adjustments API
<a name="billing-adjustments-api"></a>

The AWS Marketplace Billing Adjustments API enables you to manage billing adjustments (refunds) programmatically.

**Endpoint:** `https://agreement-marketplace.us-east-1.amazonaws.com`


| Operation | Description | 
| --- | --- | 
| ListAgreementInvoiceLineItems | Retrieve invoice line items for an agreement to identify invoices eligible for adjustment | 
| BatchCreateBillingAdjustmentRequest | Create billing adjustment requests for one or more invoices (up to 5 per request) | 
| GetBillingAdjustmentRequest | Retrieve details of a specific billing adjustment request | 
| ListBillingAdjustmentRequests | List billing adjustment requests with optional filters. Supports pagination. | 

## Channel Partner Private Offers (CPPO)
<a name="cppo-cancellations-adjustments"></a>

For Channel Partner Private Offers (CPPO), the following rules apply:
+ Only the channel partner (CP), as the seller of record, can initiate cancellation and billing adjustment requests for CPPO agreements. The ISV can't initiate these requests.
+ The ISV (manufacturer) receives email and Amazon EventBridge notifications when the CP submits a cancellation or billing adjustment request.
+ ISV notifications include the selling authorization ID, Product ID, and Buyer AWS account ID, but don't include the refund amount or message to buyer to protect CP margin information.
+ The CP can view and track all active and historical cancellation and billing adjustment requests for CPPO agreements on the [**Agreements**](https://aws.amazon.com/marketplace/management/agreements/) page and through the APIs.

## Requesting a bulk refund
<a name="bulk-refund-process"></a>

You can also process billing adjustments programmatically using the Billing Adjustments API (`BatchCreateBillingAdjustmentRequest`), regardless of the number of invoices. See [Using the AWS Marketplace APIs](#scaba-apis).

The following steps explain how to create refund requests involving 20\+ invoices or 20\+ accounts using a support case. This process streamlines large-scale refund requests and ensures that you provide the necessary information.

**To request a bulk refund**

1. Gather the following required information:
   + The seller's AWS account ID (12 digits)
   + A list of all buyer AWS account IDs (12 digits each). You can enter multiple buyers, or single buyers for multiple billing periods.
   + All product IDs
   + Offer IDs where applicable
   + All invoice IDs
   + The billing periods for each invoice
   + The AWS Marketplace Refund Ticket Reference ID

1. Compile the required information into a CSV spreadsheet with the following columns:
   + **Seller Account ID**
   + **Subscriber Account ID**
   + **Payer Account ID**
   + **Billing Period**
   + **Invoice ID**
   + **Targeted Amount**
   + **Product ID**

1. Sign in to the [Support Center Console](https://console.aws.amazon.com/support/home?) as the root user or as an IAM user with either AWSMarketplaceSellerFullAccess or AWSMarketplaceSellerProductFullAccess permissions.
**Note**  
You can't complete these steps unless you sign in as the root user or as an IAM user with either AWSMarketplaceSellerFullAccess or AWSMarketplaceSellerProductFullAccess permissions.

1. Create a support case to **Account and billing** and select **AWS Marketplace**.

1. In the subject line, enter **Request Bulk Refund**.

1. Under **Additional Comments**, enter the following:
   + Total number of accounts affected
   + Total number of invoices
   + Total refund amount
   + Business justification for the refund
   + AWS Marketplace Refund Ticket Reference ID

1. Attach the CSV file and create the support case.

1. The support case is routed to the next available agent for assistance.

## Requesting a refund or cancellation through AWS Support
<a name="legacy-refund-process"></a>

Whenever you can, use the self-service tools in the [**Agreements**](https://aws.amazon.com/marketplace/management/agreements/) tab instead of a support case. Self-service requests are validated and processed automatically, so you don't wait for a support agent to pick up your case. For more information, see [Requesting an agreement cancellation](#requesting-cancellation) and [Requesting a billing adjustment (refund)](#refund-process).

Create an AWS Support case only when the **Agreements** tab doesn't support your request.

**To request a refund or cancellation through AWS Support**

1. Sign in to the [Support Center Console](https://console.aws.amazon.com/support/home) as the root user or as an IAM user with either AWSMarketplaceSellerFullAccess or AWSMarketplaceSellerProductFullAccess permissions.
**Note**  
You can't complete these steps unless you sign in as the root user or as an IAM user with either AWSMarketplaceSellerFullAccess or AWSMarketplaceSellerProductFullAccess permissions.

1. Create a support case to **Account and billing** and select **AWS Marketplace**, using the following details:
   + **Category:** Marketplace Seller Request
   + **Subject:** Refund/cancellation request

1. In the case description, state whether you're requesting a cancellation, a billing adjustment (refund), or both:
   + **Cancellation only** — Include: "Please cancel agreement {{agreement-id}}".
   + **Billing adjustment (refund) only** — Include: "This refund targets invoice ID {{invoice-id}} dated {{invoice-date}}". Also include the following:
     + **Billing period** — You can find this on the Billed Revenue Dashboard. For monthly usage invoices, this is the calendar month previous to the invoice date.
     + **Adjustment amount** — The amount to return to the buyer for an invoice they've already paid, or the amount to reduce the balance by on an invoice they haven't paid yet.
   + **Both a cancellation and a billing adjustment** — Include both statements. Canceling a contract doesn't automatically cancel any issued invoices — you must explicitly request an adjustment for each invoice that needs to be changed.

1. In the same description, also include the following details for any request:
   + **Subscriber's AWS account ID** — The buyer's account ID used to subscribe. You can find this in the offer detail or on the Billed Revenue Dashboard. This must be the subscriber account ID.
   + **Seller's AWS account ID** — Your AWS account ID used to create the offer.
   + **Product ID** — You can find this in the offer detail or on the Billed Revenue Dashboard.

1. Create the support case. The support case is routed to the next available agent for assistance.

To request a refund for 20 or more invoices or accounts, see [Requesting a bulk refund](#bulk-refund-process).