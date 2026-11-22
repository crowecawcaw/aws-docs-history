

# VAT on Deemed Supply

Under EU, Norway and UK VAT rules, when AWS Marketplace facilitates the sale of Digital Services (e.g. SaaS, AMI), the law establishes two back-to-back supplies for VAT purposes only:
+ **Deemed Sale 1:** The Seller is treated as having supplied the Digital Service to the applicable branch of Amazon Web Services EMEA SARL ("AWS EMEA") facilitating the transaction.
+ **Deemed Sale 2:** The branch of AWS EMEA facilitating the transaction is treated as having supplied the Digital Service to the Buyer.

As a result of the Deemed Supply provisions, when both the Seller and the Buyer are in the same EU Member State, Norway or in the UK, and the transaction is facilitated by the relevant AWS EMEA branch in the same country, the Seller is expected to issue a VAT invoice to that AWS EMEA branch. AWS EMEA will pay the VAT stated on the invoice, subject to receipt of a valid VAT invoice.

You can submit invoices for transactions of AWS Marketplace sales of Digital Services where all three of the following conditions are met:

1. The Seller AWS account is located in an EU Member State, the UK or Norway.

1. The Buyer AWS account is located in the same country as the Seller.

1. The AWS Marketplace sale is facilitated by the corresponding AWS EMEA SARL branch in that country.

## Getting Started — How to view and submit your invoices for VAT on deemed supply
<a name="vat-deemed-supply-getting-started"></a>

### Step 1: Log in to AWS Partner Central
<a name="vat-deemed-supply-step1"></a>

1. Go to the AWS Console and search for AWS Partner Central

1. Choose Launch AWS Partner Central

1. In the bottom-left panel, select Marketplace Settings

![The AWS Partner Central console showing the Marketplace Settings option in the bottom-left panel.](https://docs.aws.amazon.com/marketplace/latest/userguide/images/vat-deemed-supply-screenshot-1.png)


### Step 2: Navigate to the VAT on deemed supply Section
<a name="vat-deemed-supply-step2"></a>

1. Go to Settings in AWS Partner Central

1. Choose the Tax information tab

1. Scroll down to the VAT on deemed supply section

![The Tax information tab in AWS Partner Central showing the VAT on deemed supply section.](https://docs.aws.amazon.com/marketplace/latest/userguide/images/vat-deemed-supply-screenshot-2.png)


Here you can expand two tables:
+ **VAT on deemed supply — eligible line items:** transactions eligible for VAT Invoicing  
![The VAT on deemed supply eligible line items table showing transactions eligible for VAT invoicing.](https://docs.aws.amazon.com/marketplace/latest/userguide/images/vat-deemed-supply-screenshot-3.png)
+ **VAT on deemed supply submissions:** your submitted VAT invoices and their status  
![The VAT on deemed supply submissions table showing submitted VAT invoices and their status.](https://docs.aws.amazon.com/marketplace/latest/userguide/images/vat-deemed-supply-screenshot-4.png)

### Step 3: Select Line Items for Submission
<a name="vat-deemed-supply-step3"></a>

1. Expand the VAT on deemed supply — eligible line items table, review your eligible transactions

1. Select one or more line items in the same currency (USD, EUR, or GBP)
   + Paid items qualify for immediate disbursement
   + Unpaid items can be selected but will only be disbursed once the buyer invoice is collected

1. Choose Apply VAT Disbursement

![Selecting line items and choosing Apply VAT Disbursement.](https://docs.aws.amazon.com/marketplace/latest/userguide/images/vat-deemed-supply-screenshot-5.png)


**Note**  
You can submit individual invoices for individual line items, or a single consolidated invoice covering multiple line items in the same currency.

### Step 4: Upload Your VAT Invoice
<a name="vat-deemed-supply-step4"></a>

1. On the Apply VAT on deemed supply page, review your selected line items and disbursement summary

1. Upload your VAT invoice:
   + Accepted formats: PDF, or XML where electronic invoicing is required (Italy, Belgium, Poland, and Romania). For more information about e-invoicing requirements, see [Do I need to submit an e-invoice instead of a PDF?](vat-deemed-supply-faq.md#faq-e-invoicing).
   + Maximum file size: 10 MB
   + All selected line items must be included in a single uploaded file

1. Choose Submit VAT on deemed supply disbursement

![The Apply VAT on deemed supply page showing selected line items, disbursement summary, and invoice upload.](https://docs.aws.amazon.com/marketplace/latest/userguide/images/vat-deemed-supply-screenshot-6.png)


### Step 5: Track Your Submission
<a name="vat-deemed-supply-step5"></a>

After submission, your line item will move from the Eligible Line Items table to the VAT on deemed supply Submissions table. Each submission is assigned a unique task ID. Submission statuses are:
+ **Accepted** — Your invoice has been validated. No further action is required. A green banner is displayed for 7 days.
+ **Rejected** — Your invoice could not be validated. Remediation action required, please verify reject reason and address in your next amended invoice upload. A yellow banner is displayed for 7 days with the reason for rejection.
+ **Pending** — Your submission is under review and is pending AWS for approval. (SLA: up to 3 business days).

**Note**  
To check your disbursement status, visit the Collections and Disbursements dashboard.

Refer to [Deemed Supply FAQs](vat-deemed-supply-faq.md) for more details.

![The VAT on deemed supply submissions table showing submission statuses.](https://docs.aws.amazon.com/marketplace/latest/userguide/images/vat-deemed-supply-screenshot-7.png)


## Submit a credit note for a refund
<a name="vat-deemed-supply-refunds"></a>

If AWS previously disbursed VAT to you for a transaction that is later refunded, you can submit the corresponding credit note directly in AWS Partner Central. When you finish, your credit note is submitted for validation and you can track its status in the submissions table.

### Step 1: Find the refund
<a name="vat-deemed-supply-refunds-step1"></a>

In AWS Partner Central, choose **Settings**, choose the **Tax information** tab, and scroll down to the **VAT on deemed supply** section. In the eligible line items table, locate the refund that you want to submit a credit note for. Refunds appear as separate line items and display negative amounts.

If you do not see an expected refund:
+ Confirm that your selected date range includes the transaction.
+ Allow up to 72 hours after the Buyer refund is generated for the refund to appear.

![The VAT on deemed supply eligible line items table showing refund line items with negative amounts.](https://docs.aws.amazon.com/marketplace/latest/userguide/images/vat-deemed-supply-screenshot-8.png)


### Step 2: Select the refund and upload your credit note
<a name="vat-deemed-supply-refunds-step2"></a>

Select the refund line item or eligible refund line items covered by your credit note, and then choose **Apply VAT disbursement**. Upload the applicable credit-note document:
+ Use PDF where electronic invoicing is not required.
+ Use the applicable XML format where electronic invoicing is required.
+ The maximum file size is 10 MB.

**Note**  
You can include multiple eligible refunds in one submission when the portal allows them to be selected together. You can select up to 100 eligible line items in a submission.

![The Apply VAT on deemed supply page showing a selected refund line item with a negative VAT amount and an uploaded credit note.](https://docs.aws.amazon.com/marketplace/latest/userguide/images/vat-deemed-supply-screenshot-9.png)


### Step 3: Review and submit
<a name="vat-deemed-supply-refunds-step3"></a>

Review the selected refund line items and the details of your credit note. Confirm that the VAT amount on your credit note matches the VAT amount displayed for the selected refunds. When prompted to confirm the total, enter the amount exactly as displayed, including the minus sign where applicable.

Choose **Submit VAT on deemed supply disbursement** and complete the confirmation.

**Note**  
Submitting a credit note does not itself trigger VAT recovery. For more information about when AWS recovers VAT, see [Does submitting a credit note trigger VAT recovery?](vat-deemed-supply-faq.md#faq-refund-recovery-trigger).

### Step 4: Track your credit-note submission
<a name="vat-deemed-supply-refunds-step4"></a>

After submitting your credit note, use the VAT on deemed supply submissions table to track its status. Your submission can show:
+ **Pending** – AWS received the document and is reviewing it.
+ **Accepted** – AWS successfully validated the document.
+ **Rejected** – The document did not pass validation and needs to be corrected.

If your credit note is rejected, the applicable refund line items become available again so that you can correct the document and submit a new credit note.

![The VAT on deemed supply submissions table showing an accepted credit-note submission with a negative VAT amount.](https://docs.aws.amazon.com/marketplace/latest/userguide/images/vat-deemed-supply-screenshot-10.png)


For more information about credit-note requirements, VAT recovery, document formats, and rejected submissions, see [Deemed Supply FAQs](vat-deemed-supply-faq.md).