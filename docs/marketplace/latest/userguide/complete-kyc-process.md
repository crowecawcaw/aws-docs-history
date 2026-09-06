

# Step 5: Complete the Know Your Customer (KYC) process
<a name="complete-kyc-process"></a>

AWS Marketplace has established regional invoicing entities (also referred to as Marketplace Operators or MPOs) to facilitate transactions and support buyers' and sellers' localized business needs, such as tax, reporting, disbursements, and compliance. Invoicing entities are regional entities responsible for managing these localized aspects of AWS Marketplace for their respective regions. Each invoicing entity is subject to local laws and regulations. The Know Your Customer (KYC) process is a verification procedure that helps AWS comply with regulatory requirements, including EU anti-money laundering directives and Korean financial transaction reporting requirements.

## When KYC verification applies
<a name="when-kyc-applies"></a>

Whether you need to complete KYC verification — and which type — depends on two factors: the country where your business is registered (your home country), and the countries where your buyers are located. You might need to complete one type or both.

### If your business is registered in Japan
<a name="when-kyc-applies-japan"></a>

Sellers registered in Japan must complete **Japan Installment Sales Act verification** to sell on AWS Marketplace, regardless of where their buyers are located. This is required under Japanese law and is a separate, self-service process. See [Japan Installment Sales Act verification](#japan-isa-verification).

### If your buyers are in Europe, the Middle East, and Africa (EMEA) or South Korea
<a name="when-kyc-applies-buyer-region"></a>

KYC verification is mandatory for you to transact and/or receive disbursements through the AWS Marketplace invoicing entities in the following regions:

1. Europe, Middle East, and Africa (transaction and disbursements)

1. South Korea (disbursements)

Completing the KYC process for one of these regions can expedite verification for the other. For the requirements and steps, see [KYC requirements](#kyc-requirements).

EMEA  
Sellers must complete the KYC process to use the AWS EMEA invoicing entity. AWS Marketplace transactions through the AWS EMEA invoicing entity are processed through Amazon Payments Europe, S.C.A. (APE), a licensed electronic money institution in Luxembourg. Until the KYC is completed, AWS Inc. will be used as the invoicing entity for the seller's transactions in this region. In a Channel Partner Private Offer (CPPO), both the Channel Partner and the ISV need to be KYC verified to use AWS EMEA as the invoicing entity. AWS Inc. will be the default invoicing entity if either party is not KYC verified. For information about how the invoicing entity (AWS Inc. vs. AWS EMEA) affects tax handling for your transactions, see [Tax handling for AWS Marketplace sellers](https://aws.amazon.com/tax-help/marketplace-sellers/tax-grid/). For the full terms, see the [AWS Marketplace EMEA Agreement](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/legal/approved/amazon-payments-europe-aws-marketplace-emea-agreement.pdf).

South Korea  
To receive disbursements from the AWS South Korea invoicing entity, sellers must undergo KYC verification. Completing the KYC process for the EMEA region can expedite the verification for South Korea, and vice versa.

**Sellers in India**  
This process doesn't apply to sellers in India, as they can only sell to buyers in India. For detailed information, see [Getting started as a seller in India](getting-started-seller-india.md).

**KYC email notifications**  
KYC status updates are sent to your AWS account root email address and the custom email address you provide during registration. It is highly recommended to add key KYC stakeholders to the custom email notification so that important messages are not missed. For more information, see [Adding or updating email addresses](email-notifications.md#adding-updating-email-addresses).

## Japan Installment Sales Act verification
<a name="japan-isa-verification"></a>

Under Japan's Installment Sales Act, sellers registered in Japan must complete verification to sell on AWS Marketplace. This is a home-country requirement based on where your business is registered, distinct from the buyer-region KYC described in [KYC requirements](#kyc-requirements). You complete it as a self-service process in AWS Partner Central.

**Interactive demo available in Japanese**  
To preview the verification screens before you begin, view the [interactive Japan Installment Sales Act verification demo](https://awsmarketplace.storylane.io/share/300dmygmsvyg). The demo walks through each step with screens shown in Japanese.

**What it verifies:** your business details and legal representative identity.

**Before you start:** your business registration number and business address are filled automatically from your **Tax settings** in the Billing console. If your tax registration is incomplete, the verification form is unavailable — complete your tax information in **Tax settings** first, and then return to this page.

**To complete Japan verification**

1. Sign in to AWS Partner Central at [https://us-east-1.console.aws.amazon.com/partnercentral/home](https://us-east-1.console.aws.amazon.com/partnercentral/home) and choose **Marketplace settings**.

1. Choose the **Know Your Customer (KYC)** tab, and then locate **Japan Know Your Customer (KYC)**.

1. Choose **Start verification**. (If you have already verified, choose **Update verification** to make changes.)

1. **Step 1: Business details** — review your business information (registration number and address are pre-filled from your tax settings), add business information, and add any tags. Choose **Save and continue**.

1. **Step 2: Legal representative information** — enter the legal representative's personal and contact details. Choose **Save and continue**.

1. **Step 3: Review and submit** — review the information you've provided, and then choose **Submit**. You can choose **Edit** to return to a previous step.

You can leave the wizard at any time. If you have unsaved changes on a step, you're prompted to save them before navigating away; your saved progress is retained so you can resume where you left off.

**After you submit:** your status changes to **Under review**, and you receive email notifications to your AWS account root email address and custom email address when your status changes. Verification statuses are:
+ **Not started** — you haven't begun verification.
+ **Under review** — your submission is being verified.
+ **Successful** — verification is complete.
+ **Action required** — more information is needed. Correct the issues shown and resubmit.

If you update your details after verifying, submitting the changes triggers reverification, which can take up to 7 business days.

## KYC requirements
<a name="kyc-requirements"></a>

The KYC process requires you to provide additional information and documentation to verify your identity and business details. Before starting **buyer-region KYC**, ensure you can monitor your AWS account root email address, as the KYC team will send status updates and requests to that address. For more information about managing account communications, see [Managing account communications](managing-account-communications.md) in [Managing your seller account](seller-account-management.md).

KYC is a 3-step process:

Step 1: Business Verification  
During this step, you will be required to provide information about your business entity, related documents associated to the business, and the registration and verification of key individuals within your organization (primary contacts, business owners, and legal representatives).  
You will also need to provide identity verification documents and address verification documents for the nominated individuals. In some cases you might be asked to provide authorization documentation on a company letterhead, signed by a legal representative of the business, if a nominated individual is not legally authorized to represent the company.

Step 2: Bank Account Verification  
After the business verification step is completed, your seller account will be KYC verified, but you must provide a bank statement on the **Payment information** tab before you can receive disbursements through Amazon Payments Europe. For detailed information, see [Step 6: Complete bank account verification](complete-bank-verification.md).

Step 3: Secondary User Verification  
Only authorized users are allowed to manage your KYC and financial details after KYC verification. The secondary user verification is an optional step used if you need to nominate other users within your organization to manage your KYC and financial details on AWS Marketplace, for example, if your finance team needs access to manage disbursement settings. For detailed information, see [Managing secondary users for Know Your Customer (KYC)](managing-secondary-users.md).

**Important**  
All provided documents must be clear, legible, and on official letterhead where applicable. Business documents should be signed by a legal representative and issued within 180 days unless otherwise specified.  
The document requirements listed in this guide are not exhaustive. During the verification process, compliance teams may request additional information or documentation based on their assessment. Requirements are evaluated on a case-by-case basis.

## Steps to complete Step 1 of the KYC process - Business Verification
<a name="complete-kyc-process-steps"></a>

Follow these steps to complete Step 1 of the KYC process in AWS Marketplace:

**Note**  
For accepted document types, templates, and formatting requirements referenced throughout these steps, see the [Templates and best practices for completing the KYC process](#kyc-best-practices) section at the end of this page.  
You will be asked to review and accept the [AWS Marketplace EMEA Agreement](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/legal/approved/amazon-payments-europe-aws-marketplace-emea-agreement.pdf) during this process. We recommend reviewing it before you begin.

1. Sign in to AWS Partner Central at [https://us-east-1.console.aws.amazon.com/partnercentral/home](https://us-east-1.console.aws.amazon.com/partnercentral/home) and choose **Marketplace settings**.

1. In the **Account summary** section, confirm that the **Country** that is shown is correct.
**Note**  
Choose the **Info** link to see how to change your country.

1. In the same section, review your **KYC Verification** status to see where you are in the verification process.

1. To start or review your KYC journey, select the **Know Your Customer (KYC)** tab.
**Note**  
In the main KYC tab, you can see a table with customer regions, invoicing entity, transaction status, and disbursement status. Use this table to understand which AWS invoicing entity your customer will get their invoices from. If your transaction or disbursement status is 'Blocked' for an invoicing entity, use the Next Steps column to understand what is required from you.

1. To start or review your business verification, choose **Update Business Verification**. You will be directed to the KYC Registration Portal.

1. Enter the **Basic details** as directed, including selecting your entity type (such as privately-owned business or publicly listed company). After you review the Amazon Payments Europe Terms & Conditions, choose **Agree and continue**.
**Important**  
If the registered seller account name is not publicly listed on a stock exchange, please select 'privately-owned business'.
Ensure the business name you enter matches your AWS Marketplace seller account name, as this is the company being verified.
Input your business details exactly as shown in official registration documents (country of incorporation, entity type, name, registration number, etc.).
Any discrepancies or mismatched information may delay the verification process.

   When you continue to the next page or next step in the KYC process, that action indicates that you accept the Amazon Payments Europe Terms & Conditions.

   If you have questions, see **Frequently Asked Questions (FAQ)** located on the right side of the console.

1. Enter the required **Business information** as directed, and then choose **Next**.
**Note**  
Registration Extract is your Company Registration or Incorporation Document.
For US companies, if the Registration Extract or Incorporation Document is older than 180 days, please additionally provide a certificate of good standing, certificate of (account) status, or valid (not expired) business license.
For accepted Proof of Address documents, see the templates section below.
Your information is saved every time you choose **Next** to go to the next step.

1. Enter the required **Point of contact information** as directed, and then choose **Next**.
**Note**  
The Primary Contact person is the person who manages the AWS Marketplace account on behalf of the company, and where possible the root user for the seller account. This person must have legal capacity to represent the company; otherwise, a Letter of Authorization (LOA) is required to be uploaded in the 'Additional documents' section. See the templates section below for an LOA template.
Provide an accepted Identity document and Proof of Address. See the templates section below.

1. Choose whether the **Beneficial owner** is the same as the point of contact, add beneficial owners (up to four) if necessary, confirm your additions, and then choose **Next**.
**Note**  
At least one Beneficial Owner or a Senior Management Official needs to be registered on the account if the Beneficial Owner is not the Point of Contact.
If privately owned company (beneficial owner required): An individual who directly or indirectly owns more than 25% of the shares or voting rights in your business must be registered on the account. If this is not applicable, please register an individual (senior managing official) who controls the company through other means (chief executive officer, chief financial officer, managing or executive director, or president).
If publicly listed company (senior manager always required): Any individual who holds the position of senior managing official, such as a chief executive officer, chief financial officer, managing or executive director, or president. (Please enter Senior Manager Official details and document uploads in the beneficial owner section.)
Provide an accepted Identity document and Proof of Address. See the templates section below.

1. Choose whether the **Legal representative** is the same as the point of contact or beneficial owner. If the legal representative is a different entity, provide the required information, save your entry, and then choose **Next**.

1. In the **Additional documents** section, upload your letter of authorization (if applicable) and statute documents.
**Note**  
Letter of Authority (LOA): This is required to confirm the primary contact is authorized to act on behalf of the company. Provide this letter using the recommended template. See the templates section below.
Statute Document: This document should contain Articles of Association, bylaws, and/or a most recent share allotment document (statement of capital/annual return/share register). It is the governing document of a company. For privately owned companies, the statute document should include the full names of each beneficial owner who directly or indirectly owns more than 25% shareholding. If the above data point is missing, you would be required to provide an organization chart showing the entire structure of the registered business (see the templates section below). The exact requirements for statute documents vary by country and legal entity type; therefore, please provide a document that most closely aligns with the descriptions.
Ensure all submitted documents are signed by a legal representative, are on letterhead or stamped, and dated within 180 days. If further documents are required, the KYC verification team will contact you via the main/root email address and where possible they will provide an example template.

1. On **Review and Submit**, review and verify all of the information that you have entered.

   You can select **Edit** to return to any previous section if necessary.

1. Choose **Submit for verification**.

The status of your KYC compliance will be reviewed (typically within 24 hours). You will be notified through an email message after the review is complete.

You can return to the **Marketplace settings** tab to view the status of your KYC compliance on the **Account summary** card. For more information about your KYC status, choose the **Know Your Customer (KYC)** tab under the **Account summary** card. It will display **Under review** until the review has been completed.

**Important**  
After your KYC is verified, you must provide a bank statement on the **Payment information** tab before you can receive disbursements through Amazon Payments Europe.

If you need to add secondary users who can manage KYC information and financial details, see [Managing secondary users for Know Your Customer (KYC)](managing-secondary-users.md) in [Managing your seller account](seller-account-management.md).

## Templates and best practices for completing the KYC process
<a name="kyc-best-practices"></a>

### Accepted identity documents
<a name="kyc-identity-documents"></a>

If you need to provide an identity document for an individual, the following documents are accepted:
+ Passport
+ National identity card
+ US passport card
+ Driving license
+ Residence permit

Requirements for identity documents:
+ Document copy/image must be high quality, in color, unobstructed, and legible.
+ Document size should be less than 10MB.
+ Accepted formats include: .png, .tiff, .tif, .jpg, .jpeg, and .pdf.
+ The document must be a copy of a government-issued ID document containing a photo and personal information.
+ The document must contain full name, date of birth, place of birth, and country of citizenship. If a standalone ID document does not contain all the data points, please provide two ID documents in combination (for example, driving license and birth certificate).
+ The document must not be expired.
+ If the identity document has two sides, both sides must be uploaded.
+ The signature page of the document should be provided, where applicable.

### Accepted proof of address documents
<a name="kyc-proof-of-address"></a>

The following documents are accepted as proof of address:
+ Utility bill (gas, water, electricity, TV, Internet, mobile phone, or landline)
+ Bank statement (documents issued by a financial services provider other than a bank, such as third-party providers or online digital banks, are not acceptable as proof of address)
+ Credit union or building society statement
+ Credit card statement or bill
+ Mortgage statement
+ Rent receipt from a local council or letting agent

Requirements for proof of address documents:
+ The proof of address must show the provider's logo.
+ The proof of address must be addressed to the corresponding person or legal entity (names should match the ID/legal document provided).
+ The full name and country of residence must be visible on the document. Other sensitive information such as account balance or card number can be covered.
+ The document must not be a screenshot.
+ The document must be dated within 180 days.

### Letter of authorization template
<a name="kyc-loa-template"></a>

If you need a letter of authorization, you can use the following sample:

```
Letterhead of the company

POWER TO ACT ON BEHALF OF THE COMPANY
The undersigned **Enter Company name here** (hereinafter, the "Company"), with tax
registration number **add tax registration number here**, duly represented by
**add full name of the authorized representative here**, confirms that
**add full name of the Point of Contact here**, born on **add date of birth here**,
residing at **add address here**, and whose relationship to the authorized representative is
**add relationship here**,
is authorized to open an Amazon Web Services Marketplace account with Amazon Payments,
accept the User Agreement and other Policies, have access to the Amazon Web Services
Marketplace account, initiate transactions in the name and on behalf of the Company and
approve new Secondary users added to the account and if required, grant them access to
update listings, respond to buyers and initiate refunds.

    Dated this:

    Representative: ______________________ (Signature/Stamp)
```

### Organization chart template
<a name="kyc-org-chart"></a>

As part of the statute document, you may be required to provide an organization chart showing the entire structure of the registered business. Example below:

![Example organization chart showing the entire structure of a registered business, including parent company, subsidiaries, and beneficial owners.](http://docs.aws.amazon.com/marketplace/latest/userguide/images/kyc-organization-chart.png)


### General best practices
<a name="kyc-general-best-practices"></a>

Consider these best practices when completing the KYC process:
+ Prepare all required documentation in advance to streamline the process.
+ Ensure all documents are clear, legible, and current (typically issued within the last 3-6 months for address verification).
+ Provide consistent information across all documents and verification steps.
+ Respond promptly to any requests for additional information or clarification.
+ If you're unsure about any requirements, contact AWS Marketplace Seller Support for assistance.

## Next steps
<a name="next-steps-after-kyc"></a>

After completing the KYC process, you can proceed to the final step in the registration process: [Step 6: Complete bank account verification](complete-bank-verification.md).