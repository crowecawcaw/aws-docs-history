

# Deemed Supply FAQs

This FAQ answers commonly asked questions about VAT on AWS Marketplace Deemed Supplies in the EU, Norway and UK.

**Topics**
+ **General**
+ [What is a "Deemed Supply" on AWS Marketplace?](#faq-what-is-deemed-supply)
+ [Which transactions can I currently submit through the VAT on Deemed Supply tool?](#faq-which-transactions)
+ **Identifying the Correct AWS EMEA Branch**
+ [How do I identify which AWS EMEA branch I need to invoice?](#faq-identify-branch)
+ [For which countries can I submit a request for VAT on Deemed Supply?](#faq-countries-branches)
+ [What if I sell to Buyers in the UK, Norway and multiple EU countries?](#faq-multiple-countries)
+ **Access and Permissions**
+ [Why can't I see the Deemed VAT section in my AWS Marketplace Management portal?](#faq-iam-permissions)
+ **Invoice Submission Process**
+ [How do I submit a VAT invoice for VAT payment?](#faq-how-to-submit)
+ [Can I submit a VAT invoice for a Deemed Supply before the Buyer has paid AWS?](#faq-submit-before-buyer-paid)
+ [Can I consolidate multiple transactions into a single invoice?](#faq-consolidate-invoices)
+ [Is there a time limit for submitting a VAT invoice for a Deemed Supply?](#faq-time-limit)
+ **Mandatory Invoice Fields**
+ [What information must be included on my VAT invoice for a Deemed Supply?](#faq-mandatory-fields)
+ **Invoice Language and Legal References**
+ [What legal reference should I include on my VAT invoice?](#faq-legal-reference)
+ **E-Invoicing**
+ [Do I need to submit an e-invoice instead of a PDF?](#faq-e-invoicing)
+ **VAT Payment**
+ [How and when will I receive the VAT disbursement?](#faq-receive-disbursement)
+ [How can I track the status of my VAT payment?](#faq-track-status)
+ **Refunds and Credit Notes**
+ [When do I need to submit a credit note for a refund?](#faq-refund-when-credit-note)
+ [What happens if a Buyer is refunded after I have already received the VAT disbursement?](#faq-refund-credit-note)
+ [Where can I find refunds and submit a credit note?](#faq-refund-find-submit)
+ [How can I identify a refund?](#faq-refund-identify)
+ [How soon will a refund appear in AWS Partner Central?](#faq-refund-timing)
+ [Does submitting a credit note trigger VAT recovery?](#faq-refund-recovery-trigger)
+ [What will I see when AWS recovers the VAT?](#faq-refund-recovery-view)
+ [Can I include multiple refunds on one credit note?](#faq-refund-consolidate)
+ [Should I submit a PDF or an XML credit note?](#faq-refund-format)
+ [How can I check whether my credit note was accepted?](#faq-refund-status)
+ [What should I enter in the Type of Document field?](#faq-refund-document-type)
+ **Self-Billing**
+ [Can AWS generate a VAT invoice for Deemed Supplies on my behalf?](#faq-self-billing)
+ **Reporting and Reconciliation**
+ [How do I identify which transactions I can submit VAT invoices for?](#faq-identify-transactions)
+ [Where can I see whether VAT has been disbursed for my eligible transactions?](#faq-vat-disbursed)
+ [How do I reconcile VAT disbursement?](#faq-reconcile-vat-disbursement)
+ **Errors, Duplicates, and Corrections**
+ [What happens if my invoice is rejected?](#faq-invoice-rejected)
+ [Can I submit more than one invoice for the same transaction?](#faq-duplicate-invoice)
+ **Deemed VAT Supply vs Tax Portal**
+ [How do Deemed VAT Supply Invoicing and the Tax Portal differ?](#faq-deemed-vs-tax-portal)
+ **Support**
+ [Where can I get additional help with VAT on Deemed Supplies?](#faq-additional-help)

## What is a "Deemed Supply" on AWS Marketplace?
<a name="faq-what-is-deemed-supply"></a>

Under EU, Norway and UK VAT rules, when AWS Marketplace facilitates the sale of Digital Services (e.g. SaaS, AMI), the law establishes two back-to-back supplies for VAT purposes only:
+ **Deemed Sale 1:** The Seller is treated as having supplied the Digital Service to the applicable branch of Amazon Web Services EMEA SARL ("AWS EMEA") facilitating the transaction.
+ **Deemed Sale 2:** The branch of AWS EMEA facilitating the transaction is treated as having supplied the Digital Service to the Buyer.

This treatment arises under the provisions of Article 9a of EU VAT Council Regulation 282/2011 of 15 March 2011 and Article 28 of EU VAT Directive 2006/112/EC (for EU transactions), the provisions of Section 47(4) of the UK VAT Act 1994 (for UK transactions) and the Merverdiavgiftsloven - Norwegian VAT Act § 3-1, second paragraph (for Norway transactions). These are collectively referred to as "Marketplace Operator Rules".

Please note that this treatment is for VAT purposes only and it does not change the commercial and legal relationship between Buyer and Seller.

As a result of the Deemed Supply provisions, when both the Seller and the Buyer are in the same EU Member State, Norway or in the UK, and the transaction is facilitated by the relevant AWS EMEA branch in the same country, an obligation might exist for VAT to be paid by the Marketplace Operator to the Seller. Sellers can issue a VAT invoice to that AWS EMEA branch facilitating the transaction and AWS EMEA will pay the VAT stated on the invoice, subject to receipt of a valid VAT invoice.

## Which transactions can I currently submit through the VAT on Deemed Supply tool?
<a name="faq-which-transactions"></a>

Currently, you can submit invoices for transactions of AWS Marketplace sales of Digital Services where all three of the following conditions are met:

1. The Seller AWS account is located in the UK, Norway or an EU Member State where AWS EMEA SARL has a branch.

1. The Buyer AWS account is located in the same country as the Seller.

1. The AWS Marketplace sale is facilitated by the corresponding AWS EMEA SARL branch in that country.

This applies to all Marketplace Private Offer (MPPO) transactions, including both B2B and B2C sales. Consulting Partner Private Offer (CPPO) transactions between ISV - Distributor and ISV/Distributor - Channel Partners are currently out of scope for the VAT payment on Deemed Supply automation. Channel Partners can submit VAT invoices for their Private Offer transactions under a CPPO agreement.

For any other transactions where the Seller needs to raise an invoice under Marketplace Operator rules (i.e. cross-border sales), please continue to email invoices (PDF) to: awsmpeuisv@amazon.com.

## How do I identify which AWS EMEA branch I need to invoice?
<a name="faq-identify-branch"></a>

Your invoice must be addressed to the AWS EMEA branch where the Buyer is located. The Buyer's country code determines the correct branch. To identify the country of the branch facilitating the transaction, navigate to the Tax Information Tab in AWS Partner Central.

**Important**  
Always use the branch information as displayed in these FAQs. Do not assume the branch name and address based on the Buyer's country alone. The correct legal entity name and address must be verified in the branch listing.

## For which countries can I submit a request for VAT on Deemed Supply?
<a name="faq-countries-branches"></a>

The following countries and branch names are where Sellers can submit for VAT payment under Deemed Supply rules on AWS Marketplace:

Luxembourg (Headquarters)  
Legal Name: Amazon Web Services EMEA SARL  
Address: 38 Avenue John F. Kennedy, L-1855 Luxembourg  
Legal Basis: EU Art 9a / Art 28

Austria  
Legal Name: Amazon Web Services EMEA SARL, Austrian Branch  
Address: Wiedner Gurtel 13, Turm 24/17.OG, 1100 Vienna, Austria  
Legal Basis: EU Art 9a / Art 28

Belgium  
Legal Name: Amazon Web Services EMEA SARL, succursale belge  
Address: Avenue des Arts 27, 5th Floor, 1040 Brussels, Belgium  
Legal Basis: EU Art 9a / Art 28

Czech Republic  
Legal Name: Amazon Web Services EMEA SARL, Czech Branch  
Address: Sokolovska 689/115, Karlin, 186 00 Prague, Czech Republic  
Legal Basis: EU Art 9a / Art 28

Denmark  
Legal Name: Amazon Web Services, Dansk filial af Amazon Web Services EMEA SARL, Luxembourg  
Address: c/o Spaces Ny Carlsberg Vej 80, 1799 Copenhagen, Denmark  
Legal Basis: EU Art 9a / Art 28

Estonia  
Legal Name: Amazon Web Services EMEA SARL, Eesti filiaal  
Address: Sopruse pst 145, Kristiine linnaosa, Tallinn, Harju maakond 13425, Estonia  
Legal Basis: EU Art 9a / Art 28

Finland  
Legal Name: Amazon Web Services EMEA SARL, sivuliike Suomessa  
Address: c/o HEM13 Mikonkatu 7, 00100 Helsinki, Finland  
Legal Basis: EU Art 9a / Art 28

France  
Legal Name: Amazon Web Services EMEA SARL, succursale francaise  
Address: 31 place des Corolles, Tour Carpe Diem, 92400 Courbevoie, France  
Legal Basis: EU Art 9a / Art 28

Germany  
Legal Name: Amazon Web Services EMEA SARL, Niederlassung Deutschland  
Address: Anni-Albers-Str. 21, 80807 Munchen, Deutschland  
Legal Basis: EU Art 9a / Art 28

Greece  
Legal Name: Amazon Web Services EMEA SARL Greek Branch  
Address: Athens Green Plaza, Ag. Konstantinou 59-61, Suite 136, Maroussi, Athens, Greece  
Legal Basis: EU Art 9a / Art 28

Ireland  
Legal Name: Amazon Web Services EMEA SARL, Irish Branch  
Address: One Burlington Plaza, Burlington Road, Dublin 4, Ireland  
Legal Basis: EU Art 9a / Art 28

Italy  
Legal Name: Amazon Web Services EMEA SARL, sede secondaria  
Address: Viale Monte Grappa 3/5, 20124 Milan, Italy  
Legal Basis: EU Art 9a / Art 28

Netherlands  
Legal Name: Amazon Web Services EMEA SARL, Dutch Branch  
Address: Mr. Treublaan 7, 1097 DP Amsterdam, Netherlands  
Legal Basis: EU Art 9a / Art 28

Poland  
Legal Name: Amazon Web Services EMEA SARL spolka z ograniczona odpowiedzialnoscia Oddzial w Polsce  
Address: Generation Park Z, 9th floor, ul. Towarowa 28, Warsaw, Poland  
Legal Basis: EU Art 9a / Art 28

Portugal  
Legal Name: Amazon Web Services EMEA SARL, Sucursal em Portugal  
Address: Avenida D. Joao II, 50, andar 4, Edificio Mar Vermelho, Parque das Nacoes, 1990-095 Lisboa, Portugal  
Legal Basis: EU Art 9a / Art 28

Romania  
Legal Name: Amazon Web Services EMEA SARL Luxemburg Sucursala Bucuresti  
Address: District 2, 4B si 2-4 George Constantinescu Street, Lot 1, Building A (Section A), Floor 11, Bucharest, Romania  
Legal Basis: EU Art 9a / Art 28

Spain  
Legal Name: Amazon Web Services EMEA SARL, sucursal en Espana  
Address: Calle de Ramirez de Prado 5, 28045 Madrid, Spain  
Legal Basis: EU Art 9a / Art 28

Sweden  
Legal Name: Amazon Web Services EMEA SARL, Sverige filial  
Address: Malmskillnadsgatan 36, Stockholm, Sweden  
Legal Basis: EU Art 9a / Art 28

Norway  
Legal Name: Amazon Web Services EMEA SARL, Norwegian Branch  
Address: c/o Aker Brygge Business Village, 4th Floor, Grundingen 6, 0250 Oslo, Norway  
Legal Basis: NO VAT Act §§ 3-1

United Kingdom  
Legal Name: Amazon Web Services EMEA SARL, UK Branch  
Address: 1 Principal Place, Worship Street, London, EC2A 2FA, United Kingdom  
Legal Basis: UK VAT Act 1994, s.47(4)

## What if I sell to Buyers in the UK, Norway and multiple EU countries?
<a name="faq-multiple-countries"></a>

If you sell to Buyers with AWS accounts in multiple countries from multiple Seller accounts, you must issue separate invoices to each relevant AWS EMEA branch facilitating the transaction. Each branch has its own name, address, and VAT identification number.

## Why can't I see the Deemed VAT section in my AWS Marketplace Management portal?
<a name="faq-iam-permissions"></a>

Your AWS Identity and Access Management (IAM) user or role might lack the required permissions. Attach the following IAM policy to the user or role that you use to sign in.

This policy grants access to the Deemed VAT feature:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SellerSettings",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:StartInvoiceSubmissionTask",
                "aws-marketplace:GetInvoiceSubmissionTask",
                "aws-marketplace:ListInvoiceSubmissionTasks",
                "aws-marketplace:ListPayables"
            ],
            "Resource": "*"
        },
        {
            "Sid": "MarketplaceEphemeralWriteS3Access",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::aws-partner-central-marketplace-ephemeral-writeonly-files/${aws:PrincipalAccount}/*"
            ]
        }
    ]
}
```

Without these permissions, the Deemed VAT section does not appear in the portal. Contact your administrator if AWS has not yet enabled your account.

## How do I submit a VAT invoice for VAT payment?
<a name="faq-how-to-submit"></a>

You can submit a VAT invoice in AWS Partner Central. Navigate to the Tax Information tab. Then:

1. Select Deemed Supply-eligible line items to upload a VAT invoice.

1. Choose Apply VAT disbursement once line items are selected.

1. Review the submission page details and upload the VAT invoice by choosing the Upload file button.

1. Once you have reviewed the submission details, choose the Submit disbursement button and confirm.

## Can I submit a VAT invoice for a Deemed Supply before the Buyer has paid AWS?
<a name="faq-submit-before-buyer-paid"></a>

Yes. You can upload your VAT invoice as soon as the transaction has been reported, even if AWS has not yet received payment from the Buyer. AWS Marketplace will hold the invoice and process the VAT disbursement once both conditions are met:

1. AWS systems have validated the VAT invoice you submitted for the transaction.

1. AWS has received payment from the Buyer.

## Can I consolidate multiple transactions into a single invoice?
<a name="faq-consolidate-invoices"></a>

Yes. You may consolidate all AWS Marketplace deemed supply transactions for a given AWS EMEA branch into a single VAT invoice, provided the following conditions are met:
+ All transactions on the consolidated invoice must relate to the same AWS EMEA branch (i.e., same country).
+ The VAT amounts on the consolidated invoice must match the sum of the deemed supply VAT amounts for the underlying transactions.
+ The invoices which are consolidated must be in the same original offer currency.

## Is there a time limit for submitting a VAT invoice for a Deemed Supply?
<a name="faq-time-limit"></a>

You should submit your VAT invoice as soon as practicable following the transaction. VAT invoices for Deemed Supplies that are more than 12 months old may be rejected depending on the country. AWS strongly recommends submitting invoices within the same VAT reporting period in which the deemed supply occurred, or as soon as possible thereafter.

## What information must be included on my VAT invoice for a Deemed Supply?
<a name="faq-mandatory-fields"></a>

Your VAT invoice must contain all the fields listed below. Invoices that do not contain all mandatory fields will be rejected.

1. **AWS EMEA Branch Bill-To Address** — The registered address of the AWS EMEA SARL branch to which the invoice is addressed.

1. **AWS EMEA Branch VAT Number** — The local VAT identification number of the AWS EMEA SARL branch.

1. **Type of Document** — Specify whether the document is an Invoice or a Credit Note. For accepted credit-note terms, see [What should I enter in the Type of Document field?](#faq-refund-document-type).

1. **Supplier Name** — Your legal entity name as registered with your local tax authority.

1. **Supplier Address** — Your legal registered address.

1. **Supplier VAT ID** — Your local VAT identification number.

1. **Invoice Date** — The date on which the invoice is issued.

1. **Invoice Number** — Your unique sequential invoice number (1-50 characters).

1. **Invoice Currency** — Must match the offer currency or local currency.

1. **VAT Legal Currency** — The currency in which VAT must be displayed.

1. **Invoice Description** — Description of the supply including quantity and unit price.

1. **Net Amount** — Total net amount (excluding VAT).

1. **VAT Rate (%)** — The applicable domestic VAT rate.

1. **VAT Amount in Invoice Currency** — Net Amount multiplied by VAT rate.

1. **VAT Amount in Legal Currency** — Total VAT in legal currency.

1. **Invoice Total** — Net Amount plus VAT Amount.

## What legal reference should I include on my VAT invoice?
<a name="faq-legal-reference"></a>

AWS recommends including a reference to the applicable Marketplace Operator Rules in the invoice description field.

For EU transactions, include: "Supply of Digital Services deemed to be made under the provisions of Article 9a of EU VAT Council Implementing Regulation (EU) No 282/2011 of 15 March 2011 and Article 28 of EU VAT Directive 2006/112/EC. VAT only due for payment."

For UK transactions, include: "Supply of Digital Services deemed to be made under the provisions of Section 47(4) of the UK Value Added Tax Act 1994. VAT only due for payment."

For Norway transactions, include: "Supply of Digital Services deemed to be made under the provisions of Merverdiavgiftsloven (Norwegian VAT Act) § 3-1, second paragraph, whereby the marketplace operator is treated as having received and supplied the service. VAT only due for payment."

This language may be included in the Invoice Description field or as a separate line item or footnote on the invoice.

## Do I need to submit an e-invoice instead of a PDF?
<a name="faq-e-invoicing"></a>

In jurisdictions where e-invoicing is mandatory (e.g., Italy via the Sistema di Intercambio), you must submit your e-invoice in the required electronic format. XMLs must be submitted for Italy, Belgium, Poland and Romania transactions. Please note that XMLs will be rejected if used for VAT payment requests in any other jurisdiction.

Where e-invoices are represented by a PDF, you can submit e-invoices through AWS Partner Central. AWS Marketplace will validate your e-invoice against the applicable government system requirements. If validation fails, you will receive an error response detailing the issue, and you will be asked to re-submit a corrected e-invoice.

For jurisdictions where e-invoicing is not currently mandatory, you must submit your invoice in PDF format. As more EU Member States adopt mandatory e-invoicing requirements, additional e-invoicing formats may be required. AWS will communicate any changes to supported formats in advance.

## How and when will I receive the VAT disbursement?
<a name="faq-receive-disbursement"></a>

Once your VAT invoice has been validated and the Buyer has paid the corresponding invoice to AWS, the VAT amount will be disbursed to you automatically. The VAT disbursement is separate from your standard Marketplace disbursement.

**Important**  
AWS will only disburse the VAT amount stated on the invoice. The net amount of the deemed supply is already included in your standard Marketplace disbursement cycle. AWS recommends that your invoice includes the disclaimer "VAT only due for payment".

## How can I track the status of my VAT payment?
<a name="faq-track-status"></a>

You can track the status of all your VAT invoices in the Tax Information tab of AWS Partner Central. Each invoice will display one of the following statuses:
+ **PENDING:** Invoice was received.
+ **ACCEPTED:** Invoice received and validated, awaiting payment from the Buyer.
+ **REJECTED:** Invoice failed validation. Check the rejection reason and re-upload a corrected invoice.

## When do I need to submit a credit note for a refund?
<a name="faq-refund-when-credit-note"></a>

If a Buyer receives a refund for a transaction where AWS previously disbursed EU, Norway, or UK VAT to you, AWS might recover the associated VAT from your seller balance. You might also need to provide a credit note for the refunded transaction.

You need to submit a credit note when AWS previously disbursed VAT to you for the original transaction and that transaction is later refunded. If AWS has not disbursed VAT to you for the original transaction, you can't submit a credit note under this refund process solely because a refund appears in AWS Partner Central. You will still see the original sale and the corresponding refund as separate line items. If VAT is later disbursed to you for the original sale, the applicable refund and credit-note requirements then apply.

## What happens if a Buyer is refunded after I have already received the VAT disbursement?
<a name="faq-refund-credit-note"></a>

If AWS previously disbursed VAT to you for the original transaction, AWS recovers the applicable VAT after the refund conditions are met. You must also provide a credit note for the refunded transaction. You can submit the credit note directly through AWS Partner Central. This process applies to eligible AWS Marketplace transactions, including Channel Partner Private Offer (CPPO) transactions. Your credit note must:
+ Use the applicable document format for the transaction. For more information about document formats, see [Should I submit a PDF or an XML credit note?](#faq-refund-format).
+ Include a reference to the original Seller invoice ID that you uploaded to receive VAT for the original transaction. You can find it in the **Seller invoice ID** column of the **VAT on deemed supply submissions** table.
+ Include a recognized credit-note value in the Type of Document field. For more information about accepted values, see [What should I enter in the Type of Document field?](#faq-refund-document-type).

## Where can I find refunds and submit a credit note?
<a name="faq-refund-find-submit"></a>

In AWS Partner Central, choose **Settings**, choose the **Tax information** tab, and scroll down to the **VAT on deemed supply** section. Refunds appear in the eligible line items table. To submit a credit note:

1. Select the refund line item or line items that the credit note covers.

1. Choose **Apply VAT disbursement**.

1. Upload your credit note in the required PDF or XML format. The maximum file size is 10 MB.

1. Review the submission details.

1. Choose **Submit VAT on deemed supply disbursement** and complete the confirmation.

At the confirmation step, enter the total amount exactly as displayed, including the "-" sign where applicable.

By default, the table displays transactions from the previous 14 days. If you do not see an expected refund, expand the date range and confirm that it includes the transaction.

## How can I identify a refund?
<a name="faq-refund-identify"></a>

A refund appears as a separate line item from the original sale. Refund line items display negative values for the Net amount, VAT amount, and Line item total. For example, you might see:
+ The original sale and a separate negative line item for a partial refund.
+ The original sale and an equal negative line item when the transaction is fully refunded.

The Line item status has a different meaning for refunds:
+ For a sale, **Paid** means the Buyer has paid AWS.
+ For a refund, **Paid** means the Buyer's refund has been credited.

**Note**  
A **Paid** status on the refund does not necessarily mean that AWS has already recovered the VAT from your seller balance.

## How soon will a refund appear in AWS Partner Central?
<a name="faq-refund-timing"></a>

A refund can take up to 72 hours after the Buyer refund is generated to appear in the eligible line items table. A refund might appear while its status is still **Unpaid**. If you do not see an expected refund after 72 hours, confirm that your selected date range includes the transaction before reporting it as missing.

## Does submitting a credit note trigger VAT recovery?
<a name="faq-refund-recovery-trigger"></a>

No. Creating, submitting, or having a credit note accepted does not, by itself, trigger VAT recovery. VAT is recovered after both of the following have occurred:

1. AWS has accepted the VAT invoice for the original sale.

1. The Buyer's refund has been credited and the refund line item shows **Paid**.

## What will I see when AWS recovers the VAT?
<a name="faq-refund-recovery-view"></a>

If AWS previously disbursed VAT to you for the original transaction and that transaction is later refunded, AWS deducts the applicable VAT amount from your seller balance after the recovery conditions are met. You will see the recovery as a deduction from your balance rather than as a separate charge or invoice.

To review the financial adjustment, use the Collections and Disbursements dashboard in Insights. Use the **VAT on deemed supply** section to view eligible line items and track the status of your submitted documents.

## Can I include multiple refunds on one credit note?
<a name="faq-refund-consolidate"></a>

Yes. You can include multiple eligible refunds on one credit note when they can be consolidated. After you select the first refund, AWS Partner Central shows which additional refund line items can be included in the same submission. Refunds that cannot be combined must be submitted separately.
+ Reference the Seller invoice ID of every VAT invoice involved when your credit note covers refunds from more than one original sale.
+ Select up to 100 eligible line items in one submission.
+ Match the total VAT amount on your credit note to the total VAT amount shown for the refund line items that you selected.
+ Submit sales and refunds separately. A single document cannot contain both sale and refund line items.

## Should I submit a PDF or an XML credit note?
<a name="faq-refund-format"></a>

Use the document format required for the applicable country and transaction. Submit XML where electronic invoicing is required. Submit PDF where electronic invoicing is not required. For more information about the countries that require XML, see [Do I need to submit an e-invoice instead of a PDF?](#faq-e-invoicing).

For PDF credit notes, the amounts must be negative, consistent with how the refund amounts appear in AWS Partner Central. If your country requires a specific electronic-invoicing format, follow that format's requirements. For example, in Italy, an electronic credit note submitted using the FatturaPA format requires positive amounts.

## How can I check whether my credit note was accepted?
<a name="faq-refund-status"></a>

You can track your credit-note submissions in the **VAT on deemed supply submissions** table. Each submission shows one of the following statuses:
+ **Pending** – AWS received the document and is reviewing it.
+ **Accepted** – AWS successfully validated the document.
+ **Rejected** – The document did not pass validation and must be corrected before you resubmit it.

After you submit a credit note, AWS Partner Central removes the corresponding refund line items from the eligible line items table. If the credit note is rejected, those line items become available again so that you can correct the document and submit a new credit note. Common reasons for rejection include:
+ The AWS VAT entity information on your credit note does not match the transaction.
+ The VAT amount does not match the amount shown for the selected refund line items.
+ Your legal entity name does not match your registered legal entity name.
+ Required information is missing from the document.

Use the VAT amount displayed for the refund line items when preparing your credit note. Recalculating the amount independently might result in a different value because VAT rounding can vary by country.

## What should I enter in the Type of Document field?
<a name="faq-refund-document-type"></a>

Enter a recognized credit-note document type in the Type of Document field. You can use the applicable credit-note term for your language. Supported examples include:
+ Credit Note
+ Credit Memo
+ Nota de Crédito
+ Gutschrift

Matching is not case-sensitive. If your local-language credit-note term is not recognized, use Credit Note in English.

## Can AWS generate a VAT invoice for Deemed Supplies on my behalf?
<a name="faq-self-billing"></a>

No. At the moment AWS Marketplace does not offer a Self-Billing option where AWS generates the VAT invoice on your behalf for deemed sale transactions.

## How do I identify which transactions I can submit VAT invoices for?
<a name="faq-identify-transactions"></a>

The Tax Dashboard in AWS Partner Central has been enhanced to include data columns to help you identify deemed sale transactions and self-serve the generation of your VAT invoice, including:
+ Legal VAT amount (in local currency and USD)
+ Legal currency
+ Seller's local VAT ID
+ Buyer's legal address
+ Buyer billing country
+ AWS EMEA branch that facilitated the transaction (including branch name, address, and VAT ID)
+ Seller billing country
+ VAT amount calculated using the applicable FX rate (for consolidated billing)

You can apply filters on these columns to retrieve the exact transactions where you can submit a VAT invoice for payment. The Tax Dashboard has a 1 to 2 day delay for the latest data to be reflected.

## Where can I see whether VAT has been disbursed for my eligible transactions?
<a name="faq-vat-disbursed"></a>

VAT disbursement on Deemed Supplies information is available in the following locations:
+ **Seller Reports:** The Seller reports include new data points indicating whether VAT payment on Deemed Supplies is applicable and whether it has been disbursed for each transaction. A new "Seller Invoice ID" column and "VAT on Deemed Supplies Flag" column have been added.
+ **Disbursement Dashboard:** The Collection and Disbursement dashboard displays the Seller Invoice ID and VAT on Deemed Supplies Flag for all transactions involving VAT payment, allowing you to reconcile disbursements with your uploaded invoices.
+ **Seller Data Delivery Service (SDDS):** The data feeds have been updated to include VAT disbursement data for programmatic access.

These reports are designed to support your internal reconciliation, financial reporting, and audit requirements.

## How do I reconcile VAT disbursement?
<a name="faq-reconcile-vat-disbursement"></a>

Visit the Collections and Disbursements dashboard in your Seller reports. You can use the following columns:
+ **Seller issued invoice ID:** An invoice issued by the Seller to AWS. Once you submit an invoice, it feeds into the Submission table and is associated with your "Seller Invoice ID." This same ID appears in the Collections and Disbursements dashboard for reconciliation.
+ **Seller issued invoice variant:** Displays "TAX\_VAT," indicating an invoice from the Seller to AWS for Deemed VAT payment.
+ **Seller tax share:** The VAT amount invoiced.

For each transaction reference, two rows will appear in the dashboard:
+ One for the original disbursement
+ One for the VAT disbursement

The VAT disbursement row contains the disbursement status, disbursement date, Bank Trace ID, and reference number.

To match disbursements with their respective invoices, use the Collections and Disbursements dashboard to filter by the Bank Trace ID found in your bank statement. The Seller Invoice ID assigned at submission appears consistently across both the Submission table and the Collections and Disbursements dashboard, providing end-to-end traceability from invoice submission to payment receipt.

## What happens if my invoice is rejected?
<a name="faq-invoice-rejected"></a>

If your invoice fails validation, you will receive an error response identifying the specific issue. Common rejection reasons include:
+ Invoice format non-compliant (e.g., missing mandatory fields).
+ VAT amount on invoice does not match the calculated VAT for the transaction(s).
+ Incorrect AWS EMEA branch name or VAT number.

You can correct the issue and re-upload the invoice through AWS Partner Central.

## Can I submit more than one invoice for the same transaction?
<a name="faq-duplicate-invoice"></a>

No. The automated validation system includes controls to prevent duplicate invoicing.

## How do Deemed VAT Supply Invoicing and the Tax Portal differ?
<a name="faq-deemed-vs-tax-portal"></a>

AWS Marketplace has launched the following capabilities accessible through AWS Partner Central:
+ **Deemed VAT Supply Invoicing:** Enables Sellers to submit VAT invoices to AWS and receive automated VAT disbursements for deemed supply of Digital Services in the EU, Norway, and the UK. This capability is for Sellers transacting through AWS EMEA SARL branches who must invoice AWS for VAT under deemed supply law.
+ **Tax Portal:** Provides Sellers centralized access to view, search, filter, and download listing fee and tax invoices issued by AWS. For more information, see [Managing invoices](https://docs.aws.amazon.com/marketplace/latest/userguide/managing-invoices.html). This capability is for all Sellers needing the ability to download and reconcile listing fee invoices or tax invoices issued by AWS across any invoicing entity.

The following table summarizes the key differences:


| Dimension | Deemed VAT Supply Invoicing | Tax Portal | 
| --- | --- | --- | 
| Invoice direction | Seller submits invoices to AWS | Seller retrieves invoices from AWS | 
| Scope | EU, Norway, UK deemed supply transactions | All invoicing entities globally | 
| Key action | Submit, track, and receive VAT disbursements | View, search, filter, and download Listing Fee invoices and India customer invoices only | 
| Validation | Automated field validation; disbursement on buyer payment | Sellers can download and reconcile invoices | 
| Use case | VAT compliance under deemed supply arrangements | Listing fee invoice download and financial reconciliation | 

## Where can I get additional help with VAT on Deemed Supplies?
<a name="faq-additional-help"></a>

For questions about the VAT on Deemed Supplies invoicing process, invoice submission, or disbursement status, contact support on the AWS Partner Central and Marketplace Support page.

For tax-specific questions regarding the Deemed Supply treatment, applicable VAT rates, or legal references, consult your tax advisor. AWS is unable to provide tax advice on the VAT treatment of your individual transactions.