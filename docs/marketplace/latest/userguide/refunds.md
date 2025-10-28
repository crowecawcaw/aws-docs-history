# Product refunds in AWS Marketplace

###### Note

If you transact through an Amazon Web Services EMEA operator,
only verified users can process refunds, amend Know Your Customer (KYC) information, and change financial information
such as bank account details. Verified users are KYC verified users and secondary users who
complete verification. For more information on the KYC process, refer to
[Complete the Know Your Customer process](registration-process.md#complete-kyc-process "registration-process.md#complete-kyc-process").

All paid products in AWS Marketplace, regardless of pricing model, must have a stated refund policy
for software charges. The refund policy must include the terms of the refund, and a method
of contacting the seller to request a refund.

As a seller, the details of the refund policy are
up to you. However, we encourage you to offer buyers some manner of refund for usage of the
product. You must comply with your posted refund policies. This topic provides information about
the types of AWS Marketplace product refund requests, the related policy and approvals process, and how
you can submit a refund request for a buyer.

###### Topics

- [Refund request types for AWS Marketplace products](#refund-requests "#refund-requests")
- [AWS Marketplace product refund policy and approvals](#refund-approval "#refund-approval")
- [Requesting a product refund](#refund-process "#refund-process")
- [Requesting a bulk refund](#bulk-refund-process "#bulk-refund-process")

## Refund request types for AWS Marketplace products

Buyers can request different types of refunds for AWS Marketplace products. For AWS Marketplace products
sold by AWS, refer to the refund policy page and then submit the contact support form using
the AWS Support Center Console. If a buyer requests a software refund directly from AWS, we
instruct them to contact the seller using your posted support contact information for the
product in question. Refunds of any AWS infrastructure charges are up to the discretion of
AWS and are handled independently of software refunds.

For products sold by a third-party, buyers must view refund policies
on the product detail page. Software charges for AWS Marketplace subscriptions are paid to the seller of
the product, and refunds must be requested from the seller directly. Each AWS Marketplace seller is
required to include a refund policy on their AWS Marketplace page.

## AWS Marketplace product refund policy and approvals

The following list describes the AWS Marketplace refund policy and whether your approval is
needed:

- **Free trials**

If you list your software as a free trial product, AWS can issue refunds on your
behalf for software charges accruing within seven days of a conversion from a free trial
to a paid subscription. Refunds issued in connection with free trial conversions require
no action on your part. By enabling a free trial on a product, you agree to this
policy.

- **Private offers**

All refunds for private offers must be authorized by you before AWS can process
them.

- **Software metering refunds**

If you use the AWS Marketplace Metering Service to meter the usage of your software, AWS can issue
refunds on your behalf for software charges resulting from software metering errors. If
these errors are common across multiple buyers, AWS reserves the right to determine
an appropriate refund for each buyer and apply it directly to each buyer. Refunds
issued in connection with the AWS Marketplace Metering Service must be confirmed with the seller one time, but does
not require the seller to confirm each individual refund. By using the AWS Marketplace Metering Service with a
product, you are agreeing to this policy.

- **Subscription cancellation within 48 hours of
  purchase**

If a buyer cancels their subscription within 48 hours of a non-private offer purchase,
AWS issues a full refund (cancel with 100 percent refund). Refunds issued in
connection with cancellation within 48 hours of purchase require no action on your part.
After 48 hours, such buyer request is at your discretion. By listing your product on
AWS Marketplace, you agree to this policy.

- **Subscription upgrade**

If a buyer replaces an existing non-private offer subscription with a more expensive
subscription or a subscription of equal value, AWS can issue refunds on your behalf for
the lower-tier subscription. This is a two-step process for the buyer: Buy a new
subscription and then request cancellation of the old subscription with a refund.

- **Subscription downgrade**

All downgrade subscription refund requests must be authorized by you before AWS can
process them.

All AWS authorized refunds are processed automatically and require no action on your
part.

## Requesting a product refund

Use the following procedure to request a software refund for an external buyer or an
internal testing account.

###### To request a software refund

1. Gather the following information:
   - Buyer AWS account ID (12 digits) used to subscribe to the product. If the buyer
     is the payer of their organization, obtain the AWS account ID of the linked account
     used to subscribe.
   - The buyer’s email address that is associated with their AWS account.
   - Seller AWS account ID (12 digits).
   - Product ID. You can find the Product ID in the [agreements and renewals dashboard](agreements-renewals-dashboard.md "agreements-renewals-dashboard.md") or [billed revenue dashboard](billed-revenue-dashboard.md "billed-revenue-dashboard.md").
   - Offer ID. You can find the Offer ID in the [agreements and renewals dashboard](agreements-renewals-dashboard.md "agreements-renewals-dashboard.md") or [billed revenue dashboard](billed-revenue-dashboard.md "billed-revenue-dashboard.md"), **Offers** tab, or **Agreements** tab in the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/homepage "https://aws.amazon.com/marketplace/management/homepage").
   - Billing period.
   - Invoice number from your [billed revenue dashboard](billed-revenue-dashboard.md "billed-revenue-dashboard.md").
   - Pre-tax refund amount.

2. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management").
3. Choose **Support**.
4. Choose **Request Refund**.
5. Enter the subscriber's AWS account number, product ID, and billing period.
6. In the **Additional comments (optional)** field, enter a brief
   description of the request, including the product ID, refund type, and invoice number (if
   available). For example:

`Cancel the buyer’s subscription to *<product-ID>* and *<offer-ID>* and process a full refund for invoice *<invoice-number>*.` 7. To submit a request for a refund, upgrade, or downgrade of an annual subscription, do
the following:

    1. Verify the buyer has purchased an annual subscription using the [agreements and renewals dashboard](agreements-renewals-dashboard.md "agreements-renewals-dashboard.md") or [billed revenue dashboard](billed-revenue-dashboard.md "billed-revenue-dashboard.md").
    2. In the **Additional comments (optional)** field, enter the subscription cancellation date and specify if the buyer is requesting a refund, upgrade, or downgrade.

8.  Submit the form. We'll be notified and will begin to process the refund and issue it
    to the buyer.
9.  To manage the refund request, the AWS Marketplace buyer support team will create a corresponding support case in the [Support Center Console](https://console.aws.amazon.com/support/home? "https://console.aws.amazon.com/support/home?"). The status of the refund will appear in the subject line of the support case. The status can be one of the following:

        * **Completed** – The refund was processed and no
         further action is required.
        * **Pending** – The refund will be processed once
         the current billing cycle ends.
        * **Action Required** – The request could not be
         processed, and we need additional information from you. You can respond directly to
         the support case; however, you will also need to submit a new refund request
         form.

    A refund will appear in the buyer’s account
    within 24–48 hours. However, it can take up to five business days for the funds to
    appear in the buyer’s financial account.

## Requesting a bulk refund

The following steps explain how to create refund requests involving 20+ invoices or 20+ accounts,
This process streamlines large-scale refund requests and ensures that you provide the necessary information.

###### To request a bulk refund

1. Gather the following required information:
   - The seller's AWS account ID (12 digits)
   - A list of all buyer AWS account IDs (12 digits each). You can enter multiple buyers, or single buyers for multiple billing periods.
   - All product IDs
   - Offer IDs where applicable
   - All invoice IDs
   - The billing periods for each invoice
   - The AWS Marketplace Refund Ticket Reference ID

2. Compile the required information into a CSV spreadsheet with the following columns:
   - `Seller Account ID`
   - `Subscriber Account ID`
   - `Payer Account ID`
   - `Billing Period`
   - `Invoice ID`
   - `Targeted Amount`
   - `Product ID`

3. Sign in to the [Support Center Console](https://console.aws.amazon.com/support/home? "https://console.aws.amazon.com/support/home?") as the root user.

###### Note

You can't complete these steps unless you sign in as the root user. 4. Create a support case to **Account and billing** and select **AWS Marketplace**. 5. In the subject line, enter `Request Bulk Refund`. 6. Under **Additional Comments**, enter the following:

    * Total number of accounts affected
    * Total number of invoices
    * Total refund amount
    * Business justification for the refund
    * AWS Marketplace Refund Ticket Reference ID

7. Attach the CSV file and create the support case.
8. The support case is routed to the next available agent for assistance.
